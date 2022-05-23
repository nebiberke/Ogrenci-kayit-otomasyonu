import sqlite3
ogrlist=[]
ogrencidb=[]
db=sqlite3.connect('Kutuphane1.db')
im=db.cursor()
im.execute("CREATE TABLE IF NOT EXISTS Ogrenci ('Numara','Ad','Soyad','Dogum Tarihi','Sinif','Veli Adi',' Veli Telefon')")


def bilgial():
    print("\n","-"*7,"Öğrenci bilgilerini giriniz","-"*7,"\n")
    numara=int(input("Öğrencinin numarası: "))
    ad=input("Öğrencinin adı: ")
    soyad=input("Öğrencinin soyadı: ")
    dgtarih=input("Öğrencinin doğum tarihi: ")
    sinif=input("Öğrencinin sınıfı: ")
    veliadi=input("Öğrenci velisinin adı: ")
    velitel=int(input("Öğrenci velisinin telefon numarası: "))
    
    #veritabanına ekler
    ogrencidb=[numara,ad,soyad,dgtarih,sinif,veliadi,velitel]
    im.execute("INSERT INTO Ogrenci VALUES (?,?,?,?,?,?,?)",(ogrencidb))
    db.commit()
    ogrencidb.clear()

    #Sözlük olarak kaydeder
    ogrenci={"Numarası":numara,"Adı":ad,"Soyadı":soyad,"Doğum tarihi":dgtarih
    ,"Sınıfı":sinif,"Öğrenci velisinin adı":veliadi,"Veli Telefon no":velitel}
    ogrenci1=ogrenci.copy()
    ogrenci.clear()
    return ogrenci1

def ogrencisil(ogrencidel):
    im.execute("DELETE FROM Ogrenci WHERE numara = ?",[ogrencidel])
    db.commit()

def ogrenciguncel(ogrenciguncel):
    im.execute("DELETE FROM Ogrenci WHERE numara = ?",[ogrenciguncel])
    db.commit()


def rapor(GenelListe):
    print("\n")
    print("-"*7,"Gün sonu raporu","-"*7)
    for i in GenelListe:
        print("\n")
        print("{}. Öğrenci bilgileri ".format(GenelListe.index(i)+1))
        print(i)
        
def hangiogrenci(GenelListe,i):
    print("\nİsmi {} {} olan öğrencinin bilgilerinde işlem yapıyorsunuz..".format(GenelListe[GenelListe.index(i)]["Adı"],GenelListe[GenelListe.index(i)]["Soyadı"]))
