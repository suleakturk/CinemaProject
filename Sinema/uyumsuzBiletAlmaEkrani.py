from tkinter import *
import sqlite3
from tkinter import messagebox

def uyumsuzBiletAl():

    # Musteri ekrani olusturma
    uyumsuzRoot = Toplevel()
    uyumsuzRoot.title("Uyumsuz Filmi Bilet Alma Ekranı")
    uyumsuzRoot.geometry("720x470")
    uyumsuzRoot.config(bg="light slate gray")

    # Musteri database i olusturma:
    musteriDB = sqlite3.connect('musteriDB.db')
    musteriCursor = musteriDB.cursor()

    musteriCursor.execute("""CREATE TABLE IF NOT EXISTS Musteri
                (musteriAdi,musteriSoyadi,sectigiFilm,koltukNo,filmTuru,ucret)""")
    musteriDB.commit()

    # Koltuklar icin database olusturma:
    koltukDB = sqlite3.connect('koltukDB.db')
    koltukCursor = koltukDB.cursor()

    koltukCursor.execute("""CREATE TABLE IF NOT EXISTS UyumsuzFilm
                (id,bg,state)""")
    koltukDB.commit()

    # #Ilk ekleme islemi sirasinda yazilir
    # koltukCursor.execute("""INSERT INTO UyumsuzFilm VALUES ('koltuk1A','green','normal')""")
    # koltukDB.commit()


    def koltukRengiDegis(koltukButonu):
        if(koltukButonu["bg"] == "green"):
            koltukButonu.config(bg = "yellow")
        else:
            return


    def koltukSec(koltuk):
        global seciliKoltuk
        seciliKoltuk = str(koltuk)
        koltukCursor.execute("""UPDATE UyumsuzFilm SET bg = ?, state = ? WHERE id = ?""", ('red','disabled',koltuk))
        koltukDB.commit()


    def satinAl():
        liste = [isim.get(), soyisim.get(), "Uyumsuz", seciliKoltuk, "Fantastik-Aksiyon", var.get()]
        musteriCursor.execute("""INSERT INTO Musteri VALUES (?,?,?,?,?,?)""", liste)
        musteriDB.commit()

        # Bilet alindi bilgisi verilmesi:
        messagebox.showinfo("Biletiniz başarıyla alınmıştır", "Alıcı bilgisi: " + isim.get() + " " + soyisim.get() +
                            "\nSeçilen film: " + "Uyumsuz" + "(Fantastik-Aksiyon)\n" +
                            "Koltuk no: " + seciliKoltuk)
        uyumsuzRoot.destroy()

    # A grubu Koltuklari yerlestirme:
    Label(uyumsuzRoot, text="PERDE", font="Verdana 11").place(x=300, y=20)
    Label(uyumsuzRoot, text="DOLU", font="Verdana 11", bg="red").place(x=530, y=50)
    Label(uyumsuzRoot, text="BOŞ", font="Verdana 11", bg="green").place(x=590, y=50)
    Label(uyumsuzRoot, text="SEÇİLİ KOLTUK", font="Verdana 11", bg="yellow").place(x=530, y=100)

    Label(uyumsuzRoot, text="A", font="Verdana 11").place(x=80, y=60)
    koltukCursor.execute("""SELECT bg,state FROM UyumsuzFilm WHERE id = '%s'""" % ('koltuk1A'))
    temp = koltukCursor.fetchall()
    koltuk1A = Button(uyumsuzRoot, text="1", width=3, height=1, bg=temp[0][0], state = temp[0][1],
                      command=lambda: [koltukSec("koltuk1A"), koltukRengiDegis(koltuk1A)])
    koltuk1A.place(x=150, y=60)

    koltukCursor.execute("""SELECT bg,state FROM UyumsuzFilm WHERE id = '%s'""" % ('koltuk2A'))
    temp = koltukCursor.fetchall()
    koltuk2A = Button(uyumsuzRoot, text="2", width=3, height=1, bg=temp[0][0], state = temp[0][1],
                      command=lambda: [koltukSec("koltuk2A"), koltukRengiDegis(koltuk2A)])
    koltuk2A.place(x=190, y=60)

    koltukCursor.execute("""SELECT bg,state FROM UyumsuzFilm WHERE id = '%s'""" % ('koltuk3A'))
    temp = koltukCursor.fetchall()
    koltuk3A = Button(uyumsuzRoot, text="3", width=3, height=1, bg=temp[0][0], state = temp[0][1],
                      command=lambda: [koltukSec("koltuk3A"), koltukRengiDegis(koltuk3A)])
    koltuk3A.place(x=230, y=60)

    koltukCursor.execute("""SELECT bg,state FROM UyumsuzFilm WHERE id = '%s'""" % ('koltuk4A'))
    temp = koltukCursor.fetchall()
    koltuk4A = Button(uyumsuzRoot, text="4", width=3, height=1, bg=temp[0][0], state = temp[0][1],
                      command=lambda: [koltukSec("koltuk4A"), koltukRengiDegis(koltuk4A)])
    koltuk4A.place(x=270, y=60)

    koltukCursor.execute("""SELECT bg,state FROM UyumsuzFilm WHERE id = '%s'""" % ('koltuk5A'))
    temp = koltukCursor.fetchall()
    koltuk5A = Button(uyumsuzRoot, text="5", width=3, height=1, bg=temp[0][0], state = temp[0][1],
                      command=lambda: [koltukSec("koltuk5A"), koltukRengiDegis(koltuk5A)])
    koltuk5A.place(x=310, y=60)

    koltukCursor.execute("""SELECT bg,state FROM UyumsuzFilm WHERE id = '%s'""" % ('koltuk6A'))
    temp = koltukCursor.fetchall()
    koltuk6A = Button(uyumsuzRoot, text="6", width=3, height=1, bg=temp[0][0], state = temp[0][1],
                      command=lambda: [koltukSec("koltuk6A"), koltukRengiDegis(koltuk6A)])
    koltuk6A.place(x=350, y=60)

    koltukCursor.execute("""SELECT bg,state FROM UyumsuzFilm WHERE id = '%s'""" % ('koltuk7A'))
    temp = koltukCursor.fetchall()
    koltuk7A = Button(uyumsuzRoot, text="7", width=3, height=1, bg=temp[0][0], state = temp[0][1],
                      command=lambda: [koltukSec("koltuk7A"), koltukRengiDegis(koltuk7A)])
    koltuk7A.place(x=390, y=60)

    koltukCursor.execute("""SELECT bg,state FROM UyumsuzFilm WHERE id = '%s'""" % ('koltuk8A'))
    temp = koltukCursor.fetchall()
    koltuk8A = Button(uyumsuzRoot, text="8", width=3, height=1, bg=temp[0][0], state = temp[0][1],
                      command=lambda: [koltukSec("koltuk8A"), koltukRengiDegis(koltuk8A)])
    koltuk8A.place(x=430, y=60)

    koltukCursor.execute("""SELECT bg,state FROM UyumsuzFilm WHERE id = '%s'""" % ('koltuk9A'))
    temp = koltukCursor.fetchall()
    koltuk9A = Button(uyumsuzRoot, text="9", width=3, height=1, bg=temp[0][0], state = temp[0][1],
                      command=lambda: [koltukSec("koltuk9A"), koltukRengiDegis(koltuk9A)])
    koltuk9A.place(x=470, y=60)

    # B grubu Koltuklari yerlestirme:
    Label(uyumsuzRoot, text="B", font="Verdana 11").place(x=80, y=100)
    koltukCursor.execute("""SELECT bg,state FROM UyumsuzFilm WHERE id = '%s'""" % ('koltuk1B'))
    temp = koltukCursor.fetchall()
    koltuk1B = Button(uyumsuzRoot, text="1", width=3, height=1, bg=temp[0][0], state = temp[0][1],
                      command=lambda: [koltukSec("koltuk1B"), koltukRengiDegis(koltuk1B)])
    koltuk1B.place(x=150, y=100)

    koltukCursor.execute("""SELECT bg,state FROM UyumsuzFilm WHERE id = '%s'""" % ('koltuk2B'))
    temp = koltukCursor.fetchall()
    koltuk2B = Button(uyumsuzRoot, text="2", width=3, height=1, bg=temp[0][0], state = temp[0][1],
                      command=lambda: [koltukSec("koltuk2B"), koltukRengiDegis(koltuk2B)])
    koltuk2B.place(x=190, y=100)

    koltukCursor.execute("""SELECT bg,state FROM UyumsuzFilm WHERE id = '%s'""" % ('koltuk3B'))
    temp = koltukCursor.fetchall()
    koltuk3B = Button(uyumsuzRoot, text="3", width=3, height=1, bg=temp[0][0], state = temp[0][1],
                      command=lambda: [koltukSec("koltuk3B"), koltukRengiDegis(koltuk3B)])
    koltuk3B.place(x=230, y=100)

    koltukCursor.execute("""SELECT bg,state FROM UyumsuzFilm WHERE id = '%s'""" % ('koltuk4B'))
    temp = koltukCursor.fetchall()
    koltuk4B = Button(uyumsuzRoot, text="4", width=3, height=1, bg=temp[0][0], state = temp[0][1],
                      command=lambda: [koltukSec("koltuk4B"), koltukRengiDegis(koltuk4B)])
    koltuk4B.place(x=270, y=100)

    koltukCursor.execute("""SELECT bg,state FROM UyumsuzFilm WHERE id = '%s'""" % ('koltuk5B'))
    temp = koltukCursor.fetchall()
    koltuk5B = Button(uyumsuzRoot, text="5", width=3, height=1, bg=temp[0][0], state = temp[0][1],
                      command=lambda: [koltukSec("koltuk5B"), koltukRengiDegis(koltuk5B)])
    koltuk5B.place(x=310, y=100)

    koltukCursor.execute("""SELECT bg,state FROM UyumsuzFilm WHERE id = '%s'""" % ('koltuk6B'))
    temp = koltukCursor.fetchall()
    koltuk6B = Button(uyumsuzRoot, text="6", width=3, height=1, bg=temp[0][0], state = temp[0][1],
                      command=lambda: [koltukSec("koltuk6B"), koltukRengiDegis(koltuk6B)])
    koltuk6B.place(x=350, y=100)

    koltukCursor.execute("""SELECT bg,state FROM UyumsuzFilm WHERE id = '%s'""" % ('koltuk7B'))
    temp = koltukCursor.fetchall()
    koltuk7B = Button(uyumsuzRoot, text="7", width=3, height=1, bg=temp[0][0], state = temp[0][1],
                      command=lambda: [koltukSec("koltuk7B"), koltukRengiDegis(koltuk7B)])
    koltuk7B.place(x=390, y=100)

    koltukCursor.execute("""SELECT bg,state FROM UyumsuzFilm WHERE id = '%s'""" % ('koltuk8B'))
    temp = koltukCursor.fetchall()
    koltuk8B = Button(uyumsuzRoot, text="8", width=3, height=1, bg=temp[0][0], state = temp[0][1],
                      command=lambda: [koltukSec("koltuk8B"), koltukRengiDegis(koltuk8B)])
    koltuk8B.place(x=430, y=100)

    koltukCursor.execute("""SELECT bg,state FROM UyumsuzFilm WHERE id = '%s'""" % ('koltuk9B'))
    temp = koltukCursor.fetchall()
    koltuk9B = Button(uyumsuzRoot, text="9", width=3, height=1, bg=temp[0][0], state = temp[0][1],
                      command=lambda: [koltukSec("koltuk9B"), koltukRengiDegis(koltuk9B)])
    koltuk9B.place(x=470, y=100)


    # Etiketleri olusturma
    Label(uyumsuzRoot, text="İsim:", padx=10, pady=10, font="Verdana 11").place(x=100, y=205)
    Label(uyumsuzRoot, text="Soyisim:", padx=10, pady=10, font="Verdana 11").place(x=100, y=250)

    # isim soyisim entry  olusturma:
    isim = Entry(uyumsuzRoot)
    isim.place(x=200, y=215)

    soyisim = Entry(uyumsuzRoot)
    soyisim.place(x=200, y=260)

    # Ucret alma checkbox i olusturma :
    var = IntVar()

    ogrenciBox = Radiobutton(uyumsuzRoot, text="Ogrenci Ucreti", variable=var, value=15)
    ogrenciBox.place(x=450, y=215)

    tamBox = Radiobutton(uyumsuzRoot, text="Tam Ucreti", variable=var, value=30)
    tamBox.place(x=450, y=255)

    # Satin al ve cikis
    cikisButonu = Button(uyumsuzRoot, text="Çıkış", font="Verdana 11", bg="beige", command=uyumsuzRoot.destroy)
    cikisButonu.place(x=610, y=380)

    satinalButonu = Button(uyumsuzRoot, text="Satın al", font="Verdana 11", bg="beige", command= satinAl)
    satinalButonu.place(x=510, y=380)

    mainloop()
