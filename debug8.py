#!python3
"""
Debug this program so that it runs

original code:
x = input("enter a decimal number"))
xi = int(x)
if (x - xi) == 0:
    print(f"{x} is an integer")
"""
x = input("enter a decimal number:")
x = float(x)
xi = round(x,0)

if x - xi == 0:
    print(f"{x} is an integer")
else:
    print(f"{x} is not an ineger")