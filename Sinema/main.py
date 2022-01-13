from tkinter import *
import sqlite3
from tkinter import messagebox
from PIL import Image,ImageTk
from  duneBiletAlmaEkrani import duneBiletAl
from  truvaBiletAlmaEkrani import truvaBiletAl
from  uyumsuzBiletAlmaEkrani import uyumsuzBiletAl
from adminEkrani import adminKontrolEkrani

def adminEkrani():
    mainRoot.destroy()
    adminRoot = Tk()
    adminRoot.title("Giriş Ekranı")
    adminRoot.geometry("340x180")
    adminRoot.config(bg = "pink")

    frame = Frame(adminRoot,bg = "pink")
    frame.pack(expand = YES)


    userDB = sqlite3.connect('userDB.db')

    userCursor = userDB.cursor()

    userCursor.execute("""CREATE TABLE IF NOT EXISTS adminler
           (kullanici_adi , parola)""")

    # kullanicilar = [
    #     ("sule_akturk" , "12345"),
    #     ("kullanici_2" , "123456")
    # ]

    #ilk tanimlama yapilirken bunlar yazilir
    # for user in kullanicilar:
    #     userCursor.execute("""INSERT INTO adminler VALUES %s""" %(user, ))
    #
    # userDB.commit()


    Label(frame, text = "Kullanıcı adı: ",font="Verdana 10", bg = "pink").grid(row = 0, column = 0, sticky = E)
    Label(frame, text = "Parola: ",font="Verdana 10", bg = "pink").grid(row = 1, column = 0, sticky = E)

    kullaniciAdi = Entry(frame)
    kullaniciAdi.grid(row = 0, column = 1, sticky = W)
    parolaEntry = Entry(frame, show = "*")
    parolaEntry.grid(row = 1, column = 1, sticky = W)

    #Parolayi yildizli ve normal gosterme
    def parolaGoster():
        if(parolaVar.get() == 1):
            parolaEntry.config(show = "")
        else:
            parolaEntry.config(show = "*")

    parolaVar = IntVar()
    parolaCheckBox = Checkbutton(frame, text = "Şifremi göster", variable = parolaVar, onvalue=1, offvalue=0,bg = "alice blue" ,command = parolaGoster )
    parolaCheckBox.grid(row = 1, column = 2, padx = 10)


    def onEnterButtonClick():
        userCursor.execute("""SELECT * FROM adminler WHERE kullanici_adi ='%s' AND parola ='%s'""" %(kullaniciAdi.get(), parolaEntry.get()))
        data = userCursor.fetchone()

        if(data):
            messagebox.showinfo("GİRİŞ BAŞARILI","Başarıyla giriş yaptınız...")
            adminRoot.destroy()
            adminKontrolEkrani()
        else:
            kullaniciAdi.delete(0, END)
            parolaEntry.delete(0, END)
            messagebox.showerror("UYARI","Yanlış kullanıcı adı ya da parola!\nLütfen tekrar deneyiniz...")



    girisButon = Button(frame, text = "Giriş yap", borderwidth = 5, command = onEnterButtonClick)
    girisButon.grid(row = 2, column = 1, sticky = SW)

    adminRoot.mainloop()

########################################################################################################################


def musteriSecimEkrani():
    mainRoot.destroy()
    # Musteri ekrani olusturma
    musteriRoot = Tk()
    musteriRoot.title("Müşteri Girişi")
    musteriRoot.geometry("850x500")
    musteriRoot.config(bg="light slate gray")

    # --Film secimi yapiniz-- label olusturma
    Label(musteriRoot, text="Lütfen bilet almak istediğiniz filmi seçiniz:", bg="gray12", fg="beige",
          font="Verdana 12").place(x=225, y=30)

    # Filmlerin resimlerini ekleme
    truvaImage = ImageTk.PhotoImage(Image.open("resized_truva_image.jpg"))
    Label(musteriRoot, image=truvaImage).place(x=50, y=70)

    uyumsuzImage = ImageTk.PhotoImage(Image.open("resized_dune_image.jpeg"))
    Label(musteriRoot, image=uyumsuzImage).place(x=300, y=80)

    duneImage = ImageTk.PhotoImage(Image.open("resized_uyumsuz_image.jpg"))
    Label(musteriRoot, image=duneImage).place(x=550, y=70)


    # Filmlerin koltuk seçimine giden butonlari olusturma
    Button(musteriRoot, text="Truva Filmi", bg="gray19", fg="beige", command=truvaBiletAl).place(x=115, y=410)
    Button(musteriRoot, text="Dune Filmi", bg="gray19", fg="beige", command=duneBiletAl).place(x=367, y=410)
    Button(musteriRoot, text="Uyumsuz Filmi", bg="gray19", fg="beige", command=uyumsuzBiletAl).place(x=612, y=410)

    mainloop()

########################################################################################################################

#Baslangic ekranini olusturma
mainRoot = Tk()
mainRoot.title("Başlangıç Ekranı")
mainRoot.geometry("450x300")
mainRoot.config(bg = "LightSkyBlue4")


adminEkrani = Button(mainRoot, text = "Admin Ekranı",font="Verdana 11", borderwidth = 7, bg = "MediumPurple1",
                     padx = 20, pady = 5, command = adminEkrani)
adminEkrani.place(x = 155, y = 50)

musteriEkrani = Button(mainRoot, text = "Müşteri Ekranı",font="Verdana 11", borderwidth = 7,padx = 20, pady = 5,
                       bg = "alice blue", command = musteriSecimEkrani)
musteriEkrani.place(x = 150, y = 125)

cikisEkrani = Button(mainRoot, text = "Çıkış", borderwidth = 7,font="Verdana 11", bg = "SlateBlue1",padx = 20,
                     pady = 5, command = mainRoot.quit)
cikisEkrani.place(x = 185, y = 200)


mainRoot.mainloop()