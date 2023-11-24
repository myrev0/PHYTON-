def register():
    print("ONSİS PTKS REGİSTER EKRANINA HOŞGELDİNİZ.")
    print("Kullanıcı Adı:")
    print("Şifre:")

    user_name = input("Lütfen Kullanıcı Adı Belirleyiniz.")
    password = input("Lütfen Şifre Belirleyiniz")
    print("Başarıyla Kayıt Oldunuz.")


    print("ONSİS PTKS LOGİN EKRANINA HOŞ GELDİNİZ.")
    print("Kullanıcı Adı")
    print("Şifre")
    sifre = input("Lütfen Şifrenizi Giriniz.")
    kullanici_adi = input("Lütfen Şifrenizi Giriniz.")

    if sifre == password:
        print("Şifre Ve Kullanıcı Adı Başarılı.")

    if user_name == kullanici_adi:
        print("as")
