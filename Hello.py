from antlr4 import *
from HelloLexer import HelloLexer
from HelloListener import HelloListener
from HelloParser import HelloParser
from mido import MidiFile
from mingus.core import chords
from midiutil import MIDIFile
import sys


class HelloPrintListener(HelloListener):
  def enterHi(self, ctx):
      partitures = ctx.PARTITURE()
      
      inter = ctx.OCT()
      if(len(inter) == 1):
            inti = float(str(inter[0]))
            time = ctx.TIME_LIST()
      else:
            inti = float(str(inter[0]))
            time = inter[1]
      if(type(partitures) != list):
          MyMIDI = song_maker_boi(str(partitures).split(","),inti,str(ctx.FILE_NAME()),float(time))
      else:
          MyMIDI = song_maker_boi2(partitures,inti,str(ctx.FILE_NAME()),time)

def swap_accidentals(note):
    if note == 'Db':
        return 'C#'
    if note == 'D#':
        return 'Eb'
    if note == 'E#':
        return 'F'
    if note == 'Gb':
        return 'F#'
    if note == 'G#':
        return 'Ab'
    if note == 'A#':
        return 'Bb'
    if note == 'B#':
        return 'C'

    return note


def note_to_number(note: str, octave: int) -> int:
    NOTES = ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B']
    OCTAVES = [1,2,3,4,5,6,7,8]
    NOTES_IN_OCTAVE = len(NOTES)
    note = swap_accidentals(note)
    assert note in NOTES, errors['notes']
    assert octave in OCTAVES, errors['notes']

    note = NOTES.index(note)
    note += (NOTES_IN_OCTAVE * octave)

    assert 0 <= note <= 127, errors['notes']

    return note

def song_maker_boi(array_of_notes, tempo_, file_name, time_factor = 1):
    NOTES = ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B']
    OCTAVES = [1,2,3,4,5,6,7,8]
    NOTES_IN_OCTAVE = len(NOTES)

    errors = {
        'notes': 'Bad input, please refer this spec-\n'
    }


    array_of_note_numbers = []
    for note in array_of_notes:
        array_of_note_numbers.append(note_to_number(note[0:-1], int(note[-1])))
    
    track = 0
    channel = 0
    time = 0  # In beats
    duration = 1  # In beats
    tempo = tempo_  # In BPM
    volume = 100  # 0-127, as per the MIDI standard

    MyMIDI = MIDIFile(1)
    MyMIDI.addTempo(track, time, tempo)


    for i, pitch in enumerate(array_of_note_numbers):
        MyMIDI.addNote(track, channel, pitch, time + (i*time_factor), duration, volume)
    
    with open(file_name, "wb") as output_file:
        MyMIDI.writeFile(output_file)

        
def song_maker_boi2(array_of_notes, tempo_, file_name, time_factor):
    time_factors = [float(x) for x in str(time_factor).split(",")]
    
    NOTES = ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B']
    OCTAVES = [1,2,3,4,5,6,7,8]
    NOTES_IN_OCTAVE = len(NOTES)
    
    array_of_arrays_of_notes = []
    for parti in array_of_notes:
        array_of_arrays_of_notes.append(str(parti).split(","))
        
    
    array_of_note_numbers_m = []
    for i in range(0, len(array_of_arrays_of_notes)):
        array_of_note_numbers = []
        for note in array_of_arrays_of_notes[i]:
            array_of_note_numbers.append(note_to_number(note[0:-1], int(note[-1])))
        array_of_note_numbers_m.append(array_of_note_numbers)
    
    track = 0
    channel = 0
    time = 0  # In beats
    duration = 1  # In beats
    tempo = tempo_  # In BPM
    volume = 100  # 0-127, as per the MIDI standard

    MyMIDI = MIDIFile(len(array_of_arrays_of_notes))
    for i in range(0, len(array_of_arrays_of_notes)):
        MyMIDI.addTempo(i, time, tempo)

    for j in range(0, len(array_of_note_numbers_m)):
        for i, pitch in enumerate(array_of_note_numbers_m[j]):
            MyMIDI.addNote(j, channel, pitch, time + (i*time_factors[j]), duration, volume)
    
    with open(file_name, "wb") as output_file:
        MyMIDI.writeFile(output_file)


def main():

    lexer = HelloLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = HelloParser(stream)
    tree = parser.hi()
    printer = HelloPrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == '__main__':
    print("Formato: name FILE_NAME tempo INT compose PARTITURA(+ PARTITURA)* time_factors TIME_LIST|OCT")
    try:
        main()
    except:
        print("Error, intentalo de nuevo")
        
    
