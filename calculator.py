class Calculator:
    ## a simple calculator class which perform 4 math operators.
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    ## Initialize the calculator with two numbers.

    def addition(self):
        return self.num1 + self.num2
    def subtraction(self):
        return self.num1 - self.num2
    def multiplication(self):
        return self.num1 * self.num2
    def division(self):
        if self.num2 == 0:
            return "cannot divide by zero"
        else:
            return self.num1 / self.num2

def main():
    print("welcome to calculator")
    num1 = float(input("enter first number: "))
    num2 = float(input("enter second number: "))
    operation = input("choose operation: + - / *")
    calc = Calculator(num1, num2)
    if operation == '+':
        print('result:', calc.addition())
    elif operation == '-':
        print('result:', calc.subtraction())
    elif operation == '*':
        print('result:', calc.multiplication())
    elif operation == '/':
        print('result:', calc.division())
    else:
        print("invalid operation")


print(main())






