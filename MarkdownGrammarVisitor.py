# Generated from MarkdownGrammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MarkdownGrammarParser import MarkdownGrammarParser
else:
    from MarkdownGrammarParser import MarkdownGrammarParser

# This class defines a complete generic visitor for a parse tree produced by MarkdownGrammarParser.

class MarkdownGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MarkdownGrammarParser#doc.
    def visitDoc(self, ctx:MarkdownGrammarParser.DocContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownGrammarParser#block.
    def visitBlock(self, ctx:MarkdownGrammarParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownGrammarParser#header.
    def visitHeader(self, ctx:MarkdownGrammarParser.HeaderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownGrammarParser#blockquote.
    def visitBlockquote(self, ctx:MarkdownGrammarParser.BlockquoteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownGrammarParser#blockquoteLine.
    def visitBlockquoteLine(self, ctx:MarkdownGrammarParser.BlockquoteLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownGrammarParser#list.
    def visitList(self, ctx:MarkdownGrammarParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownGrammarParser#unorderedItem.
    def visitUnorderedItem(self, ctx:MarkdownGrammarParser.UnorderedItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownGrammarParser#orderedItem.
    def visitOrderedItem(self, ctx:MarkdownGrammarParser.OrderedItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownGrammarParser#ul_marker.
    def visitUl_marker(self, ctx:MarkdownGrammarParser.Ul_markerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownGrammarParser#horizontalRule.
    def visitHorizontalRule(self, ctx:MarkdownGrammarParser.HorizontalRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownGrammarParser#table.
    def visitTable(self, ctx:MarkdownGrammarParser.TableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownGrammarParser#tableHeaderLine.
    def visitTableHeaderLine(self, ctx:MarkdownGrammarParser.TableHeaderLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownGrammarParser#tableSepLine.
    def visitTableSepLine(self, ctx:MarkdownGrammarParser.TableSepLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownGrammarParser#tableBodyLine.
    def visitTableBodyLine(self, ctx:MarkdownGrammarParser.TableBodyLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownGrammarParser#tableRow.
    def visitTableRow(self, ctx:MarkdownGrammarParser.TableRowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownGrammarParser#paragraph.
    def visitParagraph(self, ctx:MarkdownGrammarParser.ParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownGrammarParser#inlineContent.
    def visitInlineContent(self, ctx:MarkdownGrammarParser.InlineContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownGrammarParser#inlineItem.
    def visitInlineItem(self, ctx:MarkdownGrammarParser.InlineItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownGrammarParser#inlineItem_no_pipe.
    def visitInlineItem_no_pipe(self, ctx:MarkdownGrammarParser.InlineItem_no_pipeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownGrammarParser#bold_italic.
    def visitBold_italic(self, ctx:MarkdownGrammarParser.Bold_italicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownGrammarParser#bold.
    def visitBold(self, ctx:MarkdownGrammarParser.BoldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownGrammarParser#italic.
    def visitItalic(self, ctx:MarkdownGrammarParser.ItalicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownGrammarParser#strikethrough.
    def visitStrikethrough(self, ctx:MarkdownGrammarParser.StrikethroughContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownGrammarParser#link.
    def visitLink(self, ctx:MarkdownGrammarParser.LinkContext):
        return self.visitChildren(ctx)



del MarkdownGrammarParser