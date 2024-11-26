"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.

Enter a number: 6
Enter a number: 8
Is one of these the hypotenus: no

The missing side is 10

Enter a number: 6
Enter a number: 8
Is one of these the hypotenus: yes

The missing side is 6.7

"""

x=input("Enter a number:")
y=input("Enter a number:")
IsH = input("Is one of these the hypotenus?(Yes/No):")
z=2.22
x = float(x)
y = float(y)
z = float(z)

if IsH =="Yes" and y>x:
    z=(y**2-x**2)**0.5
    z=round(z,1)
    print(f"The missing side is {z}")
if IsH=="Yes" and x>y:
    z=(x**2-y**2)**0.5
    z=round(z,1)
    print(f"The missing side is {z}")
if IsH=="No":
    z=(x**2+y**2)**0.5
    z=round(z,1)
    print(f"The missing side is {z}")
    