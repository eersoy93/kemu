# Kemu main script
# Copyright (C) 2022 Erdem Ersoy (eersoy93)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import subprocess
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton,
                             QLabel, QLineEdit, QGridLayout, QMessageBox)

from version import KEMU_VERSION

class Kemu(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.imageLabel = QLabel("CD-ROM Image file location:")
        self.imageLine = QLineEdit()

        self.memoryLabel = QLabel("Memory size:")
        self.memoryLine = QLineEdit()

        self.otherLabel = QLabel("Other command line arguments:")
        self.otherLine = QLineEdit()

        self.runButton = QPushButton("Run")
        self.runButton.clicked.connect(self.onRun)

        self.aboutButton = QPushButton("About")
        self.aboutButton.clicked.connect(self.onAbout)
        
        self.aboutQtButton = QPushButton("About Qt")
        self.aboutQtButton.clicked.connect(self.onAboutQt)

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

        self.gridLayout.addWidget(self.aboutQtButton, 6, 0, 1, 4)

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

    def onAbout(self):
        self.aboutBox = QMessageBox.about(self,
                                          "About Kemu",
                                          "Kemu " + KEMU_VERSION + "\n" +
                                          "Written by Erdem Ersoy (eersoy93).\n" +
                                          "Copyright (c) 2022 Erdem Ersoy\n" +
                                          "Kemu is licensed with GPLv3.\n" +
                                          "Kemu GitHub link: https://github.com/eersoy93/kemu")

    def onAboutQt(self):
        self.aboutQtBox = QMessageBox.aboutQt(self, "About Qt")

    def onRun(self, event):
        print(os.path.join(os.environ.get("PROGRAMFILES"), "qemu", "qemu-system-x86_64w.exe"))
        subprocess.call(os.path.join(os.environ.get("PROGRAMFILES"), "qemu", "qemu-system-x86_64w.exe") + " " +
                        "-m " + self.memoryLine.text() + " " +
                        "-cdrom " + self.imageLine.text() + " " +
                        self.otherLine.text() + " "
                        )

def main(args):
    app = QApplication(sys.argv)
    kemu = Kemu()
    return app.exec()

if __name__ == "__main__":
    sys.exit(main(sys.argv))
