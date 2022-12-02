def hitungKata(kalimat):
    c = input("Masukan kata yang ingin dihitung : ").lower()
    ab = kalimat.count(c)

    return ab, c
def ubahKata(kalimat):
    c = input("Masukan kata yang ingin diubah : ").lower()
    d = input("Masukan kata pengganti : ").lower()
    ab = kalimat.replace(c, d)
   

    return ab, c, d
print ("=======Program Manipulasi String=======")
print ("Pilihan Menu")
print ("1. Hitung kata")
print ("2. ubah kata")


a = int(input("Pilihan anda : "))
b = input("Masukan sebuah kalimat/kata : ")
kalimat = b.lower()

if a == 1:
    ab = hitungKata(kalimat)
    print(f"Terdapat sebanyak {ab[0]} kata {ab[1]}")

else:
    ab = ubahKata(kalimat)
    print(f"String berhasil diubah menjadi : {ab[0]}")
   
