# Python Programming - Day 5: Operators in Python

## **Operators in Python**

### **Introduction**
স্বাগতম **100 Days of Python** সিরিজের ৫ম দিনে! আজকের ভিডিওতে আমরা শিখবো:
- **অপারেটর (Operators)** কী এবং কেন ব্যবহার করা হয় 🛠️
- **Python-এ বিভিন্ন ধরণের অপারেটর এবং তাদের ব্যবহার** 📊
- **প্র্যাকটিক্যাল উদাহরণসহ অপারেটর শেখা** 💡

---

## **Python-এ অপারেটর (Operators)**

অপারেটর হলো বিশেষ symbols বা keywords যেগুলো দিয়ে আমরা variables বা values-এর মধ্যে বিভিন্ন অপারেশন চালাতে পারি। যেমন, যোগ, বিয়োগ, গুণ, ভাগ, তুলনা করা ইত্যাদি। Python-এ প্রধানত ৬ ধরনের অপারেটর রয়েছে:

| অপারেটর | বর্ণনা |
|-----------|----------------|
| **Arithmetic Operators** | গাণিতিক অপারেশন পরিচালনার জন্য |
| **Assignment Operators** | ভেরিয়েবলে মান সংরক্ষণ করার জন্য |
| **Comparison Operators** | তুলনা করার জন্য |
| **Logical Operators** | লজিক্যাল শর্ত যাচাই করার জন্য |
| **Bitwise Operators** | বিট-লেভেল অপারেশন পরিচালনার জন্য |
| **Membership & Identity Operators** | সদস্যতা ও পরিচয় যাচাই করার জন্য |

---

## **Arithmetic Operators (গাণিতিক অপারেটর)**

Arithmetic Operators দিয়ে আমরা গাণিতিক অপারেশন করি। যেমন:

| অপারেটর | বর্ণনা | উদাহরণ |
|---------|--------|--------|
| `+` | যোগ | `a + b` |
| `-` | বিয়োগ | `a - b` |
| `*` | গুণ | `a * b` |
| `/` | ভাগ | `a / b` |
| `%` | ভাগশেষ | `a % b` |
| `**` | সূচক | `a ** b` |
| `//` | পূর্ণসংখ্যা ভাগ | `a // b` |

### **উদাহরণ:**
```python
a = 10
b = 3

print(a + b)  # Output: 13
print(a - b)  # Output: 7
print(a * b)  # Output: 30
print(a / b)  # Output: 3.333...
print(a % b)  # Output: 1
print(a ** b) # Output: 1000
print(a // b) # Output: 3
```

---

## Assignment Operators (অ্যাসাইনমেন্ট অপারেটর)

🔹 একটি ভেরিয়েবলে মান সংরক্ষণ বা পরিবর্তনের জন্য ব্যবহার করা হয়।

| অপারেটর | ব্যবহার | সমতুল্য |
|-----------|---------|---------|
| `=` | `a = b` | a = b |
| `+=` | `a += b` | a = a + b |
| `-=` | `a -= b` | a = a - b |
| `*=` | `a *= b` | a = a * b |
| `/=` | `a /= b` | a = a / b |
| `%=` | `a %= b` | a = a % b |
| `**=` | `a **= b` | a = a ** b |
| `//=` | `a //= b` | a = a // b |

### **উদাহরণ:**
```python
# Simple Assignment
x = 10
print("Initial Value of x:", x)  # Output: 10

# Addition Assignment
x += 5  # x = x + 5
print("After x += 5:", x)  # Output: 15

# Subtraction Assignment
x -= 3  # x = x - 3
print("After x -= 3:", x)  # Output: 12

# Multiplication Assignment
x *= 2  # x = x * 2
print("After x *= 2:", x)  # Output: 24

# Division Assignment
x /= 4  # x = x / 4
print("After x /= 4:", x)  # Output: 6.0

# Modulus Assignment
x %= 5  # x = x % 5
print("After x %= 5:", x)  # Output: 1.0

# Exponentiation Assignment
x **= 3  # x = x ** 3
print("After x **= 3:", x)  # Output: 1.0

# Floor Division Assignment
x //= 1  # x = x // 1
print("After x //= 1:", x)  # Output: 1.0
```
### Output:
```
8
```
---
## **Comparison Operators (তুলনামূলক অপারেটর)**

Comparison Operators দিয়ে আমরা দুটি value বা variable-কে তুলনা করি। যেমন:

| অপারেটর | বর্ণনা | উদাহরণ |
|---------|--------|--------|
| `==` | সমান | `a == b` |
| `!=` | অসমান | `a != b` |
| `>` | বড় | `a > b` |
| `<` | ছোট | `a < b` |
| `>=` | বড় বা সমান | `a >= b` |
| `<=` | ছোট বা সমান | `a <= b` |

### **উদাহরণ:**
```python
x = 5
y = 10

print(x == y)  # Output: False
print(x != y)  # Output: True
print(x > y)   # Output: False
print(x < y)   # Output: True
print(x >= y)  # Output: False
print(x <= y)  # Output: True
```

---

## **Logical Operators (লজিক্যাল অপারেটর)**

Logical Operators দিয়ে আমরা একাধিক condition-কে যুক্ত করতে পারি। যেমন:

| অপারেটর | বর্ণনা | উদাহরণ |
|---------|--------|--------|
| `and` | উভয় condition সত্য হলে True | `a and b` |
| `or` | যেকোনো একটি condition সত্য হলে True | `a or b` |
| `not` | condition-এর বিপরীত মান রিটার্ন করে | `not a` |

### **উদাহরণ:**
```python
p = True
q = False

print(p and q)  # Output: False
print(p or q)   # Output: True
print(not p)    # Output: False
```

---

## **Practical Example (প্র্যাকটিক্যাল উদাহরণ)**

এখন চলুন একটি Practical Example দেখি যেখানে আমরা সব ধরণের Operators ব্যবহার করবো।

```python
num1 = 15
num2 = 7

# Arithmetic
sum_result = num1 + num2
print("Sum:", sum_result)

# Comparison
is_greater = num1 > num2
print("Is num1 greater than num2?", is_greater)

# Logical
check = (num1 > 10) and (num2 < 10)
print("Both conditions true?", check)
```

### **Output:**
```
Sum: 22
Is num1 greater than num2? True
Both conditions true? True
```

---

## **Today's Challenge! 🎯**

✅ নিচের কোডটি রান করুন এবং আউটপুট পর্যবেক্ষণ করুন:

```
🧮 Write a Python Programme to make your own Calculator.
```


📢 **কমেন্টে জানান, আপনি সফলভাবে কোড রান করতে পেরেছেন কিনা!** 💬

---

## **Next Topic: Conditional Statements in Python!**
🔔 **তাই, ভিডিওটি লাইক করুন, কমেন্ট করুন, এবং চ্যানেলটি সাবস্ক্রাইব করুন!** 🚀

👉 **CodeWithTanim - 100 Days of Python 🚀**

--- 

**End of README.md**