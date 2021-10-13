# Generated from killComment.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\13")
        buf.write(";\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\6\2\f\n\2\r\2\16")
        buf.write("\2\r\3\2\3\2\3\3\3\3\7\3\24\n\3\f\3\16\3\27\13\3\3\3\3")
        buf.write("\3\5\3\33\n\3\3\4\3\4\5\4\37\n\4\3\4\3\4\5\4#\n\4\3\4")
        buf.write("\3\4\5\4\'\n\4\3\4\3\4\5\4+\n\4\3\4\3\4\5\4/\n\4\3\4\3")
        buf.write("\4\5\4\63\n\4\5\4\65\n\4\3\5\3\5\5\59\n\5\3\5\2\2\6\2")
        buf.write("\4\6\b\2\2\2F\2\13\3\2\2\2\4\32\3\2\2\2\6\64\3\2\2\2\b")
        buf.write("\66\3\2\2\2\n\f\5\4\3\2\13\n\3\2\2\2\f\r\3\2\2\2\r\13")
        buf.write("\3\2\2\2\r\16\3\2\2\2\16\17\3\2\2\2\17\20\7\2\2\3\20\3")
        buf.write("\3\2\2\2\21\25\5\b\5\2\22\24\5\6\4\2\23\22\3\2\2\2\24")
        buf.write("\27\3\2\2\2\25\23\3\2\2\2\25\26\3\2\2\2\26\33\3\2\2\2")
        buf.write("\27\25\3\2\2\2\30\33\5\6\4\2\31\33\7\t\2\2\32\21\3\2\2")
        buf.write("\2\32\30\3\2\2\2\32\31\3\2\2\2\33\5\3\2\2\2\34\36\7\3")
        buf.write("\2\2\35\37\7\t\2\2\36\35\3\2\2\2\36\37\3\2\2\2\37\65\3")
        buf.write("\2\2\2 \"\7\4\2\2!#\7\t\2\2\"!\3\2\2\2\"#\3\2\2\2#\65")
        buf.write("\3\2\2\2$&\7\5\2\2%\'\7\t\2\2&%\3\2\2\2&\'\3\2\2\2\'\65")
        buf.write("\3\2\2\2(*\7\6\2\2)+\7\t\2\2*)\3\2\2\2*+\3\2\2\2+\65\3")
        buf.write("\2\2\2,.\7\7\2\2-/\7\t\2\2.-\3\2\2\2./\3\2\2\2/\65\3\2")
        buf.write("\2\2\60\62\7\b\2\2\61\63\7\t\2\2\62\61\3\2\2\2\62\63\3")
        buf.write("\2\2\2\63\65\3\2\2\2\64\34\3\2\2\2\64 \3\2\2\2\64$\3\2")
        buf.write("\2\2\64(\3\2\2\2\64,\3\2\2\2\64\60\3\2\2\2\65\7\3\2\2")
        buf.write("\2\668\7\n\2\2\679\7\t\2\28\67\3\2\2\289\3\2\2\29\t\3")
        buf.write("\2\2\2\r\r\25\32\36\"&*.\62\648")
        return buf.getvalue()


