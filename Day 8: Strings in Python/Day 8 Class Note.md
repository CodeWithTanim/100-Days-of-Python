# Python Programming - Day 8: Strings in Python

## Strings in Python

### **Introduction**
স্বাগতম **100 Days of Python** সিরিজের ৮ম দিনে! আজকের ভিডিওতে আমরা শিখবো:
- **স্ট্রিংস (Strings)** কী এবং কিভাবে কাজ করে 📜
- **স্ট্রিংস তৈরি করার বিভিন্ন উপায়** 🛠️
- **স্ট্রিংসের বৈশিষ্ট্য এবং ব্যবহার** 🔍

---

## **স্ট্রিংস (Strings) কী?**

স্ট্রিংস হলো Python-এ টেক্সট বা লেখা কে রিপ্রেজেন্ট করার জন্য একটি ডাটা টাইপ। স্ট্রিংস কে সিঙ্গেল কোট (`' '`) বা ডাবল কোট (`" "`) এর মধ্যে লিখা হয়।

### **স্ট্রিংস তৈরি করার উদাহরণ:**
```python
name = "Tanim"
greeting = 'Hello, World!'
```
### Output:
```
Tanim
Hello, World!
```

🔹 **Python-এ স্ট্রিংস Immutable, মানে একবার তৈরি হয়ে গেলে এর মধ্যে কোনো ক্যারেক্টার চেঞ্জ করা যায় না।**

---

## **Multiline Strings**

যদি আমরা অনেক লাইন জুড়ে টেক্সট লিখতে চাই, তাহলে Multiline Strings ব্যবহার করতে পারি। Multiline Strings তৈরি করতে Triple Quotes (`'''` বা `"""`) ব্যবহার করা হয়।

### **Multiline Strings উদাহরণ:**
```python
poem = """বিদ্রোহী - কাজী নজরুল ইসলাম
বল বীর, বল উন্নত মম শির!
শির নেহারি' আমারি, নত শির ওই শিখর হিমাদ্রির!
বল বীর, আমি চির উন্নত শির,
চির উন্নত মম শির, নত শির নহি কারো।"""
```
### Output:
```
বিদ্রোহী - কাজী নজরুল ইসলাম
বল বীর, বল উন্নত মম শির!
শির নেহারি' আমারি, নত শির ওই শিখর হিমাদ্রির!
বল বীর, আমি চির উন্নত শির,
চির উন্নত মম শির, নত শির নহি কারো।
```

---

## **স্ট্রিংসের ক্যারেক্টার এক্সেস করা**

Python-এ স্ট্রিংস হলো একটি Sequence of Characters। প্রতিটি ক্যারেক্টার এর একটা ইনডেক্স থাকে, যা দিয়ে আমরা ক্যারেক্টার গুলো এক্সেস করতে পারি।

### **ক্যারেক্টার এক্সেস করার উদাহরণ:**
```python
word = "Python"
print(word[0])  # Output: P
print(word[2])  # Output: t
```
### Output:
```
P
t
```

🔹 **স্ট্রিংসের ইনডেক্স সবসময় 0 থেকে শুরু হয়।**

---

## **স্ট্রিংস Concatenation (জোড়া লাগানো)**

দুটি স্ট্রিংস কে জোড়া লাগানোর প্রক্রিয়াকে Concatenation বলে। Concatenation করতে `+` অপারেটর ব্যবহার করা হয়।

### **Concatenation উদাহরণ:**
```python
first_name = "MSR"
last_name = "Tanim"
full_name = first_name + " " + last_name
print(full_name)  # Output: MSR Tanim
```
### Output:
```
MSR Tanim
```

---

## **স্ট্রিংস Repetition (পুনরাবৃত্তি)**

স্ট্রিংস কে Repeat করতে `*` অপারেটর ব্যবহার করা হয়।

### **Repetition উদাহরণ:**
```python
laugh = "Ha"
print(laugh * 3)  # Output: HaHaHa
```
### Output:
```
HaHaHa
```

---

## **স্ট্রিংসের Length বের করা**

স্ট্রিংসের Length বা দৈর্ঘ্য বের করতে `len()` ফাংশন ব্যবহার করা হয়।

### **Length বের করার উদাহরণ:**
```python
word = "Python"
print(len(word))  # Output: 6
```
### Output:
```
6
```

---

## **Escape Characters in Strings**

Python-এ কিছু বিশেষ ক্যারেক্টার আছে, যেগুলোকে Escape Characters বলে। এগুলো স্ট্রিংসের মধ্যে বিশেষ কিছু কাজ করে।

### **Escape Characters উদাহরণ:**
```python
print("Hello\nWorld")  # New Line
print("Hello\tWorld")  # Tab Indent
```
### Output:
```
Hello
World
Hello    World
```

---

## **Today's Challenge! 🎯**

✅ নিচের কোডটি রান করুন এবং আউটপুট পর্যবেক্ষণ করুন:
```python
name = input("Write Your Name: ")
age = int(input("Type Your Age: "))
print(f"Welcome {name}! You are {age} years old!")
```
📢 **কমেন্টে জানান, আপনি সফলভাবে কোড রান করতে পেরেছেন কিনা!** 💬

---

## **Next Topic: Strings Slicing and Methods in Python**
🔔 **তাই, ভিডিওটি লাইক করুন, কমেন্ট করুন, এবং চ্যানেলটি সাবস্ক্রাইব করুন!** 🚀

👉 **CodeWithTanim - 100 Days of Python 🚀**

---

**[End of README.md]**