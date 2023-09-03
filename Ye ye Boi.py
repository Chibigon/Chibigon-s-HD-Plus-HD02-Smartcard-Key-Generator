import sys
import random
import time
import os
import pygame
import pypresence
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QTextEdit, QVBoxLayout, QWidget, QStyleFactory
from PyQt5.QtGui import QIcon, QPalette, QColor, QPixmap
from PyQt5.QtCore import Qt
def IllIlIllIlIIIII(IlllIIIllll):
    IllIIlIIl = "0123456789ABCDEF"
    llIlIIlIllllllIl = ''.join(random.choice(IllIIlIIl) for IIlIIlII in range(IlllIIIllll))
    return llIlIIlIllllllIl
class lIllllIllIlllIlllIll(QMainWindow):
    def __init__(IllIlIllIlll):
        super().__init__()
        IllIlIllIlll.IIlIIIlIlI = 128
        IllIlIllIlll.IllIIIIlIIl = 16
        IllIlIllIlll.lIIIIIlIllI()
        IllIlIllIlll.IlIIIIIllllllIl()
        IllIlIllIlll.lIIlIIllIllIllI()
    def lIIIIIlIllI(IllIlIllIlll):
        IllIlIllIlll.setWindowTitle("Chibigon's HD Plus HD02 Smartcard Key Generator")
        IllIlIllIlll.setWindowIcon(QIcon("icon.png"))
        IllIlIllIlll.resize(2100, 1000)
        llIlIlIIlIIlllII = QPalette()
        llIlIlIIlIIlllII.setColor(QPalette.Window, QColor(53, 53, 53))
        llIlIlIIlIIlllII.setColor(QPalette.WindowText, Qt.white)
        llIlIlIIlIIlllII.setColor(QPalette.Button, QColor(53, 53, 53))
        llIlIlIIlIIlllII.setColor(QPalette.ButtonText, Qt.white)
        llIlIlIIlIIlllII.setColor(QPalette.Base, QColor(25, 25, 25))
        llIlIlIIlIIlllII.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        llIlIlIIlIIlllII.setColor(QPalette.ToolTipBase, Qt.white)
        llIlIlIIlIIlllII.setColor(QPalette.ToolTipText, Qt.white)
        llIlIlIIlIIlllII.setColor(QPalette.Text, Qt.white)
        llIlIlIIlIIlllII.setColor(QPalette.Link, QColor(42, 130, 218))
        llIlIlIIlIIlllII.setColor(QPalette.Highlight, QColor(42, 130, 218))
        llIlIlIIlIIlllII.setColor(QPalette.HighlightedText, Qt.black)
        IllIlIllIlll.setPalette(llIlIlIIlIIlllII)
        QApplication.setStyle(QStyleFactory.create("Fusion"))
        IllIlIllIlll.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
        IllIlIllIlll.lIllIIIl = QWidget()
        IllIlIllIlll.setCentralWidget(IllIlIllIlll.lIllIIIl)
        IllIlIllIlll.IIlIlIIllllIlllll = QVBoxLayout(IllIlIllIlll.lIllIIIl)
        IllIlIllIlll.IIlllllIIlIlIlllIII = QTextEdit()
        IllIlIllIlll.IIlllllIIlIlIlllIII.setReadOnly(True)
        IllIlIllIlll.IIlIlIIllllIlllll.addWidget(IllIlIllIlll.IIlllllIIlIlIlllIII)
        IllIlIllIlll.IIllIllIllI = QPushButton("Generate Keys")
        IllIlIllIlll.IIllIllIllI.clicked.connect(IllIlIllIlll.llIIlIIIllIIlIllllI)
        IllIlIllIlll.IIlIlIIllllIlllll.addWidget(IllIlIllIlll.IIllIllIllI)
        IllIlIllIlll.IIlllllIIlIlIlllIII.append("This program generates RSA and Box Keys for the HD Plus HD02 Smartcard.")
        IllIlIllIlll.IIlllllIIlIlIlllIII.append("My Website: https://www.chibigon.moe")
        IlIlIllll = QLabel()
        IlllllIIIIlIIlllIlll = QPixmap("ChibigonGirlBig.png")
        IlIlIllll.setPixmap(IlllllIIIIlIIlllIlll)
        IllIlIllIlll.IIlIlIIllllIlllll.addWidget(IlIlIllll)
        IllIlIllIlll.show()
    def IlIIIIIllllllIl(IllIlIllIlll):
        pygame.mixer.init()
        pygame.mixer.music.load("xxx.mp3")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1) 
    def lIIlIIllIllIllI(IllIlIllIlll):
        IllIlIllIlll.IIllIIlIIlIlIlllIIl = pypresence.Presence(client_id='1147820406179385405')
        IllIlIllIlll.IIllIIlIIlIlIlllIIl.connect()
        IllIlIllIlll.llllIIIIlllIl()
    def llllIIIIlllIl(IllIlIllIlll):
        IllIlIllIlll.IIllIIlIIlIlIlllIIl.update(
            details="Generating keys...",
            large_image="chibigongirlbig",
            start=int(time.time())
        )
    def llIIlIIIllIIlIllllI(IllIlIllIlll):
        IlllIIIlIlII = IllIlIllIlIIIII(IllIlIllIlll.IIlIIIlIlI)
        lllIIIIIlIlI = IllIlIllIlIIIII(IllIlIllIlll.IllIIIIlIIl)
        IllIlIllIlll.IIlllllIIlIlIlllIII.append("RSA Key = " + IlllIIIlIlII)
        IllIlIllIlll.IIlllllIIlIlIlllIII.append("BOX Key = " + lllIIIIIlIlI)
if __name__ == "__main__":
    lllIllIlIIIIIllI = QApplication(sys.argv)
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    lIIIIlIlI = lIllllIllIlllIlllIll()
    sys.exit(lllIllIlIIIIIllI.exec_())