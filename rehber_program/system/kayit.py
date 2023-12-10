class Kayit:  # Sınıf Oluşturduk Buraya
    def __int__(self,gad,gsoyad,gtelefon="---",gemail="---"): #__int__ fonksiyonu 
        self.ad = gad 
        self.soy_ad = gsoyad
        self.numara = gtelefon
        self.email = gemail
    def __str__(self):
        return f"{self.ad} + {self.soyad} + {self.numara}"







def kayit(): # kayit fonksiyonum
    kayit = open("kayit.txt","a")  # kayit değişkeni içerisinde open fonksiyonu ile dosya oluşturdum
    ad = input("Lütfen İsim Giriniz.") # ad değişkeni içerisinde input fonksiyonu ile bilgi istedim
    soy_ad = input("Lütfen Soy İsim Giriniz.") # soyad değişkeni içerisinde input fonksiyonu ile bilgi istedim
    numara = input("Lütfen Numara Giriniz.") # numara değişkeni içerisinde input fonksiyonu ile bilgi istedim
    email = input("Lütfen Email Hesabı Giriniz.") # email değişkeni içerisinde input fonksiyonu ile bilgi istedim
    oku = "Adı : " + ad + "\n " + "Soy Adı:" + soy_ad + "\n" + "Numarası: " + numara + "\n" + "email hesabı:" + email + "\n" # Ekrana kayit.txt dosyasına yazdırdım
    #oku = Kayit(ad,soy_ad,numara,email)
    print("Adı: ",ad, "\nSoy Adı:",soy_ad,"\nNumarası:",numara,"\nemail:",email)
    input("DEVAM ETMEK İÇİN ENTERİ TUŞLAYHINIZ")
    kayit()
    kayit.write(oku)
    # system.kayitli.kayitli.kayitli

    # import system.kayitli

    kayit.close()


