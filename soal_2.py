#!/usr/bin/python3
# Muhammad Shofuwan Anwar
# 18/431931/SV/15902

arr_a = [21, 34, 41, 22, 35]
arr_b = [61, 34, 45, 21, 11]
dump_intersec = []

print("Intersection finder")
print("Array A : ", arr_a)
print("Array B : ", arr_b)

for x in range(len(arr_a)):
    if arr_a[x] == arr_b[x]:
        dump_intersec.append(arr_a[x])

print("\nIntersec : ", dump_intersec)
