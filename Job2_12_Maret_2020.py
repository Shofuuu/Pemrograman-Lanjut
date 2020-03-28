def genap(n, hg):
    # ketik program anda di sini
    if n % 2 == 0:
        hg = n
    else:
        hg = -1
    return hg

def ganjil(n, hj):
    # ketik program anda di sini
    if n % 2 != 0:
        hj = n
    else:
        hj = -1
    return hj

bil = [1, 6, 2, 9, 4, 5, 2, 3, 7]
jgenap = 0
jganjil = 0

# ketik program anda di sini (Pakai LOOP)
for x in range(len(bil)):
    if genap(bil[x], 0) != -1:
        jgenap += 1
    if ganjil(bil[x], 0) != -1:
        jganjil += 1

print('Jumlah Genap: ', jgenap, 'dan Jumlah Ganjil: ', jganjil)