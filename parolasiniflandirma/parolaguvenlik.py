# YUSUF YİGİT

#Parola Güvenliği

# -*- coding:utf-8 -*-
import string

kulAd = []
kulParola = []
kulparolaPuanlama = []
guvenlikPuan = 0
"""
--3 Kategori Altında -3 ile 6 Puan Aralığı ile Sınıflandırma
Puanlam Aralığı
[ --> Dahil demek
[-3,1] --> Zayıf Puanlı
[2,4]  --> Orta Puanlı
[5,6]  --> Yüksek Puanlı, demek

"""
print("Kullanıcı Ad ve Parola Girmeye Hazır!\nİstediğiniz Zaman Çıkabilirsiniz.")

while True: #Kullanıcı Ad ve Parola Kaydetmek için
    alAd = str(input("Kullanıcı Adı Giriniz: "))
    kulAd.append(alAd)
    alParola = str(input("Kullanıcı Parolası Giriniz: "))
    kulParola.append(alParola)
    devam=str(input("Devam Etmek İstiyor musunuz? (Y/N):"))
    devam=devam.upper()
    if devam != "Y":
        break

islemParola = ""

for i in range(0, len(kulParola)):
    islemParola = kulParola[i] #Parolayı bozmadan işlem yapmak için

    #Kategori 1 (Uzunluk Kontrolü)
    if len(islemParola) > 5 and len(islemParola) < 8: #Parola uzunluğunu kontrol etme
        guvenlikPuan += 1
    elif len(islemParola) >= 8:
        guvenlikPuan += 2
    else:
        guvenlikPuan -= 1 #Uzunluk kısa ise

    #Buradan sonrası hataları yakalayarak işlem yapılırs
    varSayi = 0
    indexKontrolu = 0
    varsaSayi = []
    ozelKarakter=0
    for j in range(0, len(islemParola)): #eğer hata alırsak str inte çevirmeye çalıştığı için alırız. Hata vermesse index
        rakamVarmi=0                                                           # int ten int dönüşür ve var old. anlarız
        try:                                                                   # Yani hataları yakalarız parolanın içinde
            varsaSayi.append(int(islemParola[indexKontrolu]))
            varSayi += 1
            indexKontrolu += 1
        except:
            indexKontrolu += 1

        if islemParola[j] in string.punctuation: #Parolada özel karakter kontrolü
            ozelKarakter += 1

        if type(islemParola[j]) == int:
            varSayi += 1

    # Kategori 2 (Özel Karakter Kontrolü)
    if ozelKarakter > 0 and ozelKarakter < 3: #Özel karakter sayı adeti sayma
        guvenlikPuan += 1
    elif ozelKarakter >= 3:
        guvenlikPuan += 2
    else:
        guvenlikPuan -= 1 #Özel karakter yoksa

    # Kategori 3 (Rakam Kontrolü)
    if varSayi != len(islemParola): #Parola sadece sayılardan oluşma durumu
        guvenlikPuan += 1
    elif varSayi > 3:
        guvenlikPuan += 1
    else:
        guvenlikPuan -= 1 #Rakam yoksa

    kulparolaPuanlama.append(guvenlikPuan) #puanlamayı indexlere göre kaydettik
    guvenlikPuan = 0 #diğer indexi kontrol için sıfırlıyoruz

print("*" * 30)
print("Güvenli Parola Sahipleri Sıralması")
Zayıf = []
Orta = []
Guclu = []
for i in range(0, len(kulparolaPuanlama)):
    a = kulparolaPuanlama[i]
    if a >= -3 and a <= 1:
        Zayıf.append(kulAd[i])
    elif a >= 2 and a <= 4:
        Orta.append(kulAd[i])
    else:
        Guclu.append(kulAd[i])

print("Güçlü Parolaya Sahipler:", Guclu)
print("Orta Parolaya Sahipler:", Orta)
print("Zayıf Parolaya Sahipler:", Zayıf)
print("*" * 30)
print("\nMade by TheQuark\n\nYUSUF YİGİT")