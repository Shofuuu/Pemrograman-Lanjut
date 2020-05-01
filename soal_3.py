#!/usr/bin/python3
# Muhammad Shofuwan Anwar
# 18/431931/SV/15902
import random

data = []
modus = {}
median = 0

for x in range(20):
    data.append(random.randint(1, 100))

print("Collected Data :", data)

counter = 0
for x in range(20):
    for y in range(20):
        if data[x] == data[y]:
            counter += 1
    modus[data[x]] = counter
    counter = 0

print("\nModus : ")
print(modus)

for x in range(20):
    median += data[x]
median /= 20

print("\nMedian : ", round(median))
