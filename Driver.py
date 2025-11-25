"""
Driver para convertir archivos Markdown a HTML usando la gramática y el visitor definidos
en MarkdownGrammar.g4 y MarkdownVisitor.py.  Este script se ejecuta desde la línea de
comandos indicando el archivo de entrada `.md` y el archivo de salida `.html`.

Uso:

    python Driver.py entrada.md salida.html

El script lee el contenido de entrada, asegura que termina con un salto de línea (para
evitar errores de análisis), parsea el texto con el lexer/parser de ANTLR y genera el
HTML correspondiente mediante el visitor.
"""

import sys
from antlr4 import InputStream, CommonTokenStream

from MarkdownGrammarLexer import MarkdownGrammarLexer
from MarkdownGrammarParser import MarkdownGrammarParser
from MarkdownVisitor import MarkdownToHtmlVisitor


def convert_markdown_to_html(text: str) -> str:
    """Convierte un texto en Markdown a una cadena HTML usando ANTLR."""
    # Asegurar un salto de línea final para que el parser no falle al final de archivo
    if not text.endswith("\n"):
        text += "\n"
    lexer = MarkdownGrammarLexer(InputStream(text))
    token_stream = CommonTokenStream(lexer)
    parser = MarkdownGrammarParser(token_stream)
    tree = parser.doc()
    visitor = MarkdownToHtmlVisitor()
    return visitor.visit(tree)


def convert_file(input_path: str, output_path: str) -> None:
    """Lee un archivo Markdown y escribe el HTML resultante en otro archivo."""
    with open(input_path, "r", encoding="utf-8") as f:
        md_text = f.read()
    html = convert_markdown_to_html(md_text)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)


if __name__ == "__main__":
    convert_file("entrada.md", "salida.html")