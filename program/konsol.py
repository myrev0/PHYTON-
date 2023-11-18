# sytnax night code

import hesapm
import evektorel
import oyun
import yassınırı
import yas
import sinif

# sytnax night code



def ekran(): # Çalışabilmesi İçin Önce Bunu Fonksiyona Aldım Ki İlk Bu Alan Çıksın
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

  print("╔═════════════════════════╗")
  print("║      Console Menu       ║")
  print("║                         ║")
  print("║*Hesap Makinesi -1       ║")
  print("║*E Vektörel  -2          ║")
  print("║*sayı tahmin oyunu  -3   ║")
  print("║*Yaş Testi     -5        ║")
  print("║*Sınıf Bİlgileri         ║")
  print("║                         ║")
  print("║                         ║")
  print("║                         ║")
  print("║                         ║")
  print("║                         ║")
  print("║                         ║")
  print("║*Çıkış (e)               ║")
  print("╚═════════════════════════╝")  

  # Konsol Menüsünü Yaptım.

  secim = input("Lütfen Seçim Yapınız 1-10 Çıkış İçin E")
  if secim == "1":
    print("Hesap Makinasına Aktarıyorum")
    #hesapm.hesap()
            
  if secim == "2":
    print("E Vektörele Aktarıyorum")
    evektorel.menU()

  if secim == "3":
    print("Sayı Tahmin Oyununa Aktarıyorum")
    oyun.tahmin()

  if secim == "4":
    print("Yaş Testine Aktarıyorum")
    yas.yastesti()

  if secim == "5":
    print("Sınıf Bilgilerine Aktarıyorum")
    sinif.sinif_bilgi()
  if secim == "e" or "E":
     print("Programdan Çıkıyorsunuz")
     exit()
