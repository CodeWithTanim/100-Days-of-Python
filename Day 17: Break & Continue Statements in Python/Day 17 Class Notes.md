# Python Programming - Day 17: Break & Continue Statements

## Break এবং Continue স্টেটমেন্ট

### **ভূমিকা**
স্বাগতম **100 Days of Python** সিরিজের ১৭তম দিনে! আজকের ভিডিওতে আমরা শিখবো:
- লুপের ফ্লো কন্ট্রোল করার শক্তিশালী টুলস 🔧
- `break` স্টেটমেন্টের ব্যবহার এবং প্রয়োগ 🛑
- `continue` স্টেটমেন্টের ব্যবহার এবং প্রয়<｜place▁holder▁no▁430｜> 🚩
- বাস্তব উদাহরণের মাধ্যমে এই কনসেপ্টগুলোর প্র্যাকটিক্যাল ইউজ ✔️

---

## **break স্টেটমেন্ট**

লুপ থেকে সম্পূর্ণ বের হয়ে যাওয়ার জন্য ব্যবহৃত হয়।

### **সিনট্যাক্স:**
```python
for item in sequence:
    if condition:
        break
```

### **উদাহরণ ১:**
```python
# Break when number equals 5
for number in range(1, 11):
    if number == 5:
        print("Found 5! Breaking loop!")
        break
    print(number)
```

### **আউটপুট:**
```
1
2
3
4
Found 5! Breaking loop!
```

🔹 **নোট:** break পেলে লুপ সম্পূর্ণ বন্ধ হয়ে যায়!

---

## **continue স্টেটমেন্ট**

বর্তমান ইটারেশন স্কিপ করে পরবর্তী ইটারেশনে যেতে ব্যবহৃত হয়।

### **সিনট্যাক্স:**
```python
for item in sequence:
    if condition:
        continue
```

### **উদাহরণ ২:**
```python
# Skip even numbers
for num in range(1, 11):
    if num % 2 == 0:
        continue
    print(num)
```

### **আউটপুট:**
```
1
3
5
7
9
```

🔹 **নোট:** continue শুধু বর্তমান ইটারেশন স্কিপ করে!

---

## **কম্বাইন্ড উদাহরণ**

```python
# Break and continue in one loop
fruits = ["apple", "banana", "cherry", "damaged", "mango"]

for fruit in fruits:
    if fruit == "damaged":
        print("Stopping processing!")
        break
    if fruit == "banana":
        print("Skipping banana!")
        continue
    print(f"Processing: {fruit}")
```

### **আউটপুট:**
```
Processing: apple
Skipping banana!
Processing: cherry
Stopping processing!
```

---

## **আজকের চ্যালেঞ্জ! 🎯**
✅ নিচের সমস্যাটি সমাধান করুন:
```python
# 1 থেকে 20 পর্যন্ত প্রিন্ট করুন
# কিন্তু:
# - ৩ এর গুণিতক হলে স্কিপ করুন (continue)
# - ১৫ পেলে লুপ ব্রেক করুন (break)
```

📢 **কমেন্টে আপনার সমাধান শেয়ার করুন!** 💬

---

🔔 **ভিডিওটি লাইক করুন, কমেন্ট করুন এবং চ্যানেলটি সাবস্ক্রাইব করুন!**  
👉 **CodeWithTanim - 100 Days of Python 🚀**
