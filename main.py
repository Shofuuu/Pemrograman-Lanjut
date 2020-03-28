#!/usr/bin/python3
str = "Simple adder"
print(str)
x = int(input("Data 1 : "))
y = float(input("Data 2 : "))
z = input("Random Text : ")

print("x + y =", (x+y), "| tipe :", type(x))

y = int(y)
data_logic = {"x and y":(x&y), "x or y":(x|y), "x xor y":(x^y), "x == y":(x==y), "x > y":(x>y)}
data_arith = {"x+y":x+y, "x-y":x-y, "x/y":x/y, "x*y":x*y, "x**y":x**y}

print(data_logic.keys())
print(data_logic.values())
print("\n", data_arith.keys())
print(data_arith.values())
print("Random " + z + " Text")