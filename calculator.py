number1=int(input("Enter number1:"))
number2=int(input("Enter number2:"))
print("+ =addition, - =subtraction, * =multiplication, / =division")
operation=input("Enter operation you want to perform: ")
def add():
    return number1+number2
def sub():
    return number1-number2
def mul():
    return number1*number2
def div():
    return number1/number2
if operation=="+":
    print(add())
elif operation=="-":
    print(sub())
elif operation=="*":
    print(mul())
elif operation=="/":
    print(div())
else:
    print("Wrong operation")
