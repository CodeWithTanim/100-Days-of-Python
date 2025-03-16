# Python Programming - Day 27: DocStrings in Python

## **DocStrings in Python**

### **Introduction**
স্বাগতম **100 Days of Python** সিরিজের ২৭তম দিনে! আজকের ভিডিওতে আমরা শিখবো:
- **DocStrings** কী এবং কেন ব্যবহার করা হয় 📄
- **DocStrings** কিভাবে লিখতে হয় এবং এক্সেস করতে হয় 🛠️
- **DocStrings** এর ব্যবহারের উদাহরণ 📝

---

## **Python-এ DocStrings**

DocStrings হলো Python-এ একটি বিশেষ ধরনের স্ট্রিং, যেটা কোনো ফাংশন, ক্লাস, বা মডিউল সম্পর্কে তথ্য দেয়। এটা ট্রিপল কোট (**''' '''** বা **""" """**) এর মধ্যে লেখা হয়।  

### **DocStrings এর সুবিধা:**
- কোডকে আরও রিডেবল এবং মেইনটেইনেবল করে তোলে।
- অন্য প্রোগ্রামারদের (বা ভবিষ্যৎ আপনার নিজের) জন্য কোডের ব্যাপারে সবকিছু ব্যাখ্যা করে দেওয়া।

---

## **DocStrings কিভাবে লিখতে হয়?**

### **ফাংশনের জন্য DocStrings:**
```python
def add(a, b):
    """
    This function takes two numbers as input and returns their sum.
    """
    return a + b
```

### **ক্লাসের জন্য DocStrings:**
```python
class Dog:
    """
    A class representing a Dog.
    """
    def __init__(self, name):
        self.name = name

    def bark(self):
        """
        Makes the dog bark.
        """
        print(f"{self.name} says Woof!")
```

---

## **DocStrings কিভাবে এক্সেস করতে হয়?**

Python এ `__doc__` attribute ব্যবহার করে আপনি DocStrings টা এক্সেস করতে পারেন।  

### **ফাংশনের DocStrings এক্সেস:**
```python
print(add.__doc__)
```

**Output:**
```
This function takes two numbers as input and returns their sum.
```

### **ক্লাসের DocStrings এক্সেস:**
```python
print(Dog.__doc__)
```

**Output:**
```
A class representing a Dog.
```

### **মেথডের DocStrings এক্সেস:**
```python
print(Dog.bark.__doc__)
```

**Output:**
```
Makes the dog bark.
```

---

## **উদাহরণ: DocStrings এর ব্যবহার**

```python
def greet(name):
    """
    This function greets the person passed in as a parameter.
    """
    print(f"Hello, {name}! How are you?")
```

**Output:**
```python
greet("Alice")
```
```
Hello, Alice! How are you?
```

---

## **Today's Challenge! 🎯**
✅ নিচের কোডটি রান করুন এবং আউটপুট পর্যবেক্ষণ করুন:
```python
def multiply(a, b):
    """
    This function takes two numbers as input and returns their product.
    """
    return a * b

print(multiply.__doc__)
print(multiply(5, 3))
```
📢 **কমেন্টে জানান, আপনি সফলভাবে কোড রান করতে পেরেছেন কিনা!** 💬

---

## **Next Topic: Modules in Python**
🔔 **তাই, ভিডিওটি লাইক করুন, কমেন্ট করুন, এবং চ্যানেলটি সাবস্ক্রাইব করুন!** 🚀

👉 **CodeWithTanim - 100 Days of Python 🚀**