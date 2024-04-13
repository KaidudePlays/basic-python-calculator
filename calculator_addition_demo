import os
numbers_list = []
final_sum = float(0)
print("Welcome to Kai's Python Calculator demoAddition demo - utilizing lists")
try:
    addition = int(input("How many numbers do you want to add up?  Enter how many on the next line.\nInput: "))
except ValueError:
    exit("Invalid input.  Please restart the program and only enter a positive number.")
os.system("clear")

if addition == 0 or addition < 0:
    exit("Please restart the program and enter a positive number (above zero).")
    
for i in range(addition):
    print("Number: " + str(i+1))
    try:
        number_add = float(input("Enter a number that you want to add.\nNumber:"))
    except ValueError:
        exit()
    
    
    if i == addition-1:
        final_sum = final_sum + number_add
        numbers_list.extend(str(number_add))
    else: 
        final_sum = final_sum + number_add
        numbers_list.extend(str(number_add) + "+")
final = "".join(numbers_list)
os.system("clear")
print("Your final calculation: " + final + "=" +str(final_sum))
