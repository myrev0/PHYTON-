import sistem


def login_screen():
    print("Kullanıcı Oluşturma Ekranına Hoş Geldiniz.")

    belirle_username = input("Kullanıcı Adı Belirleyiniz.")
    belirle_password = input("Şifre Belirleyiniz.")

    gir_username = input("Lütfen Kullanıcı Adınızı Giriniz.")
    gir_password = input("Lütfen Şifre Giriniz.")

    if belirle_username == gir_username and belirle_password == gir_password:
        print("Tebrikler Başarıyla Girdiniz.")
        sistem.sistem()
    else:
        print("Malesef Giriş Yapamadınız. Şifre Ve ya Kullanıcı Adı Hatalı.")
        exit()

    
