class Ilan:
    def __init__(self,gilanno,gbaslik,gaciklama):
        self.ilanno = gilanno 
        self.baslik = gbaslik 
        self.aciklama = gaciklama
    def __str__(self) -> str:
        return f"({self.ilanno})"
    
class Emlak(Ilan):
    def __init__(self, gilanno,gbaslik,gaciklama,gadres,gfiyat):
        self.ilanno = gilanno
        self.baslik = gbaslik 
        self.aciklama = gaciklama 
        self.adres = gadres 
        self.fiyat = gfiyat 
    def __str__(self) -> str:
        return f"{self.ilanno} {self.baslik} {self.aciklama} {self.adres} {self.fiyat}"
    

class Tasit(Ilan):
    def __init__(self, gilanno,gbaslik,gaciklama,gadres,gfiyat,gmodel,gmarka,gtipi,grengi,gkm):
        self.ilanno = gilanno 
        self.baslik = gbaslik 
        self.aciklama = gaciklama 
        self.adres = gadres     
        self.fiyat = gfiyat 
        self.model = gmodel
        self.marka = gmarka 
        self.tip = gtipi 
        self.renk = grengi 
        self.km = gkm 
    def __str__(self) -> str:
        return f"{self.ilanno} {self.baslik} {self.aciklama} {self.adres} {self.fiyat} {self.model} {self.marka} {self.tip} {self.renk} {self.km}"
    
        
ilan1 = Emlak("1","Sahibinden Satılık Villa","Sahibinden Satılık Gölbaşı Çayyolunda Villa","Ankara/gölbaşı","24000000")
ilan2 = Tasit("2","TEK DEĞİŞEN YILLAR","DEĞİŞENSİZ ÇITIR HASARLI","ANKARA/KIZILAY","299.000","Doğan SLX 1.6 ie", "Tofaş","sedan","gri","100000")

print(ilan1)
print("İlan Bilgisi",ilan2)
input()
