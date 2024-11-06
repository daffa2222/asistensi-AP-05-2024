import re
def sisfo(eee):
    if len(eee) != 45:
        return "False"
    apa = r"^[A-Z-a-z02468]{40}"
    haa = r"[13579\s]{5}$"
    eh = apa + haa
    if re.match(eh, eee):
        return "True"
    else:
        return "False"
karakter = input("Masukkan disini: ")
print(sisfo(karakter))
