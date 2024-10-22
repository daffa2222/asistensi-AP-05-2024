inventory = {
    "gelas": {
        "id": "001",
        "jumlah": 10,
        "harga": 10000
    },
    "sendok": {
        "id": "002",
        "jumlah": 3,
        "harga": 4000
    }
}

def handleInput(pesanInput, tipe):
    while True:
        try:
            fieldInput = tipe(input(pesanInput))
            return fieldInput
        except ValueError:
            print("Input tidak valid")

def tingkatkanId(inventory):
    idTerakhir = int(inventory[list(inventory)[-1]]['id'])
    idSekarang = str(idTerakhir  + 1)
    return idSekarang.rjust(3, "0")

def tampilkanBarang(inventory):
    print("------------------------------------")
    print("            Daftar Barang           ")
    for temp in inventory:
        print("------------------------------------")
        print(f"Nama Barang : {temp}")
        print(f"Id : {inventory[temp]["id"]}")
        print(f"Jumlah : {inventory[temp]["jumlah"]}")
        print(f"Harga : {inventory[temp]["harga"]}")
    print("------------------------------------")

def inputBarang(inventory):
    namaBarang = handleInput("Input Nama Barang : ", str)
    if namaBarang not in inventory:
        id = tingkatkanId(inventory)
        jumlah = handleInput("Masukkan Jumlah : ", int)
        if jumlah < 1:
            print("Jumlah tidak boleh kurang dari 0")
            jumlah = handleInput("Masukkan Jumlah : ", int)
        harga = handleInput("Masukkan Harga : ", int)
        if harga < 0:
            print("Harga tidak boleh kurang dari 0")
            harga = handleInput("Masukkan Harga : ", int)
            
        inventory[namaBarang] = {
            "id": id,
            "jumlah": jumlah,
            "harga": harga
        }

        return inventory

def updateBarang(inventory, idBarang):
    barangDitemukan = False
    for temp in inventory:
        if inventory[temp]["id"] == idBarang:
            barangDitemukan = True

            nama = handleInput("Update Nama : ", str)
            if nama == "":
                print("Nama tidak boleh string kosong")
                nama = handleInput("Update Nama : ", str)
            jumlah = handleInput("Update Jumlah : ", int)
            if jumlah < 0:
                print("Jumlah tidak boleh kurang dari 0")
                jumlah = handleInput("Update Jumlah : ", int)
            harga = handleInput("Update Harga : ", int)
            if harga < 0:
                print("Harga tidak boleh kurang dari 0")
                harga = handleInput("Update Harga : ", int)
                
            inventory[nama] = inventory[temp]
            inventory[nama]["jumlah"] = jumlah
            inventory[nama]["harga"] = harga

            del inventory[temp]
            print("Berhasil update barang")
            return inventory
                
    if not barangDitemukan:
        return "Barang tidak ditemukan"

def cariBarang(inventory, idBarang):
    barangDitemukan = False
    for temp in inventory:
        if inventory[temp]["id"] == idBarang:
            barangDitemukan = True

            print("------------------------------------")
            print("           Barang Ditemukan         ")
            print("------------------------------------")
            print(f" Nama Barang : {temp}")
            print(f" Id : {inventory[temp]["id"]}")
            print(f" Jumlah : {inventory[temp]["jumlah"]}")
            print(f" Harga : {inventory[temp]["harga"]}")
            print("------------------------------------")
            
    if not barangDitemukan:
        print("Barang tidak ditemukan")

def hapusBarang(inventory, idBarang):
    barangDitemukan = False
    for temp in inventory:
        if inventory[temp]["id"] == idBarang:
            barangDitemukan = True
            del inventory[temp]
            return inventory
            
    if not barangDitemukan:
        return "Barang tidak ditemukan"

while True:
    print()
    print("===================================")
    print("Selamat Datang di Program Inventory")
    print("===================================")
    print("1. Menambah Barang")
    print("2. Menghapus Barang")
    print("3. Menampilkan Daftar Barang")
    print("4. Mencari Barang")
    print("5. Mengupdate Data Barang")
    print("0. Stop")
    print("===================================")
    opsi = handleInput("Pilih Opsi : ", int)

    if opsi == 0:
        break
    elif opsi not in range(1, 6):
        continue
    else: 
        if opsi not in range(3,5):
            tampilkanBarang(inventory)
        
    match opsi:
        case 1:
            print("=================================")
            print("         Menambah Barang         ")
            print("=================================")
            res = inputBarang(inventory)
            if type(res) == dict:
                inventory = res
                tampilkanBarang(inventory)
            else:
                print(res)
        case 2:
            print("=================================")
            print("         Hapus Barang            ")
            print("=================================")
            idBarang = input("Masukkan id : ")
            res = hapusBarang(inventory, idBarang)
            if type(res) == dict:
                inventory = res
                tampilkanBarang(inventory)
            else:
                print(res)
        case 3:
            tampilkanBarang(inventory)
        case 4:
            print("=================================")
            print("         Mencari Barang          ")
            print("=================================")
            idBarang = input("Masukkan id : ")
            cariBarang(inventory, idBarang)
        case 5:
            print("=================================")
            print("         Update Barang          ")
            print("=================================")
            idBarang = input("Masukkan id : ")
            res = updateBarang(inventory, idBarang)
            if type(res) == dict:
                inventory = res
            else:
                print(res)
        case _:
            continue