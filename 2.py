def cetakAngka(kata):
    if len(kata) % 2 == 1:
        a = len(kata)//2

        if (len(kata) % 2 == 0) and ((len(kata) / 2) % 2 == 0):
            return kata[(a) // 2 : ((a) // 2) * -1]
        elif (len(kata) % 2 == 0) and ((len(kata) / 2) % 2 != 0):
            return kata[((a) // 2) + 1 : (((a) // 2) + 1) * -1]
        else:
            return kata[(((a) + 1) // 2) : (((a) + 1) // 2) * -1]
    else:
        b = kata[:3]
        c = kata[-3:]
        return b,c

kata = str(input("Masukan kata : "))
if len(kata) % 2 == 1:
    print ("Huruf yang diambil pada kata", kata, "adalah", cetakAngka(kata))
else:
    print ("Huruf yang diambil pada kata", kata, "adalah", cetakAngka(kata)[0], "dan", cetakAngka(kata)[1])

