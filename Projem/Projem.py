import Fonksiyonlar
import sqlite3
import pandas as pd
import numpy as np

db=sqlite3.connect('Kutuphane1.db')
im=db.cursor()
GenelListe=[]
ogrenci1={}
ogrenci={}


while True:
   
    try:
        print("""
1) Öğrenci ekle
2) Öğrenci sil
3) Öğrenci bilgilerini güncelle
4) Tüm öğrencileri listele
                 """)
        secim = int(input("Seçim yap: "))
        
        if secim==1:
            try:
                GenelListe.append(Fonksiyonlar.bilgial())                
                print("\n")
                print("Öğrenci başarıyla eklendi")
            except ValueError:
                print("\n")
                print("Lütfen geçerli değer giriniz")
            
        elif secim==2:
            
            try:
                ogrencidel=int(input("Silinecek öğreninin numarası: "))
                for i in GenelListe:
                    if GenelListe[GenelListe.index(i)]["Numarası"]==ogrencidel:
                        Fonksiyonlar.hangiogrenci(GenelListe,i)
                        GenelListe.pop(GenelListe.index(i))
                        Fonksiyonlar.ogrencisil(ogrencidel)
                        print("\n")
                        print("Öğrenci başarıyla silindi")
                        break
                else:
                    print("\n")
                    print("Girdiğiniz numarada öğrenci bulunamadı")
                    
                        
            except ValueError:
                print("\n")
                print("Lütfen geçerli değer giriniz")
                
        elif secim==3:
            try:
                ogrenciguncel=int(input("Güncellenecek öğrenicinin numarası: "))
                veri=im.execute("SELECT * FROM Ogrenci").fetchall()
                for i in veri:
                    if veri[veri.index(i)][0]==ogrenciguncel:
                        Fonksiyonlar.ogrenciguncel(ogrenciguncel)
                        Fonksiyonlar.bilgial()
                        print("\n")
                        print("Öğrenci bilgileri başarıyla güncellendi")
                        break
                else:
                    print("\n")
                    print("Girdiğiniz numarada öğrenci bulunamadı")
                        
                for i in GenelListe: 
                    if GenelListe[GenelListe.index(i)]["Numarası"]==ogrenciguncel:
                        Fonksiyonlar.hangiogrenci(GenelListe,i)
                        GenelListe.pop(GenelListe.index(i))
                        Fonksiyonlar.ogrenciguncel(ogrenciguncel)
                        GenelListe.append(Fonksiyonlar.bilgial())
                        print("\n")
                        print("Öğrenci bilgileri başarıyla güncellendi")
                        break
                
                    
            except ValueError:
                print("\n")
                print("Lütfen geçerli değer giriniz")
                
        elif secim==4:
            veri=im.execute("SELECT * FROM Ogrenci").fetchall()
            if len(veri)==0:
                print("\nLisetede hiç öğrenci yok")
            else:
                
                for i in veri:
                    numaralar=[]
                    numaralar.append(veri[veri.index(i)][0])
                    adlar=[]
                    adlar.append(veri[veri.index(i)][1])
                    soyadlar=[]
                    soyadlar.append(veri[veri.index(i)][2])
                    tarihler=[]
                    tarihler.append(veri[veri.index(i)][3])
                    siniflar=[]
                    siniflar.append(veri[veri.index(i)][4])
                    veliadlar=[]
                    veliadlar.append(veri[veri.index(i)][5])
                    veliteller=[]
                    veliteller.append(veri[veri.index(i)][6])
                    
                   
                sozluk = {'Numara':pd.Series(numaralar),'Ad':pd.Series(adlar),'Soyad':pd.Series(soyadlar),'Dogum Tarihi':pd.Series(tarihler),'Sınıf':pd.Series(siniflar),'Veli ad':pd.Series(veliadlar),
                          'Veli tel':pd.Series(veliteller)}
                veriler=pd.DataFrame(sozluk)
                print(veriler)
     
        else:
            print("\n")
            print("*"*7," LÜTFEN GEÇERLİ SEÇİM YAPINIZ ","*"*7)
                
            
    except ValueError:
        print("\n")
        print("*"*7," LÜTFEN SADECE SAYI GİRİNİZ ","*"*7)
        
        
    print("\n") 
    print("Ana menüye dönmek için 'anamenu' / Çıkmak için 'cikis'")
    secim2=input("Seçim yap: ")
    if secim2=="anamenu":
        continue
    elif secim2=="cikis":
        break
    else:
        print("\n")
        print("*"*7," LÜTFEN GEÇERLİ SEÇİM YAPINIZ ","*"*7)
        continue
    
if len(GenelListe)==0:
    print("Bugün yeni veri eklenmemiş")
else:
    #Günlük yapılan değişiklikleri gösterir
    Fonksiyonlar.rapor(GenelListe)
db.close()
