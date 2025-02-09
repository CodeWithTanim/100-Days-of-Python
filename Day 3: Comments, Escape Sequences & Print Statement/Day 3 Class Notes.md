# Python Programming - Day 3: Comments, Escape Sequences & Print Statement

## Comments, Escape Sequences & Print Statement

### **Introduction**
স্বাগতম **100 Days of Python** সিরিজের ৩য় দিনে! আজকের ভিডিওতে আমরা শিখবো:
- **Python-এ কমেন্টস** কীভাবে কাজ করে 📝
- **এস্কেপ সিকোয়েন্স** কী এবং কীভাবে ব্যবহার করা হয় 🔄
- **প্রিন্ট স্টেটমেন্ট** এবং এর বিভিন্ন ফিচার 📢

---

## **Python-এ কমেন্টস (Comments)**

প্রোগ্রামিং কোড সহজে বুঝতে **কমেন্টস** ব্যবহার করা হয়। এটি প্রোগ্রামের কার্যকারিতায় কোনো পরিবর্তন আনে না।

### **Single-line Comment:**
```python
# This is a single Line Comment
print("Hello, Python!")
```
### Output:
```
Hello, Python!
```

### **Multi-line Comment:**
```python
"""
This is a multi-line comment, 
which is used for explanation.
"""
print("Python is fun!")
```
### Output:
```
Python is fun!
```

---

## **Escape Sequences (এস্কেপ সিকোয়েন্স)**

| Escape Sequence | ব্যবহার |
|---------------|--------------|
| `\n`          | নতুন লাইন |
| `\t`          | ট্যাব স্পেস |
| `\"`          | ডাবল কোটেশন |
| `\'`          | সিঙ্গেল কোটেশন |
| `\\`          | ব্যাকস্ল্যাশ |

### **Example:**
```python
# \n - New Line
print("Hello\nWorld!")  # It will go to a new line.

# \t - Tab Space
print("Python\tProgramming")  # It will give a tab space.

# \" - Double Quotation
print("He said, \"Python is awesome!\"")  # It will print the double quotation mark.

# \' - Single Quotation
print('It\'s a beautiful day!')  # It will print the single quotation mark.

# \\ - Backslash
print("This is a backslash: \\")  # It will print a single backslash.
```
### Output:
```
Hello
World!
Python    Programming
He said, "Python is awesome!"
It's a beautiful day!
This is a backslash: \
```

---

## **Print Statement (প্রিন্ট স্টেটমেন্ট)**

Python-এ `print()` ফাংশনের মাধ্যমে আউটপুট স্ক্রিনে কিছু প্রদর্শন করা যায়।

### **Basic Print Statement:**
```python
print("Hello, Python!")
print("Welcome to Python programming.")
```
### Output:
```
Hello, Python!
Welcome to Python programming.
```


### **Multiple Items Print:**
```python
print("Python", "is", "fun!")
print("Hello", "World", sep="-")
```
### Output:
```
Python is fun!
Hello-World
```

### **End Parameter Usage:**
```python
print("Hello", end=" ")
print("World!")
```
### Output:
```
Hello World!
```

---

## **Today's Challenge! 🎯**
✅ নিচের কোডটি রান করুন এবং আউটপুট পর্যবেক্ষণ করুন:
```python
print("Write Your Name:")
name = input()
print("Welcome, " + name + "! Let's Start Coding!")
```
📢 **কমেন্টে জানান, আপনি সফলভাবে কোড রান করতে পেরেছেন কিনা!** 💬

---

## **Next Topic: Variables & Data Types in Python!**
🔔 **তাই, ভিডিওটি লাইক করুন, কমেন্ট করুন, এবং চ্যানেলটি সাবস্ক্রাইব করুন!** 🚀

👉 **CodeWithTanim - 100 Days of Python 🚀**

