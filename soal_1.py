#!/usr/bin/python3
# Muhammad Shofuwan Anwar
# 18/431931/SV/15902
import random

full_item = [x for x in range(1, 1001, 1)]
missing_item = []

# copy item from full to missing
for x in range(len(full_item)):
    missing_item.append(full_item[x])

print("Item dalam keadaan penuh : ", full_item, end="\n\n")

del missing_item[random.randint(1,100)]
print("Item yang telah di hilangkan : ", missing_item, end="\n\n")

for x in range(len(missing_item)):
    if full_item[x] != missing_item[x]:
        print("Ditemukan!, item hilang adalah", full_item[x])
        break
