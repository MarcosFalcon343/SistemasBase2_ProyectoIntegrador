import sys
import os
import webbrowser
import tempfile
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QPushButton, QTextEdit, QFileDialog,
                             QSplitter, QMessageBox, QLabel, QDialog)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont

# --- IMPORTACIÓN DE TU LÓGICA ANTLR ---
try:
    from antlr4 import InputStream, CommonTokenStream
    from MarkdownGrammarLexer import MarkdownGrammarLexer
    from MarkdownGrammarParser import MarkdownGrammarParser
    from MarkdownVisitor import MarkdownToHtmlVisitor

    ANTLR_AVAILABLE = True
except ImportError:
    ANTLR_AVAILABLE = False
    print("ADVERTENCIA: No se encontraron los archivos de ANTLR (Lexer/Parser/Visitor).")
    print("Se usará un modo de simulación para la interfaz gráfica.")


class MarkdownConverter:
    """Clase encargada de la lógica de negocio y formateo."""

    @staticmethod
    def convert(text: str) -> str:
        """Convierte Markdown a HTML."""
        if not text.endswith("\n"):
            text += "\n"

        if ANTLR_AVAILABLE:
            try:
                lexer = MarkdownGrammarLexer(InputStream(text))
                token_stream = CommonTokenStream(lexer)
                parser = MarkdownGrammarParser(token_stream)
                tree = parser.doc()
                visitor = MarkdownToHtmlVisitor()
                return visitor.visit(tree)
            except Exception as e:
                return f"<div style='color:red;'>Error de Parsing: {str(e)}</div>"
        else:
            return f"<h1>Simulación</h1><p>{text}</p>"

    @staticmethod
    def generate_ast(text: str) -> str:
        """Genera el AST formateado con indentación para mejor lectura."""
        if not text.endswith("\n"):
            text += "\n"

        raw_ast = ""
        if ANTLR_AVAILABLE:
            try:
                lexer = MarkdownGrammarLexer(InputStream(text))
                token_stream = CommonTokenStream(lexer)
                parser = MarkdownGrammarParser(token_stream)
                tree = parser.doc()
                # Obtenemos la cadena LISP plana de ANTLR: (rule (child1) (child2))
                raw_ast = tree.toStringTree(recog=parser)
            except Exception as e:
                return f"Error generando AST: {str(e)}"
        else:
            # AST Simulado para pruebas sin librerías
            raw_ast = "(doc (header (level ##) (text Tabla de ejemplo)) (paragraph (text ...)))"

        # Formateamos la cadena plana a algo visualmente indentado
        return MarkdownConverter.format_ast_string(raw_ast)

    @staticmethod
    def format_ast_string(lisp_str: str) -> str:
        """
        Transforma una cadena estilo LISP '(a (b c))' en un árbol indentado:
        a
          b
            c
        """
        formatted_output = []
        indent_level = 0
        current_token = ""

        # Recorremos caracter por caracter para formatear
        # Nota: Esta es una lógica simple de visualización basada en paréntesis
        for char in lisp_str:
            if char == '(':
                if current_token.strip():
                    formatted_output.append(current_token.strip())
                    current_token = ""

                if formatted_output:  # Nueva línea para cada nodo nuevo
                    formatted_output.append("\n")

                formatted_output.append("    " * indent_level)  # Indentación
                formatted_output.append("├─ ")  # Adorno opcional
                indent_level += 1
            elif char == ')':
                if current_token.strip():
                    formatted_output.append(current_token.strip())
                    current_token = ""
                indent_level -= 1
            else:
                current_token += char

        if current_token.strip():
            formatted_output.append(current_token.strip())

        return "".join(formatted_output)


