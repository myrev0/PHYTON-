#Sytnax Night Code
import random
import konsolm


def oyun():

  print("\033[1;34;34m SAYI TAHMİN OYUNUNA HOŞ GELDİN\033[0m")

  sayi = int(input("Lütfen Sayı Tahmin Ediniz. 1-10"))

  rasgele = random.randint(1, 5)

  if sayi == rasgele:
    print("\033[1;32;32m Tebrikler Bildiniz\033[0m")
    konsolm.konsolmenu()
  else:
    print("\033[1;35;35m Malesef Bilemediniz. Tekrar Deneyiniz.\033[0m")
    print("Doğru Cevap", rasgele, "İdi.")
    oyun()


oyun()
