a = []

for ab in range(15):
    satir=[]
    for b in range(15):
        satir.append("▒")
    a.append(satir)

satir1 = ""
for xx in a:
    for tt in xx:
        satir1 += tt
    print(satir1)
    satir1=""
