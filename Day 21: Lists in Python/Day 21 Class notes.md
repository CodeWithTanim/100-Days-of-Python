# Python Programming - Day 21: Introduction to Lists

## Python লিস্ট (Lists)

### **ভূমিকা**
স্বাগতম **Python Tutorial** সিরিজের ২০তম দিনে! আজকে আমরা শিখবো:
- লিস্ট (List) কি এবং কেন ব্যবহার করা হয় 📋
- কিভাবে লিস্ট তৈরি করতে হয় 🛠️
- লিস্টের এলিমেন্ট অ্যাক্সেস করা 🔍
- লিস্ট মডিফাই করা ✏️

---

## **পাইথনে লিস্ট কি?**

লিস্ট হল পাইথনের একটি ডেটা স্ট্রাকচার যেটা একসাথে একাধিক ভ্যালু সংরক্ষণ করতে পারে। লিস্টের বিশেষত্ব:
- **অর্ডারড** (মানে এলিমেন্টগুলোর অবস্থান ঠিক থাকে)
- **মিউটেবল** (পরিবর্তনযোগ্য)
- যেকোনো ডেটা টাইপ সংরক্ষণ করতে পারে

### **লিস্ট তৈরি করার নিয়ম:**
```python
# Empty List
empty_list = []

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Mixed Data Types
mixed_list = [1, "Apple", 3.14, True]

# Nested List
nested_list = [[1, 2], [3, 4]]
```

---

## **লিস্টের এলিমেন্ট অ্যাক্সেস করা**

### **ইনডেক্সিং (Indexing):**
```python
fruits = ["apple", "banana", "cherry"]

print(fruits[0])  # Output: apple
print(fruits[2])  # Output: cherry
```

### **নেগেটিভ ইনডেক্সিং:**
```python
print(fruits[-1])  # Output: cherry (last element)
print(fruits[-2])  # Output: banana (second last)
```

---

## **লিস্ট স্লাইসিং (Slicing)**

সিনট্যাক্স: `list[start:end:step]`

```python
numbers = [1, 2, 3, 4, 5]

print(numbers[1:3])   # Output: [2, 3]
print(numbers[:3])    # Output: [1, 2, 3]
print(numbers[2:])    # Output: [3, 4, 5]
print(numbers[::2])   # Output: [1, 3, 5]
```

---

## **লিস্ট মডিফাই করা**

```python
# Single Element Modification
fruits = ["apple", "banana", "cherry"]
fruits[1] = "mango"
print(fruits)  # Output: ['apple', 'mango', 'cherry']

# Multiple Elements Modification
numbers = [1, 2, 3, 4, 5]
numbers[1:4] = [20, 30, 40]
print(numbers)  # Output: [1, 20, 30, 40, 5]
```

---

## **লিস্টের বিশেষত্ব**

🔹 **ডাইনামিক সাইজ:** লিস্টের সাইজ অটোমেটিক বাড়ে/কমে  
🔹 **ভিন্ন ডেটা টাইপ:** একই লিস্টে রাখতে পারেন Numbers, Strings, Booleans  
🔹 **নেস্টেড লিস্ট:** লিস্টের ভিতরে আরেকটি লিস্ট রাখা যায়  

```python
# Complex Example
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][2])  # Output: 6
```

---

## **আজকের চ্যালেঞ্জ! 🎯**

```python
# Challenge Code
books = ["Python Crash Course", "Atomic Habits", "1984", "Deep Work"]
# 1. "1984" বইটির ইনডেক্স বের করুন
# 2. প্রথম বইটিকে "Learn Python the Hard Way" দিয়ে প্রতিস্থাপন করুন
# 3. শেষ দুটি বই প্রিন্ট করুন
```

📢 **কমেন্টে জানান আপনার সমাধান!** 💬

---

**CodeWithTanim - 100 Days of Python 🚀**  
👍 **লাইক করুন, শেয়ার করুন, এবং সাবস্ক্রাইব করতে ভুলবেন না!** 🔔