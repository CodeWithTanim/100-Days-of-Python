# Python Programming - Day 6: Typecasting in Python

## Typecasting in Python

### **Introduction**
স্বাগতম **100 Days of Python** সিরিজের ৬ষ্ঠ দিনে! আজকের ভিডিওতে আমরা শিখবো:
- **Typecasting** কী এবং কেন এটি প্রয়োজন 🔄
- **Implicit** এবং **Explicit Typecasting** এর মধ্যে পার্থক্য 🧠
- **Python-এ Typecasting এর ব্যবহার এবং উদাহরণ** 📝

---

## **Typecasting কী?**

Typecasting হলো এক ডেটা টাইপ থেকে অন্য ডেটা টাইপে রূপান্তর করার প্রক্রিয়া। Python-এ বিভিন্ন ডেটা টাইপ যেমন `int`, `float`, `str`, ইত্যাদির মধ্যে কনভার্ট করার জন্য Typecasting ব্যবহার করা হয়।

### **উদাহরণ:**
```python
num = "10"  # এটি একটি স্ট্রিং
num = int(num)  # এখন এটি একটি ইন্টিজার
print(num + 5)  # আউটপুট: 15
```

---

## **Typecasting এর প্রকারভেদ**

### **1. Implicit Typecasting**
Python স্বয়ংক্রিয়ভাবে এক ডেটা টাইপ থেকে অন্য ডেটা টাইপে কনভার্ট করে যখন প্রয়োজন হয়। যেমন, একটি ইন্টিজার এবং একটি ফ্লোট যোগ করার সময় Python ইন্টিজার কে ফ্লোট এ কনভার্ট করে।

**[উদাহরণ: Implicit Typecasting]**
```python
a = 5      # ইন্টিজার
b = 2.5    # ফ্লোট
result = a + b  # Python স্বয়ংক্রিয়ভাবে a কে ফ্লোট এ কনভার্ট করে
print(result)  # আউটপুট: 7.5
```

### **2. Explicit Typecasting**
এটি ম্যানুয়ালি করা হয়, যেমন `int()`, `float()`, `str()` ইত্যাদি ফাংশন ব্যবহার করে।

**[উদাহরণ: Explicit Typecasting]**
```python
x = "10"
y = "20"
result = int(x) + int(y)  # স্ট্রিং কে ইন্টিজারে কনভার্ট করা
print(result)  # আউটপুট: 30
```

---

## **Python-এ Typecasting ফাংশন**

Python-এ কিছু কমন Typecasting ফাংশন হলো:

| ফাংশন | বর্ণনা | উদাহরণ |
|-------|--------|--------|
| `int()` | স্ট্রিং বা ফ্লোট কে ইন্টিজারে কনভার্ট করে | `int("10")` → `10` |
| `float()` | স্ট্রিং বা ইন্টিজার কে ফ্লোট এ কনভার্ট করে | `float("3.14")` → `3.14` |
| `str()` | যেকোনো ডেটা টাইপ কে স্ট্রিং এ কনভার্ট করে | `str(10)` → `"10"` |
| `list()` | ডেটা কে লিস্ট এ কনভার্ট করে | `list("hello")` → `['h', 'e', 'l', 'l', 'o']` |
| `tuple()` | ডেটা কে টাপল এ কনভার্ট করে | `tuple([1, 2, 3])` → `(1, 2, 3)` |
| `set()` | ডেটা কে সেট এ কনভার্ট করে | `set([1, 2, 2, 3])` → `{1, 2, 3}` |

**[উদাহরণ: `str()` ফাংশন]**
```python
age = 25
message = "My Age " + str(age) + " Years"
print(message)  # আউটপুট: আমার বয়স 25 বছর।
```

---

## **প্র্যাকটিকাল উদাহরণ**

**[উদাহরণ: ইউজার ইনপুট এবং Typecasting]**
```python
user_input = input("Write a Number: ")  # ইউজারের ইনপুট স্ট্রিং আকারে
number = int(user_input)  # স্ট্রিং কে ইন্টিজারে কনভার্ট করা
print("2X of Your Number:", number * 2)
```

---

## **সতর্কতা এবং টিপস**

1. **ভুল ডেটা টাইপ কনভার্ট করার চেষ্টা করলে এরর হতে পারে।**  
   যেমন, `int("hello")` → `ValueError`।  
   সমাধান: `try-except` ব্যবহার করুন।
    ```python
    try:
        text = "hello"
        num = int(text)
    except ValueError:
        print("ইন্টিজারে কনভার্ট করা সম্ভব নয়!")
    ```

2. **ইউজার ইনপুট নেওয়ার সময় Typecasting ব্যবহার করুন।**  
   কারণ ইউজার ইনপুট সবসময় স্ট্রিং আকারে আসে।


---

## **Today's Challenge! 🎯**
✅ নিচের কোডটি রান করুন এবং আউটপুট পর্যবেক্ষণ করুন:
```python
x = "50"
y = 10
result = int(x) + y
print(result)
```
📢 **কমেন্টে জানান, আপনি সফলভাবে কোড রান করতে পেরেছেন কিনা!** 💬

---

## **Next Topic: User Input in Python**
🔔 **তাই, ভিডিওটি লাইক করুন, কমেন্ট করুন, এবং চ্যানেলটি সাবস্ক্রাইব করুন!** 🚀

👉 **CodeWithTanim - 100 Days of Python 🚀**