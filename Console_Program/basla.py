#syntax night code comminty [ig:syntaxncode]
#syntax Vektörel Bilişim Konsol Projem




# Evet arkadaşlar bunlar import ettiğim kütüphanelerim içeri aktardım ki çalışssın :D

import gun
import hesapm
import oyun
import nothesabı
import moralbankasi
import akilli_takvim
import onsis.login
import gun
import yt
import nightgaleri.kullanici
import sekil



# Prosödür amaçlı şifre oluşturma ve giriş ekranı
def sifre(): # fonksiyona attım ki main de görsün :)
  print("╔════════════════════════════════╗")
  print("║         Account Screen         ║")
  print("║                                ║")
  print("║  User Name:                    ║")
  print("║  Password:                     ║")
  print("║                                ║")
  print("║                                ║")
  print("╚════════════════════════════════╝")

  kadı = input("Lütfen Kullanıcı Adı Giriniz.") # klavyeden veri istedik
  sifre = input("Lütfen Şifre Giriniz") # " " "

  if kadı == "myrev" and sifre =="123": # Dedimki bunlar doğruysa adamı içeri al 
    print("\033[32mTebrikler Başarılı Bir Şekilde Giriş Yaptınız.\033[0m") # bu da onun printi
    konsolmenu() # ve başarılı olduktan sonra buraya git dedim.

  else: #değilse ki şöyle olacak
    print("\033[31mMalesef Kullanıcı Adı Ve ya Şifre Uyuşmuyor. Lütfen Tekrar Deneyiniz.\033[0m") #Şu mesajı vericek
    exit() # programdan çıkıcak, başa sardırırdım ama fonksiyon kullanığıma dair bir örnek olsun diye koydum. :D






def konsolmenu(): #Evet ve menü fonksiyonumuz

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
  print("║*Galeri Sistemi -9       ║")
  print("║*Şekil Çizme Programı -10║")
  print("║*Çıkış (e)  -8           ║")
  print("╚═════════════════════════╝")

  secim = input("") # İnputun İçine Yazı yazardım seçim yap diye ama print ile yaptım niye yaptım bende bilmiyom 
  print("Seçim Yapınız. 1-8", secim) # bunu inputla yapardım ama kullanımı gözüksün diye koydum ellam
  if secim == "1": # eğer secim değişkeni 1 ise str değer oluyor bu arkadaş int istemedim, canım öyle istedi :D
    hesapm.hesap() # Bu (dosyasındaki),(fonksiyon) adresine yönlendirdim.
    konsolmenu() # işi bitnce tekrar menüye dönsün, aynı insanlar gibi :(

  if secim == "4": # Aynısı İşte yaaaaaaa
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

  if secim == "9":
    night.kullanici.login_screen()
    konsolmenu()
  
  if secim == "10":
    sekil.sekil()
    konsolmenu()


  if secim == "11": # Haaaaaa Bu da 11 derse programdan çıkıyor işte.
    print("Programdan Çıkılıyor.") # bu printi
    exit() # bu da exit() fonksiyonu çıkar iştee...

  # Ben detayına göre bu dosyayı anlattım gerisi okuyup anlamaya kalmış :D
    # Okuduğunuz İçin Teşşekürlerimi Sunuyor İyi Günler Diliyorum.
    # Ha unutmadan @revolka-myrev :D Nickm


