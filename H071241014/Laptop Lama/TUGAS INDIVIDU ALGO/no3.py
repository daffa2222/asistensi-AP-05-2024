nilaiUjian = int(input("Masukkan jumlah nilai ujian: "))
jumlahUjian = []

for i in range(nilaiUjian):
    nilai = int(input(f"Masukkan nilai ke-{i+1}: "))
    jumlahUjian.append(nilai)
    
rataRata = sum(jumlahUjian)/len(jumlahUjian)

if rataRata >= 80:
    status = "Lulus dengan Predikat A."
elif rataRata >= 70:
    status = "Lulus dengan Predikat B."
elif rataRata >= 60:
    status = "Lulus dengan Predikat C."
else:
    status = "Tidak Lulus"

print(f"Rata-rata nilai: {rataRata:.2f}")
print(f"Status: {status}")