harga_saham_kemarin = float(input("masukkan harga saham kemarin : "))
harga_saham_hari_ini = 105.0
persentase_perubahan = ((harga_saham_hari_ini - harga_saham_kemarin) / harga_saham_kemarin) * 100
rekomendasi ={
    persentase_perubahan > 5: "Beli",
    -3 < persentase_perubahan <= 5 :"Tahan",
    persentase_perubahan  < -3: "Jual"
}
rekomendasi_hasil = rekomendasi.get(True)

print(f"perubahan persentase harga saham : {persentase_perubahan:.2f}%")
print(f"Rekomendasi investasi : {rekomendasi_hasil}")

# n = int(input("Masukkan bilangan bulat n : "))
# x = "ganjil = "
# for i in range(1, n + 1):
#   if i % 2 != 0:
#       x +=f"{i}, " 
      
# o_g = x.rstrip (", ")

# print(o_g)