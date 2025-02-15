# Python Programming - Day 9: Strings Slicing and Operations on Strings

## Strings Slicing and Operations on Strings

### **Introduction**
স্বাগতম **100 Days of Python** সিরিজের ৯ম দিনে! আজকের ভিডিওতে আমরা শিখবো:
- **স্ট্রিং স্লাইসিং (Strings Slicing)** কী এবং কিভাবে ব্যবহার করা হয় 🍰
- **স্ট্রিং-এর উপর বিভিন্ন অপারেশন (Operations on Strings)** 🛠️
- **স্ট্রিং স্লাইসিং এবং অপারেশনের প্র্যাকটিক্যাল উদাহরণ** 📝

---

## **স্ট্রিং স্লাইসিং (Strings Slicing)**

স্ট্রিং স্লাইসিং হলো স্ট্রিং-এর একটি অংশ বের করার প্রক্রিয়া। Python-এ স্ট্রিং স্লাইসিং খুবই সহজ এবং পাওয়ারফুল একটি ফিচার।

### **স্ট্রিং স্লাইসিং সিনট্যাক্স:**
```python
string[start:end:step]
```
- **start**: স্লাইসিং শুরু করার ইনডেক্স (শুরু হয় 0 থেকে)।
- **end**: স্লাইসিং শেষ করার ইনডেক্স (এই ইনডেক্সের আগ পর্যন্ত নেয়)।
- **step**: কত ক্যারেক্টার পর পর নিতে চাই (ডিফল্ট হলো 1)।

### **উদাহরণ:**
```python
text = "Python Programming"

# প্রথম ৬টি ক্যারেক্টার
print(text[0:6])  # Output: Python

# শেষ থেকে ১১তম থেকে শেষ পর্যন্ত
print(text[-11:])  # Output: Programming

# স্টেপ ব্যবহার করে প্রতি ২য় ক্যারেক্টার
print(text[0:6:2])  # Output: Pto
```

---

## **স্ট্রিং-এর উপর অপারেশন (Operations on Strings)**

Python-এ স্ট্রিং-এর উপর বিভিন্ন অপারেশন করা যায়। যেমন:

### **1. Concatenation (স্ট্রিং জোড়া লাগানো):**
```python
text1 = "Hello"
text2 = "World"
result = text1 + " " + text2
print(result)  # Output: Hello World
```

### **2. Repetition (স্ট্রিং রিপিট করা):**
```python
text = "Python"
result = text * 3
print(result)  # Output: PythonPythonPython
```

### **3. Membership Testing (স্ট্রিং-এ উপস্থিতি চেক করা):**
```python
text = "Python Programming"
print("Python" in text)  # Output: True
print("Java" in text)    # Output: False
```

---

## **প্র্যাকটিক্যাল উদাহরণ (Practical Example)**

ধরুন, আমাদের একটি স্ট্রিং আছে `sentence = "I love Python Programming"`। এখন আমরা চাই এই স্ট্রিং থেকে প্রথম শব্দটি বের করতে।

```python
sentence = "I love Python Programming"
first_word = sentence[0:6]
print(first_word)  # Output: I love
```

---

## **Today's Challenge! 🎯**
✅ নিচের কোডটি রান করুন এবং আউটপুট পর্যবেক্ষণ করুন:
```python
text = "CodeWithTanim"
# Challenge 1: প্রথম ৪টি ক্যারেক্টার বের করুন
# Challenge 2: শেষ ৫টি ক্যারেক্টার বের করুন
# Challenge 3: প্রতি ৩য় ক্যারেক্টার বের করুন
```
📢 **কমেন্টে জানান, আপনি সফলভাবে কোড রান করতে পেরেছেন কিনা!** 💬

---

## **Next Topic: Advanced String Methods in Python**
🔔 **তাই, ভিডিওটি লাইক করুন, কমেন্ট করুন, এবং চ্যানেলটি সাবস্ক্রাইব করুন!** 🚀

👉 **CodeWithTanim - 100 Days of Python 🚀**

---
  
**Connect with Me:**  
- [YouTube](https://youtube.com/codewithtanim)  
- [Facebook](https://facebook.com/codewithtanim)  
- [GitHub](https://github.com/codewithtanim)  
