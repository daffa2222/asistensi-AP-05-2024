# kata = input('kata : ')

# reversedKata = "".join(reversed(kata))

# if kata == reversedKata:
#     print("kata palindrom")
# else:
#     print("bukan kata palindrom")

def polindrom(kata):
    
    kata_balik = "".join(reversed(kata))
    
    if kata.lower() == kata_balik.lower() :
        print("Palindrome")
    else :
        print("Not palindrome")

polindrom("Ibu Ratna Antar Ubi")    