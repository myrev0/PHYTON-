

def gectikaldi():


    puan = int(input("Lütfen Notunuzu Giriniz:"))

    if puan <0 or puan>100:
        print("Lütfen Geçerli Bir Sayı Giriniz. 0-100")
        gectikaldi()
    else:
        if puan > 50:
            print("Geçtiniz Tebrikler.")
            if puan > 90: print("Süpersin.")
            elif puan > 70: print("Orta Seviye")
            elif puan > 65: print("İdare Eder.")
        else:
            print("Kaldın.")


    
            
