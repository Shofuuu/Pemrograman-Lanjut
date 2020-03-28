m_a = []
m_b = []

print("Tuliskan elemen -  elemen matriks A")
for y in range(2):
    for x in range(2):
        print("A[", y, ",", x, "] = ", end="")
        m_a.append(int(input()))

print("Tuliskan elemen - elemen matriks B")
for y in range(2):
    for x in range(2):
        print("A[", y, ",", x, "] = ", end="")
        m_b.append(int(input()))

print("\nC = A+B")

m_c = []
for y in range(2):
    temp = 0
    for x in range(2):
        temp = m_a[x] + m_b[x]
        m_c.append(temp)

for y in range(2):
    for x in range(2):
        print(m_c[x], end=" ")
    print()