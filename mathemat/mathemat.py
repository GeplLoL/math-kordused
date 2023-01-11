from random import *
#arv = randint(1,1000000)
#while True:
#    if arv>9999 and arv<100000:
#        print(arv)
#        break
#    else:
#        arv = randint(1,1000000)

#random = randint(1,100000)
#random1 = randint(1,100000)
#while True:
#    if random1<random:
#        for arv in range(random1,random):
#            if arv>9999 and arv<100000:
#                print(arv)
#                break
#        break
#    else:
#        random = randint(1,100000)
#        random1 = randint(1,100000)
x=0
hind = float(input("kui palju te tunnis saate? "))
päev= int(input("mitu päeva sa töötasid? "))
for i in range(1,päev+1,1):
    day = float(input("mitu tundi sa töötasid? "))
    kõik = float(hind) * day
    print("te teenisite" ,i,"päeva jooksul" ,kõik,"$")
    x+=kõik
    if i == päev:
        print("sinu palk: " ,round(x,2), "$")

#for x in range(1,101,1):
#    if x%5==0:
#        print(x, end="")
#try:
#    Num_horiz=int(input("Sisesta ruutude arv horisontaalselt =>> \n"))
#except:
#    print("Value Errror")
#    num_horiz=randint(1, 10000)
#try:
#    num_vert=int(input("Sisesta ruutude arv vertikallselt =>> \n"))
#except:
#    print("Value Error")
#    num_vert=randint(1,20)

  
#for y in range(num_vert):
#    for x in range(num_vert):
#        print("&", end=" ")
#    print("")