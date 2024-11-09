def kapitalawalkata(string):
    n = len(string)
    for panjang in range(1, n + 1):
        for i in range(n - panjang + 1):
            substring = string[i:i + panjang]
            print(substring)


input = input("Masukkan sebuah string: ")

kapitalawalkata(input)
