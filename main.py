first_num = int(input("Enter the first number you want to calculate with: "))

operation = str(input("Enter the math operation you want to calculate with (+, -, * or /): "))

second_num = int(input("Enter the second number you want to calculate with: "))

if operation == "+":
    print(first_num + second_num)
elif operation == "-":
    print(first_num - second_num)
elif operation == "*":
    print(first_num * second_num)
elif operation == "/":
    print(first_num / second_num)
else:
    print("Something went wrong.")
