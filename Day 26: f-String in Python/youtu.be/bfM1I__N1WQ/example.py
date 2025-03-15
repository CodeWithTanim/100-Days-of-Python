name = "Tanim"
age = 20
# print("My name is {} and I am {} years old." .format(name , age))

# print("My name is %s and I am %d years old." % (name, age))

print(f"My name is {name} and I am {age} years old.")

num1 = 10
num2 = 5

print(f"The sum of {num1} and {num2} is {num1 + num2}")


print(f"My name is {name.upper()}.")

price = 49.999999
print(f"The price is {price:.2f}")

print(f"|{name:<10}|{name:^10}| {name:>10}|")

data = {"name": "Tanim", "Age": 20}

print(f"My name is {data['name']} and I am {data['Age']} years old")