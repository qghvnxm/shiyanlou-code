#!/usr/bin/env python3
n = int(input("Enter the value of n: "))
print("Enter values for the Matrix A")
a = []
for i in range(n):
    a.append([int(x) for x in input().split()])
print("Enter values for the Matrix B")
b = []
for i in range(n):
    b.append([int(x) for x in input().split()])
c = []
for i in range(n):
    c.append([a[i][j] * b[i][j] for j in range(n)])
print("After matrix multiplication")
print(c)
print("-" * 7 * n)
for x in c:   ##equal to the key in the C
    for y in x:
        print(str(y).rjust(5), end=' ')##make the 5 blank(include the exit numbers)
    print()
print("-" * 7 * n)
