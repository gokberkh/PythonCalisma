""""
print("Python\nHello")
#selam
print ("1","4","2018",sep=".")
a=3
b=3.14
c="selam"
d= [1,2,3,4,5,"Selam"]
e= (1,2,3,4,5,"Selam")
f={"selam":3,"armut":4,"kiraz":5}
g=False
f=[a,b,c,d,e,f,g]

for x in f:
    print(type(x))

    print("Toplam = ",5+9)
    print("Çıkarma = ",15-2)
    print("Bölme = ",15/5)
    print("Çarpma = ",9*8)
    break"""



sayi=int(input("Bir sayi girin:"))

if sayi<5: #blok girinti ile baslatılmaz
      print("Sayisiniz 5 ten kücüktür")
elif sayi>5:
     print("Sayiniz 5 ten büyüktür")
else:
      print("Sayiniz 5 e eşit!!")


