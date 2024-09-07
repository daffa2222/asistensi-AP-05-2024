harga_kemarin = float(input("Masukkan harga saham kemarin: "))
harga_hari_ini = 105.0 

perubahan_persen = ((harga_hari_ini - harga_kemarin) / harga_kemarin) * 100

rekomendasi = {
    True: "Beli",
    perubahan_persen <= 5 and perubahan_persen >= -3: "Tahan",
    perubahan_persen < -3: "Jual"
}.get(True, "Tahan")  

print(f"Perubahan persentase harga: {perubahan_persen:.2f}%")
print(f"Rekomendasi investasi: {rekomendasi}")
