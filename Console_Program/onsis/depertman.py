

import menu
def bolum():
    print("DEPERTMAN MENÜSÜ")
    print("Depertman Ekle -1")
    print("Depertman Sil -2")
    print("Depertman Log-3")
    print("Menüye Dön-4")

    secim = input("Lütfen Yapmak İstediğiniz İşlemi Seçiniz.")

    if secim == "1":
        dadi = input("Eklemek İstediğiniz Depertman Adını Giriniz.")
        dturu = input("Lütfen Depertman Türünü Seçiniz. teknik/mühendis/muhasebe/ofis/yönetim ")
        print("Tebrikler Başarıyla",dadi,"Depertmanını Kurdunuz.")
        bolum()
    if secim == "2":
        print("Lütfen Silmek İstediğiniz Depertmanı Seçiniz.")
        print("Depertmanlar : Tenkik Servis ID1")

        sil = input("Silmek İstediğniz Depertman ID Sini Giriniz.")
        print("Tebrikler Başarıyla DepertmanSildiniz.")
        bolum()
    if secim == "3":
        print("DEPERTMAN LOG EKRANI")
        print("Şuan İNAKTİF")
    if secim == "4":
        menu.menu()
