#Write a program to make a calculator : For making a calculator create four functions add, subtract, multiply, divide.
#  Ask for a choice from users which operation they want to perform. Take user input whatever operation they want to perform And call that function accordingly.
def calculator():
    operator = int(input("Select 1 for addition, 2 for subtraction, 3 for division, and 4 for multiplication. "))
    num1 = int(input("Enter a larger number. "))
    num2 = int(input("Enter a smaller number. "))
    if operator ==1:
        print(num1+num2)
    if operator ==2:
        print(num1-num2)
    if operator ==3:
        print(num1/num2)
    if operator ==4:
        print(num1*num2)
calculator()