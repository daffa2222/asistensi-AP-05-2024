jumlah_tim = int(input("Masukkan jumlah tim: "))

tim_data = []

print("""Masukkan data tim berturut-turut yang dibatasi spasi:
(NamaTim main menang seri kalah JumlahGol GolKebobolan)""")

for _ in range(jumlah_tim):
    data_tim = input().split()
    nama_tim = data_tim[0]
    main = int(data_tim[1])
    menang = int(data_tim[2])
    seri = int(data_tim[3])
    kalah = int(data_tim[4])
    jumlah_gol = int(data_tim[5])
    gol_kebobolan = int(data_tim[6])
    
    poin = menang * 3 + seri * 1
    selisih_gol = jumlah_gol - gol_kebobolan
    
    tim_data.append([nama_tim, poin, selisih_gol])

for i in range(len(tim_data)):
    for j in range(i + 1, len(tim_data)):
        if tim_data[i][1] < tim_data[j][1] or (tim_data[i][1] == tim_data[j][1] and tim_data[i][2] < tim_data[j][2]):
            tim_data[i], tim_data[j] = tim_data[j], tim_data[i]

for i in range(len(tim_data)):
    if i == 0:
        tim_data[i].append("[Lolos Otomatis]")
    elif i == 1:
        tim_data[i].append("[Lolos Otomatis]")
    elif i == 2 or i == 3:
        tim_data[i].append("[Play-Off]")
    else:
        tim_data[i].append("[Gugur]")

print("Klasemen Akhir:")
for tim in tim_data:
    print(f"{tim[0]} {tim[1]} Poin (Selisih Gol: {tim[2]}) {tim[3]}")
