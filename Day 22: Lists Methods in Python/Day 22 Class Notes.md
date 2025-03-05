# Python Programming - Day 22: List Methods

## List Methods in Python

### **Introduction**
স্বাগতম **Python Tutorial** সিরিজের ২২তম দিনে! আজকে আমরা শিখবো:
- **লিস্ট মেথড** কী এবং কেন জরুরি 🛠️
- **প্রতিটি মেথডের কাজ ও ব্যবহার** 🔧
- **রিয়াল-টাইম উদাহরণের সাথে প্র্যাকটিস্যাল নলেজ** 💻

---

## **Python-এ লিস্ট মেথডস (List Methods)**

লিস্ট মেথডগুলি হলো লিস্ট অবজেক্টের সাথে সরাসরি যুক্ত ফাংশন। এদের মাধ্যমে লিস্টকে মডিফাই, আপডেট ও ম্যানিপুলেট করা যায়।

---

## **প্রধান লিস্ট মেথডস ও ব্যবহার**

### **1. append()**
লিস্টের **শেষে** নতুন আইটেম যোগ করে
```python
fruits = ["apple", "banana"]
fruits.append("mango")
print(fruits)  # Output: ['apple', 'banana', 'mango']
```

### **2. extend()**
একটি লিস্টের সাথে অন্য লিস্ট যোগ করে
```python
list1 = [1, 2, 3]
list2 = [4, 5]
list1.extend(list2)
print(list1)  # Output: [1, 2, 3, 4, 5]
```

### **3. insert()**
নির্দিষ্ট ইনডেক্সে নতুন ভ্যালু যুক্ত করে
```python
numbers = [10, 20, 40]
numbers.insert(2, 30)
print(numbers)  # Output: [10, 20, 30, 40]
```

### **4. remove()**
ভ্যালু দিয়ে আইটেম ডিলিট করে
```python
colors = ["red", "blue", "green"]
colors.remove("blue")
print(colors)  # Output: ['red', 'green']
```

### **5. pop()**
ইনডেক্স দিয়ে আইটেম ডিলিট করে এবং রিটার্ন করে
```python
nums = [1, 2, 3, 4]
popped = nums.pop(1)
print(popped)  # Output: 2
print(nums)    # Output: [1, 3, 4]
```

### **6. clear()**
সমস্ত আইটেম ডিলিট করে লিস্ট খালি করে
```python
items = [5, 6, 7]
items.clear()
print(items)  # Output: []
```

### **7. index()**
ভ্যালুর প্রথম occurrence-এর ইনডেক্স খুঁজে দেয়
```python
letters = ['a', 'b', 'c', 'a']
print(letters.index('c'))  # Output: 2
```

### **8. count()**
ভ্যালু কতবার আছে তা গণনা করে
```python
scores = [5, 2, 5, 3, 5]
print(scores.count(5))  # Output: 3
```

### **9. sort()**
লিস্টকে Ascending/Descending অর্ডারে সাজায়
```python
numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)  # Output: [1, 2, 3, 4]

numbers.sort(reverse=True)
print(numbers)  # Output: [4, 3, 2, 1]
```

### **10. reverse()**
লিস্টের অর্ডার উল্টিয়ে দেয়
```python
animals = ["cat", "dog", "bird"]
animals.reverse()
print(animals)  # Output: ['bird', 'dog', 'cat']
```

### **11. copy()**
লিস্টের শ্যালো কপি তৈরি করে
```python
original = [1, 2, 3]
new = original.copy()
new.append(4)
print(original)  # Output: [1, 2, 3]
print(new)       # Output: [1, 2, 3, 4]
```

---

## **আজকের চ্যালেঞ্জ! 🎯**
✅ নিচের টাস্কটি সম্পন্ন করুন:
```python
# 1. Create a list: numbers = [5, 2, 8, 1]
# 2. Append 10, Insert 0 at index 2, Remove 8
# 3. Sort & Reverse the list
# 4. Print final list and its length
```

📢 **কমেন্টে শেয়ার করুন আপনার সমাধান!** 💬

---

🔔 **লাইক, কমেন্ট, এবং শেয়ার করে সাপোর্ট করুন!** 🚀  
👉 **CodeWithTanim - 100 Days of Python** 🐍