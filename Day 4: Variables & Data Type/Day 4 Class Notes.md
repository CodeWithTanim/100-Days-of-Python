# Python Programming - Day 4: Variables & Data Types

## Variables & Data Types

### **Introduction**
স্বাগতম **100 Days of Python** সিরিজের ৪র্থ দিনে! আজকের ভিডিওতে আমরা শিখবো:
- **ভেরিয়েবল (Variables)** কী এবং কেন ব্যবহার করা হয় 🏷️
- **ডাটা টাইপস (Data Types)** কী এবং কেন গুরুত্বপূর্ণ 🏗️
- **Python-এ বিভিন্ন ডাটা টাইপস এবং উদাহরণ** 📝

---

## **Python-এ ভেরিয়েবল (Variables)**

ভেরিয়েবল হলো এমন একটি স্টোরেজ/কন্টেইনার। যেখানে আমরা ডাটা সংরক্ষণ করতে পারি।

### **ভেরিয়েবল ডিক্লেয়ারেশন:**
```python
name = "Tanim"
age = 22
is_student = True
```
### Output:
```
Tanim
22
True
```

🔹 **Python-এ ভেরিয়েবল ডায়নামিকভাবে কাজ করে, তাই ডাটা টাইপ নির্ধারণ করার দরকার হয় না।**

---


## **ভেরিয়েবল নেমিং কনভেনশন**
🔹 **একটি ভেরিয়েবল নাম দিতে গেলে কিছু নিয়ম অনুসরণ করতে হবে:**

✅ ভেরিয়েবল নাম **A-Z, a-z, 0-9, এবং `_`** ধারণ করতে পারে।

✅ নামের শুরুতে সংখ্যা ব্যবহার করা যাবে না। ❌ `1name = "Tanim"` (ভুল ❌)

✅ নামটি অর্থবোধক হওয়া উচিত। **`x = 10` (কম বোঝা যায়) vs `age = 10` (ভালো ✅)**

✅ `camelCase`, `snake_case` ব্যবহার করা যায়। উদাহরণ: `myVariable`, `my_variable` ✅

---

## **Python-এ ডাটা টাইপস (Data Types)**

Python-এ বিভিন্ন ধরণের ডাটা টাইপ রয়েছে:

| ডাটা টাইপ | বর্ণনা | ইংরেজি নাম | উদাহরণ |
|-----------|--------|--------|--------|
| `int` | পূর্ণসংখ্যা | Integer Number | `age = 22` |
| `float` | দশমিক সংখ্যা| Floating Numebr | `pi = 3.14` |
| `str` | স্ট্রিং (টেক্সট)| String| `name = "Tanim"` |
| `bool` | সত্য বা মিথ্যা| Boolean | `is_student = True` |
| `list` | একাধিক মান সংরক্ষণ| List | `fruits = ["Apple", "Banana", "Mango"]` |
| `tuple` | অপরিবর্তনীয় লিস্ট| Tuple | `colors = ("Red", "Green", "Blue")` |
| `dict` | কী-ভ্যালু পেয়ার | Dictionary | `person = {"name": "Tanim", "age": 22}` |
| `set` | ইউনিক আইটেমের সংগ্রহ| Set | `unique_nums = {1, 2, 3, 4}` |


### **উদাহরণ:**
```python
# Integer
age = 22

# Float
pi = 3.1416

# String
name = "Tanim"

# Boolean
is_programmer = True

# List
fruits = ["Apple", "Banana", "Mango"]

# Tuple
days = ("Sunday", "Monday", "Tuesday")

# Dictionary
student = {"name": "Tanim", "age": 22, "course": "Python"}
```
### Output:
```
22
3.1416
Tanim
True
['Apple', 'Banana', 'Mango']
('Sunday', 'Monday', 'Tuesday')
{'name': 'Tanim', 'age': 22, 'course': 'Python'}
```

---

## **Today's Challenge! 🎯**
✅ নিচের কোডটি রান করুন এবং আউটপুট পর্যবেক্ষণ করুন:
```python
name = input("Write Your Name: ")
age = int(input("Type Your Age: "))
print(f"Welcome {name}! Your Age {age} Years!")
```
📢 **কমেন্টে জানান, আপনি সফলভাবে কোড রান করতে পেরেছেন কিনা!** 💬

---

## **Next Topic: Operators in Python!**
🔔 **তাই, ভিডিওটি লাইক করুন, কমেন্ট করুন, এবং চ্যানেলটি সাবস্ক্রাইব করুন!** 🚀

👉 **CodeWithTanim - 100 Days of Python 🚀**

