def enkripsi(text, shift):
    encrypted_text = ""
    
    for char in text:

        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)

        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)

        else:
            encrypted_text += char

    return encrypted_text

input_text = input("Masukkan string yang akan dienkripsi: ")
input_shift = int(input("Masukkan jumlah pergeseran (shift): "))

result = enkripsi(input_text, input_shift)
print(f"Text : {input_text}")
print(f"Shift : {input_shift}")
print("Cipher :", result)
