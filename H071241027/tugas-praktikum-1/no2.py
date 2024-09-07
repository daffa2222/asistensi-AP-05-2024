karakter = input("Masukkan sebuah abjad : ")
kalimat = input("Masukkan Kalimat : ")

pesan = "Abjad merupakan bagian dari Kalimat" * (karakter in kalimat) + \
        "Karakter tidak ditemukan dalam Kalimat" * (karakter not in kalimat)

print(pesan)