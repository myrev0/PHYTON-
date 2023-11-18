import konsolm

liste = ["Kadir","Dilara","Uğur","Ediz","Helin","Yusuf"]
puan_kadir = 100
puan_dilara = 100
puan_ugur = 100
puan_ediz = 100
puan_helin = 100
puan_yusuf = 100



def menu():

    secim = input("Lütfen Adınızı Giriniz.")

    if secim == "Kadir":
        print("Hoş Geldin Kadir. Puanın :",puan_kadir,"İyi Günler.")
    
    if secim == "dilara":
        print("Hoş Geldin Dilara. Puanın :",puan_dilara)
    
    if secim == "ugur":
        print("Hoş Geldin Uğur. Puanın :",puan_ugur)
    
    if secim == "ediz":
        print("Hoş Geldin Ediz. Puanın :",puan_ediz)

    if secim == "helin":
        print("Hoş Geldin Helin. Puanın :", puan_helin)
    
    if secim == "yusuf":
        print("Hoş Geldin Yusufa. Puanın",puan_yusuf)

    konsolm.konsolmenu()
    