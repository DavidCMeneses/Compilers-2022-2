
// Define a grammar called Hello
grammar Hello;
hi : 'name' FILE_NAME 'tempo' OCT 'compose' PARTITURE('+' PARTITURE)* 'time_factors' (TIME_LIST|OCT);
NOTE : 'C' | 'C#' | 'D' | 'Eb' | 'E' | 'F' | 'F#' | 'G' | 'Ab' | 'A' | 'Bb' | 'B';  
FILE_NAME : [a-zA-Z_]+'.mid';
OCT : [0-9]+;
TIME_LIST : OCT(','OCT)+;
PARTITURE : NOTE OCT (','NOTE OCT)*;
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
