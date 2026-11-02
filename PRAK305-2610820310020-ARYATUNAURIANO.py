Detik = int(input("Masukkan Detik: "))

hari = Detik // 86400
jam = (Detik % 86400) // 3600
menit = (Detik % 3600) // 60
detik = Detik % 60



if Detik >= 86400:
    print(f" {hari} hari { jam:02d}:{menit:02d}:{detik:02d}")
else:
    print(f"{jam:02d}:{menit:02d}:{detik:02d}")