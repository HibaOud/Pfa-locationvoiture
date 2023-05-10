from tkinter import *
import tkinter as ttk
from tkinter import messagebox
from tkinter import messagebox as ms
import sqlite3
from subprocess import  call

class menu:
    def __init__(self, win_menu):
        self.win_menu = win_menu
        self.win_menu.title("Menu")
        self.win_menu.geometry("1199x660+100+50")  # width and height(+50+100 to show the window frm the center )
        self.win_menu.resizable(False, False)
        # ACCEUIL frame
        frame_menu = Frame(self.win_menu, bg="white")
        frame_menu.place(x=330, y=150, width=600, height=500)

        # title

        title = Label(frame_menu, text="MENU", font=("Impact", 35, "bold"),fg="#6162FF", bg="white").place(x=200, y=30)


        # button menu
        lv = Button(frame_menu, text="liste voitures", cursor="hand2",font=("Goudy old style ", 15), bg="#6162FF", fg="white",command=self.liste_voiture).place(x=0, y=260, width=180, height=40)
        gc = Button(frame_menu, text="rechercher voiture", cursor="hand2",font=("Goudy old style ", 15), bg="#6162FF", fg="white",command=self.gestion_client).place(x=200, y=260, width=180, height=40)
        ga = Button(frame_menu, text="gestion admin", cursor="hand2",font=("Goudy old style ", 15), bg="#6162FF", fg="white",command=self.gestion_admin).place(x=400, y=260, width=180, height=40)
        pap= Button(frame_menu, text="penalisation a payer", cursor="hand2",font=("Goudy old style ", 15), bg="#6162FF", fg="white",command=self.liste_penalisation).place(x=200, y=360, width=280, height=40)
        
    def liste_penalisation(self):
        win_menu.destroy()
        call(["python", "penalite12.py"])

    def gestion_admin(self):
        win_menu.destroy()
        call(["python", "gestion_admin12.py"])

    def gestion_client(self):
        win_menu.destroy()
        call(["python", "gestion_client12.py"])


    def liste_voiture(self):
        win_menu.destroy()
        call(["python", "voiture1.py"])



win_menu=Tk()
obj= menu(win_menu)
win_menu.mainloop()