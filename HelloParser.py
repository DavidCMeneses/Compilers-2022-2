# Generated from Hello.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,11,19,2,0,7,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,5,0,11,8,0,10,
        0,12,0,14,9,0,1,0,1,0,1,0,1,0,0,0,1,0,0,1,1,0,8,9,18,0,2,1,0,0,0,
        2,3,5,1,0,0,3,4,5,7,0,0,4,5,5,2,0,0,5,6,5,8,0,0,6,7,5,3,0,0,7,12,
        5,10,0,0,8,9,5,4,0,0,9,11,5,10,0,0,10,8,1,0,0,0,11,14,1,0,0,0,12,
        10,1,0,0,0,12,13,1,0,0,0,13,15,1,0,0,0,14,12,1,0,0,0,15,16,5,5,0,
        0,16,17,7,0,0,0,17,1,1,0,0,0,1,12
    ]

class HelloParser ( Parser ):

    grammarFileName = "Hello.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'name'", "'tempo'", "'compose'", "'+'", 
                     "'time_factors'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NOTE", "FILE_NAME", "OCT", 
                      "TIME_LIST", "PARTITURE", "WS" ]

    RULE_hi = 0

    ruleNames =  [ "hi" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    NOTE=6
    FILE_NAME=7
    OCT=8
    TIME_LIST=9
    PARTITURE=10
    WS=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class HiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FILE_NAME(self):
            return self.getToken(HelloParser.FILE_NAME, 0)

        def OCT(self, i:int=None):
            if i is None:
                return self.getTokens(HelloParser.OCT)
            else:
                return self.getToken(HelloParser.OCT, i)

        def PARTITURE(self, i:int=None):
            if i is None:
                return self.getTokens(HelloParser.PARTITURE)
            else:
                return self.getToken(HelloParser.PARTITURE, i)

        def TIME_LIST(self):
            return self.getToken(HelloParser.TIME_LIST, 0)

        def getRuleIndex(self):
            return HelloParser.RULE_hi

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHi" ):
                listener.enterHi(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHi" ):
                listener.exitHi(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHi" ):
                return visitor.visitHi(self)
            else:
                return visitor.visitChildren(self)




    def hi(self):

        localctx = HelloParser.HiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_hi)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(HelloParser.T__0)
            self.state = 3
            self.match(HelloParser.FILE_NAME)
            self.state = 4
            self.match(HelloParser.T__1)
            self.state = 5
            self.match(HelloParser.OCT)
            self.state = 6
            self.match(HelloParser.T__2)
            self.state = 7
            self.match(HelloParser.PARTITURE)
            self.state = 12
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 8
                self.match(HelloParser.T__3)
                self.state = 9
                self.match(HelloParser.PARTITURE)
                self.state = 14
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 15
            self.match(HelloParser.T__4)
            self.state = 16
            _la = self._input.LA(1)
            if not(_la==8 or _la==9):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





