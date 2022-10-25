num1=input("Enter the first number: ")
op=input("Enter the Arithmetic operator: ")
num2=input("Enter the second number: ")
num1=int(num1)
num2=int(num2)
if op =='*':
    print(num1*num2)
elif op == '/':
    print(num1/num2)
elif op == '+':
    print(num1+num2)
elif op == '-':
    print(num1-num2)
elif op == '%':
    print(num1%num2)