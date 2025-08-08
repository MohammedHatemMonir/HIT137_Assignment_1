"""
Group Name: Sydney 11
Group Members:
Mohamed Hatem Moneir Mansour Elshekh - 393891
Roshan Pandey - 395865
Kamana Thapa - 392322
Sejal Pradhan - 396928
"""

# 1a: Check if three numbers can form a triangle

def can_form_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a #boolean expression of the equation that detects wether or not we can create a triangle within givent lengths


def get_int_from_user(name): #function that takes input from user and CHECKS if it's int
    isNumber = False #Variable to keep track wether we have a number or not
    while isNumber == False: #This while loop keeps going until we have a number.
        try:
            user_input = input(str(name)) #write a custom message to the user
            try:
                val = float(user_input) #Round the float numbers to get an int (without breaking the loop to make it more smooth for the user)
                user_input = round(val)
            except:
                pass

            val = int(user_input) #if this did not go to the except, we have got a valid number
            isNumber = True #mark that we got a number
            return val #Return the number and exit the while loop
        except:
            print("That's not a number! Please enter a valid, correct number.")
            #Do A while loop here to get the number

print("Triangle Checker") 
x = get_int_from_user("Enter First Number: ") #get the first number using the generic function, the parameter in the function is what is displayed to the user
y = get_int_from_user("Enter Second Number: ") #get the second number
z = get_int_from_user("Enter Third Number: ") #get the third number

if can_form_triangle(x, y, z): #use the function that detects wether or not we can form a triangle, it returns a boolean expression (true or false)
    print("Yes, %d, %d, %d can form a triangle." % (x,y,z))
else:
    print("NO, %d, %d, %d CANNOT form a triangle." % (x,y,z))


"""
References:
Stack overflow.
https://stackoverflow.com 
Used stack overflow for syntax correction and suggestions on how to check variable type

w3schools
https://www.w3schools.com/python
Used w2schools for python syntax

Brian McLogan (Youtube)
https://youtu.be/gSmuLNGpf_E
Used his video for the equation to determin if the numbers can form a triangle
"""
