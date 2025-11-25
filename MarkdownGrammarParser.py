# Generated from MarkdownGrammar.g4 by ANTLR 4.13.2
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
        4,1,36,281,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,1,0,1,0,5,0,49,8,0,10,0,12,0,52,9,0,1,0,
        1,0,1,1,1,1,1,1,1,1,1,1,1,1,3,1,62,8,1,1,2,1,2,3,2,66,8,2,1,2,1,
        2,1,3,4,3,71,8,3,11,3,12,3,72,1,4,1,4,3,4,77,8,4,1,4,1,4,1,5,4,5,
        82,8,5,11,5,12,5,83,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,94,8,6,1,
        7,1,7,1,8,1,8,1,8,1,9,1,9,1,9,5,9,104,8,9,10,9,12,9,107,9,9,1,10,
        1,10,1,11,3,11,112,8,11,1,11,1,11,3,11,116,8,11,1,11,1,11,3,11,120,
        8,11,1,11,4,11,123,8,11,11,11,12,11,124,1,11,3,11,128,8,11,1,11,
        1,11,1,12,1,12,1,13,3,13,135,8,13,1,13,1,13,5,13,139,8,13,10,13,
        12,13,142,9,13,1,13,4,13,145,8,13,11,13,12,13,146,1,13,3,13,150,
        8,13,1,13,1,13,1,14,1,14,1,14,1,15,4,15,158,8,15,11,15,12,15,159,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,
        200,8,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,
        1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,
        1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,234,8,17,1,18,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,248,8,18,
        1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,258,8,19,1,20,1,20,
        1,20,1,20,1,20,1,20,1,20,1,20,3,20,268,8,20,1,21,1,21,1,21,1,21,
        1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,0,0,23,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,0,3,1,0,16,18,2,0,5,
        5,13,15,3,0,13,13,18,18,24,27,352,0,50,1,0,0,0,2,61,1,0,0,0,4,63,
        1,0,0,0,6,70,1,0,0,0,8,74,1,0,0,0,10,81,1,0,0,0,12,93,1,0,0,0,14,
        95,1,0,0,0,16,97,1,0,0,0,18,100,1,0,0,0,20,108,1,0,0,0,22,111,1,
        0,0,0,24,131,1,0,0,0,26,134,1,0,0,0,28,153,1,0,0,0,30,157,1,0,0,
        0,32,199,1,0,0,0,34,233,1,0,0,0,36,247,1,0,0,0,38,257,1,0,0,0,40,
        267,1,0,0,0,42,269,1,0,0,0,44,273,1,0,0,0,46,49,3,2,1,0,47,49,5,
        1,0,0,48,46,1,0,0,0,48,47,1,0,0,0,49,52,1,0,0,0,50,48,1,0,0,0,50,
        51,1,0,0,0,51,53,1,0,0,0,52,50,1,0,0,0,53,54,5,0,0,1,54,1,1,0,0,
        0,55,62,3,16,8,0,56,62,3,4,2,0,57,62,3,18,9,0,58,62,3,6,3,0,59,62,
        3,10,5,0,60,62,3,28,14,0,61,55,1,0,0,0,61,56,1,0,0,0,61,57,1,0,0,
        0,61,58,1,0,0,0,61,59,1,0,0,0,61,60,1,0,0,0,62,3,1,0,0,0,63,65,5,
        2,0,0,64,66,3,30,15,0,65,64,1,0,0,0,65,66,1,0,0,0,66,67,1,0,0,0,
        67,68,5,1,0,0,68,5,1,0,0,0,69,71,3,8,4,0,70,69,1,0,0,0,71,72,1,0,
        0,0,72,70,1,0,0,0,72,73,1,0,0,0,73,7,1,0,0,0,74,76,5,3,0,0,75,77,
        3,30,15,0,76,75,1,0,0,0,76,77,1,0,0,0,77,78,1,0,0,0,78,79,5,1,0,
        0,79,9,1,0,0,0,80,82,3,12,6,0,81,80,1,0,0,0,82,83,1,0,0,0,83,81,
        1,0,0,0,83,84,1,0,0,0,84,11,1,0,0,0,85,86,3,14,7,0,86,87,3,30,15,
        0,87,88,5,1,0,0,88,94,1,0,0,0,89,90,5,22,0,0,90,91,3,30,15,0,91,
        92,5,1,0,0,92,94,1,0,0,0,93,85,1,0,0,0,93,89,1,0,0,0,94,13,1,0,0,
        0,95,96,7,0,0,0,96,15,1,0,0,0,97,98,7,1,0,0,98,99,5,1,0,0,99,17,
        1,0,0,0,100,101,3,20,10,0,101,105,3,22,11,0,102,104,3,24,12,0,103,
        102,1,0,0,0,104,107,1,0,0,0,105,103,1,0,0,0,105,106,1,0,0,0,106,
        19,1,0,0,0,107,105,1,0,0,0,108,109,3,26,13,0,109,21,1,0,0,0,110,
        112,5,33,0,0,111,110,1,0,0,0,111,112,1,0,0,0,112,113,1,0,0,0,113,
        122,5,23,0,0,114,116,5,33,0,0,115,114,1,0,0,0,115,116,1,0,0,0,116,
        117,1,0,0,0,117,119,7,2,0,0,118,120,5,33,0,0,119,118,1,0,0,0,119,
        120,1,0,0,0,120,121,1,0,0,0,121,123,5,23,0,0,122,115,1,0,0,0,123,
        124,1,0,0,0,124,122,1,0,0,0,124,125,1,0,0,0,125,127,1,0,0,0,126,
        128,5,33,0,0,127,126,1,0,0,0,127,128,1,0,0,0,128,129,1,0,0,0,129,
        130,5,1,0,0,130,23,1,0,0,0,131,132,3,26,13,0,132,25,1,0,0,0,133,
        135,5,33,0,0,134,133,1,0,0,0,134,135,1,0,0,0,135,136,1,0,0,0,136,
        144,5,23,0,0,137,139,3,34,17,0,138,137,1,0,0,0,139,142,1,0,0,0,140,
        138,1,0,0,0,140,141,1,0,0,0,141,143,1,0,0,0,142,140,1,0,0,0,143,
        145,5,23,0,0,144,140,1,0,0,0,145,146,1,0,0,0,146,144,1,0,0,0,146,
        147,1,0,0,0,147,149,1,0,0,0,148,150,5,33,0,0,149,148,1,0,0,0,149,
        150,1,0,0,0,150,151,1,0,0,0,151,152,5,1,0,0,152,27,1,0,0,0,153,154,
        3,30,15,0,154,155,5,1,0,0,155,29,1,0,0,0,156,158,3,32,16,0,157,156,
        1,0,0,0,158,159,1,0,0,0,159,157,1,0,0,0,159,160,1,0,0,0,160,31,1,
        0,0,0,161,200,3,44,22,0,162,200,3,36,18,0,163,200,3,38,19,0,164,
        200,3,40,20,0,165,200,3,42,21,0,166,200,5,33,0,0,167,200,5,4,0,0,
        168,200,5,34,0,0,169,200,5,20,0,0,170,200,5,21,0,0,171,200,5,16,
        0,0,172,200,5,17,0,0,173,200,5,18,0,0,174,200,5,2,0,0,175,200,5,
        3,0,0,176,200,5,22,0,0,177,200,5,13,0,0,178,200,5,14,0,0,179,200,
        5,15,0,0,180,200,5,23,0,0,181,200,5,24,0,0,182,200,5,25,0,0,183,
        200,5,26,0,0,184,200,5,27,0,0,185,200,5,5,0,0,186,200,5,6,0,0,187,
        200,5,7,0,0,188,200,5,8,0,0,189,200,5,9,0,0,190,200,5,10,0,0,191,
        200,5,11,0,0,192,200,5,12,0,0,193,200,5,19,0,0,194,200,5,28,0,0,
        195,200,5,29,0,0,196,200,5,30,0,0,197,200,5,31,0,0,198,200,5,36,
        0,0,199,161,1,0,0,0,199,162,1,0,0,0,199,163,1,0,0,0,199,164,1,0,
        0,0,199,165,1,0,0,0,199,166,1,0,0,0,199,167,1,0,0,0,199,168,1,0,
        0,0,199,169,1,0,0,0,199,170,1,0,0,0,199,171,1,0,0,0,199,172,1,0,
        0,0,199,173,1,0,0,0,199,174,1,0,0,0,199,175,1,0,0,0,199,176,1,0,
        0,0,199,177,1,0,0,0,199,178,1,0,0,0,199,179,1,0,0,0,199,180,1,0,
        0,0,199,181,1,0,0,0,199,182,1,0,0,0,199,183,1,0,0,0,199,184,1,0,
        0,0,199,185,1,0,0,0,199,186,1,0,0,0,199,187,1,0,0,0,199,188,1,0,
        0,0,199,189,1,0,0,0,199,190,1,0,0,0,199,191,1,0,0,0,199,192,1,0,
        0,0,199,193,1,0,0,0,199,194,1,0,0,0,199,195,1,0,0,0,199,196,1,0,
        0,0,199,197,1,0,0,0,199,198,1,0,0,0,200,33,1,0,0,0,201,234,3,44,
        22,0,202,234,3,38,19,0,203,234,3,40,20,0,204,234,3,42,21,0,205,234,
        5,33,0,0,206,234,5,4,0,0,207,234,5,34,0,0,208,234,5,35,0,0,209,234,
        5,20,0,0,210,234,5,21,0,0,211,234,5,16,0,0,212,234,5,17,0,0,213,
        234,5,18,0,0,214,234,5,2,0,0,215,234,5,3,0,0,216,234,5,22,0,0,217,
        234,5,13,0,0,218,234,5,14,0,0,219,234,5,15,0,0,220,234,5,5,0,0,221,
        234,5,6,0,0,222,234,5,7,0,0,223,234,5,8,0,0,224,234,5,9,0,0,225,
        234,5,10,0,0,226,234,5,11,0,0,227,234,5,12,0,0,228,234,5,19,0,0,
        229,234,5,28,0,0,230,234,5,29,0,0,231,234,5,30,0,0,232,234,5,31,
        0,0,233,201,1,0,0,0,233,202,1,0,0,0,233,203,1,0,0,0,233,204,1,0,
        0,0,233,205,1,0,0,0,233,206,1,0,0,0,233,207,1,0,0,0,233,208,1,0,
        0,0,233,209,1,0,0,0,233,210,1,0,0,0,233,211,1,0,0,0,233,212,1,0,
        0,0,233,213,1,0,0,0,233,214,1,0,0,0,233,215,1,0,0,0,233,216,1,0,
        0,0,233,217,1,0,0,0,233,218,1,0,0,0,233,219,1,0,0,0,233,220,1,0,
        0,0,233,221,1,0,0,0,233,222,1,0,0,0,233,223,1,0,0,0,233,224,1,0,
        0,0,233,225,1,0,0,0,233,226,1,0,0,0,233,227,1,0,0,0,233,228,1,0,
        0,0,233,229,1,0,0,0,233,230,1,0,0,0,233,231,1,0,0,0,233,232,1,0,
        0,0,234,35,1,0,0,0,235,236,5,5,0,0,236,237,3,30,15,0,237,238,5,5,
        0,0,238,248,1,0,0,0,239,240,5,6,0,0,240,241,3,30,15,0,241,242,5,
        7,0,0,242,248,1,0,0,0,243,244,5,8,0,0,244,245,3,30,15,0,245,246,
        5,9,0,0,246,248,1,0,0,0,247,235,1,0,0,0,247,239,1,0,0,0,247,243,
        1,0,0,0,248,37,1,0,0,0,249,250,5,10,0,0,250,251,3,30,15,0,251,252,
        5,10,0,0,252,258,1,0,0,0,253,254,5,11,0,0,254,255,3,30,15,0,255,
        256,5,11,0,0,256,258,1,0,0,0,257,249,1,0,0,0,257,253,1,0,0,0,258,
        39,1,0,0,0,259,260,5,16,0,0,260,261,3,30,15,0,261,262,5,16,0,0,262,
        268,1,0,0,0,263,264,5,19,0,0,264,265,3,30,15,0,265,266,5,19,0,0,
        266,268,1,0,0,0,267,259,1,0,0,0,267,263,1,0,0,0,268,41,1,0,0,0,269,
        270,5,12,0,0,270,271,3,30,15,0,271,272,5,12,0,0,272,43,1,0,0,0,273,
        274,5,28,0,0,274,275,3,30,15,0,275,276,5,29,0,0,276,277,5,30,0,0,
        277,278,5,32,0,0,278,279,5,31,0,0,279,45,1,0,0,0,24,48,50,61,65,
        72,76,83,93,105,111,115,119,124,127,134,140,146,149,159,199,233,
        247,257,267
    ]

