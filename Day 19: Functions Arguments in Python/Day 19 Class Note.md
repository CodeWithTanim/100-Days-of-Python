# Python Programming - Day 19: Function Arguments

## Function Arguments in Python

### **Introduction**
**100 Days of Python** সিরিজের ১৯তম দিনে স্বাগতম! আজকে আমরা শিখবো কিভাবে ফাংশনে বিভিন্ন ধরণের আর্গুমেন্ট পাঠানো যায় 🚀

---

## **ফাংশন আর্গুমেন্টের প্রকারভেদ**

### **1. Positional Arguments (পজিশনাল আর্গুমেন্ট)**
আর্গুমেন্টের অর্ডার অনুযায়ী ভ্যালু অ্যাসাইন হয়।

```python
def add(a, b):
    return a + b

print(add(5, 3))  # Output: 8
```

🔹 **অর্ডার ভুল হলে ভুল রেজাল্ট পাবেন!**

---

### **2. Keyword Arguments (কিওয়ার্ড আর্গুমেন্ট)**
প্যারামিটারের নাম উল্লেখ করে ভ্যালু পাঠানো।

```python
def greet(name, message):
    print(f"{message}, {name}!")

greet(message="Good Morning", name="Alice")
# Output: Good Morning, Alice!
```

🔹 **অর্ডার মেনে চলার প্রয়োজন নেই!**

---

### **3. Default Arguments (ডিফল্ট আর্গুমেন্ট)**
প্যারামিটারে ডিফল্ট ভ্যালু সেট করা যায়।

```python
def power(base, exponent=2):
    return base ** exponent

print(power(3))    # Output: 9
print(power(3, 4)) # Output: 81
```

🔹 **আর্গুমেন্ট না দিলে ডিফল্ট ভ্যালু ব্যবহার করে!**

---

### 4. *args (ভ্যারিয়েবল-লেন্থ আর্গুমেন্ট)**
একাধিক পজিশনাল আর্গুমেন্ট নেওয়ার জন্য।

```python
def student_report(name, *scores):
    avg = sum(scores) / len(scores)
    print(f"{name}: Average = {avg}")

student_report("Rahim", 85, 90, 78)
# Output: Rahim: Average = 84.333...
```

---

### 5. **kwargs (কিওয়ার্ড আর্গুমেন্ট ডিকশনারি)**
কিওয়ার্ড আর্গুমেন্টগুলিকে ডিকশনারি হিসেবে নেওয়া।

```python
def user_profile(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

user_profile(name="Bob", age=25, city="NYC")
# Output:
# name: Bob
# age: 25
# city: NYC
```

---

## **আর্গুমেন্ট টাইপ সামারি**

| আর্গুমেন্ট টাইপ | বর্ণনা | উদাহরণ |
|----------------|--------|--------|
| Positional | অর্ডার অনুযায়ী অ্যাসাইন | `func(5, 10)` |
| Keyword | প্যারামিটার নাম নির্দিষ্ট করে | `func(b=5, a=10)` |
| Default | ডিফল্ট ভ্যালু সহ প্যারামিটার | `def func(a=5)` |
| *args | একাধিক পজিশনাল আর্গুমেন্ট | `def func(*args)` |
| **kwargs | একাধিক কিওয়ার্ড আর্গুমেন্ট | `def func(**kwargs)` |

---

## **Today's Challenge! 🎯**
একটি ফাংশন তৈরি করুন যেটা:
1. ২টি পজিশনাল আর্গুমেন্ট নেবে
2. ১টি ডিফল্ট আর্গুমেন্ট থাকবে
3. *args এবং **kwargs সাপোর্ট করবে
4. সব আর্গুমেন্ট প্রিন্ট করবে

```python
# আপনার কোড এখানে লিখুন
```

📢 **কমেন্টে আপনার সমাধান শেয়ার করুন!** 💬

---

🔔 **ভিডিওটি লাইক করুন, কমেন্ট করুন এবং চ্যানেল সাবস্ক্রাইব করতে ভুলবেন না!** 🚀  
👉 **CodeWithTanim - 100 Days of Python** 🐍
