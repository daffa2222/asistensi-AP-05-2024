jumlahUang = int(input("Masukkan jumlah uang Lina: Rp "))
totalBelanja = []
i = 0
while True:
    harga = input(f"Masukkan harga barang ke-{i+1}: (Enter untuk menghentikan program) Rp  ")
    if not harga:
        break
    totalBelanja.append(int(harga))
    i += 1
    
    
total = sum(totalBelanja)
sisaSaldo = jumlahUang - total

if jumlahUang >= total:
    print(f"""Total belanja Bu Cila adalah: Rp {total:,}
Uang Lina cukup untuk membayar belanjaan. Sisa saldo Lina 
adalah Rp {sisaSaldo}""")
else:
    print(f"Uang lina tidak cukup untuk membayar belanjaan. Kekurangan saldo -{sisaSaldo}")