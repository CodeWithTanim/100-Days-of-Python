# Python Tutorial - Day #20: Exercise 2 - A Simple Python Calculator

## বেসিক ক্যালকুলেটর তৈরি

### **প্রজেক্ট ওভারভিউ**
আজকের এক্সারসাইজে আমরা যা শিখবো:
- ইউজার ইনপুট হ্যান্ডলিং 📥
- টাইপ কাস্টিং 🔄
- ম্যাচ-কেস স্টেটমেন্টস 🎚️
- লুপস (while লুপ) 🔁
- এরর হ্যান্ডলিং (ডিভাইড বাই জিরো) ⚠️

---

## **ক্যালকুলেটর লজিক**

### **স্টেপ ১: ইউজার ইনপুট এবং টাইপ কাস্টিং**
```python
num1 = float(input("প্রথম সংখ্যা লিখুন: "))
num2 = float(input("দ্বিতীয় সংখ্যা লিখুন: "))
```
🔹 `input()` দিয়ে ইউজার থেকে নম্বর নিচ্ছি, `float()` দিয়ে স্ট্রিংকে সংখ্যায় কনভার্ট করছি

---

### **স্টেপ ২: অপারেশন সিলেকশন (ম্যাচ-কেস)**
```python
operation = input("অপারেশন চয়েস করুন (+, -, *, /): ")

match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        result = num1 / num2 if num2 != 0 else "Error! Zero division"
    case _:
        result = "অবৈধ অপারেশন"
```
🔹 `match-case` (Python 3.10+) ব্যবহার করে অপারেশন সিলেক্ট করছি  
🔹 `/` কেসে এরর হ্যান্ডলিং যোগ করেছি

---

### **স্টেপ ৩: রিপিটেশন সিস্টেম (while লুপ)**
```python
while True:
    # সম্পূর্ণ ক্যালকুলেশন কোড এখানে
    repeat = input("আরেকবার ক্যালকুলেট করতে চান? (হ্যাঁ/না): ")
    if repeat.lower() != "হ্যাঁ":
        break
```
🔹 `while True` লুপ দিয়ে প্রোগ্রামকে রিপিটেবল বানানো হয়েছে  
🔹 `break` স্টেটমেন্ট দিয়ে লুপ থামানো হচ্ছে

---

## **সম্পূর্ণ কোড**
```python
while True:
    num1 = float(input("প্রথম সংখ্যা লিখুন: "))
    num2 = float(input("দ্বিতীয় সংখ্যা লিখুন: "))
    operation = input("অপারেশন চয়েস করুন (+, -, *, /): ")

    match operation:
        case "+":
            result = num1 + num2
        case "-":
            result = num1 - num2
        case "*":
            result = num1 * num2
        case "/":
            result = num1 / num2 if num2 != 0 else "Error! Zero division"
        case _:
            result = "অবৈধ অপারেশন"

    print(f"ফলাফল: {result}")
    
    repeat = input("আরেকবার ক্যালকুলেট করতে চান? (হ্যাঁ/না): ")
    if repeat.lower() != "হ্যাঁ":
        print("বিদায়!")
        break
```

---

## **চ্যালেঞ্জ! 🚀**
✅ এই ফিচারগুলো যোগ করে প্রোগ্রামটি আপগ্রেড করুন:
1. বর্গমূল ক্যালকুলেশন যোগ করুন (√) 
2. `try-except` ব্লক ব্যবহার করে ইনভ্যালিড ইনপুট হ্যান্ডলিং
3. আলাদা ফাংশন বানান প্রতিটি অপারেশনের জন্য
4. ক্যালকুলেশন হিস্ট্রি সংরক্ষণ করুন (লিস্ট ব্যবহার করে)

---

## **সাপোর্ট**
🔄 কোডে কোনো সমস্যা হলে কমেন্টে জানান  
💡 আপনার তৈরি করা ভার্সন শেয়ার করতে ভুলবেন না!  
👍 লাইক ও শেয়ার করতে ভুলবেন না - #CodeWithTanim