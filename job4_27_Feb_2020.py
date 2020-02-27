#!/usr/bin/python3
print("Tebak Segitiga")
sisi_a = int(input("Masukkan Sisi A : "))
sisi_b = int(input("Masukkan Sisi B : "))
sisi_c = int(input("Masukkan Sisi C : "))
flag1 = 0; flag2 = 0; flag3 = 0

if sisi_a <= (sisi_b + sisi_c):
    flag1 = 1
if sisi_b <= (sisi_c + sisi_a):
    flag2 = 1
if sisi_c <= (sisi_a + sisi_b):
    flag3 = 1

print("Hasil Cek :", "YA" if (flag1 & flag2 & flag3) == 1 else  "TIDAK")
