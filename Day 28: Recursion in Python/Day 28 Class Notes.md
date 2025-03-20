# Recursion in Python | Python Tutorial - Day #28

## রিকার্শন (Recursion)

### **Introduction**
স্বাগতম **100 Days of Python** সিরিজের ২৮তম দিনে! আজকে আমরা শিখবো:
- রিকার্শন (Recursion) কী এবং কেন ব্যবহার করা হয় 🔄
- বেস কেস (Base Case) এবং রিকার্সিভ স্টেপ (Recursive Step) 🎯
- রিকার্শন ব্যবহার করে প্র্যাকটিক্যাল উদাহরণ 📝
- ইনফাইনিট লুপ থেকে বাঁচার উপায় 🚨

---

## **রিকার্শন কি? (What is Recursion?)**

রিকার্শন হলো এমন একটি প্রক্রিয়া যেখানে একটি ফাংশন নিজেকে নিজেই কল করে, যতক্ষণ না কোনো নির্দিষ্ট শর্ত পূরণ হয় (বেস কেস)।

### **রিকার্শনের ২টি অবশ্যই প্রয়োজনীয় অংশ:**
1. **বেস কেস (Base Case)** - যেখানে ফাংশন থেমে যায়
2. **রিকার্সিভ স্টেপ (Recursive Step)** - ফাংশন নিজেকে ছোট ভ্যারিয়েন্ট দিয়ে কল করে

---

## **ফ্যাক্টোরিয়াল উদাহরণ (Factorial Example)**

```python
def factorial(n):
    if n == 1:  # Base Case
        return 1
    else:       # Recursive Step
        return n * factorial(n-1)

print(factorial(5))  # Output: 120
```

**ব্যাখ্যা:**  
`factorial(5)` → `5 * factorial(4)` → `4 * factorial(3)`... শেষে `1` এ গিয়ে থামে।

---

## **সাধারণ ভুল ⚠️ (Common Mistake)**

বেস কেস ভুলে গেলে **স্ট্যাক ওভারফ্লো (RecursionError)** হবে!

```python
def infinite_loop():
    infinite_loop()  # No base case!

infinite_loop()  # Error: maximum recursion depth exceeded
```

---

## **কাউন্টডাউন উদাহরণ (Countdown Example)**

```python
def countdown(num):
    if num <= 0:  # Base Case
        print("Blastoff! 🚀")
    else:
        print(num)
        countdown(num - 1)

countdown(3)
```

**আউটপুট:**  
```
3
2
1
Blastoff! 🚀
```

---

## **আজকের চ্যালেঞ্জ! 🎯**

**ফিবোনাচ্চি সিকোয়েন্স** রিকার্শন ব্যবহার করে বানান!  
(Formula: fib(n) = fib(n-1) + fib(n-2), Base Case: fib(0)=0, fib(1)=1)

```python
def fibonacci(n):
    # আপনার কোড এখানে লিখুন

print(fibonacci(5))  # Output: 5
```

---

## **গুরুত্বপূর্ণ নোট 📌**
- রিকার্শন ব্যবহার করার সময় **বেস কেস** অবশ্যই যুক্ত করতে হবে
- রিকার্শনে সমস্যা সমাধান করলে কোড ছোট হয়, কিন্তু বেশি ব্যবহারে **performance issue** হতে পারে
- রিকার্শন ট্রি আঁকলে বুঝতে সহজ হয় 🌳

---

**লাইক, কমেন্ট আর শেয়ার করতে ভুলবেন না!** 😊  
**CodeWithTanim - 100 Days of Python** 🚀