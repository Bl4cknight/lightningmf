from PySide.QtGui import *
from PySide.QtCore import Qt

class ProgressBar(QWidget):
    def __init__(self, label_text):
        QWidget.__init__(self)

        vbox = QVBoxLayout()
        self.label = QLabel(label_text)
        self.label.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.label)

        self.progress_bar = QProgressBar()
        self.progress_bar.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.progress_bar)

        self.setLayout(vbox)

    def setProgress(self, value):
        if value > 100:
            value = 100
        self.progress_bar.setValue(value)

    def resetProgress(self):
        self.progress_bar.setValue(0)

    def changeLabel(self, new_text):
        self.label.setText(new_text)
