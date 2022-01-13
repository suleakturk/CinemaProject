from tkinter import *
import sqlite3
from tkinter.ttk import Treeview

def adminKontrolEkrani():
    window = Tk()
    window.title("Admin Ekranı İşlemleri")
    window.geometry("620x420")
    window.config(bg = "gray")

    #Musteri db den ucret verisini cekme
    musteriDB = sqlite3.connect('musteriDB.db')
    musteriCursor = musteriDB.cursor()
    musteriCursor.execute("""SELECT sum (ucret) FROM Musteri""")
    ucret = musteriCursor.fetchall()


    #Hasilat durumunu gosterme
    Label(window, text = "ADMİN  KONTROL  PANELİ", font = "Vertana 14", borderwidth = 5).place(x = 160, y = 50)
    Label(window, text = "Anlık Hasılat:", font = "Vertana 11", borderwidth = 5).place(x = 30, y = 100)
    Label(window, text = ucret, font = "Vertana 11", bg = "beige", borderwidth = 5).place(x = 120, y = 100)

    #satin alinan koltuklar ve musteriler hakkinda treeview

    tree = Treeview(window, column = ("column1", "column2", "column3","column4", "column5", "column6"), show='headings')
    tree.heading("#1", text="Müşteri adı")
    tree.column("#1", width=50, stretch=NO)
    tree.heading("#2", text="Müşteri soyadı")
    tree.column("#2", width=100, stretch=NO)
    tree.heading("#3", text="Seçtiği film")
    tree.column("#3",width=100, stretch=NO)
    tree.heading("#4", text="Koltuk no")
    tree.column("#4", width=100, stretch=NO)
    tree.heading("#5", text="Film türü")
    tree.column("#5", width=120, stretch=NO)
    tree.heading("#6", text="Ücret")
    tree.column("#6",width=70, stretch=NO)
    tree.place(x = 30, y = 150)

    musteriCursor.execute("SELECT * FROM Musteri")
    rows = musteriCursor.fetchall()
    for row in rows:
        tree.insert("",END, values=row)

    Button(window, text = "Çıkış", font = "Vertana 14", borderwidth = 5, bg = "alice blue", command = window.destroy).place(x = 500, y = 70)

    mainloop()
