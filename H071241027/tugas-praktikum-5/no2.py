kalimat = input("Masukkan kalimat: ")

akronim = ''.join([kata[0].upper() for kata in kalimat.split()])

print(akronim)
