#Write a program to make a calculator : For making a calculator create four functions add, subtract, multiply, divide.
#  Ask for a choice from users which operation they want to perform. Take user input whatever operation they want to perform And call that function accordingly.
def addition(num1,num2):
    print(num1+num2)
def subtraction(num1,num2):
    print(num1-num2)
def division(num1,num2):
    print(num1/num2)
def multiplication(num1,num2):
    print(num1*num2)
def calculator():
    operator = int(input("Select 1 for addition, 2 for subtraction, 3 for division, and 4 for multiplication. "))
    num1 = int(input("Enter a larger number. "))
    num2 = int(input("Enter a smaller number. "))
    if operator ==1:
        addition(num1,num2)
    if operator ==2:
        subtraction(num1,num2)
    if operator ==3:
        division(num1,num2)
    if operator ==4:
        multiplication(num1,num2)
calculator()