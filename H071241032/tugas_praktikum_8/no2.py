import re
def IPaddress(baris):
    sifour =r"^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\."\
            r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\."\
            r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\."\
            r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$"
    sisix = r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$"
    addres = []
    for i in range(baris):
        ip = input("masukkan IP : ")
        if re.fullmatch(sifour,ip):
            addres.append("Ipv4 addres")
        elif re.fullmatch(sisix,ip):
            addres.append("Ipv6 addres")
        else:
            addres.append("bukan IP address")
    for i in addres:
        print(i)
d = int(input("masukkan baris : "))
IPaddress(d)




