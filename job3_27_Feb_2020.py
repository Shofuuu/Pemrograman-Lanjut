#!/usr/bin/python3

waktu = int(input("Masukkan Detik :"))

jam = int(waktu/3600)
menit = int((waktu%3600)/60)
detik = int((waktu%3600)%60)

print("Detik :", waktu, "\n\nJam :", jam, "\nMenit :", menit, "\nDetik :", detik)