# Python Programming - Day 7: User Input in Python

## **Introduction**
স্বাগতম **100 Days of Python** সিরিজের ৭ম দিনে! 🎉 আজকের ভিডিওতে আমরা শিখবো:
- **Python-এ User Input কী?**
- **Text এবং Numeric Input নেওয়ার পদ্ধতি**
- **Multiple Inputs এবং Error Handling**
- **একটি Mini Project: Simple Calculator**

---

## **User Input কী? 🤔**
Python-এ `input()` ফাংশনের মাধ্যমে ইউজারের কাছ থেকে ইনপুট নেওয়া হয়। উদাহরণস্বরূপ:

```python
name = input("Write Your name: ")
print("Your Name is:", name)
```
🔹 `input()` ফাংশন ইউজারের দেওয়া ইনপুট **string** হিসেবে গ্রহণ করে।
### Output:
```
Write Your name: Tanim
Your Name is: Tanim
```

---

## **ইউজার ইনপুটকে সংখ্যায় কনভার্ট করা 🧮**
যেহেতু `input()` সব ইনপুটকে **string** হিসেবে গ্রহণ করে, তাই সংখ্যার ক্ষেত্রে `int()` বা `float()` ব্যবহার করতে হবে।

```python
age = input("Enter Your Age: ")
age = int(age)  # স্ট্রিংকে ইন্টিজারে কনভার্ট করা
print("After 10 Years your Age:", age + 10)
```
### Output:
```
Enter Your Age: 22
After 10 Years your Age: 32
```
📌 **Tip:** `int()` ব্যবহার করলে শুধুমাত্র পূর্ণসংখ্যা নেওয়া যাবে। দশমিক সংখ্যা নিতে চাইলে `float()` ব্যবহার করুন।

---

## **Multiple User Inputs 📥**

```python
name = input("Enter Your Name: ")
age = input("Enter Your Age: ")
city = input("Enter Your City Name: ")

print("Your Name:", name)
print("Your Age:", age)
print("Your City:", city)
```
### Output:
```
Enter Your Name: Tanim
Enter Your Age: 22
Enter Your City Name: Dhaka
Your Name: Tanim
Your Age: 22
Your City: Dhaka
```
📌 **Note:** প্রতিটি ইনপুট আলাদা ভেরিয়েবলে সংরক্ষণ করতে হবে।

---

## **Common Mistakes & Error Handling 🚨**
নিচের ভুলটি দেখুন:

```python
age = input("Enter Your Age: ")
print("After 10 Year Your Age:", age + 10)  # এটি Error দেবে!
```
✅ **সঠিক উপায়:**

```python
age = int(input("Enter Your Age: "))
print("After 10 Year Your Age:", age + 10)
```
📌 **Tip:** Input নেওয়ার পরে প্রয়োজন অনুযায়ী **Typecasting** করতে হবে।

---

## **Mini Project: Simple Calculator 🧮**
একটি ছোট ক্যালকুলেটর বানিয়ে ফেলুন!

```
Do Your Self :)
```

<!-- ```python
num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Numebr: "))

sum = num1 + num2
difference = num1 - num2
product = num1 * num2
division = num1 / num2

print("Addition:", sum)
print("Substuction:", difference)
print("Multiplication:", product)
print("Divition:", division)
``` -->
📢 **চ্যালেঞ্জ:** এই ক্যালকুলেটরটি বানিয়ে কমেন্টে ‍কোড লিখুন 💡

## **Next Topic: Strings in Python!**
🔔 **তাই, ভিডিওটি লাইক করুন, কমেন্ট করুন, এবং চ্যানেলটি সাবস্ক্রাইব করুন!** 🚀

👉 **[CodeWithTanim - 100 Days of Python](https://www.youtube.com/@CodeWithTanim)**
