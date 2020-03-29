#!/usr/bin/python3
data = [
    ['apel', 'mangga', 'jeruk'],
    [2000, 5000, 3500]
]
print(data)

index = 0
buah, harga = data

for urutan in range(len(buah)):
    print(index, 'Buah', buah[urutan], 'harganya', harga[urutan])
    index += 1

counter = 0
for cek in buah:
    if cek == 'mangga':
        break
    else:
        counter += 1

print('\nmangga berada pada index', counter)

data[0].pop(counter) # hapus buah
data[1].pop(counter) # hapus harga
print('mangga dihapus!')

print(data)
