
# Group Name: Sydney 11
# Group Members:
# Mohamed Hatem Moneir Mansour Elshekh - 393891
# Roshan Pandey - 395865
# Kamana Thapa - 392322
# [Member 4 Name] - [Member 4 ID]

# 1a: Check if three numbers can form a triangle

def can_form_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a
def get_int_from_user(name): #function that takes input from user and CHECKS if it's int
    isNumber = False #Variable to keep track wether we have a number or not
    while isNumber == False: #This while loop keeps going until we have a number.
        try:
            user_input = input(str(name))
            val = int(user_input) #if this did not go to the except, we have got a valid number
            isNumber = True #mark that we got a number
            return val #Return the number and exit the while loop
        except:
            print("That's not a number! Please enter a valid, correct number.")
            #Do A while loop here to get the number

print("Triangle Checker")
x = get_int_from_user("Enter First Number: ")
y = get_int_from_user("Enter Second Number: ")
z = get_int_from_user("Enter Third Number: ")

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
