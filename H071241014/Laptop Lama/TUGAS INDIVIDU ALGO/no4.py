namaKaryawan = input("Masukkan nama karyawan: ")
tarifPerJam = int(input(f"Masukkan tarif per jam {namaKaryawan}: "))
jamKerja = int(input(f"Masukkan jam kerja {namaKaryawan} dalam sebulan: "))
jamWeekend = int(input(f"Masukkan ja kerja di weekend {namaKaryawan}: "))

jamNormal = jamKerja - jamWeekend
gajiBulanan = tarifPerJam * jamNormal
gajiWeekend = tarifPerJam * 1.5 * jamWeekend


if jamKerja > 150:
    bonus = 500000
elif jamKerja > 100:
    bonus = 200000
else:
    bonus = 0

total = gajiBulanan + gajiWeekend + bonus
print(f"total Gaji {namaKaryawan}: {total:,.0f}")