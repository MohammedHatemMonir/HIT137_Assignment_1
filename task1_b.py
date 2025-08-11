"""
Group Name: Sydney 11
Group Members:
Mohamed Hatem Moneir Mansour Elshekh - 393891
Roshan Pandey - 395865
Kamana Thapa - 392322
Sejal Pradhan - 396928
"""

print("""
  ____                               ____                              
 / ___|  __ _ _   _  __ _ _ __ ___  |  _ \ _ __ __ ___      _____ _ __ 
 \___ \ / _` | | | |/ _` | '__/ _ \ | | | | '__/ _` \ \ /\ / / _ \ '__|
  ___) | (_| | |_| | (_| | | |  __/ | |_| | | | (_| |\ V  V /  __/ |   
 |____/ \__, |\__,_|\__,_|_|  \___| |____/|_|  \__,_| \_/\_/ \___|_|   
           |_|                                                         
        """)    #r in print allows pythin to draw line breaks too, used it to add this text deawing -Mohamed

#This function was also used in task-1, It is very generic so I used it here aswell -Mohamed
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

size = 0

while size <= 0 or size > 100 : #Make sure that the size is greater than 0 before drawing
    size = get_int_from_user("Enter the size of the square: ")
    if size <= 0 or size > 100:
        print("Please enter a number between 1 and 100.")


for i in range(size): #make a loop based on the number we have taken from the user

    if i == 0 or i == size - 1: 
        print("* " * size)
    else:
        print("* " + "  " * (size - 2) + "*")


"""
References:

w3schools
https://www.w3schools.com/python
Used w2schools for python syntax

w3schools
https://www.w3schools.com/python/python_functions.asp
used w3schools to learn the functions

w3schools
https://www.w3schools.com/python/gloss_python_multi_line_strings.asp
Multi-line strings, used for printing "Square Drawer"

Console Text Generator
https://edukits.co/text-art
Used this to get the "Square Drawer" design at the beginning of the program.

"""
