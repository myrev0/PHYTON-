#syntax night code
#yönetici paneli

def sistem():
    arabalar = ["BMW 3.2D","Tofaş Doğan SLX","Mercedes E200 Compressor","Fiat Linea"] # Arabalar Listesi
    print("Stoktaki Araçlarımız:",arabalar) # Arabalar Listesindeki Arabaları Göstericek
    eklenti = input("Stok Eklemek İçin Araba Marka Model Giriniz.")

    arabalar.insert(4,eklenti)
    print("Eklenen Aracımız:",arabalar)

    silme = int(input("Silmek İstediğiniz Aracın Numarasını Giriniz."))

    arabalar.pop(silme)
    print("Silinen Araç",arabalar)
