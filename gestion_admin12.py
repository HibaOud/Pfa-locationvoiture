from tkinter import *
from PIL import ImageTk
import tkinter as tk
from tkinter import messagebox
from tkinter import messagebox as ms
import sqlite3

from subprocess import  call
db=sqlite3.connect("main12.db")
c=db.cursor()
c.execute("create table if not exists voiture(mod text not null primary key,img text not null, marq text not null , trans text not null ,type text not null, disp text not null, prix text not null, nb text not null );")
db.commit()
db.close()
class Admin :
    def __init__(self, root):

        self.root = root
        self.root.title("GESTION VOITURE")
        self.root.geometry("1350x700+0+0")  # width and height(+50+100 to show the window frm the center )
        self.root.resizable(False, False)

        # login frame
        frame_admin = Frame(self.root, bg="white")
        frame_admin.place(x=330, y=50, width=900, height=900)
        title = Label(frame_admin, text="ESPACE ADMIN ", font=("Impact", 35, "bold"), fg="#6162FF", bg="white").place(x=90,y=30)

        lbl_nom = Label(frame_admin, text="MARQUE:", font=("Goudy old style ", 15, "bold"), fg="grey",
                        bg="white").place(x=90, y=140)
        self.marque = Entry(frame_admin, font=("Goudy old style ", 15), bg="#E7E6E6")
        self.marque.place(x=400, y=140, width=320, height=35)

        lbl_cin = Label(frame_admin, text="MODELE :", font=("Goudy old style ", 15, "bold"), fg="grey",
                        bg="white").place(x=90, y=210)
        self.modele = Entry(frame_admin, font=("Goudy old style ", 15), bg="#E7E6E6")
        self.modele.place(x=400, y=210, width=320, height=35)

        lbl_date_d = Label(frame_admin, text="TYPE CARBURANT :", font=("Goudy old style ", 15, "bold"), fg="grey",
                           bg="white").place(x=90, y=280)
        self.type_carburant = Entry(frame_admin, font=("Goudy old style ", 15), bg="#E7E6E6")
        self.type_carburant.place(x=400, y=280, width=320, height=35)

        lbl_date_f = Label(frame_admin, text="NOMBRE DE PLACE:", font=("Goudy old style ", 15, "bold"), fg="grey",
                           bg="white").place(x=90, y=350)
        self.nbre_de_place = Entry(frame_admin, font=("Goudy old style ", 15), bg="#E7E6E6")
        self.nbre_de_place.place(x=400, y=350, width=320, height=35)

        e3 = Label(frame_admin, text="TRANSMISSION : ", font=("Goudy old style ", 15, "bold"), fg="grey",
                   bg="white").place(x=90, y=420)
        self.transsmission = Entry(frame_admin, font=("Goudy old style ", 15, "bold"), bg="#E7E6E6")
        self.transsmission.place(x=400, y=420, width=320, height=35)

        lbl_date_f = Label(frame_admin, text="prix par jours:", font=("Goudy old style ", 15, "bold"), fg="grey",
                           bg="white").place(x=90, y=490)
        self.prix = Entry(frame_admin, font=("Goudy old style ", 15), bg="#E7E6E6")
        self.prix.place(x=400, y=490, width=320, height=35)

        lbl_date_f = Label(frame_admin, text="disponibilité:", font=("Goudy old style ", 15, "bold"), fg="grey",bg="white").place(x=90, y=560)
        self.disponibilité = Entry(frame_admin, font=("Goudy old style ", 15), bg="#E7E6E6")
        self.disponibilité.place(x=400, y=560, width=320, height=35)
        

        ajouter=Button(frame_admin,text="AJOUTER", cursor="hand2",font=("Goudy old style ",15), bg="#6162FF",fg="white",command=self.ajouter).place(x=0,y=590 ,width=180 , height=40)
        supprimer=Button(frame_admin,text="SUPPRIMER", cursor="hand2",font=("Goudy old style ",15), bg="#6162FF",fg="white",command=self.supprimer).place(x=200,y=590 ,width=180 , height=40)
        modifier=Button(frame_admin,text="MODIFIER", cursor="hand2",font=("Goudy old style ",15), bg="#6162FF",fg="white",command=self.modifier).place(x=400,y=590 ,width=180 , height=40)
        retour=Button(frame_admin,text="RETOUR", cursor="hand2",font=("Goudy old style ",15), bg="#6162FF",fg="white",command=self.retour).place(x=600,y=590 ,width=180 , height=40)
        #table

        

        #affichage des informations
        try:
            # new-cnx
            def new_client():
                db = sqlite3.connect("main12.db")
                cursor = db.cursor()
                find_client = ('select cin from voiture where mat=?')
                #stockage type paiement??
                cursor.execute(find_client, (self.marque.get(), self.modele.get(),self.type_carburant.get(),self.nbre_de_place.get(), self.transsmission.get(), self.prix.get(),self.disponibilité.get()))
                if c.fetchall():
                    ms.showerror("ERROR")
                else:
                    # insertion
                    insert = 'insert into voiture(marque, modele, type_carburant, nbre_de_place, transmission, prix, disponibilite) values (  ?,?,?,?,? )'
                    db.execute(insert, (self.marque.get(), self.modele.get(),self.type_carburant.get(),self.nbre_de_place.get(), self.transsmission.get(), self.prix.get(),self.disponibilité.get()))
                    db.commit()
                    db.close()
                    ms.showinfo("voiture est ajouté")
        except Exception as es:
            messagebox.showerror("ERROR", "smting went wrong")

    

    
    def ajouter(self):
        db=sqlite3.connect("main12.db")
        insert = "insert into voiture values (?, ?, ?, ?, ?, ?, ?)"
        db.execute(insert, (self.modele.get(), self.marque.get(), self.transsmission.get(), self.type_carburant.get(), self.disponibilité.get(), self.prix.get(), self.nbre_de_place.get()))
        db.commit()
        db.close()
        messagebox.showinfo(title="ajouter", message="voiture  est ajouté")

    def retour(self):
        root.destroy()
        call(["python", "menu.py"])

#modifier mn tr et dtabase
    def modifier(self, modele):
        db=sqlite3.connect("main12.db")
        insert = "update produit set marque=?, type_carbuant=?, nbre_de_place=?, transmission=?, prix=?, disponibilite=? where modele=?"
        db.execute(insert, (self.marque.get(), self.transsmission.get(), self.type_carburant.get(), self.disponibilité.get(), self.prix.get(), self.nbre_de_place.get(), self.modele.get()))
        db.commit()
        db.close()
        messagebox.showinfo(title="ajouter", message="voiture  est modifier")
        

    def supprimer(self):
        self.marque.delete(0, END)
        self.modele.delete(0, END)
        self.type_carburant.delete(0, END)
        self.nbre_de_place.delete(0, END)
        self.transsmission.delete(0, END)
        self.prix.delete(0, END)
        self.disponibilité.delete(0, END)
        # supp mn treview et database
        db=sqlite3.connect("main12.db")
        insert = "delete from voiture where mod = ?"
        db.execute(insert, (self.modele.get()))
        db.commit()
        db.close()
        messagebox.showinfo(title="ajouter", message="voiture  est supprimer")


root=Tk()
obj= Admin(root)
root.mainloop()
