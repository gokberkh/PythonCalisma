"""import keyword
print(keyword.kwlist)"""

#basit aylık yol ücreti hesaplama

günsayisi=30
gidisücreti=1.25
gelisücreti=2.25
masraf=günsayisi*(gidisücreti+gelisücreti)
print(masraf)

#pow fonksiyonu

print(pow(12,2,5)) #ilk parametresi sayı ,ikincisi üssünü alıyor,ücüncüsü bölüp kalanı söylüyor

# değişkenleri takas etme
A="Proje sorumlusu"
B="Arge müdürü"
A,B=B,A
print(A,"Artık",B+" Oldu")

#tırnak kullanımı
print('Python programlama dilinin adı "piton" yılanından gelmez')


#txt olusturup yazma işlemi

dosya = open("deneme.txt", "w")
print("Ben Python, Monty Python!", file=dosya)
dosya.close()

f=open("kisiselbilgi.txt","w")
print("Gokberk",file=f,flush=True)
print("Hidiroglu",file=f)
print("23",file=f)
f.close()

#yıldızlı parametre
print(*"Linux", sep=".")
print(*"Sivasspor")
print(*"abcçdefgğh", sep="/")