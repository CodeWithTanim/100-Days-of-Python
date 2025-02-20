# Python Programming - Day 14: Match Case Statements in Python

## **Match Case Statements**

### **Introduction**
স্বাগতম **100 Days of Python** সিরিজের ১৪তম দিনে! আজকের ভিডিওতে আমরা শিখবো:
- **Match Case Statements** কী এবং কেন ব্যবহার করা হয় 🏷️
- **Python 3.10** এ নতুন যুক্ত এই ফিচারটি কিভাবে কাজ করে 🏗️
- **Match Case** এর মাধ্যমে কিভাবে একাধিক conditions কে elegant ভাবে handle করা যায় 📝

---

## **Python-এ Match Case Statements**

Match Case Statement হলো Python 3.10 এ যুক্ত একটি নতুন ফিচার, যা আমাদেরকে একাধিক conditions কে খুব সুন্দর এবং readable ভাবে handle করতে সাহায্য করে। আগে আমরা যদি একাধিক conditions check করতে চাইতাম, তাহলে `if-elif-else` ব্যবহার করতাম। কিন্তু Match Case এর মাধ্যমে আমরা সেই একই কাজটা আরও elegant ভাবে করতে পারি।

### **Match Case Syntax:**
```python
match variable:
    case pattern1:
        # Action for pattern1
    case pattern2:
        # Action for pattern2
    case _:
        # Default action
```

🔹 **`case _` হলো default case, মানে যদি কোনও case match না হয়, তাহলে এইটা কাজ করবে।**

---

## **Match Case এর উদাহরণ**

### **উদাহরণ ১: Basic Match Case**
```python
# Example 1: Basic Match Case
def check_number(num):
    match num:
        case 1:
            return "You entered One"
        case 2:
            return "You entered Two"
        case 3:
            return "You entered Three"
        case _:
            return "You entered something else!"

# Testing the function
print(check_number(2))  # Output: You entered Two
print(check_number(5))  # Output: You entered something else!
```

**ব্যাখ্যা:**  
এই উদাহরণটায় আমরা দেখতে পাচ্ছি, কিভাবে Match Case Statement ব্যবহার করে আমরা একটি সংখ্যা check করছি। `case 1`, `case 2`, `case 3` দিয়ে আমরা আলাদা আলাদা ভ্যালু handle করছি। আর `case _` হলো default case, মানে যদি কোনও case match না হয়, তাহলে এইটা কাজ করবে।

---

### **উদাহরণ ২: Match Case with Patterns**
```python
# Example 2: Match Case with Patterns
def check_data(data):
    match data:
        case [name, age]:
            return f"Name: {name}, Age: {age}"
        case {"name": name, "age": age}:
            return f"Name: {name}, Age: {age}"
        case _:
            return "Unknown data format!"

# Testing the function
print(check_data(["Alice", 25]))  # Output: Name: Alice, Age: 25
print(check_data({"name": "Bob", "age": 30}))  # Output: Name: Bob, Age: 30
print(check_data("Hello"))  # Output: Unknown data format!
```

**ব্যাখ্যা:**  
এই উদাহরণটায় আমরা দেখলাম কিভাবে Match Case Statement দিয়ে আমরা লিস্ট এবং ডিকশনারি এর মত ডাটা স্ট্রাকচার কে handle করতে পারি। প্রথম case টা চেক করছে যদি ডাটা টা একটা লিস্ট হয়, আর দ্বিতীয় case টা চেক করছে যদি ডাটা টা একটা ডিকশনারি হয়। আর যদি কিছুই match না হয়, তাহলে default case টা কাজ করবে।

---

### **উদাহরণ ৩: Match Case with Conditions**
```python
# Example 3: Match Case with Conditions
def check_age(age):
    match age:
        case age if age < 18:
            return "You are a minor."
        case age if 18 <= age < 60:
            return "You are an adult."
        case age if age >= 60:
            return "You are a senior citizen."
        case _:
            return "Invalid age!"

# Testing the function
print(check_age(15))  # Output: You are a minor.
print(check_age(25))  # Output: You are an adult.
print(check_age(65))  # Output: You are a senior citizen.
```

**ব্যাখ্যা:**  
এই উদাহরণটায় আমরা দেখলাম কিভাবে Match Case Statement এর সাথে conditions যোগ করে আমরা আরও precise ভাবে কাজ করতে পারি। এখানে আমরা age এর উপর ভিত্তি করে আলাদা আলাদা মেসেজ রিটার্ন করছি।

---

## **Today's Challenge! 🎯**
✅ নিচের কোডটি রান করুন এবং আউটপুট পর্যবেক্ষণ করুন:
```python
def check_fruit(fruit):
    match fruit:
        case "Apple":
            return "You chose Apple!"
        case "Banana":
            return "You chose Banana!"
        case "Mango":
            return "You chose Mango!"
        case _:
            return "Unknown fruit!"

# Test the function
print(check_fruit("Banana"))  # What will be the output?
```
📢 **কমেন্টে জানান, আপনি সফলভাবে কোড রান করতে পেরেছেন কিনা!** 💬

---

## **Next Topic: Advanced Python Concepts**
🔔 **তাই, ভিডিওটি লাইক করুন, কমেন্ট করুন, এবং চ্যানেলটি সাবস্ক্রাইব করুন!** 🚀

👉 **CodeWithTanim - 100 Days of Python 🚀**