class killCommentParser ( Parser ):

    grammarFileName = "killComment.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "COMMENT_HASHTAG", "COMMENT_TRIPLE_SINGLE_QUOTES", 
                      "COMMENT_TRIPLE_DOUBLE_QUOTES", "COMMENT_DOUBLE_SLASHES", 
                      "COMMENT_SLASH_STAR", "COMMENT_DOUBLE_HYPHEN", "NEWLINE", 
                      "ALL", "WS" ]

    RULE_program = 0
    RULE_line = 1
    RULE_comments = 2
    RULE_instruction = 3

    ruleNames =  [ "program", "line", "comments", "instruction" ]

    EOF = Token.EOF
    COMMENT_HASHTAG=1
    COMMENT_TRIPLE_SINGLE_QUOTES=2
    COMMENT_TRIPLE_DOUBLE_QUOTES=3
    COMMENT_DOUBLE_SLASHES=4
    COMMENT_SLASH_STAR=5
    COMMENT_DOUBLE_HYPHEN=6
    NEWLINE=7
    ALL=8
    WS=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(killCommentParser.EOF, 0)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(killCommentParser.LineContext)
            else:
                return self.getTypedRuleContext(killCommentParser.LineContext,i)


        def getRuleIndex(self):
            return killCommentParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = killCommentParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.line()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << killCommentParser.COMMENT_HASHTAG) | (1 << killCommentParser.COMMENT_TRIPLE_SINGLE_QUOTES) | (1 << killCommentParser.COMMENT_TRIPLE_DOUBLE_QUOTES) | (1 << killCommentParser.COMMENT_DOUBLE_SLASHES) | (1 << killCommentParser.COMMENT_SLASH_STAR) | (1 << killCommentParser.COMMENT_DOUBLE_HYPHEN) | (1 << killCommentParser.NEWLINE) | (1 << killCommentParser.ALL))) != 0)):
                    break

            self.state = 13
            self.match(killCommentParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruction(self):
            return self.getTypedRuleContext(killCommentParser.InstructionContext,0)


        def comments(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(killCommentParser.CommentsContext)
            else:
                return self.getTypedRuleContext(killCommentParser.CommentsContext,i)


        def NEWLINE(self):
            return self.getToken(killCommentParser.NEWLINE, 0)

        def getRuleIndex(self):
            return killCommentParser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)




    def line(self):

        localctx = killCommentParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        try:
            self.state = 24
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [killCommentParser.ALL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.instruction()
                self.state = 19
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 16
                        self.comments() 
                    self.state = 21
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                pass
            elif token in [killCommentParser.COMMENT_HASHTAG, killCommentParser.COMMENT_TRIPLE_SINGLE_QUOTES, killCommentParser.COMMENT_TRIPLE_DOUBLE_QUOTES, killCommentParser.COMMENT_DOUBLE_SLASHES, killCommentParser.COMMENT_SLASH_STAR, killCommentParser.COMMENT_DOUBLE_HYPHEN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 22
                self.comments()
                pass
            elif token in [killCommentParser.NEWLINE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 23
                self.match(killCommentParser.NEWLINE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CommentsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMENT_HASHTAG(self):
            return self.getToken(killCommentParser.COMMENT_HASHTAG, 0)

        def NEWLINE(self):
            return self.getToken(killCommentParser.NEWLINE, 0)

        def COMMENT_TRIPLE_SINGLE_QUOTES(self):
            return self.getToken(killCommentParser.COMMENT_TRIPLE_SINGLE_QUOTES, 0)

        def COMMENT_TRIPLE_DOUBLE_QUOTES(self):
            return self.getToken(killCommentParser.COMMENT_TRIPLE_DOUBLE_QUOTES, 0)

        def COMMENT_DOUBLE_SLASHES(self):
            return self.getToken(killCommentParser.COMMENT_DOUBLE_SLASHES, 0)

        def COMMENT_SLASH_STAR(self):
            return self.getToken(killCommentParser.COMMENT_SLASH_STAR, 0)

        def COMMENT_DOUBLE_HYPHEN(self):
            return self.getToken(killCommentParser.COMMENT_DOUBLE_HYPHEN, 0)

        def getRuleIndex(self):
            return killCommentParser.RULE_comments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComments" ):
                listener.enterComments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComments" ):
                listener.exitComments(self)




    def comments(self):

        localctx = killCommentParser.CommentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_comments)
        try:
            self.state = 50
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [killCommentParser.COMMENT_HASHTAG]:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.match(killCommentParser.COMMENT_HASHTAG)
                self.state = 28
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 27
                    self.match(killCommentParser.NEWLINE)


                pass
            elif token in [killCommentParser.COMMENT_TRIPLE_SINGLE_QUOTES]:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.match(killCommentParser.COMMENT_TRIPLE_SINGLE_QUOTES)
                self.state = 32
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 31
                    self.match(killCommentParser.NEWLINE)


                pass
            elif token in [killCommentParser.COMMENT_TRIPLE_DOUBLE_QUOTES]:
                self.enterOuterAlt(localctx, 3)
                self.state = 34
                self.match(killCommentParser.COMMENT_TRIPLE_DOUBLE_QUOTES)
                self.state = 36
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 35
                    self.match(killCommentParser.NEWLINE)


                pass
            elif token in [killCommentParser.COMMENT_DOUBLE_SLASHES]:
                self.enterOuterAlt(localctx, 4)
                self.state = 38
                self.match(killCommentParser.COMMENT_DOUBLE_SLASHES)
                self.state = 40
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 39
                    self.match(killCommentParser.NEWLINE)


                pass
            elif token in [killCommentParser.COMMENT_SLASH_STAR]:
                self.enterOuterAlt(localctx, 5)
                self.state = 42
                self.match(killCommentParser.COMMENT_SLASH_STAR)
                self.state = 44
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 43
                    self.match(killCommentParser.NEWLINE)


                pass
            elif token in [killCommentParser.COMMENT_DOUBLE_HYPHEN]:
                self.enterOuterAlt(localctx, 6)
                self.state = 46
                self.match(killCommentParser.COMMENT_DOUBLE_HYPHEN)
                self.state = 48
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 47
                    self.match(killCommentParser.NEWLINE)


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InstructionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ALL(self):
            return self.getToken(killCommentParser.ALL, 0)

        def NEWLINE(self):
            return self.getToken(killCommentParser.NEWLINE, 0)

        def getRuleIndex(self):
            return killCommentParser.RULE_instruction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruction" ):
                listener.enterInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruction" ):
                listener.exitInstruction(self)




    def instruction(self):

        localctx = killCommentParser.InstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_instruction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(killCommentParser.ALL)
            self.state = 54
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 53
                self.match(killCommentParser.NEWLINE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





