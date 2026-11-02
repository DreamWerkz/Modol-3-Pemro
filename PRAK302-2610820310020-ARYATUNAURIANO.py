#Soal 2

nilai = int(input("Masukkan angka: "))

if nilai > 0 and nilai <= 100:
    if nilai > 79 :
        print("A")
    elif nilai > 69:
        print("B")
    elif nilai > 59:
        print("C") 
    elif nilai > 49:
        print("D") 
    else:
        print("E")
else:
    print("Nilai yang dimasukkan tidak valid")