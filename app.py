import sys
import os
import time
import pdfminer.high_level
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QAction, QTextEdit, QVBoxLayout, QWidget, QLabel, QSlider, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QRectF, QObject
from PyQt5.QtGui import QTextCursor, QPainter, QColor, QBrush, QPen, QFontMetrics

class ConvertThread(QThread):
    text_ready = pyqtSignal(str)

    def __init__(self, filename):
        QThread.__init__(self)
        self.filename = filename

    def run(self):
        text = pdfminer.high_level.extract_text(self.filename)
        self.text_ready.emit(text)

class Highlighter(QObject):
    def __init__(self, editor):
        super().__init__()
        self.editor = editor
        self.highlights = []

    def highlight(self, start, end):
        self.highlights.append((start, end))
        self.editor.setExtraSelections(self.highlights)

    def clear(self):
        self.highlights = []
        self.editor.setExtraSelections(self.highlights)

class AudioConverter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("PDF to Audio Converter")

        # Create actions for the menu
        open_action = QAction("Open PDF...", self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.open_file)

        quit_action = QAction("Quit", self)
        quit_action.setShortcut("Ctrl+Q")
        quit_action.triggered.connect(self.quit)

        # Create the menu bar and add actions
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        file_menu.addAction(open_action)
        file_menu.addAction(quit_action)

        # Create a widget for the editor and add it to the window
        self.editor = QTextEdit()
        self.editor.setReadOnly(True)
        self.highlighter = Highlighter(self.editor)
        self.setCentralWidget(self.editor)

        # Create a slider for adjusting the speed and add it to the window
        self.speed_label = QLabel("Speed")
        self.speed_slider = QSlider(Qt.Horizontal)
        self.speed_slider.setRange(1, 10)
        self.speed_slider.setValue(5)

        speed_layout = QHBoxLayout()
        speed_layout.addWidget(self.speed_label)
        speed_layout.addWidget(self.speed_slider)

        # Create a button for starting and stopping the audio conversion and add it to the window
        self.convert_button = QPushButton("Convert")
        self.convert_button.clicked.connect(self.convert)
        self.convert_button.setEnabled(False)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.convert_button)

        # Create a layout for the speed slider and button and add it to the window
        controls_layout = QVBoxLayout()
        controls_layout.addLayout(speed_layout)
        controls_layout.addLayout(button_layout)

        controls_widget = QWidget()
        controls_widget.setLayout(controls_layout)

        self.addDockWidget(Qt.BottomDockWidgetArea, controls_widget)

        self.show()

    def open_file(self):
        # Open a file dialog to select a PDF file
        filename, _ = QFileDialog.getOpenFileName(self, "Open PDF", "", "PDF Files (*.pdf)")

        if filename:
            # Create a thread for converting the PDF to text
            self.convert_thread = ConvertThread(filename)
            self.convert_thread.text_ready.connect(self.text_ready)
            self.convert_thread.start()

    def text_ready(self, text):
        # Set the text inthe editor and enable the convert button
        self.editor.setPlainText(text)
        self.convert_button.setEnabled(True)

def convert(self):
    # Get the text from the editor
    text = self.editor.toPlainText()

    # Get the font metrics to calculate the height of each line
    fm = self.editor.fontMetrics()
    line_height = fm.height()

    # Create a highlight brush and pen
    highlight_brush = QBrush(QColor(255, 255, 0, 128))
    highlight_pen = QPen(Qt.NoPen)

    # Create a QPainter to draw the highlights
    painter = QPainter(self.editor.viewport())

    # Create a list to store the highlight rectangles
    highlights = []

    # Create a thread for converting the text to audio
    self.audio_thread = QThread()
    self.audio_thread.started.connect(lambda: self.convert_button.setEnabled(False))
    self.audio_thread.finished.connect(lambda: self.convert_button.setEnabled(True))
    self.audio_thread.start()

    for i, line in enumerate(text.split("\n")):
        # Calculate the height of the line
        line_rect = fm.boundingRect(QRectF(0, 0, self.editor.viewport().width(), line_height), Qt.TextSingleLine, line)

        # Create a highlight rectangle for the line
        highlight_rect = QRectF(0, i * line_height, line_rect.width(), line_height)

        # Add the highlight rectangle to the list
        highlights.append(highlight_rect)

        # Highlight the current line in the editor
        self.highlighter.highlight(QTextCursor(self.editor.document().findBlockByLineNumber(i)), QTextCursor(self.editor.document().findBlockByLineNumber(i+1)))

        # Calculate the position and size of the highlight rectangle
        highlight_pos = self.editor.viewport().mapToGlobal(self.editor.mapFromGlobal(self.editor.pos())) + self.editor.cursorRect(QTextCursor(self.editor.document().findBlockByLineNumber(i))).topLeft()
        highlight_rect.moveTopLeft(highlight_pos)

        # Draw the highlight rectangle
        painter.setBrush(highlight_brush)
        painter.setPen(highlight_pen)
        painter.drawRect(highlight_rect)

        # Wait for a short time to simulate the text being read
        time.sleep(0.1 * (10 - self.speed_slider.value()))

    # Clear the highlights
    self.highlighter.clear()

    # Delete the QPainter
    del painter

#def quit(self):
    # Close the window
    #self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AudioConverter()
    sys.exit(app.exec_())
