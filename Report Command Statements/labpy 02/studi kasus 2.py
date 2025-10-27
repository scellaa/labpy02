print("Simple Calculator (+, -, *, /)")
print('Type "exit" to quit')

while True:
    op = input("\nEnter operation (+, -, *, /) or exit: ")
    if op == "exit":
        print("See ya next session!")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if op == '+':
        print("Result:", num1 + num2)
    elif op == '-':
        print("Result:", num1 - num2)
    elif op == '*':
        print("Result:", num1 * num2)
    elif op == '/':
        print("Result:", num1 / num2)
    else:
        print("Invalid operation!")