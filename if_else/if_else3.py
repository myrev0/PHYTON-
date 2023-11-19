#syntax night code

# Ne Yapacağım
# Evet Algoritma Mantığı İle Sıralayalım..
# Ehliyet Başvurusu Yapsın isim soy istesin
# sonra TC vatandaşımı, Yaş sınırını geçebiliyormu birde bir kaç soru sorsun sınav tazrı
# isteğe bağlı fonksiyon kullanabiliriz


def baslangic():

    print("Merhaba T.C Sürücü Eğitim Kursu Başvuru Ekranına Hoş Geldiniz. İşlem Yapmak İçin Soruları Cevaplayınız.")

    baslangic = input("Başvuru Yapmak İsitiyorsanız Devam İstemiyorsanız İptal Yazınız.")

    if baslangic == "devam":
        basvuru()
    if baslangic == "iptal"
        print("Sistemden çıkılıyor.")
        exit()


def basvuru():

    print("T.C Başvuru Ekranı")

    yas = int(input("soru 1: Yaşınız Nedir?"))
    isim = input("Soru 2: İsim?")
    soy_isim = input("Soru 3: Soy İsim?")
    memleket = input("Soru 4:Memleketiniz Nedir?")
    uyruk = input("Soru 5: Uyruğunuz Nedir? TC/DİĞER ")
    cinsiyet = input("Cinsiyetiniz Nedir Erkek/Kadın")
    if yas < 18:
        print("Malesef Yaşınız Yetmiyor Ehliyet Alamazsınız!")
        baslangic() 
    
    if uyruk != "diğer":
        baslangic()

    print("Merhaba",isim,soy_isim,"Ehliyet Alabilirsiniz.")
    cikti_sor = input("Çıktı Almak İstiyormusunuz? evet/hayır")

    if cikti_sor == "evet":
        print("İsim :",isim,"Soy İsim:",soy_isim,"Yaş:",yas,"Memleket:",memleket,"Uyruk",uyruk,"cinsiyet:",cinsiyet,)

    