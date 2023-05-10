from tkinter import *

from tkinter import messagebox
from tkinter import messagebox as ms
import sqlite3
from subprocess import  call

class Acceuil:
    def __init__(self,win_acceuil):
        self.win_acceuil = win_acceuil
        self.win_acceuil.title("ACCEUIL")
        self.win_acceuil.geometry("1199x660+100+50")  # width and height(+50+100 to show the window frm the center )
        self.win_acceuil.resizable(False, False)
        #ACCEUIL frame
        frame_acceuil= Frame(self.win_acceuil, bg="white")
        frame_acceuil.place(x=330, y=150, width=900, height=800)

        #title

        title=Label(frame_acceuil, text="Agence ALAMY pour location de voiture",font=("Impact",35,"bold"),fg="grey",bg="white").place(x=0,y=30)
        a = Label(frame_acceuil , text="AGENCE ALAMY : cest une agence de location de voiture a marrakech .", font=("Goudy old style ", 15, "bold"), fg="black", bg="white").place(x=90, y=140)
        b = Label(frame_acceuil , text="toutes destinations possibles a travers le maroc.Nous sommes a votre", font=("Goudy old style ", 15, "bold"), fg="black", bg="white").place(x=90, y=180)
        c = Label(frame_acceuil , text="disposition pour toutes etude personnalsée .De la simple premenade au", font=("Goudy old style ", 15, "bold"), fg="black", bg="white").place(x=90, y=220)
        d= Label(frame_acceuil , text="circuit de plusieurs jours, l agence vous mettra a disposition les vehicules", font=("Goudy old style ", 15, "bold"), fg="black", bg="white").place(x=90, y=260)
        e = Label(frame_acceuil , text="necessaires afin que votre sejour soit inoubliable", font=("Goudy old style ", 15, "bold"), fg="black", bg="white").place(x=90, y=300)


        #button menu
        menuu=Button(frame_acceuil,command=self.go_menu,text="suivre", cursor="hand2",font=("Goudy old style ",15), bg="grey",fg="white").place(x=360,y=360 ,width=180 , height=40)


    def go_menu(self):
        win_acceuil.destroy()
        call(["python", "menu12.py"])



win_acceuil=Tk()
obj= Acceuil(win_acceuil)
win_acceuil.mainloop()



