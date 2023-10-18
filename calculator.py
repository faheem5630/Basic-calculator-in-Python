# Creating a Calculator 
import time
print("Welcome To my Calculator ")

while True:
    print("""
options
1: Division
2: Multiplication
3: Addition
4: Substraction
5: Exit          
        """)   

    option = eval(input("Select any operation (1-5):"))

    if option == 5:
        print("Ta ta bye...")
        time.sleep(2)
        break
    elif option == 4:
        num1 = eval(input("Enter the first number: ")) 
        num2 = eval(input("Enter the Second number: ")) 
        print("Result = ", num1 - num2)
    elif option == 3:
        num1 = eval(input("Enter the first number: ")) 
        num2 = eval(input("Enter the Second number: ")) 
        print("Result = ", num1 + num2)
    elif option == 2:
        num1 = eval(input("Enter the first number: ")) 
        num2 = eval(input("Enter the Second number: ")) 
        print("Result = ", num1 * num2)
    elif option == 1:
        num1 = eval(input("Enter the first number: ")) 
        num2 = eval(input("Enter the Second number: ")) 
        if num1 == 0 or num2 == 0:
            print("Sorry 0 is not divisible.")
        else:
            print("Answer = ", num1 / num2)
    else:
        print("Please Enter an Valid Number between(1-5)")