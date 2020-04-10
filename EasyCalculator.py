print('Easy calculator!')
print('It can add, subtract, multiply and divide ')
num1 = int(input('Please choose your first number: '))
sign = input('What do you want to do? +, -, /, or *: ')
num2 = int(input('Please choose your second number: '))
gama3=num1 + num2
tarah=num1 - num2
qismah=num1/num2
darob=num1*num2


if sign == "+":
    print(num1, sign, num2, "=",gama3)
if sign == "-":
    print(num1, sign, num2, "=",tarah)
if sign == "/":
    print(num1, sign, num2, "=",qismah)
if sign == "*":
    print(num1, sign, num2, "=",darob)
