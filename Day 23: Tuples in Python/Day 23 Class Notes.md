# Python Programming - Day 23: Tuples in Python

## টাপল (Tuple) - Python-এর অপরিবর্তনীয় ডাটা স্ট্রাকচার

### **Introduction**
স্বাগতম **100 Days of Python** সিরিজের ২৩তম দিনে! আজকে আমরা শিখবো Python-এর সবচেয়ে **জেদি** ডাটা টাইপ সম্পর্কে - যাকে একবার বানালে চাইলেই পরিবর্তন করা যায় না! 🚫

🔹 **টাপল কী?**  
- Ordered Collection (ধারাবাহিকভাবে সাজানো)
- Immutable (অপরিবর্তনীয়)
- Parentheses `()` দিয়ে তৈরি (`tuple = (1, 2, 3)`)
- লিস্টের চাচাতো ভাই, কিন্তু একটু **জেদি** 😤

---

## **টাপল তৈরি করার নিয়ম**

### **Basic Syntax:**
```python
# Simple tuple
fruits = ("apple", "banana", "mango")
print(fruits)  # Output: ('apple', 'banana', 'mango')

# Without parentheses (ও কাজ করে!)
colors = "red", "green", "blue"
print(colors)  # Output: ('red', 'green', 'blue')
```

### **একটি উপাদান বিশিষ্ট টাপল:**
```python
# Wrong way - becomes string ❌
not_tuple = ("hello")
print(type(not_tuple))  # <class 'str'>

# Correct way ✅
real_tuple = ("hello",)
print(type(real_tuple))  # <class 'tuple'>
```
**নোট:** কমা (`,`) থাকতে হবে, নইলে টাপল হবে না!

---

## **টাপলের বৈশিষ্ট্য**

| বৈশিষ্ট্য | বর্ণনা | উদাহরণ |
|-----------|---------|--------|
| **Immutable** | একবার তৈরি হলে পরিবর্তন করা যায় না | `tuple[0] = 5` → Error ❌ |
| **Ordered** | ইনডেক্সিং/স্লাইসিং সাপোর্ট করে | `print(tuple[1])` ✅ |
| **Duplicates Allowed** | একই ভ্যালু বার বার থাকতে পারে | `(1, 1, 2)` ✅ |

### **Immutability Demo:**
```python
numbers = (1, 2, 3)
numbers[0] = 99  # TypeError: 'tuple' object does not support item assignment
```

---

## **মিক্সড ডাটা টাইপের টাপল**
টাপলে সব ধরণের ডাটা টাইপ রাখা যায় - ইন্টিজার, স্ট্রিং, 심ি এমনকি অন্য টাপলও! 🎉

```python
mixed_tuple = (42, "Python", 3.14, True, ("nested", "tuple"))
print(mixed_tuple)  
# Output: (42, 'Python', 3.14, True, ('nested', 'tuple'))
```

---

## **Today's Challenge! 🎯**
একটি টাপল তৈরি করুন যাতে থাকবে:
- আপনার প্রিয় বইয়ের নাম (স্ট্রিং)
- প্রকাশনার বছর (ইন্টিজার)
- রেটিং (ফ্লোট)
- পড়া শেষ হয়েছে কিনা (বুলিয়ান)

```python
# Example Solution
my_tuple = ("The Alchemist", 1988, 4.5, True)
print(my_tuple)
```
📢 **কমেন্টে শেয়ার করুন আপনার টাপলটি!** 💬

---

🔔 **ভিডিওটি লাইক করুন, বন্ধুদের সাথে শেয়ার করুন এবং চ্যানেলটি সাবস্ক্রাইব করুন!** 🚀  
👉 **CodeWithTanim - 100 Days of Python** 🐍