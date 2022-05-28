import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton,
                             QLabel, QLineEdit, QGridLayout, QMessageBox)

class Kemu(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.imageLabel = QLabel("Image file location:")
        self.imageLine = QLineEdit()

        self.memoryLabel = QLabel("Memory file location:")
        self.memoryLine = QLineEdit()

        self.otherLabel = QLabel("Other command line arguments:")
        self.otherLine = QLineEdit()

        self.runButton = QPushButton("Run")
        self.runButton.clicked.connect(self.onRun)

        self.aboutButton = QPushButton("About")
        self.aboutButton.clicked.connect(self.onAbout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(10)

        self.gridLayout.addWidget(self.imageLabel, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.imageLine, 1, 1, 1, 3)

        self.gridLayout.addWidget(self.memoryLabel, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.memoryLine, 2, 1, 1, 3)

        self.gridLayout.addWidget(self.otherLabel, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.otherLine, 3, 1, 1, 3)

        self.gridLayout.addWidget(self.runButton, 4, 0, 1, 4)
        self.gridLayout.addWidget(self.aboutButton, 5, 0, 1, 4)

        self.setLayout(self.gridLayout)
        self.setFixedSize(500, 200)
        self.center()
        self.setWindowTitle("Kemu")
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()

        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Exiting Kemu", "Are you sure to quit?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()

    def onAbout(self, event):
        print("About")  # DEBUG

    def onRun(self, event):
        print("Run")  # DEBUG

def main(args):
    app = QApplication(sys.argv)
    kemu = Kemu()
    return app.exec()

if __name__ == "__main__":
    sys.exit(main(sys.argv))