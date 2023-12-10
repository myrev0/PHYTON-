import interface.menu


def login():

    print("Hesap Oluşturunuz!")
    print("════════════════════════")
    print("Kullanıcı Adı:")
    print("Şifre:")
    print("════════════════════════")

    belirle_kadi = input("Lütfen Kullanıcı Adı Belirleyiniz.")
    belirle_sifre = input("Lütfen Şifre Belirleyiniz.")

    print("GİRİŞ EKRANI!")
    print("════════════════════════")
    print("Kullanıcı Adı:")
    print("Şifre:")
    print("════════════════════════")

    girdi_kadi = input("Lütfen Kullanıcı Adı Giriniz.")
    girdi_sifre = input("Lütfen Şifre Giriniz.")

    if girdi_kadi == belirle_kadi and belirle_sifre == girdi_sifre:
        interface.menu.menu()
    else:
        print("Lütfen Şifre Veya Kullanıcı Adını Kontrol Ediniz.")
        login()
login()
