Angka  = int(input("Masukkan angka: "))

if Angka > 0 and Angka < 100:
    if Angka == 10 or Angka >= 20 :
        print("puluhan")
    elif Angka > 10 and Angka < 20:
        print("belasan")
    elif Angka < 10:
        print("satuan")
elif Angka == 0:
    print("Nol.")
else:
    print("Anda Menginput Melebihi Limit Bilangan")