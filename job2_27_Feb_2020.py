#!/usr/bin/python3
# JANGAN MENGUBAH BAGIAN PROGRAM YANG SUDAH DISIAPKAN.
# Silakan menulis bagian program anda pada area yang sudah disiapkan
import tkinter as tk
import random
def pesan(benar):
    root = tk.Tk()
    if benar:
        kal1 = "SELAMAT, ANDA BENAR!!!!"
        kal2 = "HOREEEEE HEBAATTTTTT"
    else:
        kal1 = "MAAF, ANDA SALAH!!!!"
        kal2 = "YAH SEDIH DEHHHH"
    tk.Label(root,
             text=kal1,
             fg="red",
             font="Times").pack()
    tk.Label(root,
              text=kal2,
              fg="light green",
              bg="dark green",
              font="Helvetica 16 bold italic").pack()
    tk.Label(root,
             font="Verdana 10 bold").pack()

    root.mainloop()

# KETIK PROGRAM ANDA DI ANTARA BARIS INI HINGGA BARIS YANG DIBERI TANDA #
# Your program is here

counter = 0
guest = random.randint(5, 8)
print("Mengacak Angka..")
benar = 0

for counter in range(3):
    print("[Try -", counter, "]")
    tebak = int(input("Tebak Angka > "))

    if tebak == guest:
        benar = 1
        break
    else:
        print("Try -1\n")

print("Jawaban :", guest)
# end of your program
pesan(benar)  # jangan dihapus
