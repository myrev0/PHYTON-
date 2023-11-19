#syntax night code 

soru = int(input("Ehliyet alabilmeniz için yaşınızı yazmanız gereklidir.")) # Ehliyet İçin Yaşını Sorduk

if soru >= 18: # İF ile Dedikki Eğer Yaşın 18 ve 18 den büyükse kabul etsin
    print("Evet Ehliyet Alabilirsini.") # budda ekrana yazı yazdırsın
else: # ama değilse
  print("\033[1;31;31m Ehliyet Alamazsınız") # ehliyet alamazsın baştaki garip kodlar kırmızı renk kodu 

  # ha dip not sona \0[0m eklemeseydik devamındaki printlere aynı rengi verirdi. Yani Kırmızı Olurdu

  #Synta Night Code İle Basit İf Komutu 