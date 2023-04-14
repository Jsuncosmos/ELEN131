"""
1) The program asks the users for an integer number between 1-10. If the user gives an invalid input, the program needs to let the user know and asks for a new integer number. Let us assume that the integer number is N. 
2) After the user provides the input, the program prints N random float numbers from 0 to 100. 
3) Thank the user and end the program. 
4) Make sure you have detailed comments for your program. 
"""
import random

val = input("Enter an integer between 1-10: ")
val = int(val)
print(val)

check = True

while (check == True):
    if val in range(1,10):
        print("Given integer : ", val)
        break
    else:
        print("Invalid number, please enter again:")
        val = input("Enter an integer between 1-10: ")
        val = int(val)

print("Output"+str(val)+" random float numbers from 0-100")

x = random.random()
for i in range(1,val):
    print(random.random()*100)

print("Thank for for your participation!")

