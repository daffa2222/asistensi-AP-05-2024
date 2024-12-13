def nilai(benar, salah):
    TotalSoal = benar+salah
    if  TotalSoal>50:
        print("Tidak Valid")
    elif TotalSoal==0:
        print("Anda di diskualifikasi")
    else:
        skor = benar*5+salah*-3
        print(f"skor total : {skor}")
        print(f"Soal dijawab : {TotalSoal}")
        if skor>100:
            print("Lolos ke tahap selanjutnya")
        else:
            print("Pesertanya di Nyatakan Gugur")
nilai(45,5)

