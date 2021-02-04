def add(a,b):
    return a + b
    
def sub(a,b):
    return a - b
    
def div(a,b):
    if (b == 0):
        raise ValueError("Cannot Divide by Zero")
    return a / b
    
def mult(a,b):
    return a * b
    
#num1 = float(input("Enter first number: "))
#num2 = float(input("Enter second number: "))
#op = str(input("Enter the type of operation e.g. 'add', 'sub', 'div', 'mult': "))
#ans = 0
#if(op == 'add'):
#    ans = add(num1, num2)
#if (op == 'sub'):
#    ans = sub(num1, num2)
#if (op == 'div'):
#    ans = div(num1, num2)
#if (op == 'mult'):
#    ans = mult(num1, num2)
    
#print("The answer is: " + str(ans))