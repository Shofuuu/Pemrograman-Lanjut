#!/usr/bin/python3
print("--=[ Buku Programming With Python]=--")

book_price = 24.95*(40/100)
price_total = 0
book_total = int(input("Masukkan Jumlah Buku : "))

for book in range(book_total):
    if book == 0:
        price_total += book_price + 3
    else:
        price_total += book_price + 0.75
    print("Buku ("+str(book)+") :", "$"+str(price_total))

print("Harga yang harus dibayar :", str("$") + str(price_total))
