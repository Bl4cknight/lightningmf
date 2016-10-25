from PySide.QtGui import *
from PySide.QtCore import Qt

class DownloadingWindow(QWidget):
    def __init__(self, label_text):
        QWidget.__init__(self)

        vbox = QVBoxLayout()
        label = QLabel(label_text)
        label.setAlignment(Qt.AlignCenter)
        vbox.addWidget(label)

        self.progress_bar = QProgressBar()
        self.progress_bar.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.progress_bar)

        self.setLayout(vbox)

    def setProgress(self, value):
        if value > 100:
            value = 100
        self.progress_bar.setValue(value)
