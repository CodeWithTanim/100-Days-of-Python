# str = "4354356"

# num1 = "10"
# num2 = 5

# print(int(num1) + num2)


num = "10"
num = int(num)

print(num + 5)

a = 10
b = 6.5

print(a + b)

x = 10
y = "7"

print(x + int(y))

# A = "10tanim"
# B = 10
# A = int(A)
# print(A + B)

age = 25
message = "My Age " + str(age) + " s"
print(message)  # আউটপুট: আমার বয়স 25 বছর।Year

user_input = input("Write a Number: ")  # ইউজারের ইনপুট স্ট্রিং আকারে
number = int(user_input)  # স্ট্রিং কে ইন্টিজারে কনভার্ট করা
print("2X of Your Number:", number * 2)

try:
    text = "hello"
    num = int(text)
except ValueError:
    print("Intger convert not possible")