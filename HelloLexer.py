# Generated from Hello.g4 by ANTLR 4.11.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,11,115,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,0,1,0,1,0,1,
        1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,74,8,5,1,6,
        4,6,77,8,6,11,6,12,6,78,1,6,1,6,1,6,1,6,1,6,1,7,4,7,87,8,7,11,7,
        12,7,88,1,8,1,8,1,8,4,8,94,8,8,11,8,12,8,95,1,9,1,9,1,9,1,9,1,9,
        1,9,5,9,104,8,9,10,9,12,9,107,9,9,1,10,4,10,110,8,10,11,10,12,10,
        111,1,10,1,10,0,0,11,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,
        10,21,11,1,0,3,3,0,65,90,95,95,97,122,1,0,48,57,3,0,9,10,13,13,32,
        32,129,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,
        0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,
        0,0,21,1,0,0,0,1,23,1,0,0,0,3,28,1,0,0,0,5,34,1,0,0,0,7,42,1,0,0,
        0,9,44,1,0,0,0,11,73,1,0,0,0,13,76,1,0,0,0,15,86,1,0,0,0,17,90,1,
        0,0,0,19,97,1,0,0,0,21,109,1,0,0,0,23,24,5,110,0,0,24,25,5,97,0,
        0,25,26,5,109,0,0,26,27,5,101,0,0,27,2,1,0,0,0,28,29,5,116,0,0,29,
        30,5,101,0,0,30,31,5,109,0,0,31,32,5,112,0,0,32,33,5,111,0,0,33,
        4,1,0,0,0,34,35,5,99,0,0,35,36,5,111,0,0,36,37,5,109,0,0,37,38,5,
        112,0,0,38,39,5,111,0,0,39,40,5,115,0,0,40,41,5,101,0,0,41,6,1,0,
        0,0,42,43,5,43,0,0,43,8,1,0,0,0,44,45,5,116,0,0,45,46,5,105,0,0,
        46,47,5,109,0,0,47,48,5,101,0,0,48,49,5,95,0,0,49,50,5,102,0,0,50,
        51,5,97,0,0,51,52,5,99,0,0,52,53,5,116,0,0,53,54,5,111,0,0,54,55,
        5,114,0,0,55,56,5,115,0,0,56,10,1,0,0,0,57,74,5,67,0,0,58,59,5,67,
        0,0,59,74,5,35,0,0,60,74,5,68,0,0,61,62,5,69,0,0,62,74,5,98,0,0,
        63,74,2,69,70,0,64,65,5,70,0,0,65,74,5,35,0,0,66,74,5,71,0,0,67,
        68,5,65,0,0,68,74,5,98,0,0,69,74,5,65,0,0,70,71,5,66,0,0,71,74,5,
        98,0,0,72,74,5,66,0,0,73,57,1,0,0,0,73,58,1,0,0,0,73,60,1,0,0,0,
        73,61,1,0,0,0,73,63,1,0,0,0,73,64,1,0,0,0,73,66,1,0,0,0,73,67,1,
        0,0,0,73,69,1,0,0,0,73,70,1,0,0,0,73,72,1,0,0,0,74,12,1,0,0,0,75,
        77,7,0,0,0,76,75,1,0,0,0,77,78,1,0,0,0,78,76,1,0,0,0,78,79,1,0,0,
        0,79,80,1,0,0,0,80,81,5,46,0,0,81,82,5,109,0,0,82,83,5,105,0,0,83,
        84,5,100,0,0,84,14,1,0,0,0,85,87,7,1,0,0,86,85,1,0,0,0,87,88,1,0,
        0,0,88,86,1,0,0,0,88,89,1,0,0,0,89,16,1,0,0,0,90,93,3,15,7,0,91,
        92,5,44,0,0,92,94,3,15,7,0,93,91,1,0,0,0,94,95,1,0,0,0,95,93,1,0,
        0,0,95,96,1,0,0,0,96,18,1,0,0,0,97,98,3,11,5,0,98,105,3,15,7,0,99,
        100,5,44,0,0,100,101,3,11,5,0,101,102,3,15,7,0,102,104,1,0,0,0,103,
        99,1,0,0,0,104,107,1,0,0,0,105,103,1,0,0,0,105,106,1,0,0,0,106,20,
        1,0,0,0,107,105,1,0,0,0,108,110,7,2,0,0,109,108,1,0,0,0,110,111,
        1,0,0,0,111,109,1,0,0,0,111,112,1,0,0,0,112,113,1,0,0,0,113,114,
        6,10,0,0,114,22,1,0,0,0,7,0,73,78,88,95,105,111,1,6,0,0
    ]

class HelloLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    NOTE = 6
    FILE_NAME = 7
    OCT = 8
    TIME_LIST = 9
    PARTITURE = 10
    WS = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'name'", "'tempo'", "'compose'", "'+'", "'time_factors'" ]

    symbolicNames = [ "<INVALID>",
            "NOTE", "FILE_NAME", "OCT", "TIME_LIST", "PARTITURE", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "NOTE", "FILE_NAME", 
                  "OCT", "TIME_LIST", "PARTITURE", "WS" ]

    grammarFileName = "Hello.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None

