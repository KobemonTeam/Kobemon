"""Import section"""
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter.font import Font
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image
from pygame import mixer
import arrow as a
import threading as tr
import time as t
import pyglet as glet
import Crypto.Random.random as r
#import random as r
import json
import sys
import os
import os.path
"""Class"""
class Window(Frame):
    
    def __init__(self, master=None):       
        Frame.__init__(self, master)        
        self.master = master
        self.Image = Image.open("Logo/LogoSmall.png")
        self.ImageLab = ImageTk.PhotoImage(self.Image)
        self.Kobes = json.load(open("Data/Kobemons.json","rb"),encoding="utf-8")        
        self.Lines = json.load(open("Data/Lines.json","rb"), encoding="utf-8")
        self.Types = json.load(open("Data/Types.json","rb"), encoding="utf-8")
        self.Fin = IntVar()
        self.TextPause = IntVar()
        self.InBattle = IntVar()
        self.KobySelectedVar = IntVar()
        self.BattleWon = IntVar()
        self.RouteDone = IntVar()               
        self.TName = "Kobemon Woah" 
        glet.font.add_file("Font/Pokemon GB.ttf")
        self.FontName = glet.font.load("Pokemon GB")  
        self.Font = Font(family="Pokemon GB", size=10)
        mixer.init()
        self.PILMaker()     
        self.StartScreen() #Starting the base window

    def PILMaker(self):
        self.KobePics = {}
        for x in os.listdir("Kobes/KobesIcons"):
            name = x.split(".")[0]
            x = Image.open("Kobes/KobesIcons/"+x)
            x = ImageTk.PhotoImage(x)
            self.KobePics[name] = x

        print(self.KobePics)



    def StartScreen(self):
        root.withdraw()            
        self.StartScreen = Toplevel()
        self.StartScreen.title(self.TName)
        self.app = (self.StartScreen)
        self.StartScreen.iconbitmap("Logo/Logo.ico")
        self.StartScreen.geometry("350x329")
        Begin = Button(self.StartScreen, text="Begin your adventure!!!",command=self.Starting)
        Begin.config(image=self.ImageLab,width="10",height="10")
        Begin.pack(fill=BOTH,expand=1)

    

    def KobySelected(self):
        self.KobySelection.destroy()
        self.Starters.destroy()
        self.OwnKobes = {
        "Koby":{
        "Stats":{
        "Health":r.randint(self.Kobes["all"]["Kobedex"]["Koby"]["stat ranges"]["health-min"],self.Kobes["all"]["Kobedex"]["Koby"]["stat ranges"]["health-max"]),
        "Sdamage-min":self.Kobes["all"]["Kobedex"]["Koby"]["special move"]["damage-min"],
        "Sdamage-max":self.Kobes["all"]["Kobedex"]["Koby"]["special move"]["damage-max"],
        "Ndamage-min":self.Kobes["all"]["Kobedex"]["Koby"]["stat ranges"]["damage-min"],
        "Ndamage-max":self.Kobes["all"]["Kobedex"]["Koby"]["stat ranges"]["damage-max"],
        "Level":4,
        "Exp":0,
        "NextLevel":90
        }
        }
        }
        self.RivalKobes = {
        "Jerry":{
        "Stats":{
        "Health":r.randint(self.Kobes["all"]["Kobedex"]["Jerry"]["stat ranges"]["health-min"],self.Kobes["all"]["Kobedex"]["Jerry"]["stat ranges"]["health-max"]),
        "damage-min":self.Kobes["all"]["Kobedex"]["Jerry"]["stat ranges"]["damage-min"],
        "damage-max":self.Kobes["all"]["Kobedex"]["Jerry"]["stat ranges"]["damage-max"],
        }
        }
        }
        self.RivalKobesList = ["Jerry"]
        self.KobesList = ["Koby"]
        self.KobySelectedVar.set(1) 



    def KobySelection(self):
        self.KobySelection = Toplevel()
        self.KobySelection.title("Koby")
        self.app = (self.KobySelection)
        self.KobySelection.iconbitmap("Logo/Logo.ico")
        self.KobySelection.geometry("770x670")
        KobyPic = Label(self.KobySelection,image=self.KobePics["Koby"])
        KobyPic.pack()
        T = Text(self.KobySelection, font=self.Font)
        T.pack(fill=BOTH,expand=1)
        T.insert(END,self.Kobes["all"]["Kobedex"]["Koby"]["desc"] + "\n\n\nSpecial move:\n" + self.Kobes["all"]["Kobedex"]["Koby"]["special move"]["name"] + "\nDamage:" + str(self.Kobes["all"]["Kobedex"]["Koby"]["special move"]["damage"]))
        Pick = Button(self.KobySelection, font=self.Font,text="Pick Koby!",command=self.KobySelected)
        Pick.pack(fill=BOTH,expand=1)
        ChooseOther = Button(self.KobySelection, font=self.Font,text="Choose other!",command=self.KobySelection.destroy)
        ChooseOther.pack(fill=BOTH,expand=1)

    def BurnnSelected(self):
        self.BurnnSelection.destroy()
        self.Starters.destroy()
        self.OwnKobes = {
        "Sam Burnn":{
        "Stats":{
        "Health":r.randint(self.Kobes["all"]["Kobedex"]["Sam Burnn"]["stat ranges"]["health-min"],self.Kobes["all"]["Kobedex"]["Sam Burnn"]["stat ranges"]["health-max"]),
        "Sdamage-min":self.Kobes["all"]["Kobedex"]["Sam Burnn"]["special move"]["damage-min"],
        "Sdamage-max":self.Kobes["all"]["Kobedex"]["Sam Burnn"]["special move"]["damage-max"],
        "Ndamage-min":self.Kobes["all"]["Kobedex"]["Sam Burnn"]["stat ranges"]["damage-min"],
        "Ndamage-max":self.Kobes["all"]["Kobedex"]["Sam Burnn"]["stat ranges"]["damage-max"],
        "Level":4,
        "Exp":0,
        "NextLevel":90
        }
        }
        }
        self.KobesList = ["Sam Burnn"]
        self.RivalKobes = {
        "Koby":{
        "Stats":{
        "Health":r.randint(self.Kobes["all"]["Kobedex"]["Koby"]["stat ranges"]["health-min"],self.Kobes["all"]["Kobedex"]["Koby"]["stat ranges"]["health-max"]),
        "damage-min":self.Kobes["all"]["Kobedex"]["Koby"]["stat ranges"]["damage-min"],
        "damage-max":self.Kobes["all"]["Kobedex"]["Koby"]["stat ranges"]["damage-max"],
        }
        }
        }
        self.RivalKobesList = ["Koby"]
        self.KobySelectedVar.set(1) 

    def BurnnSelection(self):
        self.BurnnSelection = Toplevel()
        self.BurnnSelection.title("Sam Burnn")
        self.app = (self.BurnnSelection)
        self.BurnnSelection.iconbitmap("Logo/Logo.ico")
        self.BurnnSelection.geometry("670x690")
        BurnnPic = Label(self.BurnnSelection,image=self.KobePics["Sam Burnn"])
        BurnnPic.pack()
        T = Text(self.BurnnSelection, font=self.Font)
        T.pack(fill=BOTH,expand=1)
        T.insert(END,self.Kobes["all"]["Kobedex"]["Sam Burnn"]["desc"] + "\n\n\nSpecial move:\n" + self.Kobes["all"]["Kobedex"]["Sam Burnn"]["special move"]["name"] + "\nDamage:" + str(self.Kobes["all"]["Kobedex"]["Sam Burnn"]["special move"]["damage"]))
        Pick = Button(self.BurnnSelection, font=self.Font,text="Pick Sam Burnn!",command=self.BurnnSelected)
        Pick.pack(fill=BOTH,expand=1)
        ChooseOther = Button(self.BurnnSelection, font=self.Font,text="Choose other!",command=self.BurnnSelection.destroy)
        ChooseOther.pack(fill=BOTH,expand=1)

    def JerrySelected(self):
        self.JerrySelection.destroy()
        self.Starters.destroy()
        self.OwnKobes = {
        "Jerry":{
        "Stats":{
        "Health":r.randint(self.Kobes["all"]["Kobedex"]["Jerry"]["stat ranges"]["health-min"],self.Kobes["all"]["Kobedex"]["Jerry"]["stat ranges"]["health-max"]),
        "Sdamage-min":self.Kobes["all"]["Kobedex"]["Jerry"]["special move"]["damage-min"],
        "Sdamage-max":self.Kobes["all"]["Kobedex"]["Jerry"]["special move"]["damage-max"],
        "Ndamage-min":self.Kobes["all"]["Kobedex"]["Jerry"]["stat ranges"]["damage-min"],
        "Ndamage-max":self.Kobes["all"]["Kobedex"]["Jerry"]["stat ranges"]["damage-max"],
        "Level":4,
        "Exp":0,
        "NextLevel":90
        }
        }
        }
        self.RivalKobes = {
        "Sam Burnn":{
        "Stats":{
        "Health":r.randint(self.Kobes["all"]["Kobedex"]["Sam Burnn"]["stat ranges"]["health-min"],self.Kobes["all"]["Kobedex"]["Sam Burnn"]["stat ranges"]["health-max"]),
        "Damage":r.randint(self.Kobes["all"]["Kobedex"]["Sam Burnn"]["stat ranges"]["damage-min"],self.Kobes["all"]["Kobedex"]["Sam Burnn"]["stat ranges"]["damage-max"])
        }
        }
        }
        self.RivalKobesList = ["Sam Burnn"]
        self.KobesList = ["Jerry"]
        self.KobySelectedVar.set(1) 

    def JerrySelection(self):
        self.JerrySelection = Toplevel()
        self.JerrySelection.title("Jerry")
        self.app = (self.JerrySelection)
        self.JerrySelection.iconbitmap("Logo/Logo.ico")
        self.JerrySelection.geometry("790x695")
        JerryPic = Label(self.JerrySelection,image=self.KobePics["Jerry"])
        JerryPic.pack()
        T = Text(self.JerrySelection, font=self.Font)
        T.pack(expand=1)
        T.insert(END,self.Kobes["all"]["Kobedex"]["Jerry"]["desc"] + "\n\n\nSpecial move:\n" + self.Kobes["all"]["Kobedex"]["Jerry"]["special move"]["name"] + "\nDamage:" + str(self.Kobes["all"]["Kobedex"]["Jerry"]["special move"]["damage"]))
        Pick = Button(self.JerrySelection, font=self.Font,text="Pick Jerry!",command=self.JerrySelected)
        Pick.pack(fill=BOTH,expand=1)
        ChooseOther = Button(self.JerrySelection, font=self.Font,text="Choose other!",command=self.JerrySelection.destroy)
        ChooseOther.pack(fill=BOTH,expand=1)


    def Starters(self):
        self.Starters = Toplevel()
        self.Starters.title("Choose your Kobemon")
        self.app = (self.Starters)
        self.Starters.iconbitmap("Logo/Logo.ico")
        self.Starters.geometry("310x260")
        KobySelect = Button(self.Starters, font=self.Font,text="Koby",command=self.KobySelection)        
        SamBurnnSelect = Button(self.Starters, font=self.Font,text="Sam Burnn",command=self.BurnnSelection)
        JerrySelect = Button(self.Starters, font=self.Font,text="Jerry",command=self.JerrySelection)
        KobySelect.pack(fill=BOTH,expand=1)
        SamBurnnSelect.pack(fill=BOTH,expand=1)
        JerrySelect.pack(fill=BOTH,expand=1)

       
    def Starting(self):
        mixer.music.load("Sounds/WowRoodShort.mp3")
        mixer.music.play()
        root.deiconify()
        self.StartScreen.destroy()
        self.start()

    def FetchName(self):
        self.Username = self.NameEntry.get()
        self.NameMaker.destroy()
        self.Fin.set(2)

    def NameMaker(self):
        self.NameMaker = Toplevel()
        self.NameMaker.title("Input name")
        self.app = (self.NameMaker)
        self.NameMaker.iconbitmap("Logo/Logo.ico")
        self.NameMaker.geometry("310x110")
        self.NameEntry = Entry(self.NameMaker, font=self.Font)
        self.NameLabel = Label(self.NameMaker, font=self.Font,text="Enter Name:")
        EntryButton = Button(self.NameMaker, font=self.Font,text="Submit Name",command=self.FetchName)        
        self.NameLabel.pack()        
        self.NameEntry.pack()        
        EntryButton.pack()
 
    def CatchSpecialAttack(self):
        if self.DoneTalking.get() == 0:
            return        
        self.CatchT.delete(1.0,END)
        self.CatchSpecialButton.pack_forget()
        self.CatchPoundButton.pack_forget()
        AttackD = self.AttackGenerator(0,True)
        FoeHealth = self.OFool["health"] - AttackD
        Lines = ["{} attacked with it's special move {} against Jake O'fool dealing {} damage".format(self.Username,self.Kobes["all"]["Kobedex"][self.KobesList[0]]["special move"]["name"],AttackD)]
        self.Fin.set(0)
        self.TextScroller(Lines,Lines[0],self.CatchT)
        root.wait_variable(self.Fin)
        self.CatchT.delete(1.0,END)
        self.Fin.set(0)
        self.DoneTalking.set(0)

    def CatchThrowRamen(self): 
        self.CatchT.delete(1.0,END)
        Lines = ["{} threw Ramen at Jake O'fool".format(self.Username),"RAMEN","RAMEN","RAMEN!","{} Caught Jake O'fool!".format(self.Username)]
        self.Fin.set(0)
        self.TextScroller(Lines,Lines[0],self.CatchT)
        root.wait_variable(self.Fin)
        self.DoneTalking.set(1)      




    def CatchTutorial(self):
        self.CatchTutorial = Toplevel()
        self.CatchTutorial.title("Catch a Kobé")
        self.CatchTutorial.iconbitmap("Logo/Logo.ico")
        self.app = (self.CatchTutorial)
        self.CatchTutorial.geometry("900x640")
        self.DoneTalking = IntVar()
        self.DoneTalking.set(0)
        self.OFool = {
        "health":r.randint(self.Kobes["all"]["Kobedex"]["Jake O'fool"]["stat ranges"]["health-min"],self.Kobes["all"]["Kobedex"]["Jake O'fool"]["stat ranges"]["health-max"]),
        "Damage":r.randint(self.Kobes["all"]["Kobedex"]["Jake O'fool"]["stat ranges"]["damage-min"],self.Kobes["all"]["Kobedex"]["Jake O'fool"]["stat ranges"]["damage-max"])
        }
        JakePic = Label(self.CatchTutorial, image=self.KobePics["Jake O'fool"])
        JakePic.pack()
        self.CatchT = Text(self.CatchTutorial)
        self.CatchT.configure(font=self.Font)
        self.CatchT.pack(fill=BOTH,expand=1)
        self.CatchSpecialButton = Button(self.CatchTutorial,font=self.Font,text=self.Kobes["all"]["Kobedex"][self.KobesList[0]]["special move"]["name"],command=self.CatchSpecialAttack)
        self.CatchSpecialButton.pack(fill=BOTH,expand=1)
        self.CatchPoundButton = Button(self.CatchTutorial,font=self.Font,text="Pound Attack")
        self.CatchPoundButton.pack(fill=BOTH,expand=1)
        Lines = ["Now watch here {} I'll show you what to do!".format(self.Username),"First you want to damage them with your special move!"]
        self.Fin.set(0)
        self.TextScroller(Lines,Lines[0],self.CatchT)        
        root.wait_variable(self.Fin)
        self.DoneTalking.set(1)
        Lines = ["{} was hit with Pound leaving him with {} health left!".format(self.KobesList[0],self.OwnKobes[self.KobesList[0]]["Stats"]["Health"]-r.randint(13,17))]
        root.wait_variable(self.DoneTalking)
        self.Fin.set(0)
        self.TextScroller(Lines,Lines[0],self.CatchT)
        root.wait_variable(self.Fin)
        self.CatchT.delete(1.0,END)
        CatchMenu = Menu(self.CatchTutorial)
        self.Fin.set(1)        
        CatchMenu.add_command(label="Throw Ramen",command=self.CatchThrowRamen)        
        Lines = ["Now we need to throw the ramen! Best make it quick!"]
        self.TextScroller(Lines,Lines[0],self.CatchT)
        root.wait_variable(self.Fin)
        self.CatchTutorial.config(menu=CatchMenu)
        root.wait_variable(self.DoneTalking)
        self.CatchTutorial.destroy()

    def ChooseJake(self,Version):
        JakeKobe = {
        Version:{
        "Stats":{
        "Health":r.randint(self.Kobes["all"]["Kobedex"][Version]["stat ranges"]["health-min"],self.Kobes["all"]["Kobedex"][Version]["stat ranges"]["health-max"]),
        "Sdamage-min":self.Kobes["all"]["Kobedex"][Version]["special move"]["damage-min"],
        "Sdamage-max":self.Kobes["all"]["Kobedex"][Version]["special move"]["damage-max"],
        "Ndamage-min":self.Kobes["all"]["Kobedex"][Version]["stat ranges"]["damage-min"],
        "Ndamage-max":self.Kobes["all"]["Kobedex"][Version]["stat ranges"]["damage-max"],
        "Level":4,
        "Exp":0,
        "NextLevel":90
        }
        }
        }
        self.KobesList.append(Version)
        self.OwnKobes.update(JakeKobe)
        self.DoneTalking.set(1)
        self.JakeSelector.destroy()
        self.JakeShow.destroy()

    def JakeShower(self,Version):
        try:
            self.JakeShow.destroy()
        except:
            pass
        self.JakeShow = Toplevel()
        self.JakeShow.title(Version)
        self.app = (self.JakeSelector)
        self.JakeShow.iconbitmap("Logo/Logo.ico")
        self.JakeShow.geometry("800x600")
        try:
            JakePIL = self.KobePics[Version]
            JakeLabel = Label(self.JakeShow,image=JakePIL)
            JakeLabel.pack()

        except:
            pass

        T = Text(self.JakeShow)
        T.configure(font=self.Font)
        T.pack(fill=BOTH,expand=1)
        T.insert(END,self.Kobes["all"]["Kobedex"][Version]["desc"] + "\n\n\nSpecial move:\n" + self.Kobes["all"]["Kobedex"][Version]["special move"]["name"] + "\nDamage:" + str(self.Kobes["all"]["Kobedex"][Version]["special move"]["damage"]))
        ButtonText = "Select {}".format(Version)
        SelectButton = Button(self.JakeShow,font=self.Font,text=ButtonText,command=lambda:self.ChooseJake(Version))
        SelectButton.pack(fill=BOTH,expand=1)
        ExitButton = Button(self.JakeShow,font=self.Font,text="Choose other!",command=self.JakeShow.destroy)
        ExitButton.pack(fill=BOTH,expand=1)  

    def JakeSelector(self):
        self.JakeSelector = Toplevel()
        self.JakeSelector.title("Evolve Jake")
        self.app = (self.JakeSelector)
        self.JakeSelector.iconbitmap("Logo/Logo.ico")
        self.JakeSelector.geometry("800x800")
        DontButton = Button(self.JakeSelector,font=self.Font,text="Don't evolve!",command=lambda:self.JakeShower("Jake O'fool"))
        DontButton.pack(fill=BOTH,expand=1)
        LakeButton = Button(self.JakeSelector,font=self.Font,text="Lake O'drool",command=lambda:self.JakeShower("Lake O'drool"))
        LakeButton.pack(fill=BOTH,expand=1)
        BlakeButton = Button(self.JakeSelector,font=self.Font,text="Blake O'fuel",command=lambda:self.JakeShower("Blake O'fuel"))
        BlakeButton.pack(fill=BOTH,expand=1)
        DracButton = Button(self.JakeSelector,font=self.Font,text="Drac O'cruel",command=lambda:self.JakeShower("Drac O'cruel"))
        DracButton.pack(fill=BOTH,expand=1)
        SlateButton = Button(self.JakeSelector,font=self.Font,text="Slate O'haul",command=lambda:self.JakeShower("Slate O'haul"))
        SlateButton.pack(fill=BOTH,expand=1)
        RakeButton = Button(self.JakeSelector,font=self.Font,text="Rake O'fall",command=lambda:self.JakeShower("Rake O'fall"))
        RakeButton.pack(fill=BOTH,expand=1)
        StateButton = Button(self.JakeSelector,font=self.Font,text="State O'small",command=lambda:self.JakeShower("State O'small"))
        StateButton.pack(fill=BOTH,expand=1)
        HateButton = Button(self.JakeSelector,font=self.Font,text="Hate O'mall",command=lambda:self.JakeShower("Hate O'mall"))
        HateButton.pack(fill=BOTH,expand=1)
        MateButton = Button(self.JakeSelector,font=self.Font,text="Mate O'jewel",command=lambda:self.JakeShower("Mate O'jewel"))
        MateButton.pack(fill=BOTH,expand=1)
        FakeButton = Button(self.JakeSelector,font=self.Font,text="Fake O'maul",command=lambda:self.JakeShower("Fake O'maul"))
        FakeButton.pack(fill=BOTH,expand=1)

    def Route1Sneak(self):
        if self.InBattle.get() == 1:
            return

        else:
            pass
        if self.R1FirstBattle == False:
            probability = r.randint(0,100)
            if probability >= 70:
                self.Battle("Daboran","Carlisle Jim",3)
                self.R1FirstBattle = True
                

            else:
                self.MainT.delete(1.0,END)
                Lines = ["{} snuck past the first trainer.".format(self.Username)]
                self.Fin.set(0)
                self.R1FirstBattle = True
                self.TextScroller(Lines,Lines[0],self.MainT)
                root.wait_variable(self.Fin)
                
                
            self.R1FirstBattle = True
            return

        else:
            if self.R1SecondBattle == False:
                probability = r.randint(0,100)
                if probability >=  70:
                    self.Battle("Daboran","Manny Map",4)
                    self.R1SecondBattle = True


                else:
                    self.MainT.delete(1.0,END)
                    Lines = ["{} snuck past the second trainer.".format(self.Username)]
                    self.Fin.set(0)
                    self.R1SecondBattle = True
                    self.TextScroller(Lines,Lines[0],self.MainT)
                    root.wait_variable(self.Fin)                    

                self.R1SecondBattle = True
            else:
                pass

        self.RouteDone.set(1)


    def Route1Battle(self):
        if self.InBattle.get() == 1:
            return

        else:
            pass
        if self.R1FirstBattle == False:
            self.Battle("Daboran","Carlisle Jim",3)
            self.R1FirstBattle = True
            return

        else:
            pass       

        if self.R1SecondBattle == False:
            self.Battle("Daboran","Manny Map",4)
            self.R1SecondBattle = True

        else:
            pass
        self.RouteDone.set(1)

        return

    def Route1Window(self):
        self.Route1 = Toplevel()
        self.Route1.title("Route 1")
        self.app = (self.Route1)
        self.Route1.iconbitmap("Logo/Logo.ico")
        self.Route1.geometry("600x350")
        self.R1FirstBattle = False
        self.R1SecondBattle = False
        SneakButton = Button(self.Route1,font=self.Font,text="Attempt sneak",command=self.Route1Sneak)
        SneakButton.pack(fill=BOTH,expand=1,side=LEFT)
        BattleButton = Button(self.Route1,font=self.Font,text="Battle trainer",command=self.Route1Battle)
        BattleButton.pack(fill=BOTH,expand=1,side=RIGHT)

    def LearntMore(self):
        self.LearnMore.destroy()
        self.MainT.delete(1.0,END)
        self.Fin.set(0)
        Lines = [
        "Receptionist:Well the chess club was founded a few weeks ago by gym leader Mr Nunn.",
        "Receptionist:He aimed to help all kids learn and play chess.",
        "Receptionist:Now we even have our very own chess team! The Pheasey Fazbears!",
        "Receptionist:Would you like to join?"]
        self.TextScroller(Lines,Lines[0],self.MainT)
        root.wait_variable(self.Fin)
        self.DoneTalking.set(1)


    def ChessLearnMore(self):
        self.LearnMore = Toplevel()
        self.LearnMore.title("Join chess club")
        self.app = (self.LearnMore)
        self.LearnMore.iconbitmap("Logo/Logo.ico")
        self.LearnMore.geometry("400x200")
        LearnButton = Button(self.LearnMore,font=self.Font,text="Learn more!",command=self.LearntMore)
        LearnButton.pack(fill=BOTH,expand=1)
        JoinButton = Button(self.LearnMore,font=self.Font,text="Join chess club!",command=lambda:[self.LearnMore.destroy(),self.DoneTalking.set(1)])
        JoinButton.pack(fill=BOTH,expand=1)

    def HealthUpdate(self):
        self.HealthLab.config(text="{}: {}".format(self.KobesList[0],self.KobesHealth))
        self.FoeHealthLab.config(text="{}: {}".format(self.FoeKobe,self.FoeHealth))

    def FoeAttack(self):
        if self.FoeLastMove == "Special":                
            self.FoeLastMove = "Pound"
            attackD = self.FoeAttackGenerator(self.FoeKobe,False,self.Foe[self.FoeKobe]["Stats"]["Level"])
            Lines = ["{} attacked {} dealing {} damage".format(self.FoeName,self.KobesList[0],attackD)]
            

        else:
            probability = r.randint(0,100)
            if probability > 60:                    
                self.FoeLastMove = "Special"
                attackD = self.TypeCheck(self.FoeKobe,self.FoeAttackGenerator(self.FoeKobe,True,self.Foe[self.FoeKobe]["Stats"]["Level"]),self.KobesList[0])
                Lines = ["{} attacked with it's special move {} against {} dealing {} damage".format(self.FoeName,self.Kobes["all"]["Kobedex"][self.FoeKobe]["special move"]["name"],self.KobesList[0],attackD)]
                

            else:                    
                self.FoeLastMove = "Pound"
                attackD = self.FoeAttackGenerator(self.FoeKobe,False,self.Foe[self.FoeKobe]["Stats"]["Level"])
                Lines = ["{} attacked {} dealing {} damage".format(self.FoeName,self.KobesList[0],attackD)]

        self.Fin.set(0)
        self.KobesHealth -= attackD
        if self.KobesHealth <= 2:
            self.LoweHealed = True
            self.KobesHealth += 20
        self.TextScroller(Lines,Lines[0],self.BattleT)
        root.wait_variable(self.Fin)
        self.HealthUpdate()
        self.BattleT.delete(1.0,END)
        if self.LoweHealed == True:
            self.attacked.set(0)
            return

        else:
            pass
                               
        if self.PackSpecial == True:
            self.AttackFoe.pack(fill=BOTH,expand=1)
        else:
            pass
        self.AttackNorm.pack(fill=BOTH,expand=1)
        self.attacked.set(0)



    def NormAttack(self,FoeKobe):
        if self.attacked.get() == 1:
            return
        else:
            pass
        self.AttackFoe.forget()
        self.AttackNorm.forget()
        self.BattleT.delete(1.0,END)
        attackD = self.AttackGenerator(0,False)
        self.FoeHealth -= attackD
        if self.FoeHealth < 0:
            self.FoeHealth = 0
        else:
            pass
        self.LastMove = "Pound"
        self.PackSpecial = True
        self.Fin.set(0)
        Lines = ["{} pounded {} dealing {} damage!!".format(self.KobesList[0],FoeKobe,attackD),
        "{} now has {} health left!!".format(FoeKobe,self.FoeHealth)
        ]
        self.TextScroller(Lines,Lines[0],self.BattleT)
        root.wait_variable(self.Fin)
        self.BattleT.delete(1.0,END)   
        self.attacked.set(1)
        self.HealthUpdate()
        if self.FoeHealth <= 0:
            return
        else:
            self.FoeAttack()

    def SpecialAttack(self,FoeKobe):
        if self.attacked.get() == 1:
            return
        else:
            pass
        if self.LastMove == "Special":
            return
        self.AttackFoe.forget()
        self.AttackNorm.forget()
        self.BattleT.delete(1.0,END)        
        attackD = self.TypeCheck(self.KobesList[0],self.AttackGenerator(0,True),FoeKobe)
        self.FoeHealth -= attackD
        if self.FoeHealth < 0:
            self.FoeHealth = 0
        else:
            pass
        self.LastMove = "Special"
        self.PackSpecial = False
        self.attacked.set(1)
        self.Fin.set(0)
        Lines = ["{} attacked with it's special move {} against {}\ndealing {} damage".format(self.Username,self.Kobes["all"]["Kobedex"][self.KobesList[0]]["special move"]["name"],FoeKobe,attackD),
        "{} now has {} health left!!".format(FoeKobe,self.FoeHealth)
        ]
        self.TextScroller(Lines,Lines[0],self.BattleT)
        root.wait_variable(self.Fin)
        self.BattleT.delete(1.0,END)        
        self.HealthUpdate()
        if self.FoeHealth <= 0:
            return
        else:
            self.FoeAttack()

    def BattleLoop(self):
        self.LoweHealed = False
        while True:
            if self.FoeHealth <= 0:
                break

            else:
                pass

            if self.LoweHealed == True:
                while self.Fin.get() == 0:
                    pass
                self.Fin.set(0)
                HealedLines = [
                "{} remembered Peters wisdom filled words echoing through his ears!!!".format(self.Username),
                "{} was healed by 20 points!".format(self.KobesList[0])
                ]
                self.TextScroller(HealedLines,HealedLines[0],self.BattleT)
                root.wait_variable(self.Fin)
                self.BattleT.delete(1.0,END)
                self.LoweHealed = False
                if self.PackSpecial == True:
                    self.AttackFoe.pack(fill=BOTH,expand=1)
                else:
                    pass
                self.AttackNorm.pack(fill=BOTH,expand=1)

            else:
                pass
        self.BattleWon.set(1)
        return



    def Battle(self,FoeKobe,FoeName,Level):
        try:
            self.BattleWindow.destroy()
        except:
            pass
        self.InBattle.set(1)
        self.BattleWindow = Toplevel()
        self.BattleWindow.title("Battle {}".format(FoeName))
        self.app = (self.BattleWindow)
        self.BattleWindow.geometry("900x640")
        self.BattleWindow.iconbitmap("Logo/Logo.ico")
        self.attacked = IntVar()
        self.BattleWon.set(0)
        self.FoeName = FoeName
        self.FoeKobe = FoeKobe
        self.Foe = {
        FoeKobe:{
        "Stats":{
        "Health":r.randint(self.Kobes["all"]["Kobedex"][FoeKobe]["stat ranges"]["health-min"],self.Kobes["all"]["Kobedex"][FoeKobe]["stat ranges"]["health-max"]) - (4-Level)*2,
        "Level":Level,
        "ExpGain":(Level + 3) * 14
        }
        }
        }
        self.FoeLastMove = "Pound"
        self.LastMove = "Pound"
        self.FoeHealth = self.Foe[FoeKobe]["Stats"]["Health"]
        self.KobesHealth = self.OwnKobes[self.KobesList[0]]["Stats"]["Health"]
        try:
            FoePic = Label(self.BattleWindow,image=self.KobePics[FoeKobe])
            FoePic.pack()
        except:
            pass
        self.HealthLab = Label(self.BattleWindow,font=self.Font,text="{}: {}".format(self.KobesList[0],self.KobesHealth))
        self.HealthLab.pack()
        self.FoeHealthLab = Label(self.BattleWindow,font=self.Font,text="{}: {}".format(FoeKobe,self.FoeHealth))
        self.FoeHealthLab.pack()
        self.Fin.set(0)
        self.BattleT = Text(self.BattleWindow)
        self.BattleT.configure(font=self.Font)
        self.BattleT.pack(fill=BOTH,expand=1)
        self.Fin.set(0)
        Lines = ["{} Wants to fight!".format(FoeName),"{} has Kobémon: {}".format(FoeName,FoeKobe)]
        self.TextScroller(Lines,Lines[0],self.BattleT)
        root.wait_variable(self.Fin)
        self.Fin.set(0)
        self.AttackFoe = Button(self.BattleWindow,font=self.Font,text=self.Kobes["all"]["Kobedex"][self.KobesList[0]]["special move"]["name"],command=lambda:self.SpecialAttack(FoeKobe))
        self.AttackFoe.pack(fill=BOTH,expand=1)
        self.AttackNorm = Button(self.BattleWindow,font=self.Font,text="Pound attack",command=lambda:self.NormAttack(FoeKobe))
        self.AttackNorm.pack(fill=BOTH,expand=1)
        self.BattleThread = tr.Thread(target=self.BattleLoop)
        self.BattleThread.daemon = True
        self.BattleThread.start()
        root.wait_variable(self.BattleWon)      
        self.BattleWindow.destroy()
        self.Fin.set(0)
        Lines = ["Congratulations {}!".format(self.Username),"You defeated {}!".format(FoeName)]
        self.OwnKobes[self.KobesList[0]]["Stats"]["Exp"] += self.Foe[FoeKobe]["Stats"]["ExpGain"]
        self.MainT.delete(1.0,END)
        self.TextScroller(Lines,Lines[0],self.MainT)
        root.wait_variable(self.Fin)
        self.InBattle.set(0)
        self.CheckLevel()


    def TypeCheck(self,Kobe,Damage,FoeKobe):
        Type = self.Kobes["all"]["Kobedex"][Kobe]["type"]
        FoeType = self.Kobes["all"]["Kobedex"][FoeKobe]["type"]
        for i in Type:
            for x in FoeType:
                if x in self.Types[i]["effective"]:
                    return Damage + r.randint(0,4)
                else:
                    pass

        for i in Type:
            for x in FoeType:
                if x in self.Types[i]["uneffective"]:
                    return Damage - r.randint(0,4)
                else:
                    pass
        return Damage

    def FoeAttackGenerator(self,Foe,special,level):
        if special == True:
            return r.randint(self.Kobes["all"]["Kobedex"][Foe]["special move"]["damage-min"],self.Kobes["all"]["Kobedex"][Foe]["special move"]["damage-max"]) + (level-4)

        else:
            return r.randint(self.Kobes["all"]["Kobedex"][Foe]["stat ranges"]["damage-min"],self.Kobes["all"]["Kobedex"][Foe]["stat ranges"]["damage-max"]) + (level-4)



    def AttackGenerator(self,PartyNum,special):
        if special == True:
            return r.randint(self.OwnKobes[self.KobesList[PartyNum]]["Stats"]["Sdamage-min"],self.OwnKobes[self.KobesList[PartyNum]]["Stats"]["Sdamage-max"])

        else:
            return r.randint(self.OwnKobes[self.KobesList[PartyNum]]["Stats"]["Ndamage-min"],self.OwnKobes[self.KobesList[PartyNum]]["Stats"]["Ndamage-max"])

    def CheckEvolve(self,Kobe,KobeName):
        try:
            KobeUse = self.Kobes["all"]["Kobedex"][KobeName]["evolution"]
        except KeyError:
            return False
        if Kobe["Level"] >= KobeUse["Level"]:
            self.OwnKobes.pop(KobeName)
            EvolvedName = KobeUse["Evolves"]
            Evolved = self.Kobes["all"]["Kobedex"][EvolvedName]
            self.OwnKobes[EvolvedName] = {
            "Stats":{
            "Health":r.randint(self.Kobes["all"]["Kobedex"][EvolvedName]["stat ranges"]["health-min"],self.Kobes["all"]["Kobedex"][EvolvedName]["stat ranges"]["health-max"]),
            "Sdamage-min":self.Kobes["all"]["Kobedex"][EvolvedName]["special move"]["damage-min"],
            "Sdamage-max":self.Kobes["all"]["Kobedex"][EvolvedName]["special move"]["damage-max"],
            "Ndamage-min":self.Kobes["all"]["Kobedex"][EvolvedName]["stat ranges"]["damage-min"],
            "Ndamage-max":self.Kobes["all"]["Kobedex"][EvolvedName]["stat ranges"]["damage-max"],
            "Level":KobeUse["Level"],
            "Exp":0,
            "NextLevel":KobeUse["Level"]*32
            }
            }
            insert = self.KobesList.index(KobeName)
            self.KobesList.pop(insert)
            self.KobesList.insert(insert,EvolvedName)
            self.LevelLines.append("Woah!","Your {} is evolving!!".format(KobeName),"You got a {}!".format(EvolvedName))
            return True
        else:
            return False

    def CheckLevel(self):       
        for i in self.KobesList:
            self.LevelLines = []
            exp = self.OwnKobes[i]["Stats"]["Exp"]
            req = self.OwnKobes[i]["Stats"]["NextLevel"]
            while exp >= req:
                Overflow = exp - req
                if Overflow < 0:
                    Overflow = 0
                else:
                    pass
                self.OwnKobes[i]["Stats"]["Exp"] = 0 + Overflow
                self.OwnKobes[i]["Stats"]["NextLevel"] += 30
                self.OwnKobes[i]["Stats"]["Level"] += 1
                self.OwnKobes[i]["Stats"]["Health"] += 2
                self.OwnKobes[i]["Stats"]["Sdamage-min"] += 1
                self.OwnKobes[i]["Stats"]["Sdamage-max"] += 1
                self.OwnKobes[i]["Stats"]["Ndamage-min"] += 1
                self.OwnKobes[i]["Stats"]["Ndamage-max"] += 1
                if self.CheckEvolve(self.OwnKobes[i]["Stats"],i) == True:
                    pass

                else:
                    self.LevelLines.append("{} leveled up to {}!".format(i,self.OwnKobes[i]["Stats"]["Level"]))
                self.MainT.delete(1.0,END)
                self.Fin.set(0)
                self.TextScroller(self.LevelLines,self.LevelLines[0],self.MainT)
                root.wait_variable(self.Fin)
                root.after(1000)
                exp = self.OwnKobes[i]["Stats"]["Exp"]
                req = self.OwnKobes[i]["Stats"]["NextLevel"]

    def PartyShuffle(self,Kobe):
        self.PartyView.destroy()
        KobePop = self.KobesList.pop(Kobe)
        self.KobesList.insert(0,KobePop)

    def PartyMove(self):
        if self.InBattle.get() == 1:
            return
        else:
            pass
        try:
            self.PartyView.destroy()

        except:
            pass

        self.PartyView = Toplevel()
        self.PartyView.title("Shuffle Party")
        self.app = (self.PartyView)
        self.PartyView.iconbitmap("Logo/Logo.ico")
        slots = 0
        dimensionsY = 0
        Buttons = []
        for i in self.KobesList:
            Buttons.append(Button(self.PartyView,font=self.Font,text=i,command=lambda:self.PartyShuffle(self.KobesList.index(i))))
            dimensionsY += 100
        for x in Buttons:
            x.pack(fill=BOTH,expand=1)
        self.PartyView.geometry("400x{}".format(dimensionsY))

                


    def KobedexSearcher(self):
        self.KobedexSearcher = Toplevel()
        self.KobedexSearcher.title("Find Kobé")
        self.app = (self.KobedexSearcher)
        self.KobedexSearcher.iconbitmap("Logo/Logo.ico")
        self.KobedexSearcher.geometry("310x110")
        self.KobeEntry = Entry(self.KobedexSearcher, font=self.Font)
        self.KobeLabel = Label(self.KobedexSearcher, font=self.Font,text="Enter Kobe:")
        EntryButton = Button(self.KobedexSearcher, font=self.Font,text="Submit Kobe",command=lambda:self.KobedexView(self.KobeEntry.get()))        
        self.KobeLabel.pack()        
        self.KobeEntry.pack()        
        EntryButton.pack()

    def KobedexView(self,Kobe):
        try:
            self.KobedexSearcher.destroy()
        except:
            pass

        if Kobe not in self.Kobes["all"]["Kobedex"].keys():
            messagebox.showinfo("Invalid Kobé","There is no Kobé with that name!\nPlease check capitals\nor if the Kobé exists!")
            return

        else:
            pass
        self.KobedexViewer = Toplevel()
        self.KobedexViewer.title("Kobedex")
        self.KobedexViewer.iconbitmap("Logo/Logo.ico")
        self.app = (self.KobedexViewer)
        self.KobedexViewer.geometry("790x500")
        
        try:
            KobePIL = self.KobePics[Kobe]
        except:
            pass

        if KobePIL:
            KobePic = Label(self.KobedexViewer,image=KobePIL)
            KobePic.pack()
        else:
            pass
        T = Text(self.KobedexViewer)
        T.configure(font=self.Font)
        T.pack(fill=BOTH,expand=1)
        T.insert(END,self.Kobes["all"]["Kobedex"][Kobe]["desc"] + "\n\n\nSpecial move:\n" + self.Kobes["all"]["Kobedex"][Kobe]["special move"]["name"] + "\nDamage:" + str(self.Kobes["all"]["Kobedex"][Kobe]["special move"]["damage"]))
        ExitButton = Button(self.KobedexViewer,font=self.Font,text="OK!",command=self.KobedexViewer.destroy)
        ExitButton.pack(fill=BOTH,expand=1)



    def TextScroller(self, lines, line,T):
        if line:
            if self.TextPause.get() == 1:
                root.wait_variable(self.TextPause)
            T.insert(END, line[0])
            if len(line) > 1:
                root.after(50, self.TextScroller, lines, line[1:], T)
            elif len(lines) > 1:
                root.after(1000,lambda:T.delete(1.0,END))                
                root.after(1000, self.TextScroller, lines[1:], lines[1], T)
            else:
                root.after(1000,lambda:self.Fin.set(1))

    def Formatter(self,EndsWith,var,Dict):
        num = 0
        Strings = []
        for x in Dict.values():
            try:
                if x.endswith(EndsWith[num]) == True:
                    x = x.format(var[num])
                    num +=1
                else:
                    pass
            except:
                pass
            
            Strings.append(x)
        return Strings            



    def start(self):
        root.iconbitmap("Logo/Logo.ico")
        self.master.title(self.TName)#setting name of window
        self.pack(fill=BOTH,expand=1)
        self.BaseMenu = Menu(self.master)
        self.master.config(menu=self.BaseMenu)
        self.OptionsMenu = Menu(self.master)
        self.OptionsMenu.add_command(label="Pause Text",command=lambda:self.TextPause.set(1))
        self.OptionsMenu.add_command(label="Resume Text",command=lambda:self.TextPause.set(0))
        self.BaseMenu.add_cascade(label="Options",menu=self.OptionsMenu)
        self.BaseMenu.add_command(label="Exit!",command=root.destroy)
        self.master.iconbitmap("Logo/Logo.ico")    
        IntroLines = list(self.Lines["Intro"].values())
        self.MainT = Text(self)        
        self.MainT.configure(font=self.Font)
        self.MainT.pack(fill=BOTH,expand=1)
        while mixer.music.get_busy() == 1:
            pass                   
        #root.after(100, self.TextScroller, IntroLines, IntroLines[0], self.MainT)
        #root.wait_variable(self.Fin)
        self.MainT.delete(1.0,END)        
        self.NameMaker()
        root.wait_variable(self.Fin)
        StartLines = self.Formatter(["it's {}"],[self.Username],self.Lines["Start"])                
        #root.after(100, self.TextScroller, StartLines, StartLines[0],self.MainT)
        #root.wait_variable(self.Fin)
        self.MainT.delete(1.0,END)
        self.Starters()
        self.KobySelectedVar.set(0) 
        root.wait_variable(self.KobySelectedVar)
        self.Fin.set(0)
        print(self.OwnKobes)
        BeginLines = self.Formatter(["{}!"],[self.KobesList[0]],self.Lines["Begin"])
        #root.after(100, self.TextScroller, BeginLines, BeginLines[0],self.MainT)
        #root.wait_variable(self.Fin)
        self.MainT.delete(1.0,END)
        HomeLines = self.Formatter(["now!","s!","s!"],[self.Username,self.Username,self.Username],self.Lines["Home"])
        self.Fin.set(0)
        #root.after(2000, self.TextScroller, HomeLines, HomeLines[0],self.MainT)
        #root.wait_variable(self.Fin)
        self.MainT.delete(1.0,END)
        self.Fin.set(0)
        Battle1Lines = list(self.Lines["Battle1"].values())
        #root.after(2000, self.TextScroller, Battle1Lines, Battle1Lines[0],self.MainT)
        #root.wait_variable(self.Fin)
        self.Battle(list(self.RivalKobes.keys())[0],"Sock",4)
        self.BattleWon.set(0)
        self.MainT.delete(1.0,END)
        PostSockLines = list(self.Lines["PostSock1"].values())
        self.Fin.set(0)
        root.after(1000, self.TextScroller, PostSockLines, PostSockLines[0],self.MainT)
        root.wait_variable(self.Fin)
        self.MainT.delete(1.0,END)
        Route1Lines = self.Formatter(["with you!"],[self.Username],self.Lines["Route1"])
        self.Fin.set(0)
        root.after(2000, self.TextScroller, Route1Lines, Route1Lines[0],self.MainT)
        root.wait_variable(self.Fin)
        self.MainT.delete(1.0,END)
        root.after(1000)
        self.CatchTutorial()
        CaughtJakeLines = self.Formatter(["{}!"],[self.Username],self.Lines["OFoolLines"])
        self.Fin.set(0)
        root.after(2000, self.TextScroller, CaughtJakeLines, CaughtJakeLines[0],self.MainT)
        root.wait_variable(self.Fin)
        self.MainT.delete(1.0,END)
        self.DoneTalking.set(0)
        self.JakeSelector()
        self.Fin.set(0)
        ChoseLines = self.Formatter(["well!","dex!","men!","{}!"],[self.Username,self.Username,self.Username,self.Username],self.Lines["ChoseLines"])
        root.wait_variable(self.DoneTalking)
        root.after(1000, self.TextScroller, ChoseLines,ChoseLines[0],self.MainT)
        self.BaseMenu.add_command(label="Change party!",command=self.PartyMove)        
        self.BaseMenu.add_command(label="Kobedex!",command=self.KobedexSearcher)
        self.Ramen = {
        "Reg":10
        }
        self.RouteDone.set(0)
        root.wait_variable(self.Fin)
        print(self.OwnKobes)
        self.MainT.delete(1.0,END)
        self.Route1Window()
        root.wait_variable(self.RouteDone)
        print(self.OwnKobes)
        self.Route1.destroy()
        self.Fin.set(0)
        MysteriousLines = self.Formatter(["leader."],[self.Username],self.Lines["MysteriousLines"])
        root.after(1000)
        self.Fin.set(0)
        self.MainT.delete(1.0,END)
        self.TextScroller(MysteriousLines,MysteriousLines[0],self.MainT)
        root.wait_variable(self.Fin)
        root.after(1000)
        self.MainT.delete(1.0,END)
        Lines = ["Receptionist:Hey {} welcome to the Pheasey Fazbears headquarters".format(self.Username),"Receptionist:Would you like to join or learn more?"]
        self.Fin.set(0)
        self.TextScroller(Lines,Lines[0],self.MainT)
        root.wait_variable(self.Fin)
        self.Fin.set(0)
        self.DoneTalking.set(0)
        self.ChessLearnMore()
        root.wait_variable(self.DoneTalking)
        self.MainT.delete(1.0,END)
        ChessLines = list(self.Lines["Nunnsville1Lines"].values())
        self.Fin.set(0)
        self.TextScroller(ChessLines,ChessLines[0],self.MainT)
        root.wait_variable(self.Fin)
        self.Battle("McBrero","Jar MesCake",4)
        self.Fin.set(0)
        ChessLines = self.Formatter(["ber."],[self.Username],self.Lines["ChessClubLines"])
        self.MainT.delete(1.0,END)
        self.TextScroller(ChessLines,ChessLines[0],self.MainT)
        root.wait_variable(self.Fin)
        self.Battle("Mate O'jewel","Finlay",5)
        self.MainT.delete(1.0,END)
        self.BattleWon.set(0)
        PostLines = self.Formatter(["FINAL!","right??"],[self.Username,self.Username],self.Lines["PostFinlayLines"])
        self.Fin.set(0)
        self.TextScroller(PostLines,PostLines[0],self.MainT)
        root.wait_variable(self.Fin)
        print(self.OwnKobes)








"""Main"""

root = Tk()
root.geometry("780x200")
app = Window(root)
root.mainloop()
