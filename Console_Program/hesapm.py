

def hesap():


    print("╔════════════════════════════╗")
    print("║       Hesap Makinesi       ║")
    print("║                            ║")
    print("║    -1 Toplama              ║")
    print("║    -2 Çıkarma              ║")
    print("║    -3 Çarpma               ║")
    print("║    -4 Bölme                ║")
    print("╚════════════════════════════╝")


    secim = input()
    print("Lütfen Seçim Yapınız. 1-4",secim)

    if secim == "1": topla()
    if secim == "2": cikar()
    if secim == "3": carp()
    if secim == "4": bol()





def topla():
    tbir = int(input("Lütfen Birinci Değeri Giriniz."))
    tiki = int(input("Lütfen İkinci Değeri Giriniz."))
    print("Girimiş Olduğunuz Değerlerin Toplamı", tbir+tiki ,"Eder")


def cikar():
  cbir = int(input("Lütfen Çıkarmak İstediğiniz Birinci Değeri Giriniz."))
  ciki = int(input("Lütfen Çıkarmak İstediğiniz İkinci Değeri Giriniz."))
  print(cbir,"Değeri İle", ciki ,"Değerinin Çıkarımı", cbir-ciki ,"Eder")



def carp():
  cbir = int(input("Lütfen Çarpmak İstediğiniz Birinci Değeri Giriniz"))
  ciki = int(input("Lütfen Çarpmak İstediğiniz İkinci Değeri Giriniz."))
  print(cbir, "Değeri İle", ciki ,"Değerinin Çarpım Sonucu:", cbir*ciki ,"Eder.")


def bol():
  cbir = int(input("Lütfen Bölmek İstediğiniz Birinci Değeri Giriniz"))
  ciki = int(input("Lütfen Bölmek İstediğiniz İkinci Değeri Giriniz."))
  print(cbir, "Değeri İle", ciki ,"Değerinin Bölüm Sonucu:", cbir/ciki ,"Eder.")