class MarkdownGrammarParser ( Parser ):

    grammarFileName = "MarkdownGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'>'", "<INVALID>", 
                     "'***'", "'**_'", "'_**'", "'__*'", "'*__'", "'**'", 
                     "'__'", "'~~'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'*'", "'+'", "'-'", "'_'", "'.'", "':'", "<INVALID>", 
                     "'|'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'['", "']'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "NEWLINE", "HASHES", "GT", "INDENT", 
                      "BOLD_ITALIC_STAR", "BOLD_ITALIC_STAR_UNDER_START", 
                      "BOLD_ITALIC_STAR_UNDER_END", "BOLD_ITALIC_UNDER_STAR_START", 
                      "BOLD_ITALIC_UNDER_STAR_END", "BOLD_STAR", "BOLD_UNDER", 
                      "STRIKE", "HR_DASH", "HR_STAR", "HR_UNDER", "STAR", 
                      "PLUS", "MINUS", "UNDER", "DOT", "COLON", "OL_NUM", 
                      "PIPE", "COLON_DASHES_COLON", "DASHES_COLON", "COLON_DASHES", 
                      "DASHES", "LBRACKET", "RBRACKET", "LPAREN", "RPAREN", 
                      "URL", "WS", "TEXT", "ANY_SYMBOL_NO_PIPE", "ANY_SYMBOL" ]

    RULE_doc = 0
    RULE_block = 1
    RULE_header = 2
    RULE_blockquote = 3
    RULE_blockquoteLine = 4
    RULE_list = 5
    RULE_listItem = 6
    RULE_ul_marker = 7
    RULE_horizontalRule = 8
    RULE_table = 9
    RULE_tableHeaderLine = 10
    RULE_tableSepLine = 11
    RULE_tableBodyLine = 12
    RULE_tableRow = 13
    RULE_paragraph = 14
    RULE_inlineContent = 15
    RULE_inlineItem = 16
    RULE_inlineItem_no_pipe = 17
    RULE_bold_italic = 18
    RULE_bold = 19
    RULE_italic = 20
    RULE_strikethrough = 21
    RULE_link = 22

    ruleNames =  [ "doc", "block", "header", "blockquote", "blockquoteLine", 
                   "list", "listItem", "ul_marker", "horizontalRule", "table", 
                   "tableHeaderLine", "tableSepLine", "tableBodyLine", "tableRow", 
                   "paragraph", "inlineContent", "inlineItem", "inlineItem_no_pipe", 
                   "bold_italic", "bold", "italic", "strikethrough", "link" ]

    EOF = Token.EOF
    NEWLINE=1
    HASHES=2
    GT=3
    INDENT=4
    BOLD_ITALIC_STAR=5
    BOLD_ITALIC_STAR_UNDER_START=6
    BOLD_ITALIC_STAR_UNDER_END=7
    BOLD_ITALIC_UNDER_STAR_START=8
    BOLD_ITALIC_UNDER_STAR_END=9
    BOLD_STAR=10
    BOLD_UNDER=11
    STRIKE=12
    HR_DASH=13
    HR_STAR=14
    HR_UNDER=15
    STAR=16
    PLUS=17
    MINUS=18
    UNDER=19
    DOT=20
    COLON=21
    OL_NUM=22
    PIPE=23
    COLON_DASHES_COLON=24
    DASHES_COLON=25
    COLON_DASHES=26
    DASHES=27
    LBRACKET=28
    RBRACKET=29
    LPAREN=30
    RPAREN=31
    URL=32
    WS=33
    TEXT=34
    ANY_SYMBOL_NO_PIPE=35
    ANY_SYMBOL=36

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class DocContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MarkdownGrammarParser.EOF, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MarkdownGrammarParser.BlockContext)
            else:
                return self.getTypedRuleContext(MarkdownGrammarParser.BlockContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MarkdownGrammarParser.NEWLINE)
            else:
                return self.getToken(MarkdownGrammarParser.NEWLINE, i)

        def getRuleIndex(self):
            return MarkdownGrammarParser.RULE_doc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoc" ):
                listener.enterDoc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoc" ):
                listener.exitDoc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDoc" ):
                return visitor.visitDoc(self)
            else:
                return visitor.visitChildren(self)




    def doc(self):

        localctx = MarkdownGrammarParser.DocContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_doc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 98784247806) != 0):
                self.state = 48
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 33, 34, 36]:
                    self.state = 46
                    self.block()
                    pass
                elif token in [1]:
                    self.state = 47
                    self.match(MarkdownGrammarParser.NEWLINE)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 53
            self.match(MarkdownGrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def horizontalRule(self):
            return self.getTypedRuleContext(MarkdownGrammarParser.HorizontalRuleContext,0)


        def header(self):
            return self.getTypedRuleContext(MarkdownGrammarParser.HeaderContext,0)


        def table(self):
            return self.getTypedRuleContext(MarkdownGrammarParser.TableContext,0)


        def blockquote(self):
            return self.getTypedRuleContext(MarkdownGrammarParser.BlockquoteContext,0)


        def list_(self):
            return self.getTypedRuleContext(MarkdownGrammarParser.ListContext,0)


        def paragraph(self):
            return self.getTypedRuleContext(MarkdownGrammarParser.ParagraphContext,0)


        def getRuleIndex(self):
            return MarkdownGrammarParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MarkdownGrammarParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_block)
        try:
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.horizontalRule()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.header()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 57
                self.table()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 58
                self.blockquote()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 59
                self.list_()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 60
                self.paragraph()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HeaderContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HASHES(self):
            return self.getToken(MarkdownGrammarParser.HASHES, 0)

        def NEWLINE(self):
            return self.getToken(MarkdownGrammarParser.NEWLINE, 0)

        def inlineContent(self):
            return self.getTypedRuleContext(MarkdownGrammarParser.InlineContentContext,0)


        def getRuleIndex(self):
            return MarkdownGrammarParser.RULE_header

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeader" ):
                listener.enterHeader(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeader" ):
                listener.exitHeader(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHeader" ):
                return visitor.visitHeader(self)
            else:
                return visitor.visitChildren(self)




    def header(self):

        localctx = MarkdownGrammarParser.HeaderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_header)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(MarkdownGrammarParser.HASHES)
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 98784247804) != 0):
                self.state = 64
                self.inlineContent()


            self.state = 67
            self.match(MarkdownGrammarParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockquoteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockquoteLine(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MarkdownGrammarParser.BlockquoteLineContext)
            else:
                return self.getTypedRuleContext(MarkdownGrammarParser.BlockquoteLineContext,i)


        def getRuleIndex(self):
            return MarkdownGrammarParser.RULE_blockquote

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockquote" ):
                listener.enterBlockquote(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockquote" ):
                listener.exitBlockquote(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockquote" ):
                return visitor.visitBlockquote(self)
            else:
                return visitor.visitChildren(self)




    def blockquote(self):

        localctx = MarkdownGrammarParser.BlockquoteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_blockquote)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 69
                    self.blockquoteLine()

                else:
                    raise NoViableAltException(self)
                self.state = 72 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockquoteLineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GT(self):
            return self.getToken(MarkdownGrammarParser.GT, 0)

        def NEWLINE(self):
            return self.getToken(MarkdownGrammarParser.NEWLINE, 0)

        def inlineContent(self):
            return self.getTypedRuleContext(MarkdownGrammarParser.InlineContentContext,0)


        def getRuleIndex(self):
            return MarkdownGrammarParser.RULE_blockquoteLine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockquoteLine" ):
                listener.enterBlockquoteLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockquoteLine" ):
                listener.exitBlockquoteLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockquoteLine" ):
                return visitor.visitBlockquoteLine(self)
            else:
                return visitor.visitChildren(self)




    def blockquoteLine(self):

        localctx = MarkdownGrammarParser.BlockquoteLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_blockquoteLine)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(MarkdownGrammarParser.GT)
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 98784247804) != 0):
                self.state = 75
                self.inlineContent()


            self.state = 78
            self.match(MarkdownGrammarParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def listItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MarkdownGrammarParser.ListItemContext)
            else:
                return self.getTypedRuleContext(MarkdownGrammarParser.ListItemContext,i)


        def getRuleIndex(self):
            return MarkdownGrammarParser.RULE_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList" ):
                return visitor.visitList(self)
            else:
                return visitor.visitChildren(self)




    def list_(self):

        localctx = MarkdownGrammarParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 80
                    self.listItem()

                else:
                    raise NoViableAltException(self)
                self.state = 83 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MarkdownGrammarParser.RULE_listItem

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class OrderedItemContext(ListItemContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MarkdownGrammarParser.ListItemContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OL_NUM(self):
            return self.getToken(MarkdownGrammarParser.OL_NUM, 0)
        def inlineContent(self):
            return self.getTypedRuleContext(MarkdownGrammarParser.InlineContentContext,0)

        def NEWLINE(self):
            return self.getToken(MarkdownGrammarParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrderedItem" ):
                listener.enterOrderedItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrderedItem" ):
                listener.exitOrderedItem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrderedItem" ):
                return visitor.visitOrderedItem(self)
            else:
                return visitor.visitChildren(self)


    class UnorderedItemContext(ListItemContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MarkdownGrammarParser.ListItemContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ul_marker(self):
            return self.getTypedRuleContext(MarkdownGrammarParser.Ul_markerContext,0)

        def inlineContent(self):
            return self.getTypedRuleContext(MarkdownGrammarParser.InlineContentContext,0)

        def NEWLINE(self):
            return self.getToken(MarkdownGrammarParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnorderedItem" ):
                listener.enterUnorderedItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnorderedItem" ):
                listener.exitUnorderedItem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnorderedItem" ):
                return visitor.visitUnorderedItem(self)
            else:
                return visitor.visitChildren(self)



    def listItem(self):

        localctx = MarkdownGrammarParser.ListItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_listItem)
        try:
            self.state = 93
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16, 17, 18]:
                localctx = MarkdownGrammarParser.UnorderedItemContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.ul_marker()
                self.state = 86
                self.inlineContent()
                self.state = 87
                self.match(MarkdownGrammarParser.NEWLINE)
                pass
            elif token in [22]:
                localctx = MarkdownGrammarParser.OrderedItemContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                self.match(MarkdownGrammarParser.OL_NUM)
                self.state = 90
                self.inlineContent()
                self.state = 91
                self.match(MarkdownGrammarParser.NEWLINE)
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


    class Ul_markerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(MarkdownGrammarParser.STAR, 0)

        def PLUS(self):
            return self.getToken(MarkdownGrammarParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(MarkdownGrammarParser.MINUS, 0)

        def getRuleIndex(self):
            return MarkdownGrammarParser.RULE_ul_marker

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUl_marker" ):
                listener.enterUl_marker(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUl_marker" ):
                listener.exitUl_marker(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUl_marker" ):
                return visitor.visitUl_marker(self)
            else:
                return visitor.visitChildren(self)




    def ul_marker(self):

        localctx = MarkdownGrammarParser.Ul_markerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_ul_marker)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 458752) != 0)):
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


    class HorizontalRuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(MarkdownGrammarParser.NEWLINE, 0)

        def HR_DASH(self):
            return self.getToken(MarkdownGrammarParser.HR_DASH, 0)

        def HR_STAR(self):
            return self.getToken(MarkdownGrammarParser.HR_STAR, 0)

        def HR_UNDER(self):
            return self.getToken(MarkdownGrammarParser.HR_UNDER, 0)

        def BOLD_ITALIC_STAR(self):
            return self.getToken(MarkdownGrammarParser.BOLD_ITALIC_STAR, 0)

        def getRuleIndex(self):
            return MarkdownGrammarParser.RULE_horizontalRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHorizontalRule" ):
                listener.enterHorizontalRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHorizontalRule" ):
                listener.exitHorizontalRule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHorizontalRule" ):
                return visitor.visitHorizontalRule(self)
            else:
                return visitor.visitChildren(self)




    def horizontalRule(self):

        localctx = MarkdownGrammarParser.HorizontalRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_horizontalRule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 57376) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 98
            self.match(MarkdownGrammarParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tableHeaderLine(self):
            return self.getTypedRuleContext(MarkdownGrammarParser.TableHeaderLineContext,0)


        def tableSepLine(self):
            return self.getTypedRuleContext(MarkdownGrammarParser.TableSepLineContext,0)


        def tableBodyLine(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MarkdownGrammarParser.TableBodyLineContext)
            else:
                return self.getTypedRuleContext(MarkdownGrammarParser.TableBodyLineContext,i)


        def getRuleIndex(self):
            return MarkdownGrammarParser.RULE_table

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTable" ):
                listener.enterTable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTable" ):
                listener.exitTable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTable" ):
                return visitor.visitTable(self)
            else:
                return visitor.visitChildren(self)




    def table(self):

        localctx = MarkdownGrammarParser.TableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_table)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.tableHeaderLine()
            self.state = 101
            self.tableSepLine()
            self.state = 105
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 102
                    self.tableBodyLine() 
                self.state = 107
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableHeaderLineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tableRow(self):
            return self.getTypedRuleContext(MarkdownGrammarParser.TableRowContext,0)


        def getRuleIndex(self):
            return MarkdownGrammarParser.RULE_tableHeaderLine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTableHeaderLine" ):
                listener.enterTableHeaderLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTableHeaderLine" ):
                listener.exitTableHeaderLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTableHeaderLine" ):
                return visitor.visitTableHeaderLine(self)
            else:
                return visitor.visitChildren(self)




    def tableHeaderLine(self):

        localctx = MarkdownGrammarParser.TableHeaderLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_tableHeaderLine)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.tableRow()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableSepLineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PIPE(self, i:int=None):
            if i is None:
                return self.getTokens(MarkdownGrammarParser.PIPE)
            else:
                return self.getToken(MarkdownGrammarParser.PIPE, i)

        def NEWLINE(self):
            return self.getToken(MarkdownGrammarParser.NEWLINE, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(MarkdownGrammarParser.WS)
            else:
                return self.getToken(MarkdownGrammarParser.WS, i)

        def DASHES(self, i:int=None):
            if i is None:
                return self.getTokens(MarkdownGrammarParser.DASHES)
            else:
                return self.getToken(MarkdownGrammarParser.DASHES, i)

        def HR_DASH(self, i:int=None):
            if i is None:
                return self.getTokens(MarkdownGrammarParser.HR_DASH)
            else:
                return self.getToken(MarkdownGrammarParser.HR_DASH, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(MarkdownGrammarParser.MINUS)
            else:
                return self.getToken(MarkdownGrammarParser.MINUS, i)

        def DASHES_COLON(self, i:int=None):
            if i is None:
                return self.getTokens(MarkdownGrammarParser.DASHES_COLON)
            else:
                return self.getToken(MarkdownGrammarParser.DASHES_COLON, i)

        def COLON_DASHES(self, i:int=None):
            if i is None:
                return self.getTokens(MarkdownGrammarParser.COLON_DASHES)
            else:
                return self.getToken(MarkdownGrammarParser.COLON_DASHES, i)

        def COLON_DASHES_COLON(self, i:int=None):
            if i is None:
                return self.getTokens(MarkdownGrammarParser.COLON_DASHES_COLON)
            else:
                return self.getToken(MarkdownGrammarParser.COLON_DASHES_COLON, i)

        def getRuleIndex(self):
            return MarkdownGrammarParser.RULE_tableSepLine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTableSepLine" ):
                listener.enterTableSepLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTableSepLine" ):
                listener.exitTableSepLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTableSepLine" ):
                return visitor.visitTableSepLine(self)
            else:
                return visitor.visitChildren(self)




    def tableSepLine(self):

        localctx = MarkdownGrammarParser.TableSepLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_tableSepLine)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 110
                self.match(MarkdownGrammarParser.WS)


            self.state = 113
            self.match(MarkdownGrammarParser.PIPE)
            self.state = 122 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 115
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==33:
                        self.state = 114
                        self.match(MarkdownGrammarParser.WS)


                    self.state = 117
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 251928576) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 119
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==33:
                        self.state = 118
                        self.match(MarkdownGrammarParser.WS)


                    self.state = 121
                    self.match(MarkdownGrammarParser.PIPE)

                else:
                    raise NoViableAltException(self)
                self.state = 124 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 126
                self.match(MarkdownGrammarParser.WS)


            self.state = 129
            self.match(MarkdownGrammarParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableBodyLineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tableRow(self):
            return self.getTypedRuleContext(MarkdownGrammarParser.TableRowContext,0)


        def getRuleIndex(self):
            return MarkdownGrammarParser.RULE_tableBodyLine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTableBodyLine" ):
                listener.enterTableBodyLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTableBodyLine" ):
                listener.exitTableBodyLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTableBodyLine" ):
                return visitor.visitTableBodyLine(self)
            else:
                return visitor.visitChildren(self)




    def tableBodyLine(self):

        localctx = MarkdownGrammarParser.TableBodyLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_tableBodyLine)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.tableRow()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableRowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PIPE(self, i:int=None):
            if i is None:
                return self.getTokens(MarkdownGrammarParser.PIPE)
            else:
                return self.getToken(MarkdownGrammarParser.PIPE, i)

        def NEWLINE(self):
            return self.getToken(MarkdownGrammarParser.NEWLINE, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(MarkdownGrammarParser.WS)
            else:
                return self.getToken(MarkdownGrammarParser.WS, i)

        def inlineItem_no_pipe(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MarkdownGrammarParser.InlineItem_no_pipeContext)
            else:
                return self.getTypedRuleContext(MarkdownGrammarParser.InlineItem_no_pipeContext,i)


        def getRuleIndex(self):
            return MarkdownGrammarParser.RULE_tableRow

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTableRow" ):
                listener.enterTableRow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTableRow" ):
                listener.exitTableRow(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTableRow" ):
                return visitor.visitTableRow(self)
            else:
                return visitor.visitChildren(self)




    def tableRow(self):

        localctx = MarkdownGrammarParser.TableRowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_tableRow)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 133
                self.match(MarkdownGrammarParser.WS)


            self.state = 136
            self.match(MarkdownGrammarParser.PIPE)
            self.state = 144 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 140
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 64164462588) != 0):
                        self.state = 137
                        self.inlineItem_no_pipe()
                        self.state = 142
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 143
                    self.match(MarkdownGrammarParser.PIPE)

                else:
                    raise NoViableAltException(self)
                self.state = 146 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 148
                self.match(MarkdownGrammarParser.WS)


            self.state = 151
            self.match(MarkdownGrammarParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParagraphContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def inlineContent(self):
            return self.getTypedRuleContext(MarkdownGrammarParser.InlineContentContext,0)


        def NEWLINE(self):
            return self.getToken(MarkdownGrammarParser.NEWLINE, 0)

        def getRuleIndex(self):
            return MarkdownGrammarParser.RULE_paragraph

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParagraph" ):
                listener.enterParagraph(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParagraph" ):
                listener.exitParagraph(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParagraph" ):
                return visitor.visitParagraph(self)
            else:
                return visitor.visitChildren(self)




    def paragraph(self):

        localctx = MarkdownGrammarParser.ParagraphContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_paragraph)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.inlineContent()
            self.state = 154
            self.match(MarkdownGrammarParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InlineContentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def inlineItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MarkdownGrammarParser.InlineItemContext)
            else:
                return self.getTypedRuleContext(MarkdownGrammarParser.InlineItemContext,i)


        def getRuleIndex(self):
            return MarkdownGrammarParser.RULE_inlineContent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInlineContent" ):
                listener.enterInlineContent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInlineContent" ):
                listener.exitInlineContent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInlineContent" ):
                return visitor.visitInlineContent(self)
            else:
                return visitor.visitChildren(self)




    def inlineContent(self):

        localctx = MarkdownGrammarParser.InlineContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_inlineContent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 156
                    self.inlineItem()

                else:
                    raise NoViableAltException(self)
                self.state = 159 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InlineItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def link(self):
            return self.getTypedRuleContext(MarkdownGrammarParser.LinkContext,0)


        def bold_italic(self):
            return self.getTypedRuleContext(MarkdownGrammarParser.Bold_italicContext,0)


        def bold(self):
            return self.getTypedRuleContext(MarkdownGrammarParser.BoldContext,0)


        def italic(self):
            return self.getTypedRuleContext(MarkdownGrammarParser.ItalicContext,0)


        def strikethrough(self):
            return self.getTypedRuleContext(MarkdownGrammarParser.StrikethroughContext,0)


        def WS(self):
            return self.getToken(MarkdownGrammarParser.WS, 0)

        def INDENT(self):
            return self.getToken(MarkdownGrammarParser.INDENT, 0)

        def TEXT(self):
            return self.getToken(MarkdownGrammarParser.TEXT, 0)

        def DOT(self):
            return self.getToken(MarkdownGrammarParser.DOT, 0)

        def COLON(self):
            return self.getToken(MarkdownGrammarParser.COLON, 0)

        def STAR(self):
            return self.getToken(MarkdownGrammarParser.STAR, 0)

        def PLUS(self):
            return self.getToken(MarkdownGrammarParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(MarkdownGrammarParser.MINUS, 0)

        def HASHES(self):
            return self.getToken(MarkdownGrammarParser.HASHES, 0)

        def GT(self):
            return self.getToken(MarkdownGrammarParser.GT, 0)

        def OL_NUM(self):
            return self.getToken(MarkdownGrammarParser.OL_NUM, 0)

        def HR_DASH(self):
            return self.getToken(MarkdownGrammarParser.HR_DASH, 0)

        def HR_STAR(self):
            return self.getToken(MarkdownGrammarParser.HR_STAR, 0)

        def HR_UNDER(self):
            return self.getToken(MarkdownGrammarParser.HR_UNDER, 0)

        def PIPE(self):
            return self.getToken(MarkdownGrammarParser.PIPE, 0)

        def COLON_DASHES_COLON(self):
            return self.getToken(MarkdownGrammarParser.COLON_DASHES_COLON, 0)

        def DASHES_COLON(self):
            return self.getToken(MarkdownGrammarParser.DASHES_COLON, 0)

        def COLON_DASHES(self):
            return self.getToken(MarkdownGrammarParser.COLON_DASHES, 0)

        def DASHES(self):
            return self.getToken(MarkdownGrammarParser.DASHES, 0)

        def BOLD_ITALIC_STAR(self):
            return self.getToken(MarkdownGrammarParser.BOLD_ITALIC_STAR, 0)

        def BOLD_ITALIC_STAR_UNDER_START(self):
            return self.getToken(MarkdownGrammarParser.BOLD_ITALIC_STAR_UNDER_START, 0)

        def BOLD_ITALIC_STAR_UNDER_END(self):
            return self.getToken(MarkdownGrammarParser.BOLD_ITALIC_STAR_UNDER_END, 0)

        def BOLD_ITALIC_UNDER_STAR_START(self):
            return self.getToken(MarkdownGrammarParser.BOLD_ITALIC_UNDER_STAR_START, 0)

        def BOLD_ITALIC_UNDER_STAR_END(self):
            return self.getToken(MarkdownGrammarParser.BOLD_ITALIC_UNDER_STAR_END, 0)

        def BOLD_STAR(self):
            return self.getToken(MarkdownGrammarParser.BOLD_STAR, 0)

        def BOLD_UNDER(self):
            return self.getToken(MarkdownGrammarParser.BOLD_UNDER, 0)

        def STRIKE(self):
            return self.getToken(MarkdownGrammarParser.STRIKE, 0)

        def UNDER(self):
            return self.getToken(MarkdownGrammarParser.UNDER, 0)

        def LBRACKET(self):
            return self.getToken(MarkdownGrammarParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(MarkdownGrammarParser.RBRACKET, 0)

        def LPAREN(self):
            return self.getToken(MarkdownGrammarParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MarkdownGrammarParser.RPAREN, 0)

        def ANY_SYMBOL(self):
            return self.getToken(MarkdownGrammarParser.ANY_SYMBOL, 0)

        def getRuleIndex(self):
            return MarkdownGrammarParser.RULE_inlineItem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInlineItem" ):
                listener.enterInlineItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInlineItem" ):
                listener.exitInlineItem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInlineItem" ):
                return visitor.visitInlineItem(self)
            else:
                return visitor.visitChildren(self)




    def inlineItem(self):

        localctx = MarkdownGrammarParser.InlineItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_inlineItem)
        try:
            self.state = 199
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self.link()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                self.bold_italic()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 163
                self.bold()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 164
                self.italic()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 165
                self.strikethrough()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 166
                self.match(MarkdownGrammarParser.WS)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 167
                self.match(MarkdownGrammarParser.INDENT)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 168
                self.match(MarkdownGrammarParser.TEXT)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 169
                self.match(MarkdownGrammarParser.DOT)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 170
                self.match(MarkdownGrammarParser.COLON)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 171
                self.match(MarkdownGrammarParser.STAR)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 172
                self.match(MarkdownGrammarParser.PLUS)
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 173
                self.match(MarkdownGrammarParser.MINUS)
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 174
                self.match(MarkdownGrammarParser.HASHES)
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 175
                self.match(MarkdownGrammarParser.GT)
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 176
                self.match(MarkdownGrammarParser.OL_NUM)
                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 177
                self.match(MarkdownGrammarParser.HR_DASH)
                pass

            elif la_ == 18:
                self.enterOuterAlt(localctx, 18)
                self.state = 178
                self.match(MarkdownGrammarParser.HR_STAR)
                pass

            elif la_ == 19:
                self.enterOuterAlt(localctx, 19)
                self.state = 179
                self.match(MarkdownGrammarParser.HR_UNDER)
                pass

            elif la_ == 20:
                self.enterOuterAlt(localctx, 20)
                self.state = 180
                self.match(MarkdownGrammarParser.PIPE)
                pass

            elif la_ == 21:
                self.enterOuterAlt(localctx, 21)
                self.state = 181
                self.match(MarkdownGrammarParser.COLON_DASHES_COLON)
                pass

            elif la_ == 22:
                self.enterOuterAlt(localctx, 22)
                self.state = 182
                self.match(MarkdownGrammarParser.DASHES_COLON)
                pass

            elif la_ == 23:
                self.enterOuterAlt(localctx, 23)
                self.state = 183
                self.match(MarkdownGrammarParser.COLON_DASHES)
                pass

            elif la_ == 24:
                self.enterOuterAlt(localctx, 24)
                self.state = 184
                self.match(MarkdownGrammarParser.DASHES)
                pass

            elif la_ == 25:
                self.enterOuterAlt(localctx, 25)
                self.state = 185
                self.match(MarkdownGrammarParser.BOLD_ITALIC_STAR)
                pass

            elif la_ == 26:
                self.enterOuterAlt(localctx, 26)
                self.state = 186
                self.match(MarkdownGrammarParser.BOLD_ITALIC_STAR_UNDER_START)
                pass

            elif la_ == 27:
                self.enterOuterAlt(localctx, 27)
                self.state = 187
                self.match(MarkdownGrammarParser.BOLD_ITALIC_STAR_UNDER_END)
                pass

            elif la_ == 28:
                self.enterOuterAlt(localctx, 28)
                self.state = 188
                self.match(MarkdownGrammarParser.BOLD_ITALIC_UNDER_STAR_START)
                pass

            elif la_ == 29:
                self.enterOuterAlt(localctx, 29)
                self.state = 189
                self.match(MarkdownGrammarParser.BOLD_ITALIC_UNDER_STAR_END)
                pass

            elif la_ == 30:
                self.enterOuterAlt(localctx, 30)
                self.state = 190
                self.match(MarkdownGrammarParser.BOLD_STAR)
                pass

            elif la_ == 31:
                self.enterOuterAlt(localctx, 31)
                self.state = 191
                self.match(MarkdownGrammarParser.BOLD_UNDER)
                pass

            elif la_ == 32:
                self.enterOuterAlt(localctx, 32)
                self.state = 192
                self.match(MarkdownGrammarParser.STRIKE)
                pass

            elif la_ == 33:
                self.enterOuterAlt(localctx, 33)
                self.state = 193
                self.match(MarkdownGrammarParser.UNDER)
                pass

            elif la_ == 34:
                self.enterOuterAlt(localctx, 34)
                self.state = 194
                self.match(MarkdownGrammarParser.LBRACKET)
                pass

            elif la_ == 35:
                self.enterOuterAlt(localctx, 35)
                self.state = 195
                self.match(MarkdownGrammarParser.RBRACKET)
                pass

            elif la_ == 36:
                self.enterOuterAlt(localctx, 36)
                self.state = 196
                self.match(MarkdownGrammarParser.LPAREN)
                pass

            elif la_ == 37:
                self.enterOuterAlt(localctx, 37)
                self.state = 197
                self.match(MarkdownGrammarParser.RPAREN)
                pass

            elif la_ == 38:
                self.enterOuterAlt(localctx, 38)
                self.state = 198
                self.match(MarkdownGrammarParser.ANY_SYMBOL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InlineItem_no_pipeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def link(self):
            return self.getTypedRuleContext(MarkdownGrammarParser.LinkContext,0)


        def bold(self):
            return self.getTypedRuleContext(MarkdownGrammarParser.BoldContext,0)


        def italic(self):
            return self.getTypedRuleContext(MarkdownGrammarParser.ItalicContext,0)


        def strikethrough(self):
            return self.getTypedRuleContext(MarkdownGrammarParser.StrikethroughContext,0)


        def WS(self):
            return self.getToken(MarkdownGrammarParser.WS, 0)

        def INDENT(self):
            return self.getToken(MarkdownGrammarParser.INDENT, 0)

        def TEXT(self):
            return self.getToken(MarkdownGrammarParser.TEXT, 0)

        def ANY_SYMBOL_NO_PIPE(self):
            return self.getToken(MarkdownGrammarParser.ANY_SYMBOL_NO_PIPE, 0)

        def DOT(self):
            return self.getToken(MarkdownGrammarParser.DOT, 0)

        def COLON(self):
            return self.getToken(MarkdownGrammarParser.COLON, 0)

        def STAR(self):
            return self.getToken(MarkdownGrammarParser.STAR, 0)

        def PLUS(self):
            return self.getToken(MarkdownGrammarParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(MarkdownGrammarParser.MINUS, 0)

        def HASHES(self):
            return self.getToken(MarkdownGrammarParser.HASHES, 0)

        def GT(self):
            return self.getToken(MarkdownGrammarParser.GT, 0)

        def OL_NUM(self):
            return self.getToken(MarkdownGrammarParser.OL_NUM, 0)

        def HR_DASH(self):
            return self.getToken(MarkdownGrammarParser.HR_DASH, 0)

        def HR_STAR(self):
            return self.getToken(MarkdownGrammarParser.HR_STAR, 0)

        def HR_UNDER(self):
            return self.getToken(MarkdownGrammarParser.HR_UNDER, 0)

        def BOLD_ITALIC_STAR(self):
            return self.getToken(MarkdownGrammarParser.BOLD_ITALIC_STAR, 0)

        def BOLD_ITALIC_STAR_UNDER_START(self):
            return self.getToken(MarkdownGrammarParser.BOLD_ITALIC_STAR_UNDER_START, 0)

        def BOLD_ITALIC_STAR_UNDER_END(self):
            return self.getToken(MarkdownGrammarParser.BOLD_ITALIC_STAR_UNDER_END, 0)

        def BOLD_ITALIC_UNDER_STAR_START(self):
            return self.getToken(MarkdownGrammarParser.BOLD_ITALIC_UNDER_STAR_START, 0)

        def BOLD_ITALIC_UNDER_STAR_END(self):
            return self.getToken(MarkdownGrammarParser.BOLD_ITALIC_UNDER_STAR_END, 0)

        def BOLD_STAR(self):
            return self.getToken(MarkdownGrammarParser.BOLD_STAR, 0)

        def BOLD_UNDER(self):
            return self.getToken(MarkdownGrammarParser.BOLD_UNDER, 0)

        def STRIKE(self):
            return self.getToken(MarkdownGrammarParser.STRIKE, 0)

        def UNDER(self):
            return self.getToken(MarkdownGrammarParser.UNDER, 0)

        def LBRACKET(self):
            return self.getToken(MarkdownGrammarParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(MarkdownGrammarParser.RBRACKET, 0)

        def LPAREN(self):
            return self.getToken(MarkdownGrammarParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MarkdownGrammarParser.RPAREN, 0)

        def getRuleIndex(self):
            return MarkdownGrammarParser.RULE_inlineItem_no_pipe

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInlineItem_no_pipe" ):
                listener.enterInlineItem_no_pipe(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInlineItem_no_pipe" ):
                listener.exitInlineItem_no_pipe(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInlineItem_no_pipe" ):
                return visitor.visitInlineItem_no_pipe(self)
            else:
                return visitor.visitChildren(self)




    def inlineItem_no_pipe(self):

        localctx = MarkdownGrammarParser.InlineItem_no_pipeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_inlineItem_no_pipe)
        try:
            self.state = 233
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 201
                self.link()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 202
                self.bold()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 203
                self.italic()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 204
                self.strikethrough()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 205
                self.match(MarkdownGrammarParser.WS)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 206
                self.match(MarkdownGrammarParser.INDENT)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 207
                self.match(MarkdownGrammarParser.TEXT)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 208
                self.match(MarkdownGrammarParser.ANY_SYMBOL_NO_PIPE)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 209
                self.match(MarkdownGrammarParser.DOT)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 210
                self.match(MarkdownGrammarParser.COLON)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 211
                self.match(MarkdownGrammarParser.STAR)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 212
                self.match(MarkdownGrammarParser.PLUS)
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 213
                self.match(MarkdownGrammarParser.MINUS)
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 214
                self.match(MarkdownGrammarParser.HASHES)
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 215
                self.match(MarkdownGrammarParser.GT)
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 216
                self.match(MarkdownGrammarParser.OL_NUM)
                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 217
                self.match(MarkdownGrammarParser.HR_DASH)
                pass

            elif la_ == 18:
                self.enterOuterAlt(localctx, 18)
                self.state = 218
                self.match(MarkdownGrammarParser.HR_STAR)
                pass

            elif la_ == 19:
                self.enterOuterAlt(localctx, 19)
                self.state = 219
                self.match(MarkdownGrammarParser.HR_UNDER)
                pass

            elif la_ == 20:
                self.enterOuterAlt(localctx, 20)
                self.state = 220
                self.match(MarkdownGrammarParser.BOLD_ITALIC_STAR)
                pass

            elif la_ == 21:
                self.enterOuterAlt(localctx, 21)
                self.state = 221
                self.match(MarkdownGrammarParser.BOLD_ITALIC_STAR_UNDER_START)
                pass

            elif la_ == 22:
                self.enterOuterAlt(localctx, 22)
                self.state = 222
                self.match(MarkdownGrammarParser.BOLD_ITALIC_STAR_UNDER_END)
                pass

            elif la_ == 23:
                self.enterOuterAlt(localctx, 23)
                self.state = 223
                self.match(MarkdownGrammarParser.BOLD_ITALIC_UNDER_STAR_START)
                pass

            elif la_ == 24:
                self.enterOuterAlt(localctx, 24)
                self.state = 224
                self.match(MarkdownGrammarParser.BOLD_ITALIC_UNDER_STAR_END)
                pass

            elif la_ == 25:
                self.enterOuterAlt(localctx, 25)
                self.state = 225
                self.match(MarkdownGrammarParser.BOLD_STAR)
                pass

            elif la_ == 26:
                self.enterOuterAlt(localctx, 26)
                self.state = 226
                self.match(MarkdownGrammarParser.BOLD_UNDER)
                pass

            elif la_ == 27:
                self.enterOuterAlt(localctx, 27)
                self.state = 227
                self.match(MarkdownGrammarParser.STRIKE)
                pass

            elif la_ == 28:
                self.enterOuterAlt(localctx, 28)
                self.state = 228
                self.match(MarkdownGrammarParser.UNDER)
                pass

            elif la_ == 29:
                self.enterOuterAlt(localctx, 29)
                self.state = 229
                self.match(MarkdownGrammarParser.LBRACKET)
                pass

            elif la_ == 30:
                self.enterOuterAlt(localctx, 30)
                self.state = 230
                self.match(MarkdownGrammarParser.RBRACKET)
                pass

            elif la_ == 31:
                self.enterOuterAlt(localctx, 31)
                self.state = 231
                self.match(MarkdownGrammarParser.LPAREN)
                pass

            elif la_ == 32:
                self.enterOuterAlt(localctx, 32)
                self.state = 232
                self.match(MarkdownGrammarParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bold_italicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOLD_ITALIC_STAR(self, i:int=None):
            if i is None:
                return self.getTokens(MarkdownGrammarParser.BOLD_ITALIC_STAR)
            else:
                return self.getToken(MarkdownGrammarParser.BOLD_ITALIC_STAR, i)

        def inlineContent(self):
            return self.getTypedRuleContext(MarkdownGrammarParser.InlineContentContext,0)


        def BOLD_ITALIC_STAR_UNDER_START(self):
            return self.getToken(MarkdownGrammarParser.BOLD_ITALIC_STAR_UNDER_START, 0)

        def BOLD_ITALIC_STAR_UNDER_END(self):
            return self.getToken(MarkdownGrammarParser.BOLD_ITALIC_STAR_UNDER_END, 0)

        def BOLD_ITALIC_UNDER_STAR_START(self):
            return self.getToken(MarkdownGrammarParser.BOLD_ITALIC_UNDER_STAR_START, 0)

        def BOLD_ITALIC_UNDER_STAR_END(self):
            return self.getToken(MarkdownGrammarParser.BOLD_ITALIC_UNDER_STAR_END, 0)

        def getRuleIndex(self):
            return MarkdownGrammarParser.RULE_bold_italic

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBold_italic" ):
                listener.enterBold_italic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBold_italic" ):
                listener.exitBold_italic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBold_italic" ):
                return visitor.visitBold_italic(self)
            else:
                return visitor.visitChildren(self)




    def bold_italic(self):

        localctx = MarkdownGrammarParser.Bold_italicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_bold_italic)
        try:
            self.state = 247
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.match(MarkdownGrammarParser.BOLD_ITALIC_STAR)
                self.state = 236
                self.inlineContent()
                self.state = 237
                self.match(MarkdownGrammarParser.BOLD_ITALIC_STAR)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
                self.match(MarkdownGrammarParser.BOLD_ITALIC_STAR_UNDER_START)
                self.state = 240
                self.inlineContent()
                self.state = 241
                self.match(MarkdownGrammarParser.BOLD_ITALIC_STAR_UNDER_END)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 243
                self.match(MarkdownGrammarParser.BOLD_ITALIC_UNDER_STAR_START)
                self.state = 244
                self.inlineContent()
                self.state = 245
                self.match(MarkdownGrammarParser.BOLD_ITALIC_UNDER_STAR_END)
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


    class BoldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOLD_STAR(self, i:int=None):
            if i is None:
                return self.getTokens(MarkdownGrammarParser.BOLD_STAR)
            else:
                return self.getToken(MarkdownGrammarParser.BOLD_STAR, i)

        def inlineContent(self):
            return self.getTypedRuleContext(MarkdownGrammarParser.InlineContentContext,0)


        def BOLD_UNDER(self, i:int=None):
            if i is None:
                return self.getTokens(MarkdownGrammarParser.BOLD_UNDER)
            else:
                return self.getToken(MarkdownGrammarParser.BOLD_UNDER, i)

        def getRuleIndex(self):
            return MarkdownGrammarParser.RULE_bold

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBold" ):
                listener.enterBold(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBold" ):
                listener.exitBold(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBold" ):
                return visitor.visitBold(self)
            else:
                return visitor.visitChildren(self)




    def bold(self):

        localctx = MarkdownGrammarParser.BoldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_bold)
        try:
            self.state = 257
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 249
                self.match(MarkdownGrammarParser.BOLD_STAR)
                self.state = 250
                self.inlineContent()
                self.state = 251
                self.match(MarkdownGrammarParser.BOLD_STAR)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 253
                self.match(MarkdownGrammarParser.BOLD_UNDER)
                self.state = 254
                self.inlineContent()
                self.state = 255
                self.match(MarkdownGrammarParser.BOLD_UNDER)
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


    class ItalicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self, i:int=None):
            if i is None:
                return self.getTokens(MarkdownGrammarParser.STAR)
            else:
                return self.getToken(MarkdownGrammarParser.STAR, i)

        def inlineContent(self):
            return self.getTypedRuleContext(MarkdownGrammarParser.InlineContentContext,0)


        def UNDER(self, i:int=None):
            if i is None:
                return self.getTokens(MarkdownGrammarParser.UNDER)
            else:
                return self.getToken(MarkdownGrammarParser.UNDER, i)

        def getRuleIndex(self):
            return MarkdownGrammarParser.RULE_italic

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItalic" ):
                listener.enterItalic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItalic" ):
                listener.exitItalic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItalic" ):
                return visitor.visitItalic(self)
            else:
                return visitor.visitChildren(self)




    def italic(self):

        localctx = MarkdownGrammarParser.ItalicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_italic)
        try:
            self.state = 267
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 259
                self.match(MarkdownGrammarParser.STAR)
                self.state = 260
                self.inlineContent()
                self.state = 261
                self.match(MarkdownGrammarParser.STAR)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 263
                self.match(MarkdownGrammarParser.UNDER)
                self.state = 264
                self.inlineContent()
                self.state = 265
                self.match(MarkdownGrammarParser.UNDER)
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


    class StrikethroughContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRIKE(self, i:int=None):
            if i is None:
                return self.getTokens(MarkdownGrammarParser.STRIKE)
            else:
                return self.getToken(MarkdownGrammarParser.STRIKE, i)

        def inlineContent(self):
            return self.getTypedRuleContext(MarkdownGrammarParser.InlineContentContext,0)


        def getRuleIndex(self):
            return MarkdownGrammarParser.RULE_strikethrough

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStrikethrough" ):
                listener.enterStrikethrough(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStrikethrough" ):
                listener.exitStrikethrough(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStrikethrough" ):
                return visitor.visitStrikethrough(self)
            else:
                return visitor.visitChildren(self)




    def strikethrough(self):

        localctx = MarkdownGrammarParser.StrikethroughContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_strikethrough)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(MarkdownGrammarParser.STRIKE)
            self.state = 270
            self.inlineContent()
            self.state = 271
            self.match(MarkdownGrammarParser.STRIKE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LinkContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(MarkdownGrammarParser.LBRACKET, 0)

        def inlineContent(self):
            return self.getTypedRuleContext(MarkdownGrammarParser.InlineContentContext,0)


        def RBRACKET(self):
            return self.getToken(MarkdownGrammarParser.RBRACKET, 0)

        def LPAREN(self):
            return self.getToken(MarkdownGrammarParser.LPAREN, 0)

        def URL(self):
            return self.getToken(MarkdownGrammarParser.URL, 0)

        def RPAREN(self):
            return self.getToken(MarkdownGrammarParser.RPAREN, 0)

        def getRuleIndex(self):
            return MarkdownGrammarParser.RULE_link

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLink" ):
                listener.enterLink(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLink" ):
                listener.exitLink(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLink" ):
                return visitor.visitLink(self)
            else:
                return visitor.visitChildren(self)




    def link(self):

        localctx = MarkdownGrammarParser.LinkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_link)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.match(MarkdownGrammarParser.LBRACKET)
            self.state = 274
            self.inlineContent()
            self.state = 275
            self.match(MarkdownGrammarParser.RBRACKET)
            self.state = 276
            self.match(MarkdownGrammarParser.LPAREN)
            self.state = 277
            self.match(MarkdownGrammarParser.URL)
            self.state = 278
            self.match(MarkdownGrammarParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





