from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
from tkinter import messagebox as ms
import sqlite3
from subprocess import call
#connection
db=sqlite3.connect("main12.db")
c=db.cursor()
c.execute('create table if not exists user(username text not null primary key, psswd text not null );')
db.commit()
db.close()


class login:
    #on a defini un constructeur
    def __init__(self,root):
        #modif
        self.psswd=StringVar()
        self.username=StringVar()
        self.n_username=StringVar()
        self.n_psswd = StringVar()
        #--------------
        self.root=root
        self.root.title("login system")
        self.root.geometry("1199x660+100+50") #width and height(+50+100 to show the window frm the center )
        self.root.resizable(False,False)

        #login frame
        frame_login= Frame(self.root,bg="white")
        frame_login.place(x=330,y=150,width=500,height=400)

        #title
        title=Label(frame_login, text="LOGIN "  ,font=("Impact",35,"bold"),fg="#6162FF",bg="white").place(x=90,y=30)
        subtitle=Label(frame_login,text="bienvenu a notre appli ! ",font=("Goudy old style ",15,"bold"),fg="#1d1d1d",bg="white").place(x=90,y=100)



        #username

        lbl_user=Label(frame_login,text="NOM :",font=("Goudy old style ",15,"bold"),fg="grey",bg="white").place(x=90,y=140)
        self.username=Entry(frame_login,textvariable=self.n_username,font=("Goudy old style ",15),bg="#E7E6E6")
        self.username.place(x=90,y=170,width=320 , height=35)

        #password
        lbl_psswd= Label(frame_login, text="MOT DE PASSE:", font=("Goudy old style ", 15, "bold"), fg="grey",bg="white").place(x=90, y=210)
        self.psswd = Entry(frame_login,textvariable=self.n_psswd ,show='*',font=("Goudy old style ", 15), bg="#E7E6E6")
        self.psswd.place(x=90, y=240, width=320, height=35)


        #button

        creer_compte= Button(frame_login, text="creer un compte?", command=self.creer_acc, bd=0, font=("Goudy old style ", 12), cursor="hand2", fg="#6162FF", bg="white").place(x=90, y=320)
        submit=Button(frame_login,text="se connecter", cursor="hand2",font=("Goudy old style ",15), bg="#6162FF",fg="white", command=self.check_function).place(x=90,y=360 ,width=180 , height=40)
    def go_acceuil(self):
        if self.username.get() == "" or self.psswd.get() == "":
            messagebox.showerror("error", "veuillez remplir tous les champs !", parent=self.root)

        else:
            root.destroy()
            call(["python", "acceuil12.py"])


    def check_function(self):
        if self.username.get()=="" or self.psswd.get()=="":
            messagebox.showerror("error","veuillez remplir tous les champs !",parent=self.root)

        else:
            # acceuil ne fctionne paaas
            root.destroy()
            call(["python", "acceuil12.py"])
            #------- prblm base de donnee : enregistrement du compte nom et password ne fctionne pas
            messagebox.showinfo("bienvenu "f"{self.username.get()}")
            #ajout

            db = sqlite3.connect("main12.db")
            insert = "insert into user values (?, ?)"
            db.execute(insert, (self.username.get(), self.psswd.get()))
            db.commit()
            db.close()
            messagebox.showinfo(title="ajouter", message="user est ajouté")
            root.destroy()
            call(["python", "acceuil12.py"])





    def creer_acc(self):
        #globaliser des entree glabale pour que je puisses les utlisee dans la fct sinscrire
        global Enom , Ecpsswd , Econfirm_psswd
        winacc=Toplevel(root) #pour dire que cette fenetre vient d'heriter de la fentre "login (son nom est root)"
        winacc.title("CREER UN COMPTE ")
        winacc.config(bg="grey")
        winacc.geometry("1199x660+100+50")
        root.resizable(False, False)
        frame_cree_acc = Frame(winacc, bg="white")
        frame_cree_acc.place(x=330, y=150, width=600, height=500)
        #title : creer account
        title=Label( frame_cree_acc , text="creer votre compte"  ,font=("Impact",35,"bold"),fg="#6162FF",bg="white").place(x=90,y=30)


        #nom
        nom = Label(frame_cree_acc , text="NOM :", font=("Goudy old style ", 15, "bold"), fg="grey", bg="white").place(x=90, y=140)
        self.Enom = Entry(frame_cree_acc , font=("Goudy old style ", 15), bg="#E7E6E6")
        self.Enom.place(x=90, y=170, width=320, height=35)

        # password creee
        lbl_psswd = Label(frame_cree_acc , text="MOT DE PASSE:", font=("Goudy old style ", 15, "bold"), fg="grey",bg="white").place(x=90, y=210)
        self.Ecpsswd = Entry(frame_cree_acc , font=("Goudy old style ", 15), show='*', bg="#E7E6E6")
        self.Ecpsswd.place(x=90, y=240, width=320, height=35)
        #confirmer passwd
        confirm_psswd = Label(frame_cree_acc , text="CONFIRMER MOT DE PASSE :", font=("Goudy old style ", 15, "bold"), fg="grey", bg="white").place(x=90, y=300)
        self.Econfirm_psswd= Entry(frame_cree_acc , font=("Goudy old style ", 15),show='*', bg="#E7E6E6")
        self.Econfirm_psswd.place(x=90, y=340, width=320, height=35)
        register=Button(frame_cree_acc,text="enregistre", cursor="hand2",font=("Goudy old style ",15), bg="#6162FF",fg="white",command=self.sinscrire).place(x=90,y=390 ,width=180 , height=40)

    def sinscrire(self):
        #-------- probleme base de donnee : on veut enregistrer le compte dans la base de donne des utilisateur(main.db)
        username=self.Enom.get()
        psswd=self.Ecpsswd.get()
        confirm_password=self.Econfirm_psswd.get()




root=Tk()
obj= login(root)
root.mainloop()
