def jumlah_penghapusan_minimum(s1, s2):
    frekuensi_s1 = [0] * 26
    frekuensi_s2 = [0] * 26

    for char in s1:
        frekuensi_s1[ord(char) - ord('a')] += 1

    for char in s2:
        frekuensi_s2[ord(char) - ord('a')] += 1

    penghapusan = 0
    for i in range(26):
        penghapusan += abs(frekuensi_s1[i] - frekuensi_s2[i])

    return penghapusan

string1 = input("Masukkan string pertama: ")
string2 = input("Masukkan string kedua: ")
    
jumlah_penghapusan = jumlah_penghapusan_minimum(string1, string2)
print(f"Jumlah minimum penghapusan untuk membuat anagram: {jumlah_penghapusan}")
