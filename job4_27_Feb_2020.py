print("Tebak Segitiga")
sisi_a = int(input("Masukkan Sisi A : "))
sisi_b = int(input("Masukkan Sisi B : "))
sisi_c = int(input("Masukkan Sisi C : "))
flag = False

if sisi_a <= (sisi_b + sisi_c):
    flag = True

if sisi_b <= (sisi_c + sisi_a):
    flag = True
else:
    flag = False

if sisi_c <= (sisi_a + sisi_b):
    flag = True
else:
    flag = False

print("Hasil Cek : ", "YA" if flag == True else  "TIDAK")
