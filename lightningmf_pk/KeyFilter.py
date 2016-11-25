from PySide.QtCore import Signal
from PySide import QtCore
from PySide import QtGui


class KeyFilter(QtCore.QObject):
    returnPressed = Signal()
    escapePressed = Signal()
    ctrlcPressed = Signal()

    def __init__(self):
        # Initialize the PunchingBag as a QObject
        QtCore.QObject.__init__(self)

    def eventFilter(self, receiver, event):
        if event.type() == QtCore.QEvent.KeyPress:
            if event.key() == QtCore.Qt.Key_Return:
                # print receiver
                # QtGui.QMessageBox.information(None, "Filtered Key Press Event!!", "You Pressed: " + event.text())
                self.returnPressed.emit()
                return True
            if int(event.modifiers()) == QtCore.Qt.ControlModifier:
                if event.key() == QtCore.Qt.Key_C:
                    self.ctrlcPressed.emit()
                    return True
            if event.key() == QtCore.Qt.Key_Escape:
                ret = QtGui.QMessageBox.question(None, "Quit Dialog", "Quit lightningmf now?",
                                                 buttons=QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
                                                 defaultButton=QtGui.QMessageBox.Yes)
                if ret == QtGui.QMessageBox.Yes:
                    self.escapePressed.emit()
                return True
            else:
                return False
        else:
            # Call Base Class Method to Continue Normal Event Processing
            return super(KeyFilter, self).eventFilter(receiver, event)
