# Generated from MarkdownGrammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MarkdownGrammarParser import MarkdownGrammarParser
else:
    from MarkdownGrammarParser import MarkdownGrammarParser

# This class defines a complete listener for a parse tree produced by MarkdownGrammarParser.
class MarkdownGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by MarkdownGrammarParser#doc.
    def enterDoc(self, ctx:MarkdownGrammarParser.DocContext):
        pass

    # Exit a parse tree produced by MarkdownGrammarParser#doc.
    def exitDoc(self, ctx:MarkdownGrammarParser.DocContext):
        pass


    # Enter a parse tree produced by MarkdownGrammarParser#block.
    def enterBlock(self, ctx:MarkdownGrammarParser.BlockContext):
        pass

    # Exit a parse tree produced by MarkdownGrammarParser#block.
    def exitBlock(self, ctx:MarkdownGrammarParser.BlockContext):
        pass


    # Enter a parse tree produced by MarkdownGrammarParser#header.
    def enterHeader(self, ctx:MarkdownGrammarParser.HeaderContext):
        pass

    # Exit a parse tree produced by MarkdownGrammarParser#header.
    def exitHeader(self, ctx:MarkdownGrammarParser.HeaderContext):
        pass


    # Enter a parse tree produced by MarkdownGrammarParser#blockquote.
    def enterBlockquote(self, ctx:MarkdownGrammarParser.BlockquoteContext):
        pass

    # Exit a parse tree produced by MarkdownGrammarParser#blockquote.
    def exitBlockquote(self, ctx:MarkdownGrammarParser.BlockquoteContext):
        pass


    # Enter a parse tree produced by MarkdownGrammarParser#blockquoteLine.
    def enterBlockquoteLine(self, ctx:MarkdownGrammarParser.BlockquoteLineContext):
        pass

    # Exit a parse tree produced by MarkdownGrammarParser#blockquoteLine.
    def exitBlockquoteLine(self, ctx:MarkdownGrammarParser.BlockquoteLineContext):
        pass


    # Enter a parse tree produced by MarkdownGrammarParser#list.
    def enterList(self, ctx:MarkdownGrammarParser.ListContext):
        pass

    # Exit a parse tree produced by MarkdownGrammarParser#list.
    def exitList(self, ctx:MarkdownGrammarParser.ListContext):
        pass


    # Enter a parse tree produced by MarkdownGrammarParser#unorderedItem.
    def enterUnorderedItem(self, ctx:MarkdownGrammarParser.UnorderedItemContext):
        pass

    # Exit a parse tree produced by MarkdownGrammarParser#unorderedItem.
    def exitUnorderedItem(self, ctx:MarkdownGrammarParser.UnorderedItemContext):
        pass


    # Enter a parse tree produced by MarkdownGrammarParser#orderedItem.
    def enterOrderedItem(self, ctx:MarkdownGrammarParser.OrderedItemContext):
        pass

    # Exit a parse tree produced by MarkdownGrammarParser#orderedItem.
    def exitOrderedItem(self, ctx:MarkdownGrammarParser.OrderedItemContext):
        pass


    # Enter a parse tree produced by MarkdownGrammarParser#ul_marker.
    def enterUl_marker(self, ctx:MarkdownGrammarParser.Ul_markerContext):
        pass

    # Exit a parse tree produced by MarkdownGrammarParser#ul_marker.
    def exitUl_marker(self, ctx:MarkdownGrammarParser.Ul_markerContext):
        pass


    # Enter a parse tree produced by MarkdownGrammarParser#horizontalRule.
    def enterHorizontalRule(self, ctx:MarkdownGrammarParser.HorizontalRuleContext):
        pass

    # Exit a parse tree produced by MarkdownGrammarParser#horizontalRule.
    def exitHorizontalRule(self, ctx:MarkdownGrammarParser.HorizontalRuleContext):
        pass


    # Enter a parse tree produced by MarkdownGrammarParser#table.
    def enterTable(self, ctx:MarkdownGrammarParser.TableContext):
        pass

    # Exit a parse tree produced by MarkdownGrammarParser#table.
    def exitTable(self, ctx:MarkdownGrammarParser.TableContext):
        pass


    # Enter a parse tree produced by MarkdownGrammarParser#tableHeaderLine.
    def enterTableHeaderLine(self, ctx:MarkdownGrammarParser.TableHeaderLineContext):
        pass

    # Exit a parse tree produced by MarkdownGrammarParser#tableHeaderLine.
    def exitTableHeaderLine(self, ctx:MarkdownGrammarParser.TableHeaderLineContext):
        pass


    # Enter a parse tree produced by MarkdownGrammarParser#tableSepLine.
    def enterTableSepLine(self, ctx:MarkdownGrammarParser.TableSepLineContext):
        pass

    # Exit a parse tree produced by MarkdownGrammarParser#tableSepLine.
    def exitTableSepLine(self, ctx:MarkdownGrammarParser.TableSepLineContext):
        pass


    # Enter a parse tree produced by MarkdownGrammarParser#tableBodyLine.
    def enterTableBodyLine(self, ctx:MarkdownGrammarParser.TableBodyLineContext):
        pass

    # Exit a parse tree produced by MarkdownGrammarParser#tableBodyLine.
    def exitTableBodyLine(self, ctx:MarkdownGrammarParser.TableBodyLineContext):
        pass


    # Enter a parse tree produced by MarkdownGrammarParser#tableRow.
    def enterTableRow(self, ctx:MarkdownGrammarParser.TableRowContext):
        pass

    # Exit a parse tree produced by MarkdownGrammarParser#tableRow.
    def exitTableRow(self, ctx:MarkdownGrammarParser.TableRowContext):
        pass


    # Enter a parse tree produced by MarkdownGrammarParser#paragraph.
    def enterParagraph(self, ctx:MarkdownGrammarParser.ParagraphContext):
        pass

    # Exit a parse tree produced by MarkdownGrammarParser#paragraph.
    def exitParagraph(self, ctx:MarkdownGrammarParser.ParagraphContext):
        pass


    # Enter a parse tree produced by MarkdownGrammarParser#inlineContent.
    def enterInlineContent(self, ctx:MarkdownGrammarParser.InlineContentContext):
        pass

    # Exit a parse tree produced by MarkdownGrammarParser#inlineContent.
    def exitInlineContent(self, ctx:MarkdownGrammarParser.InlineContentContext):
        pass


    # Enter a parse tree produced by MarkdownGrammarParser#inlineItem.
    def enterInlineItem(self, ctx:MarkdownGrammarParser.InlineItemContext):
        pass

    # Exit a parse tree produced by MarkdownGrammarParser#inlineItem.
    def exitInlineItem(self, ctx:MarkdownGrammarParser.InlineItemContext):
        pass


    # Enter a parse tree produced by MarkdownGrammarParser#inlineItem_no_pipe.
    def enterInlineItem_no_pipe(self, ctx:MarkdownGrammarParser.InlineItem_no_pipeContext):
        pass

    # Exit a parse tree produced by MarkdownGrammarParser#inlineItem_no_pipe.
    def exitInlineItem_no_pipe(self, ctx:MarkdownGrammarParser.InlineItem_no_pipeContext):
        pass


    # Enter a parse tree produced by MarkdownGrammarParser#bold_italic.
    def enterBold_italic(self, ctx:MarkdownGrammarParser.Bold_italicContext):
        pass

    # Exit a parse tree produced by MarkdownGrammarParser#bold_italic.
    def exitBold_italic(self, ctx:MarkdownGrammarParser.Bold_italicContext):
        pass


    # Enter a parse tree produced by MarkdownGrammarParser#bold.
    def enterBold(self, ctx:MarkdownGrammarParser.BoldContext):
        pass

    # Exit a parse tree produced by MarkdownGrammarParser#bold.
    def exitBold(self, ctx:MarkdownGrammarParser.BoldContext):
        pass


    # Enter a parse tree produced by MarkdownGrammarParser#italic.
    def enterItalic(self, ctx:MarkdownGrammarParser.ItalicContext):
        pass

    # Exit a parse tree produced by MarkdownGrammarParser#italic.
    def exitItalic(self, ctx:MarkdownGrammarParser.ItalicContext):
        pass


    # Enter a parse tree produced by MarkdownGrammarParser#strikethrough.
    def enterStrikethrough(self, ctx:MarkdownGrammarParser.StrikethroughContext):
        pass

    # Exit a parse tree produced by MarkdownGrammarParser#strikethrough.
    def exitStrikethrough(self, ctx:MarkdownGrammarParser.StrikethroughContext):
        pass


    # Enter a parse tree produced by MarkdownGrammarParser#link.
    def enterLink(self, ctx:MarkdownGrammarParser.LinkContext):
        pass

    # Exit a parse tree produced by MarkdownGrammarParser#link.
    def exitLink(self, ctx:MarkdownGrammarParser.LinkContext):
        pass



del MarkdownGrammarParser