inventory = {
    "gelas": 2,
    "piring": 10,
    "mangkuk": 21
}

def hapusBarang(inventory: dict, namaBarang):
    try:
        del inventory[namaBarang]
        return inventory
    except Exception as e:
        return 0

def updateBarang(inventory: dict, namaBarang, jumlah):
    try:
        inventory[namaBarang] = jumlah
        return inventory
    except Exception as e:
            return e
        
def tampilkanInventory(inventory):
    print("=================================")
    print("            Inventory            ")
    for i in inventory:
        print(f"{i} : {inventory[i]}")
    print("=================================")
   

def cariBarang(inventory, namaBarang):
    try:
        return inventory[namaBarang]
    except Exception as e:
        print(e)
        return 0

def inputBarang(inventory, namaBarang, jumlah: int):
    if namaBarang in inventory:
        inventory[namaBarang] += jumlah
    else:
        inventory[namaBarang] = jumlah    

    return inventory

while True:
    print("=================================")
    print("Selamat Data di Program Inventory")
    print("=================================")
    print("1. Menambah Barang")
    print("2. Menghapus Barang")
    print("3. Menampilkan Daftar Barang")
    print("4. Mencari Barang")
    print("5. Mengupdate Data Barang")
    print("0. Stop")
    print("=================================")
    opsi = int(input("Pilih Opsi : "))
    
    operasi = 1

    if opsi in range(1, 6):
        if opsi != 3:
            print("=================================")
            if operasi == 1:
                print("            Inventory Awal            ")
            else:
                print("            Inventory            ")
            for i in inventory:
                print(f"{i} : {inventory[i]}")
            print("=================================")

    match opsi:
        case 0:
            break
        case 1:
            print("------- Menambah barang -------")
            namaBarang = input("Nama Barang : ")
            jumlahBarang = int(input("Jumlah Barang : "))

            if jumlahBarang < 1:
                print("Penambahan barang tidak boleh kurang dari 1")
            else:
                inventory = inputBarang(inventory, namaBarang, jumlahBarang)
                tampilkanInventory(inventory)
        case 2:
            print("------- Menghapus barang ------")
            namaBarang = input("Nama Barang : ")
            res = hapusBarang(inventory, namaBarang)
            if res == 0:
                print("Barang tidak ditemukan")
            else:
                tampilkanInventory(inventory)
        case 3:
            tampilkanInventory(inventory)
        case 4:
            print("-------- Mencari Barang -------")
            namaBarang = input("Nama Barang : ")
            barang = cariBarang(inventory, namaBarang)
            if barang == 0:
                print("Barang tidak ditemukan")
            else:
                print("=================================")
                print(f"{namaBarang} : {barang}")
        case 5:
            print("-------- Update Barang --------")
            namaBarang = input("Nama Barang : ")
            if namaBarang not in inventory:
                print("Barang tidak ditemukan")
            else:
                jumlahBarang = int(input("Jumlah Barang : "))
                if jumlahBarang < 0:
                    print("Jumlah barang tidak boleh kurang dari 0")
                else:
                    inventory = updateBarang(inventory, namaBarang, jumlahBarang)
                    tampilkanInventory(inventory)
        case _:
            print("Opsi tidak valid")

    konfirmasi = input("Masi ingin melanjutkan (y/t) : ").lower()

    operasi += 1

    if konfirmasi != "y":
        break
