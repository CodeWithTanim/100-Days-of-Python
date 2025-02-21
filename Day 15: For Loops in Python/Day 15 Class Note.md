# Python Programming - Day 15: For Loops

## For Loops in Python

### **Introduction**
স্বাগতম **100 Days of Python** সিরিজের ১৫তম দিনে! আজকের ভিডিওতে আমরা শিখবো:
- **For Loop** কেন এবং কিভাবে ব্যবহার করবেন? 🔄
- **range()** ফাংশনের জাদু ✨
- নেস্টেড লুপ (লুপের ভেতর লুপ) 🌀
- বাস্তব জীবনের উদাহরণ এবং কমন ভুলগুলি 🚨

---

## **For Loop কী?**

For Loop দিয়ে আপনি যেকোনো **Iterable Object** (লিস্ট, স্ট্রিং, টাপল, ইত্যাদি) এর মধ্যে লুপ চালাতে পারবেন। এটি repetitive কাজগুলোকে সহজ করে!

### **সিনট্যাক্স:**
```python
for variable in iterable:
    # Code to repeat
```

---

## **For Loop এর বেসিক ব্যবহার**

### **উদাহরণ ১: লিস্টের ভেতর লুপ**
```python
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)
```
**আউটপুট:**
```
apple
banana
mango
```

### **উদাহরণ ২: স্ট্রিং এর উপর লুপ**
```python
language = "Python"
for char in language:
    print(char)
```
**আউটপুট:**
```
P
y
t
h
o
n
```

---

## **range() ফাংশন**

`range()` দিয়ে সহজে সংখ্যার সিকোয়েন্স জেনারেট করুন!

### **উদাহরণ ৩: ১-৫ পর্যন্ত প্রিন্ট**
```python
for num in range(1, 6):
    print(num)
```
**আউটপুট:**
```
1
2
3
4
5
```
**নোট:** `range(start, end)` এ **end** ভ্যালু এক্সক্লুসিভ (অন্তর্ভুক্ত নয়)।

---

## **নেস্টেড For Loop (লুপের ভেতর লুপ)**

### **উদাহরণ ৪: টাইম টেবিল**
```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print()  # নতুন লাইন
```
**আউটপুট:**
```
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3

2 x 1 = 2
2 x 2 = 4
2 x 3 = 6

3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
```

---

## **কমন ভুল এবং সতর্কতা ⚠️**
- **কোলন (:) ভুলে যাওয়া:** `for x in list` লিখে কোলন দেননি? Error! ❌
- **ইন্ডেন্টেশন না দেওয়া:** Python এ ইন্ডেন্টেশন জরুরি। 
```python
# ভুল ❌
for x in [1,2,3]:
print(x)

# সঠিক ✅
for x in [1,2,3]:
    print(x)
```
- **লুপের ভেরিয়েবল ভুল নাম:** `for fruit in fruits` লিখে `print(fruits)` করলে? 😅

---

## **Today's Challenge! 🎯**
**প্রবলেম:** ১ থেকে ১০০ পর্যন্ত জোড় সংখ্যাগুলোর যোগফল বের করুন For Loop ব্যবহার করে।  
**Hint:** `range(start, end, step)` এর ৩য় প্যারামিটার ব্যবহার করুন!

**সমাধান লিংক:** [Day 15 Challenge Solution](https://github.com/CodeWithTanim/100-Days-of-Python/blob/main/Day%2015%3A%20For%20Loops%20in%20Python/solution.md)

---

**ভালো লেগে থাকলে ভিডিওটি শেয়ার করুন, লাইক করুন, এবং চ্যানেলটি সাবস্ক্রাইব করুন!** 🚀  

**Happy Coding!** 💻


