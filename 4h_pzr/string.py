# a = "Erdinç DÖNMEZ"
# print (a[2])
# print (a[-3]) # sağdan index
# print (a[-3:]) # sağdan itibaren
# print (a[2:6]) #arası
# print (a[:6]) #6. indexe kadar
# print (a[2:]) #2. indexten sonra
# print (a[:])
# print (a[1:6:2]) // 1-6 arası 2şer atlayarak.
# print (len(a)) #uzunluk.


# abc = "kadir irsi"

# # print(abc[0:2]) # arası 
# # print(abc[0:6:2]) # abc değişken adı 0 başlangıç 6 sonu 2 kaçar kaçar gittiğini ifade ediyor.:) www.edrincdonmez.com

# a = "vektörel bilişim"

# for c in range(len(a)):
#     print(c)

a = input("Bir Metin Giriniz.")
b = input("Aradığınız Harfi Giriniz.")


aranan = 0
for abc in range(len(a)):
    if a[abc] == b:
        print("Başarılı")
