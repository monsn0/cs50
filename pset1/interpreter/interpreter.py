expression = input("Expression: ").strip()

operation = expression.split(" ")[1]
x = float(expression.split(" ")[0])
y = float(expression.split(" ")[2])

if operation == "+":
    print(x + y)
elif operation == "-":
    print(x - y)
elif operation == "*":
    print(x * y)
elif operation == "/":
    print(x / y)