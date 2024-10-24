inventory = {}
def menambah_barang ():
    try:
        print("=== Tambah Barang ===")  
        id = int(input("Masukkan ID Barang: "))  
        if id in inventory:
            raise ValueError("ID barang sudah ada, gunakan ID yang berbeda.")
        nama = input("Masukkan Nama Barang: ") 
        for i in inventory.values(): 
            if i["nama"] == nama:
                raise ValueError("nama barang sudah ada, gunakan nama yang berbeda.")
        jumlah = int(input("Masukkan Jumlah Barang: ")) 
        if jumlah < 0 :
             raise ValueError("jumlah barang yang di inputkan tidak valid.")
        harga = float(input("Masukkan Harga Barang: "))
        if harga < 0 :
            raise ValueError(" harga yang di inputkan tidak valid.")

        inventory[id] = {"nama": nama, "jumlah": jumlah, "harga": harga}  
        print("Barang berhasil ditambahkan!")  
    except ValueError :
        print("Masukkan angka yang valid")



def menghapus_barang ():
    try :
        print ("=== Hapus Barang ===")  
        for i in inventory:  
                print(f"ID: {i}, Nama: {inventory[i]['nama']}, Jumlah: {inventory[i]['jumlah']}, Harga: {inventory[i]['harga']}")
        id = int(input ("Masukkan ID barang: "))
        if id in inventory :
            del inventory[id]
            print ('Barang telah dihapuskan')
        else :
            print ('Barang tidak ditemukan dalam list')
    except ValueError:
        print ("TIDAK VALID")


def menampilkan_barang():
    
        print("=== Daftar Barang ===")  
        if not inventory:  
            print("Tidak ada barang dalam inventory.")  
        else:  
            for i in inventory:  
                print(f"ID: {i}, Nama: {inventory[i]['nama']}, Jumlah: {inventory[i]['jumlah']}, Harga: {inventory[i]['harga']}")  
   



def mencari_barang ():
    try :
        id = int (input ("Masukkan ID barang : "))
        if id in inventory :
            nama = inventory[id]['nama']
            jumlah = inventory[id]['jumlah']
            harga = inventory[id]['harga']
            print(f"ID: {id}, Nama: {nama}, Jumlah: {jumlah} unit, Harga: {harga}")
        else :
            print (f"Barang tidak ditemukan")
    except ValueError: 
        print ("TIDAK VALID")  
         



def mengupdate_barang ():
    try :
        print ("=== Update Barang ===")
        for i in inventory:  
                print(f"ID: {i}, Nama: {inventory[i]['nama']}, Jumlah: {inventory[i]['jumlah']}, Harga: {inventory[i]['harga']}")            
        id = int(input ("Masukkan ID barang: "))
        if id in inventory :
            nama_baru  = input ("Masukkan nama barang baru: ")
            inventory[id]["nama"]  = nama_baru
            jumlah_baru = int (input('Masukkan jumlah barang yang ingin ditambahkan:'))
            inventory [id]["jumlah"] +=  jumlah_baru 
            if  jumlah_baru  < 0 :
                raise ValueError ("Update barang tidak valid ")
            harga_baru =  float (input('Masukkan harga barang baru:'))
            inventory [id]["harga"] = harga_baru
            print (f"Barang {id} berhasil di update, Nama sekarang :{inventory[id]['nama']},  Jumlah sekarang: {inventory[id]['jumlah']}, Harga sekarang :{inventory[id]['harga']} ")
        else :
            print ("Barang tidak ada di list")
    except ValueError:
        print (" TIDAK VALID")

    
def menu ():
    try :
        while True :
            print ((3* "=" + "Menu Inventory" + 3* "=").upper())
            print ((' 1. Tambah barang ').upper())
            print ((' 2. Hapus barang ').upper())
            print ((' 3. Tampilkan daftar barang').upper())
            print ((' 4. Cari Barang ').upper())
            print ((' 5. Update barang ').upper())
            print ((' 6. Keluar').upper())

            pilihan = (input('Masukkan opsi 1-6:'))

            if pilihan == "1":
                menambah_barang()
            elif pilihan == "2":
                menghapus_barang()
            elif pilihan == "3":
                menampilkan_barang()
            elif pilihan == "4":
                mencari_barang()
            elif pilihan == "5":
                mengupdate_barang()
            elif pilihan == "6":
                print("Program keluar.")
                break
            else:
                print("Opsi tidak valid, silakan coba lagi.")
            
    except ValueError : 
        print ("TIDAK VALID")


menu()

