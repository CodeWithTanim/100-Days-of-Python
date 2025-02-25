# Python Programming - Day 18: Functions in Python

## **Functions in Python**

### **Introduction**
স্বাগতম **100 Days of Python** সিরিজের ১৮তম দিনে! আজকের ভিডিওতে আমরা শিখবো:
- **ফাংশন (Functions)** কী এবং কেন ব্যবহার করা হয় 🛠️
- **ফাংশন কিভাবে ডিফাইন এবং কল করতে হয়** 📝
- **Default Arguments এবং Keyword Arguments** এর ব্যবহার 🎯
- **ফাংশনের মাধ্যমে কোড কিভাবে reusable এবং organized করা যায়** 🧩

---

## **Python-এ ফাংশন (Functions)**

ফাংশন হলো এক ধরনের **code block**, যেটা একটা নির্দিষ্ট কাজ করার জন্য তৈরি করা হয়। আপনি একবার ফাংশন লিখে রাখবেন, আর যখনই দরকার হবে, তখনই সেটাকে কল করে ব্যবহার করবেন। এতে আপনার কোড **reusable** হয়, এবং কোডের মধ্যে **গুছানো** ভাব আসে।

### **ফাংশন ডিফাইন এবং কল করা:**
```python
# ফাংশন ডিফাইন
def greet():
    print("Hello, World!")

# ফাংশন কল
greet()
```
### Output:
```
Hello, World!
```

🔹 **ফাংশন ব্যবহার করে একই কোড বারবার লিখার ঝামেলা থেকে মুক্তি পাওয়া যায়।**

---

## **প্যারামিটার এবং রিটার্ন ভ্যালু**

ফাংশনে প্যারামিটার পাস করে ডাইনামিকভাবে কাজ করা যায়। আর রিটার্ন ভ্যালু দিয়ে ফলাফল ফেরত নেওয়া যায়।

### **উদাহরণ:**
```python
# ফাংশন ডিফাইন
def add_numbers(a, b):
    result = a + b
    return result

# ফাংশন কল
sum_result = add_numbers(5, 10)
print("The sum is:", sum_result)
```
### Output:
```
The sum is: 15
```

🔹 **প্যারামিটার দিয়ে ফাংশনে ইনপুট পাস করা যায়, এবং `return` দিয়ে ফলাফল ফেরত নেওয়া যায়।**

---

## **Default Arguments**

ফাংশনের প্যারামিটারগুলোর ডিফল্ট ভ্যালু সেট করে রাখা যায়। যদি আপনি প্যারামিটার পাস না করেন, তাহলে ডিফল্ট ভ্যালু ব্যবহার হবে।

### **উদাহরণ:**
```python
# ফাংশন ডিফাইন
def greet(name="Guest"):
    print("Hello,", name)

# ফাংশন কল
greet()  # Output: Hello, Guest
greet("Alice")  # Output: Hello, Alice
```
### Output:
```
Hello, Guest
Hello, Alice
```

🔹 **ডিফল্ট আর্গুমেন্ট ব্যবহার করে ফাংশনকে আরও ফ্লেক্সিবল করা যায়।**

---

## **Keyword Arguments**

প্যারামিটারগুলোর নাম উল্লেখ করে ভ্যালু পাস করা যায়। এতে করে প্যারামিটারগুলোর অর্ডার মেনে চলার ঝামেলা নেই।

### **উদাহরণ:**
```python
# ফাংশন ডিফাইন
def person_info(name, age, city):
    print("Name:", name)
    print("Age:", age)
    print("City:", city)

# ফাংশন কল
person_info(name="Alice", age=25, city="New York")
```
### Output:
```
Name: Alice
Age: 25
City: New York
```

🔹 **কীওয়ার্ড আর্গুমেন্ট ব্যবহার করে প্যারামিটারগুলোর অর্ডার নিয়ে চিন্তা করতে হয় না।**

---

## **Today's Challenge! 🎯**

✅ নিচের কোডটি রান করুন এবং আউটপুট পর্যবেক্ষণ করুন:
```python
def calculate_area(length, width=10):
    return length * width

area1 = calculate_area(5)
area2 = calculate_area(5, 20)
print("Area 1:", area1)
print("Area 2:", area2)
```
📢 **কমেন্টে জানান, আপনি সফলভাবে কোড রান করতে পেরেছেন কিনা!** 💬

---

🔔 **তাই, ভিডিওটি লাইক করুন, কমেন্ট করুন, এবং চ্যানেলটি সাবস্ক্রাইব করুন!** 🚀

👉 **CodeWithTanim - 100 Days of Python 🚀**