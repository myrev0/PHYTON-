# kullanıcı ekleme menüsü


def menu():

    print("ONSİS PTKS Kullanıcı arayüzüne Hoş Geldiniz.")
    print("-1 Kullanıcı Ekle")
    print("-2 Kullanıcı Sil")
    print("-3 Kullanıcı Log")
    print("-4 Kullanıcı Banla")
    print("-5 Menüye Dönüş İçin")
    
    secim = input("Lütfen Seçim Yapınız. 1-5")

    if secim == "1":
        name = input("Kullanıcı İsmi")
        sname = input("Kullanıcı Soy İsmi")
        year = input("Yaş")
        depertman = input("Depertman")

        print("Tebrikler Başarıyla",name,"Kişisini Kullanıcı Olarak Eklediniz.")

