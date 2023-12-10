
import system.düzenle
import system.sil
import system.kayitli
import system.kayit



def menu():

    print("╔══════════════════════════════╗")
    print("║    ☺ REHBER SİSTEMİ ☺       ║")
    print("║                              ║")
    print("║ • Kullanıcı Kayıt -1         ║")
    print("║ • Kullanıcı Sil -2           ║")
    print("║ • Kayıtlı Kullanıcılar -3    ║")
    print("║ • Kullanıcı Düzenle -4       ║")
    print("║                              ║")
    print("║ ▼ Çıkış -5                   ║")
    print("║                              ║")
    print("║                              ║")
    print("║                              ║")
    print("║                              ║")
    print("║                              ║")
    print("╚══════════════════════════════╝")

    secim = input("Lütfen Seçim Yapınız. 1-4 Çıkış İçin 5")

    if secim == "1":
        system.kayit.kayit()
        menu()
    if secim == "2":
        system.sil.sil()
        menu()
    if secim == "3":
        system.kayitli.kayitli()
        menu()
    if secim == "4":
        system.düzenle.düzenle()
        menu()
    if secim == "5":
        print("Başarıyla Çıkış Yapılıyor.")
