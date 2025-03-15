# Python Programming - Day 26: f-String in Python

## **f-String in Python**

### **Introduction**
স্বাগতম **100 Days of Python** সিরিজের ২৬তম দিনে! 🎉 আজকের ভিডিওতে আমরা শিখবো:
- **f-String কী এবং কেন এটি ব্যবহার করা হয়?** 🤔
- **পুরোনো স্ট্রিং ফরম্যাটিং বনাম f-String** ⚖️
- **f-String ব্যবহার করে কোড আরও সহজ, ক্লিন এবং দ্রুত করার উপায়!** 🚀

---

## **Python-এ f-String কী?**

Python-এর **f-String (formatted string literals)** হলো স্ট্রিং ফরম্যাটিংয়ের সহজ, দ্রুত, এবং কার্যকর উপায়। এটি Python 3.6 থেকে এসেছে এবং পুরোনো `.format()` এবং `%` স্টাইলের তুলনায় অনেক বেশি ব্যবহারযোগ্য।

### **পুরোনো পদ্ধতিগুলো** (ঝামেলাপূর্ণ!) 😫
```python
name = "Tanim"
age = 20
print("My name is {} and I am {} years old.".format(name, age))
```

অথবা আরও পুরোনো `%` অপারেটর ব্যবহার করলে:
```python
print("My name is %s and I am %d years old." % (name, age))
```

👉 এগুলো পড়তে কঠিন এবং ডিবাগ করাও ঝামেলার! 😑

---

## **f-String ব্যবহার করা (The Best Way!)** ✅

Python-এর f-String ব্যবহার করলে কোড আরও সহজ ও পরিষ্কার হয়ে যায়।
```python
name = "Tanim"
age = 20
print(f"My name is {name} and I am {age} years old.")
```
🔹 **Output:**
```
My name is Tanim and I am 20 years old.
```

✔️ **`f"..."` ব্যবহারে `{}` এর মধ্যে সরাসরি ভেরিয়েবল বসানো যায়।**
✔️ **রানটাইমে ভ্যালু ইনসার্ট হয়, তাই সহজ ও দ্রুত কাজ করে!**

---

## **f-String এর সুবিধা** 🎯
✅ **সহজ ও ক্লিন কোড** 🧼
✅ **পারফরম্যান্স দ্রুত (Performance-wise, f-String সবচেয়ে ফাস্ট!)** ⚡
✅ **Multiple data types একসাথে ব্যবহার করা যায়** 🏗️
✅ **Expressions ও ফাংশন `{}` এর মধ্যে সরাসরি বসানো যায়** 🧮

---

## **f-String এ Expression ব্যবহার করা** 🧮

```python
num1 = 10
num2 = 5
print(f"The sum of {num1} and {num2} is {num1 + num2}")
```
🔹 **Output:**
```
The sum of 10 and 5 is 15
```

---

## **f-String দিয়ে String Manipulation** ✨

```python
name = "tanim"
print(f"My name is {name.upper()}.")
```
🔹 **Output:**
```
My name is TANIM.
```

---

## **f-String দিয়ে Decimal Formatting (Precision Handling)** 🔢

```python
price = 49.99999
print(f"The price is {price:.2f}")
```
🔹 **Output:**
```
The price is 50.00
```

---

## **f-String দিয়ে Padding & Alignment** 📏
```python
name = "Tanim"
print(f"|{name:<10}|{name:^10}|{name:>10}|")
```
🔹 **Output:**
```
|Tanim     |  Tanim   |     Tanim|
```
📌 **Explanation:**
- `<10` → বাম দিকে সাজাবে (Left Align)
- `^10` → মাঝখানে সাজাবে (Center Align)
- `>10` → ডান দিকে সাজাবে (Right Align)

---

## **f-String দিয়ে Dictionary & List Access** 📋
```python
data = {"name": "Tanim", "age": 20}
print(f"My name is {data['name']} and I am {data['age']} years old.")
```
🔹 **Output:**
```
My name is Tanim and I am 20 years old.
```

---

## **Today's Challenge! 🎯**
✅ নিচের কোডটি রান করুন এবং আউটপুট পর্যবেক্ষণ করুন:
```python
num = int(input("Enter a number: "))
print(f"The square of {num} is {num ** 2}")
```
📢 **কমেন্টে জানান, আপনি সফলভাবে কোড রান করতে পেরেছেন কিনা!** 💬

---

## **Happy Coding! 🚀**
**Like, Share & Subscribe!** 🎥
👉 **CodeWithTanim - 100 Days of Python** 🐍

