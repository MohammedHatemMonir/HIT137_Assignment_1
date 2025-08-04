
# Group Name: Sydney 11
# Group Members:
# Mohamed Hatem Moneir Mansour Elshekh - 393891
# Roshan Pandey - 395865
# Kamana Thapa - 392322
# [Member 4 Name] - [Member 4 ID]

# 1a: Check if three numbers can form a triangle

def can_form_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

print("Triangle Checker")
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

if can_form_triangle(x, y, z):
    print("Yes, these three lengths can form a triangle.")
else:
    print("NO, these three lengths CANNOT form a triangle.")

# 1b: Print square of given size

print("\nSquare Drawer")
size = int(input("Enter the size of the square: "))

for i in range(size):
    if i == 0 or i == size - 1:
        print("* " * size)
    else:
        print("* " + "  " * (size - 2) + "*")
