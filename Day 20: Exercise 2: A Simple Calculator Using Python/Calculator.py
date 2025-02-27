while True:
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))

    operation = input("Choose Operation (+, -, *, /): ")

    match operation:
        case "+":
            result = num1 + num2
        case "-":
            result = num1 - num2
        case "*":
            result = num1 * num2
        case "/":
            if num2 == 0:
                print("Error! Division by zero")
            else:
                result = num1 / num2
        case _:
            result = "Invaild Operation"

    print("Result = ", result)

    repeat = input("Another Calculation? (yes/no): ")
    if repeat.lower() != "yes":
        print("Bye")
        break