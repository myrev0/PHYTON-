import hesapm
import oyun
import nothesabı
import for1
      
def konsolmenu():

  print("╔═════════════════════════╗")
  print("║      Console Menu       ║")
  print("║                         ║")
  print("║*Hesap Makinesi          ║")
  print("║*Oyun                    ║")
  print("║*Proje                   ║")
  print("║*sayı sor                ║")
  print("║*Çıkış (e)               ║")
  print("╚═════════════════════════╝")

  secim = input("")
  print("Seçim Yapınız. 1-6", secim)
  if secim == "1":
    hesapm.hesap()
    konsolmenu()
  if secim == "2":
    oyun.bilmece()
    konsolmenu()
  if secim == "3":
    nothesabı.gectikaldi()
    konsolmenu()
  if secim == "4":
    for1.saydir()
    input("Menüye Dönmek İçin 'ENTER' Tuşuna Basınız.")
    konsolmenu()
    

  if secim == "5" or "e":
    print("Programdan Çıkılıyor.")
    exit()






