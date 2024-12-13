lolos = True
Gagal = []
a = int(input("Masukan nilai rata-rata akademik: "))
if a<85:
    lolos = False
    Gagal.append("Nilai akademik kurang dari 85")
b = int(input("Masukan  jumlah kegiatan ekstrakurikuler yang diikuti: "))
if b<3:
    lolos = False
    Gagal.append("Jumlah kegiatan ekstrakurikuler kurang dari 3")
for i in range (1,b+1):
    poin = int(input(f"Masukkan nilai keaktifan untuk kegiatan {i}: "))
    if poin<70:
        lolos = False
        Gagal.append("Nilai keaktifan kurang dari 70")
c = int(input("Masukkan pendapatan keluarga per bulan (dalam RM): "))
if c>3000:
    lolos = False
    Gagal.append("Kamu orang kaya")
d = int(input("Masukkan nilai tes wawancara: "))
if d<75:
    lolos = False
    Gagal.append("Nilai wawancara kurang dari 75")
if lolos:
    print("Selamat! Anda lolos Beasiswa")
else:
    print(f"Tidak Lolos Beasiswa:")
    for char in Gagal:
        print(char)