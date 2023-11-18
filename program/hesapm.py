# sytnax night code

def hesap():


    print("╔════════════════════════════╗")
    print("║       Hesap Makinesi       ║")
    print("║                            ║")
    print("║    -1 Toplama              ║")
    print("║    -2 Çıkarma              ║")
    print("║    -3 Çarpma               ║")
    print("║    -4 Bölme                ║")
    print("╚════════════════════════════╝")

    # Menüyü Oluşturduk

    secim = input("Lütfen Seçim Yapınız. 1 - 4")

    if secim == "1":
        toplam_bir = int(input("Lütfen Birinci Sayıyı Giriniz."))
        toplam_iki = int(input("Lütfen İkinci Sayıyı Giriniz."))
        print(toplam_bir, "Sayısı İle" ,toplam_iki, "Sayısının Toplamı :",toplam_bir+toplam_iki"Eder")

    if secim == "2":
        cikar_bir = int(input("Lütfen Birinci Sayıyı Giriniz."))
        cikar_iki = int(input("Lütfen İkinci Sayıyı Giriniz."))
        print(cikar_bir, "Sayısı İle" ,cikar_iki, "Sayısının Çıkarılanı:",cikar_bir+cikar_iki"Eder")
    

    if secim == "3":
        carp_bir = int(input("Lütfen Birinci Sayıyı Giriniz."))
        carp_iki = int(input("Lütfen İkinci Sayıyı Giriniz."))
        print(carp_bir, "Sayısı İle" ,carp_iki, "Sayısının Çarpımı:",carp_bir+carp_iki"Eder")
    
    if secim == "4":
        bol_bir = int(input("Lütfen Birinci Sayıyı Giriniz."))
        bol_iki = int(input("Lütfen İkinci Sayıyı Giriniz."))
        print(bol_bir, "Sayısı İle" ,bol_iki, "Sayısının Toplamı :",bol_bir+bol_iki"Eder")
        konsol.konsolmenu()
    
    