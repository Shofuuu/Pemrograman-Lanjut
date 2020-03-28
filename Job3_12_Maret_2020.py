def fibb(x):
    if x <= 1:
        return x

    return fibb(x-1)+fibb(x-2)

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610,
for x in range(16):
    print(fibb(x), end=", ")