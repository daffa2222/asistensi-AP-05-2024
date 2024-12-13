Barang = int(input())
TotalHarga = []
for _ in range(Barang):
    Harga = int(input())
    TotalHarga.append(Harga)
    HargaUrut = sorted(TotalHarga)
print(HargaUrut)
if len(HargaUrut)>=2:
    HargaUrut[0] = HargaUrut[0]*0.9
Bayar = 0
for char in HargaUrut:
    Bayar+=char
if len(HargaUrut)>=3:
    Bayar = Bayar*0.95
print(int(Bayar))