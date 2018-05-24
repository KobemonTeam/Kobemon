"""imports"""
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtTest import *
from PyQt5.QtCore import *
from pygame import mixer
import threading as tr
import time as t
import random as r
import json
import sys
import os.path
import os
"""class/functions"""

class Kobemon:
    def __init__(self, KobeName,
     Level, Exp, NextLevelExp, Image,
     DamageRanges):
        self.KobeName = KobeName
        self.Image = Image
        self.Level = Level
        self.Exp = Exp
        self.NextLevelExp = NextLevelExp
        self.Health = (
            r.randint(
                self.KobeData["stat ranges"]["health-min"],
                self.KobeData["stat ranges"]["health-max"]))
        self.SpecialMin = DamageRanges[0]
        self.SpecialMax = DamageRanges[1]
        self.DamageMin = DamageRanges[2]
        self.DamageMax = DamageRanges[3]


class LoadMain(QWidget):
    def __init__(self):
        super().__init__()
        self.TextPause = False
        self.TextDone = False
        self.Kobes = json.load(open
            ("Data/Kobemons.json","rb"),
            encoding="utf-8")        
        self.Lines = json.load(open("Data/Lines.json","rb"),
            encoding="utf-8")
        self.Types = json.load(open("Data/Types.json","rb"),
            encoding="utf-8")
        self.PixmapLoad()
        self.center()
        self.init()

    def PixmapLoad(self):
        self.KobePics = dict()
        for x in os.listdir("Kobes/KobesIcons"):
            name = x.split(".")[0]
            x = QPixmap("Kobes/KobesIcons/"+x)
            self.KobePics[name] = x

        with open("Log.txt","w") as F:
            F.write(str(self.KobePics))

    def center(self):
        self.resize(700,250)
        self.setMinimumSize(700,250)
        self.setMaximumSize(700,250)
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def ForceSize(self, x, y, Window):
        Window.resize(x, y)
        Window.setMinimumSize(x, y)
        Window.setMaximumSize(x, y)

    def SetTextPause(self):
        self.TextPause = True

    def UnsetTextPause(self):
        self.TextPause = False

    def GetName(self):
        self.Username = self.NameEdit.text()
        self.NameEntry.close()
        self.GotName = True


    def NameEntry(self):
        self.NameEntry = QDialog(None,
         Qt.WindowSystemMenuHint
          | Qt.WindowTitleHint
          | Qt.WindowCloseButtonHint)
        self.ForceSize(310, 115, self.NameEntry)
        self.NameEntry.setWindowTitle("Enter Name")
        self.NameEntry.setWindowIcon(
            QIcon("Logo/Logo.ico"))
        self.NameEntry.setStyleSheet("""QDialog
         {background-color: rgb(230, 230, 240)};""")
        NameLabel = QLabel("Enter Name:", self.NameEntry)
        NameLabel.move(80, 5)
        self.NameEdit = QLineEdit(self.NameEntry)
        self.NameEdit.setGeometry(55,25,200,35)
        SubmitButton = QPushButton("Submit",
         self.NameEntry)
        SubmitButton.setStyleSheet("""QPushButton
            {background-color: rgb(130, 130, 130);
            color: rgb(200, 200, 200);}

            QPushButton::pressed
            {background-color: rgb(110, 110, 110);};""")
        self.NameEdit.setStyleSheet("""QLineEdit
            {background-color: rgb(230, 230, 240)};""")
        SubmitButton.setGeometry(90,65,130,45)
        SubmitButton.clicked.connect(self.GetName)
        self.NameEntry.setWindowModality(
            Qt.ApplicationModal)
        self.NameEntry.show()

    def ShowKoby(self):
        self.ShowKoby = QDialog(None,
         Qt.WindowSystemMenuHint
          | Qt.WindowTitleHint
          | Qt.WindowCloseButtonHint)
        self.ForceSize(600, 450, self.ShowKoby)
        self.ShowKoby.setWindowTitle("Koby")
        self.ShowKoby.setWindowIcon(QIcon("Logo/Logo.ico"))
        self.ShowKoby.setWindowModality(Qt.ApplicationModal)
        self.ShowKoby.setStyleSheet("""QDialog
            {background-color: rgb(230, 230, 240);};""")
        Name = QLabel("Koby:", self.ShowKoby)
        Name.move(270,5)
        KobyImage = QLabel(self.ShowKoby)
        KobyImage.setPixmap(self.KobePics["Koby"])
        KobyImage.move(236,25)
        KobyText = QTextEdit(self.ShowKoby)
        KobyText.setGeometry(0,180, 600,180)
        KobyText.setReadOnly(True)
        KobyText.setText("""{}\n\n\nSpecial move:
            \n{}\nDamage:{}""".format(
                self.Kobes["all"]["Kobedex"]["Koby"]["desc"],
                self.Kobes["all"]["Kobedex"]["Koby"]
                ["special move"]["name"],
                str(self.Kobes["all"]["Kobedex"]["Koby"]
                    ["special move"]["damage"])))
        KobyText.setStyleSheet("""QTextEdit
         {border: 1px solid black;
          padding: 5px;
          background-color: rgb(230, 230, 240);};""")
        SelectKoby = QPushButton("Pick Koby!",
         self.ShowKoby)
        SelectKoby.setGeometry(0,360, 600,45)
        SelectKoby.setStyleSheet("""QPushButton
            {background-color: rgb(130, 130, 130);
            color: rgb(200, 200, 200);}

            QPushButton::pressed
            {background-color: rgb(110, 110, 110);};""")
        ChooseOther = QPushButton("Choose Other",
         self.ShowKoby)
        ChooseOther.setGeometry(0,405, 600,45)
        ChooseOther.setStyleSheet("""QPushButton
            {background-color: rgb(130, 130, 130);
            color: rgb(200, 200, 200);}

            QPushButton::pressed
            {background-color: rgb(110, 110, 110);};""")
        ChooseOther.clicked.connect(self.ShowKoby.close)
        self.ShowKoby.show()

    def ShowBurnn(self):
        self.ShowBurnn = QDialog(None,
         Qt.WindowSystemMenuHint
          | Qt.WindowTitleHint
          | Qt.WindowCloseButtonHint)
        self.ForceSize(600, 450, self.ShowBurnn)
        self.ShowBurnn.setWindowTitle("Sam Burnn")
        self.ShowBurnn.setWindowIcon(QIcon("Logo/Logo.ico"))
        self.ShowBurnn.setWindowModality(Qt.ApplicationModal)
        self.ShowBurnn.setStyleSheet("""QDialog
            {background-color: rgb(230, 230, 240);};""")
        Name = QLabel("Sam Burnn:", self.ShowBurnn)
        Name.move(270,5)
        BurnnImage = QLabel(self.ShowBurnn)
        BurnnImage.setPixmap(self.KobePics["Sam Burnn"])
        BurnnImage.move(236,25)
        BurnnText = QTextEdit(self.ShowBurnn)
        BurnnText.setGeometry(0,180, 600,180)
        BurnnText.setReadOnly(True)
        BurnnText.setText("""{}\n\n\nSpecial move:
            \n{}\nDamage:{}""".format(
                self.Kobes["all"]["Kobedex"]["Sam Burnn"]["desc"],
                self.Kobes["all"]["Kobedex"]["Sam Burnn"]
                ["special move"]["name"],
                str(self.Kobes["all"]["Kobedex"]["Sam Burnn"]
                    ["special move"]["damage"])))
        BurnnText.setStyleSheet("""QTextEdit
         {border: 1px solid black;
          padding: 5px;
          background-color: rgb(230, 230, 240);};""")
        SelectBurnn = QPushButton("Pick Sam Burnn!",
         self.ShowBurnn)
        SelectBurnn.setGeometry(0,360, 600,45)
        SelectBurnn.setStyleSheet("""QPushButton
            {background-color: rgb(130, 130, 130);
            color: rgb(200, 200, 200);}

            QPushButton::pressed
            {background-color: rgb(110, 110, 110);};""")
        ChooseOther = QPushButton("Choose Other",
         self.ShowBurnn)
        ChooseOther.setGeometry(0,405, 600,45)
        ChooseOther.setStyleSheet("""QPushButton
            {background-color: rgb(130, 130, 130);
            color: rgb(200, 200, 200);}

            QPushButton::pressed
            {background-color: rgb(110, 110, 110);};""")
        ChooseOther.clicked.connect(self.ShowBurnn.close)
        self.ShowBurnn.show()

    def ShowJerry(self):
        self.ShowJerry = QDialog(None,
         Qt.WindowSystemMenuHint
          | Qt.WindowTitleHint
          | Qt.WindowCloseButtonHint)
        self.ForceSize(600, 450, self.ShowJerry)
        self.ShowJerry.setWindowTitle("Jerry")
        self.ShowJerry.setWindowIcon(QIcon("Logo/Logo.ico"))
        self.ShowJerry.setWindowModality(Qt.ApplicationModal)
        self.ShowJerry.setStyleSheet("""QDialog
            {background-color: rgb(230, 230, 240);};""")
        Name = QLabel("Jerry:", self.ShowJerry)
        Name.move(270,5)
        JerryImage = QLabel(self.ShowJerry)
        JerryImage.setPixmap(self.KobePics["Jerry"])
        JerryImage.move(236,25)
        JerryText = QTextEdit(self.ShowJerry)
        JerryText.setGeometry(0,180, 600,180)
        JerryText.setReadOnly(True)
        JerryText.setText("""{}\n\n\nSpecial move:
            \n{}\nDamage:{}""".format(
                self.Kobes["all"]["Kobedex"]["Jerry"]["desc"],
                self.Kobes["all"]["Kobedex"]["Jerry"]
                ["special move"]["name"],
                str(self.Kobes["all"]["Kobedex"]["Jerry"]
                    ["special move"]["damage"])))
        JerryText.setStyleSheet("""QTextEdit
         {border: 1px solid black;
          padding: 5px;
          background-color: rgb(230, 230, 240);};""")
        SelectJerry = QPushButton("Pick Jerry!",
         self.ShowJerry)
        SelectJerry.setGeometry(0,360, 600,45)
        SelectJerry.setStyleSheet("""QPushButton
            {background-color: rgb(130, 130, 130);
            color: rgb(200, 200, 200);}

            QPushButton::pressed
            {background-color: rgb(110, 110, 110);};""")
        ChooseOther = QPushButton("Choose Other",
         self.ShowJerry)
        ChooseOther.setGeometry(0,405, 600,45)
        ChooseOther.setStyleSheet("""QPushButton
            {background-color: rgb(130, 130, 130);
            color: rgb(200, 200, 200);}

            QPushButton::pressed
            {background-color: rgb(110, 110, 110);};""")
        ChooseOther.clicked.connect(self.ShowJerry.close)
        self.ShowJerry.show()

    def starters(self):
        self.starters = QDialog(None,
         Qt.WindowSystemMenuHint
          | Qt.WindowTitleHint
          | Qt.WindowCloseButtonHint)
        self.ForceSize(350, 270.1, self.starters)
        self.starters.setStyleSheet("""QDialog
            {background-color: rgb(230, 230, 240)};""")
        self.starters.setWindowTitle("Choose Kobemon")
        self.starters.setWindowIcon(QIcon("Logo/Logo.ico"))
        self.starters.setWindowModality(
            Qt.ApplicationModal)
        KobyButton = QPushButton("Koby", self.starters)
        KobyButton.setGeometry(0,0, 350,90)
        KobyButton.setStyleSheet("""QPushButton
            {background-color: rgb(130, 130, 130);
            color: rgb(200, 200, 200);}

            QPushButton::pressed
            {background-color: rgb(110, 110, 110);};""")
        KobyButton.clicked.connect(self.ShowKoby)
        SamButton = QPushButton("Sam Burnn", self.starters)
        SamButton.setGeometry(0,90, 350,90)
        SamButton.setStyleSheet("""QPushButton
            {background-color: rgb(130, 130, 130);
            color: rgb(200, 200, 200);}

            QPushButton::pressed
            {background-color: rgb(110, 110, 110);};""")
        SamButton.clicked.connect(self.ShowBurnn)
        JerryButton = QPushButton("Jerry", self.starters)
        JerryButton.setGeometry(0,180, 350,90)
        JerryButton.setStyleSheet("""QPushButton
            {background-color: rgb(130, 130, 130);
            color: rgb(200, 200, 200);}

            QPushButton::pressed
            {background-color: rgb(110, 110, 110);};""")
        JerryButton.clicked.connect(self.ShowJerry)
        self.starters.show()



    def Formatter(self,EndsWith,var,Dict):
        num = 0
        Strings = []
        for x in Dict.values():
            try:
                if x.endswith(EndsWith[num]):
                    x = x.format(var[num])
                    num +=1
                else:
                    pass
            except:
                pass
            
            Strings.append(x)
        return Strings    

    def TextScroller(self, lines, line, T):
        if line:
            while self.TextPause:
                QTest.qWait(500)

            else:
                cursor = T.textCursor()
                cursor.movePosition(QTextCursor.End,
                 QTextCursor.MoveAnchor)
                T.setTextCursor(cursor)
                T.insertPlainText(line[0])
                if len(line) > 1:
                    QTest.qWait(50)
                    self.TextScroller(lines, line[1:], T)

                elif len(lines) > 1:
                    QTest.qWait(1000)
                    T.setText("")
                    QTest.qWait(1000)
                    self.TextScroller(lines[1:], lines[1], T)

                else:
                    self.TextDone = True

    def init(self):
        self.setWindowIcon(QIcon("Logo/Logo.ico"))
        self.setWindowTitle("Kobemon Woah")
        self.setStyleSheet("""QWidget
         {background-color: rgb(230, 230, 240)};""")
        self.MainText = QTextEdit(self)
        self.MainText.setGeometry(-3,20,705,235)
        self.MainText.setReadOnly(True)
        self.MainText.setStyleSheet("""QTextEdit
         {border: 1px solid black;
          padding: 5px;};""")
        self.show()
        self.main()


    def main(self):
        self.menubar = QMenuBar(self)
        self.menubar.setStyleSheet("""
              QMenuBar {
                  background-color: rgb(130, 130, 130);
                  color: rgb(200, 200, 200);
                  border: 1px solid ;
              }

              QMenuBar::item {
                  background-color: rgb(130, 130, 130);
                  color: rgb(200, 200, 200);
              }

              QMenuBar::item::selected {
                  background-color: rgb(90, 90, 90);
              }

              QMenu {
                  background-color: rgb(130, 130, 130);
                  color: rgb(200, 200, 200);
                  border: 1px solid ;
              }

              QMenu::item::selected {
                  background-color: rgb(90, 90, 90);

              }
          """)
        self.FileMenu = self.menubar.addMenu("File")
        PauseText = QAction("Pause Text",self)
        PauseText.triggered.connect(self.SetTextPause)
        UnPauseText = QAction("Resume Text",self)
        UnPauseText.triggered.connect(self.UnsetTextPause)
        ExitAction = QAction("Exit",self)
        self.FileMenu.addAction(PauseText)
        self.FileMenu.addAction(UnPauseText)
        self.FileMenu.insertSeparator(ExitAction)
        self.FileMenu.addAction(ExitAction)
        ExitAction.triggered.connect(os._exit)
        ExitAction.setShortcut('Ctrl+Q')
        self.menubar.show()
        self.GotName = False
        IntroLines = list(self.Lines["Intro"].values())
        #self.TextScroller(IntroLines,IntroLines[0],self.MainText)
        self.NameEntry()
        while not self.GotName:
            QTest.qWait(100)
        self.MainText.setText("")
        StartLines = self.Formatter(
            ["it's {}"],
            [self.Username],
            self.Lines["Start"])
        #self.TextScroller(StartLines, StartLines[0],
         #self.MainText)
        self.starters()                



class LoadGame(QWidget):
    def __init__(self):
        super().__init__()
        self.center()
        self.setWindowIcon(QIcon("Logo/Logo.ico"))
        self.setWindowTitle("Kobemon Woah")
        self.IconButton = QPushButton("", self)
        self.IconButton.setGeometry(0,0,350,329)
        self.IconButton.setIcon(QIcon("Logo/LogoSmall.png"))
        self.IconButton.setIconSize(QSize(350,329))
        self.IconButton.clicked.connect(self.LoadMain)
        self.show()

    def center(self):
        self.resize(350,329)
        self.setMinimumSize(350,329)
        self.setMaximumSize(350,329)
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def LoadMain(self):
        #mixer.music.load("Sounds/WowRoodShort.mp3")
        #mixer.music.play()
        #while mixer.music.get_busy() == 1:
            #pass
        self.close()
        self.Game = LoadMain()
        


"""main"""

if __name__ == "__main__":
    mixer.init()
    app = QApplication(sys.argv)
    QFontDatabase.addApplicationFont("Font/Pokemon GB.ttf")
    QApplication.setFont(QFont("Pokemon GB", 10))
    Window = LoadGame()
    sys.exit(app.exec_())
