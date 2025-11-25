from __future__ import annotations

from typing import List
from antlr4 import ParserRuleContext
from antlr4.tree.Tree import TerminalNode

from MarkdownGrammarParser import MarkdownGrammarParser
from MarkdownGrammarVisitor import MarkdownGrammarVisitor


class MarkdownToHtmlVisitor(MarkdownGrammarVisitor):
    """Convierte el parse tree de Markdown a HTML mediante el patrón visitor."""

    def visitDoc(self, ctx: MarkdownGrammarParser.DocContext) -> str:
        html_parts: List[str] = []
        for block in ctx.block():
            piece = self.visit(block)
            if piece:
                html_parts.append(piece)

        body_content = ''.join(html_parts)

        return f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Documento Generado</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 40px auto;
            max-width: 800px;
            padding: 0 10px;
            color: #333;
        }}
        blockquote {{
            border-left: 4px solid #ccc;
            margin: 1.5em 10px;
            padding: 0.5em 10px;
            color: #666;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin-bottom: 1em;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }}
        th {{
            background-color: #f2f2f2;
        }}
        code {{
            background-color: #f4f4f4;
            padding: 2px 4px;
            border-radius: 4px;
        }}
        hr {{
            border: 0;
            border-top: 1px solid #eee;
            margin: 20px 0;
        }}
    </style>
</head>
<body>
{body_content}
</body>
</html>"""

    # --- MÉTODO DE SEGURIDAD ---
    def visitTerminal(self, node: TerminalNode) -> str:
        # Si el visitor encuentra un token terminal (hoja) directamente, devuelve su texto.
        # Esto previene que devuelva None y rompa concatenaciones.
        return node.getText()

    def visitBlock(self, ctx: MarkdownGrammarParser.BlockContext) -> str:
        for child in ctx.getChildren():
            if isinstance(child, ParserRuleContext):
                return self.visit(child)
        return ''

    def visitHeader(self, ctx: MarkdownGrammarParser.HeaderContext) -> str:
        level = len(ctx.HASHES().getText())
        inline_ctx = ctx.inlineContent()
        content = self.visit(inline_ctx) if inline_ctx is not None else ''
        return f"<h{level}>{content}</h{level}>\n"

    def visitParagraph(self, ctx: MarkdownGrammarParser.ParagraphContext) -> str:
        content = self.visit(ctx.inlineContent())
        return f"<p>{content}</p>\n"

    def visitHorizontalRule(self, ctx: MarkdownGrammarParser.HorizontalRuleContext) -> str:
        return "<hr/>\n"

    def visitBlockquote(self, ctx: MarkdownGrammarParser.BlockquoteContext) -> str:
        lines: List[str] = []
        for line_ctx in ctx.blockquoteLine():
            if line_ctx.inlineContent():
                lines.append(self.visit(line_ctx.inlineContent()))
            else:
                lines.append('')
        inner = '<br/>'.join(lines)
        return f"<blockquote>{inner}</blockquote>\n"

    # --- INICIO LÓGICA DE TABLAS ---
    def visitTable(self, ctx: MarkdownGrammarParser.TableContext) -> str:
        header_html = self.visit(ctx.tableHeaderLine())

        body_parts = []
        for body_line in ctx.tableBodyLine():
            body_parts.append(self.visit(body_line))
        body_html = ''.join(body_parts)

        return f"""<table>
<thead>
{header_html}</thead>
<tbody>
{body_html}</tbody>
</table>
"""

    def visitTableHeaderLine(self, ctx: MarkdownGrammarParser.TableHeaderLineContext) -> str:
        row_html = self.visit(ctx.tableRow())
        return row_html.replace("<td>", "<th>").replace("</td>", "</th>")

    def visitTableSepLine(self, ctx: MarkdownGrammarParser.TableSepLineContext) -> str:
        return ""

    def visitTableBodyLine(self, ctx: MarkdownGrammarParser.TableBodyLineContext) -> str:
        return self.visit(ctx.tableRow())

    def visitTableRow(self, ctx: MarkdownGrammarParser.TableRowContext) -> str:
        cells = []
        current_cell_nodes = []

        # Obtenemos todos los hijos
        children = list(ctx.getChildren())

        # Bandera para saber si ya entramos a la zona de celdas (después del primer pipe)
        first_pipe_passed = False

        for child in children:
            text = child.getText()

            # Ignoramos espacios (WS) que estén ANTES del primer pipe
            if not first_pipe_passed:
                if text.strip() == '|':
                    first_pipe_passed = True
                continue

            # Procesamiento normal de celdas
            if text.strip() == '|':
                # Al encontrar un pipe de cierre, guardamos lo acumulado como celda
                cell_content = ""
                for node in current_cell_nodes:
                    res = self.visit(node)
                    if res is not None:
                        cell_content += res
                    else:
                        cell_content += node.getText()

                cells.append(f"<td>{cell_content.strip()}</td>")
                current_cell_nodes = []
            elif text.strip() == '' and ('\n' in text or '\r' in text):
                # Ignorar saltos de línea al final
                continue
            else:
                # Acumular contenido de la celda actual
                current_cell_nodes.append(child)

        return f"<tr>{''.join(cells)}</tr>\n"
    # --- FIN LÓGICA DE TABLAS ---

    def visitList(self, ctx: MarkdownGrammarParser.ListContext) -> str:
        items_ctx = ctx.listItem()
        if not items_ctx:
            return ''
        first = items_ctx[0]
        if isinstance(first, MarkdownGrammarParser.OrderedItemContext):
            open_tag, close_tag = '<ol>', '</ol>'
        else:
            open_tag, close_tag = '<ul>', '</ul>'

        items_html = []
        for item_ctx in items_ctx:
            items_html.append(self.visit(item_ctx))
        return f"{open_tag}\n{''.join(items_html)}{close_tag}\n"

    def visitUnorderedItem(self, ctx: MarkdownGrammarParser.UnorderedItemContext) -> str:
        content = self.visit(ctx.inlineContent())
        return f"<li>{content}</li>\n"

    def visitOrderedItem(self, ctx: MarkdownGrammarParser.OrderedItemContext) -> str:
        content = self.visit(ctx.inlineContent())
        return f"<li>{content}</li>\n"

    def visitInlineContent(self, ctx: MarkdownGrammarParser.InlineContentContext) -> str:
        parts: List[str] = []
        for item in ctx.inlineItem():
            parts.append(self.visit(item))
        return ''.join(parts)

    def visitInlineItem(self, ctx: MarkdownGrammarParser.InlineItemContext) -> str:
        # 1. Estructuras complejas: Delegamos a sus métodos específicos
        if ctx.link(): return self.visit(ctx.link())
        if ctx.bold_italic(): return self.visit(ctx.bold_italic())
        if ctx.bold(): return self.visit(ctx.bold())
        if ctx.italic(): return self.visit(ctx.italic())
        if ctx.strikethrough(): return self.visit(ctx.strikethrough())

        # 2. Todo lo demás (Texto plano, Puntuación, Espacios, Símbolos nuevos):
        # En lugar de listar cada token (DOT, STAR, etc.), simplemente devolvemos
        # el texto que capturó el parser. Esto cubre CUALQUIER token simple.
        return ctx.getText()

    def visitInlineItem_no_pipe(self, ctx: MarkdownGrammarParser.InlineItem_no_pipeContext) -> str:
        # Misma lógica simplificada para tablas
        if ctx.link(): return self.visit(ctx.link())
        if ctx.bold(): return self.visit(ctx.bold())
        if ctx.italic(): return self.visit(ctx.italic())
        if ctx.strikethrough(): return self.visit(ctx.strikethrough())

        # Devuelve el texto de cualquier otro token (TEXT, WS, DOT, números, etc.)
        return ctx.getText()

    def visitLink(self, ctx: MarkdownGrammarParser.LinkContext) -> str:
        text = self.visit(ctx.inlineContent())
        url = ctx.URL().getText()
        return f'<a href="{url}">{text}</a>'

    def visitBold(self, ctx: MarkdownGrammarParser.BoldContext) -> str:
        content = self.visit(ctx.inlineContent())
        return f'<strong>{content}</strong>'

    def visitItalic(self, ctx: MarkdownGrammarParser.ItalicContext) -> str:
        content = self.visit(ctx.inlineContent())
        return f'<em>{content}</em>'

    def visitBold_italic(self, ctx: MarkdownGrammarParser.Bold_italicContext) -> str:
        content = self.visit(ctx.inlineContent())
        return f'<strong><em>{content}</em></strong>'

    def visitStrikethrough(self, ctx: MarkdownGrammarParser.StrikethroughContext) -> str:
        content = self.visit(ctx.inlineContent())
        return f'<del>{content}</del>'

    # Ya no necesitamos visitText, visitDot, visitStar, etc. por separado
    # porque visitInlineItem los cubre todos con ctx.getText()

    def visitChildren(self, node):
        return ''.join([self.visit(child) for child in node.getChildren()])


def translate_markdown_to_html(md_text: str) -> str:
    from antlr4 import InputStream, CommonTokenStream
    from MarkdownGrammarLexer import MarkdownGrammarLexer
    lexer = MarkdownGrammarLexer(InputStream(md_text))
    token_stream = CommonTokenStream(lexer)
    parser = MarkdownGrammarParser(token_stream)
    tree = parser.doc()
    visitor = MarkdownToHtmlVisitor()
    return visitor.visit(tree)