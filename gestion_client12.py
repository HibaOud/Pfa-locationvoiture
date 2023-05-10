from tkinter import *
import tkinter as ttk
from tkinter import messagebox
from tkinter import messagebox as ms
import sqlite3
from subprocess import  call
db=sqlite3.connect("main12.db")
c=db.cursor()
c.execute("create table if not exists voiture(mod text not null primary key, marq text not null , trans text not null ,type text not null, disp text not null, prix text not null, nb text not null );")
db.commit()
db.close()

class Voiture :
    def __init__(self, root):

        self.root = root
        self.root.title("RECHERCHE VOITURE")
        self.root.geometry("1350x700+0+0")  # width and height(+50+100 to show the window frm the center )
        self.root.resizable(False, False)


        frame_client = Frame(self.root, bg="white")
        frame_client.place(x=330, y=50, width=900, height=900)
        title = Label(frame_client, text="choisir votre voiture ! ", font=("Impact", 35, "bold"), fg="#6162FF", bg="white").place(x=90,y=30)


        lbl_nom= Label(frame_client, text="MARQUE:", font=("Goudy old style ", 15, "bold"), fg="grey", bg="white").place(x=90, y=140)
        self.marque = Entry(frame_client, font=("Goudy old style ", 15), bg="#E7E6E6")
        self.marque.place(x=400, y=140, width=320, height=35)

        lbl_cin = Label(frame_client, text="MODELE :", font=("Goudy old style ", 15, "bold"), fg="grey",bg="white").place(x=90, y=210)
        self.modele= Entry(frame_client, font=("Goudy old style ", 15), bg="#E7E6E6")
        self.modele.place(x=400, y=210, width=320, height=35)

        lbl_date_d= Label(frame_client, text="TYPE CARBURANT :", font=("Goudy old style ", 15, "bold"), fg="grey",bg="white").place(x=90, y=280)
        self.type_carburant= Entry(frame_client, font=("Goudy old style ", 15), bg="#E7E6E6")
        self.type_carburant.place(x=400, y=280, width=320, height=35)

        lbl_date_f = Label(frame_client, text="NOMBRE DE PLACE:", font=("Goudy old style ", 15, "bold"), fg="grey",bg="white").place(x=90, y=350)
        self.nbre_de_place= Entry(frame_client, font=("Goudy old style ", 15), bg="#E7E6E6")
        self.nbre_de_place.place(x=400, y=350, width=320, height=35)



        e3 = Label(frame_client, text="TRANSMISSION : ",font=("Goudy old style ", 15, "bold"), fg="grey",bg="white").place(x=90, y=420)
        self.transsmission = Entry(frame_client,font=("Goudy old style ", 15, "bold"), bg="#E7E6E6")
        self.transsmission.place(x=400, y=420, width=320, height=35)

        lbl_date_f = Label(frame_client, text="prix par jours:", font=("Goudy old style ", 15, "bold"), fg="grey",bg="white").place(x=90, y=490)
        self.prix= Entry(frame_client, font=("Goudy old style ", 15), bg="#E7E6E6")
        self.prix.place(x=400, y=490, width=320, height=35)

        lbl_date_f = Label(frame_client, text="disponibilité:", font=("Goudy old style ", 15, "bold"), fg="grey",bg="white").place(x=90, y=560)
        self.disponibilité = Entry(frame_client, font=("Goudy old style ", 15), bg="#E7E6E6")
        self.disponibilité.place(x=400, y=560, width=320, height=35)


        afficher=Button(frame_client,text="AFFICHER", cursor="hand2",font=("Goudy old style ",15), bg="#6162FF",fg="white",command=self.AFFICHER).place(x=0,y=600 ,width=180 , height=40)
        vider=Button(frame_client,text="VIDER", cursor="hand2",font=("Goudy old style ",15), bg="#6162FF",fg="white",command=self.supprimer).place(x=200,y=600 ,width=180 , height=40)
        retour=Button(frame_client,text="RETOUR", cursor="hand2",font=("Goudy old style ",15), bg="#6162FF",fg="white",command=self.retour).place(x=400,y=600 ,width=180 , height=40)



    

        #la on doit afficher les critere de la voiture avec son image si elle existe dans la base de donnee
        #sinon on affiche msg : voiture n est diponible

        # new-cnx
    def AFFICHER(self,marq):

        marq='147'
        db = sqlite3.connect("main12.db")
        cursor = db.cursor()
        find_client = ('select * from client where marq=?')
        res=cursor.execute(find_client,marq)
        db.commit()

    def retour(self):
        root.destroy()
        call(["python", "menu12.py"])


    def supprimer(self):
        self.marque.delete(0, END)
        self.modele.delete(0, END)
        self.type_carburant.delete(0, END)
        self.nbre_de_place.delete(0, END)
        self.transsmission.delete(0, END)
        self.prix.delete(0, END)
        self.disponibilité.delete(0, END)




root=Tk()
obj= Voiture(root)
root.mainloop()
