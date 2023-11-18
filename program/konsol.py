# sytnax night code


def login_ekran(): # Çalışabilmesi İçin Önce Bunu Fonksiyona Aldım Ki İlk Bu Alan Çıksın
    print("╔════════════════════════════╗")
    print("║                            ║")
    print("║ Kullanıcı Aadı :           ║")
    print("║                            ║")
    print("║ şifre          :           ║")
    print("║                            ║")
    print("╚════════════════════════════╝")

    # Bu Giriş Ekranının Temsili
    username = input("Lütfen Kullanıcı Adınızı Giriniz.")
    password = input("Lütfen Şifrenizi Giriniz.")

    if username == "myrev" or password == "123":
        print("Tebrikler Başarı İle Konsol Menüsüne Aktarılıyorsunuz.")
        konsolmenu()
    else:
        print("Malesef Şifre Veya Kullanıcı Adını Yanlış Girdiniz.")

def konsolmenu():
    print(sa)