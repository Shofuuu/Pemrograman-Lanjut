#!/usr/bin/python3
import random

top_val = int(input("Masukkan batas atas : "))
bottom_val = int(input("Masukkan batas bawah : "))
temp = 0

if top_val < bottom_val:
    temp = bottom_val
    bottom_val = top_val
    top_val = temp
print()

for x in range(5):
    print("Random Int ke " + str(x), random.randint(bottom_val, top_val)) # batas bawah dulu baru batas atas
print("=" * 30)

for x in range(5):
    print("Random Float ke " + str(x), int(random.random()*1000))
print("=" * 30)

for x in range(5):
    value = random.randint(bottom_val, top_val)
    if value % 2 == 0:
        sign = " Genap"
    else:
        sign = " Ganjil"
    print("Random cek sign ke " + str(x) + sign, value)
print("=" * 30)

for x in range(5):
    value = random.randint(-bottom_val, top_val)
    if value < 0:
        sign = " Negatif"
    else:
        sign = " Positif"
    print("Random cek sign ke " + str(x) + sign, value)
print("=" * 30)