durasi = int(input("masukkan durasi parkir (dalam jam): "))
biaya = 0

if durasi == 1:
    biaya = 5000
else:
    biaya = 5000 + (durasi - 1) * 3000
    
print(f"Biaya parkir yang harus dibayar: Rp {biaya}")


