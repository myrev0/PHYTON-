import gun
import hesapm
import oyun
import nothesabı
import moralbankasi
import akilli_takvim
import onsis.login
import gun
import yt


def sifre():
  print("╔════════════════════════════════╗")
  print("║         Account Screen         ║")
  print("║                                ║")
  print("║  User Name:                    ║")
  print("║  Password:                     ║")
  print("║                                ║")
  print("║                                ║")
  print("╚════════════════════════════════╝")

  kadı = input("Lütfen Kullanıcı Adı Giriniz.")
  sifre = input("Lütfen Şifre Giriniz")

  if kadı == "myrev" and sifre =="123":
    print("\033[32mTebrikler Başarılı Bir Şekilde Giriş Yaptınız.\033[0m")
    konsolmenu()

  else:
    print("\033[31mMalesef Kullanıcı Adı Ve ya Şifre Uyuşmuyor. Lütfen Tekrar Deneyiniz.\033[0m")
    exit()






def konsolmenu():

  print("╔═════════════════════════╗")
  print("║      Console Menu       ║")
  print("║                         ║")
  print("║*Hesap Makinesi -1       ║")
  print("║*Oyun  -2                ║")
  print("║*Proje  -3               ║")
  print("║*Moral Bankası :)  -4    ║")
  print("║*Akıllı Takvim     -5    ║")
  print("║*Personel Takip Sistemi-6║")
  print("║*Hangi Gündeyiz -7       ║")
  print("║*Yazı Tura -8            ║")
  print("║                         ║")
  print("║                         ║")
  print("║*Çıkış (e)  -8           ║")
  print("╚═════════════════════════╝")

  secim = input("")
  print("Seçim Yapınız. 1-8", secim)
  if secim == "1":
    hesapm.hesap()
    konsolmenu()

  if secim == "4":
    moralbankasi.moral_soru()
    konsolmenu()

  if secim == "2":
    oyun.bilmece()
    konsolmenu()

  if secim == "3":
    nothesabı.gectikaldi()
    konsolmenu()

  if secim == "5":
    akilli_takvim.akilli_takvim()
    konsolmenu()

  if secim == "6":
    onsis.login.register()
    konsolmenu()

  if secim == "7":
    gun.gun()
    konsolmenu()

  if secim == "8":
    yt.yt()
    konsolmenu()





  if secim == "11":
    print("Programdan Çıkılıyor.")
    exit()



