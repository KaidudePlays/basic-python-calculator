import os

sys_info = input("Display system information? \n Enter YES to display system information \n Prompt: ")
display_it = sys_info.upper()
os.system('clear')
if display_it == "YES".upper():
    print("System information: " + str(os.uname()))
    print(" ")
    print("You are running this on: " + os.name.upper())
    print(" ")
    clear = input("Click enter to move on and to clear the text: ")
    if clear == "" or clear != "":
        os.system('clear')

def addition():
    print("You chose addition!  \n Enter two numbers into the two prompts, click enter to get your calculation.")
    try:
        num1 = float(input("Enter the first number: "))
    except ValueError:
        exit("Only enter numbers!  Restart the program to try again.")
    try:
        num2 = float(input("Enter the second number: "))
        os.system('clear')
        try:
            add = num1 + num2
            print("Calculation: " + str(num1) + " + " + str(num2) + " = " + " " + str(add))
        except ValueError:
            quit("Only enter numnbers!  Restart the program to try again.")
    except ValueError:
        exit("Only enter numbers!  Restart the program to try again.")
        
def subtraction():
    print("You chose subtraction!  \n In the first prompt, enter a number that you would like to subtract another number from.  In the second prompt, enter the number that you would like to subtract from the first number.  After entering both numbers, remember to click enter.")
    try:
        num1 = float(input("Enter the number you want to subtract from: "))
    except ValueError:
        exit("Only enter numbers!  Restart the program to try again.")
    try:
        num2 = float(input("Enter a number you can to subtract from that other number: "))
        os.system('clear')
        subtract = num1 - num2
        print("Calculation: " + str(num1) + " - " + str(num2) + " = " + " " + str(subtract))
    except ValueError:
        exit("Only enter numbers!  Restart the program to try again.")
    
def multipication():
    print("You chose multipication!  \n First, enter a number that you would like to multiply.  Second, in the second prompt, enter a number that you would like to multiply the first number by.  Click enter when you have entered both numbers")
    try:
        num1 = float(input("Enter the first number: "))
    except ValueError:
        exit("Only enter numbers!  Restart the program to try again.")
    try:
        num2 = float(input("Enter the second number: "))
        os.system('clear')
        multiply = num1 * num2
        print("Calculation: " + str(num1) + " * " + str(num2) + " = " + " " + str(multiply))
    except ValueError:
        exit("Only enter numbers!  Restart the program to try again.")
    
def divide():
    print("You chose division!  \n First, enter a number that you would want to be divided.  Second, enter a number that you would like to divide the first number by.  Remember to click enter both times to get your calculation!")
    try:
        num1 = float(input("Enter the first number that you want to divide from: "))
    except ValueError:
        exit("Only enter numbers!  Restart the program to try again.")
    try:
        num2 = float(input("Enter the second number you want to divide the first number by: "))
        os.system('clear')
    except ValueError:
        exit("Only enter numbers!  Restart the program to try again.")
    try:
        divide = num1 / num2
        print("Calculation: " + str(num1) + " / " + str(num2) + " = " + " " + str(divide))
    except ZeroDivisionError:
        print("You can't divide by zero!  Restart the program.")
    
def g_divide():
    print("You chose floor division, which is division but the final answer is rounded!  First, enter the number you would like to be divided by.  Second, enter the number you would want to divide the first number by.  Please click enter after entering your numbers.  ")
    try:
        num1 = float(input("Enter the first number that you want to divide from: "))
    except ValueError:
        exit("Only enter numbers!  Restart the program to try again.")
    try:
        num2 = float(input("Enter the second number you want to divide the first number by: "))
        os.system('clear')
    except ValueError:
        exit("Only enter numbers!  Restart the program to try again.")
    try:
        divide = num1 // num2
        print("Calculation: " + str(num1) + " // " + str(num2) + " = " + " " + str(divide))
    except ZeroDivisionError:
        exit("You can't divide by zero!  Restart the program to try another calculation.")
    
def exponets():
    print("You chose exponets!  First, please enter the number that you would want to be multiplied by the exponet.  Second, please enter a number that you would want to raise the first number to.  Remember to click enter after entering each number.  ")
    try:
        num1 = float(input("Enter the number you want to have multiplied by the exponet: "))
    except ValueError:
        exit("Only enter numbers!  Restart the program to try again.")
    try:
        num2 = float(input("Enter the exponet: "))
        os.system('clear')
        exponet = num1 ** num2
        print("Calculation: " + str(num1) + " was raised to the power of " + str(num2) + " and the final solution is: " + str(exponet))
    except ValueError:
        exit("Only enter numbers!  Restart the program to try again.")
    
def remainder():
    print("You chose to find a remainder! \n This will work like regular division, so first please enter the number you would like to be divided by.  Second, please enter the number you would like to be divided from the first number.  You will need to click enter each inputting each number.")
    try:
        num1 = float(input("Enter the first number that you want to divide from: "))
    except ValueError:
        exit("Only enter numbers!  Restart the program to try again.")
    try:
        num2 = float(input("Enter the second number you want to divide the first number by: "))
    except ValueError:
        exit("Only enter numbers!  Restart the program to try again.")
    os.system('clear')
    
    try:
        modulus = num1 % num2
        print("The numbers " + str(num1) + " was divided by " + str(num2) + " to get the remainder " + str(modulus) + ".")
    except ZeroDivisionError:
        exit("You can't divide by zero!  Restart the program to do another calculation.")

def calculations():
    print("Calculator operation guide: \n Addition: Enter + into the prompt \n Subtraction: Enter - into the prompt \n Multipication: Enter * into the prompt \n Division: Enter / into the prompt \n Ground Division: Enter // into the prompt \n Exponentiation: Enter ** into the prompt \n Modulus (remainder): Enter % into the prompt")
    operation = input("Enter operator:")
    os.system('clear')
    if operation == "+":
        addition()
        exit()
    elif operation == "-":
        subtraction()
        exit()
    elif operation == "*":
        multipication()
        exit()
    elif operation == "/":
        divide()
        exit()
    elif operation == "//":
        g_divide()
        exit()
    elif operation == "**":
        exponets()
        exit()
    elif operation == "%":
        remainder()
        exit()
    elif operation == "":
        exit("Enter an operator, do not just click enter!  Restart the program to restart.  ")
    else:
        exit("Please restart the program and enter a VALID operator.  Refer to the guide that is given at the start of the program.")
        
        
calculations()