class ASTViewerDialog(QDialog):
    """Ventana secundaria para visualizar el AST."""

    def __init__(self, ast_content, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Visualizador de AST")
        self.resize(600, 800)

        layout = QVBoxLayout(self)

        lbl = QLabel("Árbol de Sintaxis Abstracta generado:")
        layout.addWidget(lbl)

        self.text_view = QTextEdit()
        self.text_view.setReadOnly(True)
        # Usamos fuente monoespaciada para que la indentación se vea perfecta
        self.text_view.setFont(QFont("Consolas", 10))
        self.text_view.setPlainText(ast_content)

        layout.addWidget(self.text_view)

        btn_close = QPushButton("Cerrar")
        btn_close.clicked.connect(self.accept)
        layout.addWidget(btn_close)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Traductor Markdown a HTML (ANTLR)")
        self.resize(1000, 700)

        # --- Temporizador ---
        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.setInterval(800)
        self.timer.timeout.connect(self.run_conversion)

        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)

        # --- BARRA SUPERIOR ---
        btn_layout = QHBoxLayout()
        btn_style = "QPushButton { background-color: #2b5b84; color: white; padding: 8px; border-radius: 4px; font-weight: bold; } QPushButton:hover { background-color: #3d7fb5; }"

        self.btn_open = QPushButton("Abrir Archivo")
        self.btn_open.setStyleSheet(btn_style)
        self.btn_open.clicked.connect(self.open_file)

        self.btn_ast = QPushButton("Generar AST")
        self.btn_ast.setStyleSheet(btn_style)
        self.btn_ast.clicked.connect(self.generate_and_save_ast)

        self.btn_convert = QPushButton("Convertir Manualmente")
        self.btn_convert.setStyleSheet(btn_style)
        self.btn_convert.clicked.connect(self.run_conversion)

        # Nuevo botón para abrir en navegador
        self.btn_browser = QPushButton("Abrir en Navegador")
        self.btn_browser.setStyleSheet(btn_style)
        self.btn_browser.clicked.connect(self.open_in_browser)

        self.btn_view_html = QPushButton("Ver HTML / Ocultar")
        self.btn_view_html.setStyleSheet(btn_style)
        self.btn_view_html.clicked.connect(self.toggle_preview)

        self.btn_close = QPushButton("Cerrar")
        self.btn_close.setStyleSheet("background-color: #d9534f; color: white; padding: 8px; border-radius: 4px;")
        self.btn_close.clicked.connect(self.close)

        btn_layout.addWidget(self.btn_open)
        btn_layout.addWidget(self.btn_ast)
        btn_layout.addWidget(self.btn_convert)
        btn_layout.addWidget(self.btn_browser)  # Agregado al layout
        btn_layout.addWidget(self.btn_view_html)
        btn_layout.addStretch()
        btn_layout.addWidget(self.btn_close)

        main_layout.addLayout(btn_layout)

        # --- ÁREA DE TRABAJO ---
        splitter = QSplitter(Qt.Horizontal)

        self.text_editor = QTextEdit()
        self.text_editor.setPlaceholderText("Escribe tu Markdown aquí o abre un archivo...")
        self.text_editor.setFont(QFont("Consolas", 11))
        self.text_editor.setStyleSheet("border: 1px solid #ccc; background-color: #f9f9f9;")
        self.text_editor.textChanged.connect(self.reset_timer)

        self.html_viewer = QTextEdit()
        self.html_viewer.setReadOnly(True)
        self.html_viewer.setPlaceholderText("Vista previa del HTML generado...")
        self.html_viewer.setStyleSheet("border: 1px solid #ccc; background-color: #ffffff;")

        splitter.addWidget(self.text_editor)
        splitter.addWidget(self.html_viewer)
        splitter.setSizes([500, 500])

        main_layout.addWidget(splitter, 1)  # Factor de estiramiento 1 para llenar pantalla

        self.status_label = QLabel("Listo.")
        main_layout.addWidget(self.status_label)

    def reset_timer(self):
        self.status_label.setText("Escribiendo... (Esperando para convertir)")
        self.timer.start()

    def run_conversion(self):
        markdown_text = self.text_editor.toPlainText()
        html_output = MarkdownConverter.convert(markdown_text)
        self.html_viewer.setHtml(html_output)
        self.status_label.setText("Conversión completada.")

    def open_file(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Abrir archivo Markdown", "",
                                                   "Markdown Files (*.md);;All Files (*)", options=options)
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    self.text_editor.setPlainText(content)
                    self.status_label.setText(f"Archivo cargado: {os.path.basename(file_path)}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo abrir el archivo:\n{e}")

    def generate_and_save_ast(self):
        """Genera el AST, lo guarda en archivo y lo muestra."""
        markdown_text = self.text_editor.toPlainText()
        ast_formatted = MarkdownConverter.generate_ast(markdown_text)

        # 1. Guardar Archivo
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self, "Guardar AST en archivo", "ast_output.txt",
                                                   "Text Files (*.txt);;All Files (*)", options=options)

        if file_path:
            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(ast_formatted)
                self.status_label.setText(f"AST guardado en: {file_path}")
            except Exception as e:
                QMessageBox.warning(self, "Error al guardar", f"No se pudo guardar el archivo:\n{e}")

        # 2. Mostrar Gráficamente (Texto Indentado)
        viewer = ASTViewerDialog(ast_formatted, self)
        viewer.exec_()

    def open_in_browser(self):
        """Genera el HTML y lo abre en el navegador web por defecto."""
        markdown_text = self.text_editor.toPlainText()
        html_output = MarkdownConverter.convert(markdown_text)

        try:
            # Creamos un archivo temporal con extensión .html
            # delete=False para que el archivo persista lo suficiente para ser abierto
            with tempfile.NamedTemporaryFile(delete=False, suffix='.html', mode='w', encoding='utf-8') as f:
                f.write(html_output)
                temp_path = f.name

            # Abrimos el archivo en el navegador
            webbrowser.open('file://' + temp_path)
            self.status_label.setText(f"Abierto en navegador: {temp_path}")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo abrir el navegador:\n{e}")

    def toggle_preview(self):
        if self.html_viewer.isVisible():
            self.html_viewer.hide()
        else:
            self.html_viewer.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())