num = float(input("Your Number: "))

if num > 0:
    print("Positive Number")
    if num % 2 == 0:
        print("This is an even Number")
    else:
        print("This is an Odd Number.")
else:
    print("Zero or Negative Number")