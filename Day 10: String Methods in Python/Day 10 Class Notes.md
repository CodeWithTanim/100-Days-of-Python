# Python Programming - Day 10: String Methods in Python

## **String Methods in Python**

### **Introduction**
স্বাগতম **100 Days of Python** সিরিজের ১০ম দিনে! আজকের ভিডিওতে আমরা শিখবো Python-এ **String Methods** সম্পর্কে। String Methods ব্যবহার করে আমরা Strings কে সহজেই ম্যানিপুলেট করতে পারি। যেমন: uppercase বা lowercase করা, whitespace remove করা, বা কোনো সাবস্ট্রিং খুঁজে বের করা।

---

## **String Methods in Python**

Python-এ Strings নিয়ে কাজ করার জন্য অনেক built-in মেথড রয়েছে। আজ আমরা কিছু গুরুত্বপূর্ণ মেথড শিখবো:

| মেথড | বর্ণনা | উদাহরণ |
|-------|--------|--------|
| `len()` | স্ট্রিংয়ের দৈর্ঘ্য (length) রিটার্ন করে | `len("Python")` → `6` |
| `upper()` | স্ট্রিংকে uppercase এ কনভার্ট করে | `"hello".upper()` → `"HELLO"` |
| `lower()` | স্ট্রিংকে lowercase এ কনভার্ট করে | `"HELLO".lower()` → `"hello"` |
| `strip()` | স্ট্রিংয়ের শুরু ও শেষের whitespace মুছে দেয় | `"  Python  ".strip()` → `"Python"` |
| `replace()` | স্ট্রিংয়ের কোনো অংশ অন্য টেক্সট দিয়ে প্রতিস্থাপন করে | `"I love Java".replace("Java", "Python")` → `"I love Python"` |
| `split()` | স্ট্রিংকে নির্দিষ্ট separator দিয়ে ভেঙে লিস্টে কনভার্ট করে | `"Python,Java,C++".split(",")` → `['Python', 'Java', 'C++']` |
| `startswith()` | স্ট্রিংটি নির্দিষ্ট টেক্সট দিয়ে শুরু হয়েছে কিনা চেক করে | `"https://codewithtanim.com".startswith("https")` → `True` |
| `endswith()` | স্ট্রিংটি নির্দিষ্ট টেক্সট দিয়ে শেষ হয়েছে কিনা চেক করে | `"file.txt".endswith(".txt")` → `True` |
| `find()` | সাবস্ট্রিংয়ের ইনডেক্স রিটার্ন করে (খুঁজে না পেলে -1 রিটার্ন করে) | `"Hello World".find("World")` → `6` |
| `count()` | সাবস্ট্রিং কতবার স্ট্রিংয়ে আছে তা রিটার্ন করে | `"Python is awesome, Python is easy".count("Python")` → `2` |

---

## **উদাহরণ সহ ব্যাখ্যা**

### **1. len()**
```python
text = "Code With Tanim"
print(len(text))  # আউটপুট: 14
```

### **2. upper() ও lower()**
```python
text = "Hello Python"
print(text.upper())  # আউটপুট: "HELLO PYTHON"
print(text.lower())  # আউটপুট: "hello python"
```

### **3. strip()**
```python
text = "   Python is fun!   "
print(text.strip())  # আউটপুট: "Python is fun!"
```

### **4. replace()**
```python
text = "I love Java"
new_text = text.replace("Java", "Python")
print(new_text)  # আউটপুট: "I love Python"
```

### **5. split()**
```python
text = "Python,Java,C++"
print(text.split(","))  # আউটপুট: ['Python', 'Java', 'C++']
```

### **6. startswith() ও endswith()**
```python
url = "https://www.github.com"
print(url.startswith("https"))  # আউটপুট: True
print(url.endswith(".bd"))  # আউটপুট: False
```

### **7. find()**
```python
text = "Hello World"
print(text.find("World"))  # আউটপুট: 6
```

### **8. count()**
```python
text = "Python is awesome, Python is easy"
print(text.count("Python"))  # আউটপুট: 2
```

---

## **Today's Challenge! 🎯**
✅ নিচের কোডটি রান করুন এবং আউটপুট পর্যবেক্ষণ করুন:
```python
text = "  Python Programming is Fun!  "
# Challenge:
# 1. Remove extra whitespace
# 2. Convert to uppercase
# 3. Replace "Fun" with "Awesome"
# 4. Count how many times "Python" appears in the string
```

📢 **কমেন্টে জানান, আপনি সফলভাবে কোড রান করতে পেরেছেন কিনা!** 💬

---

## **Next Topic: If Else Coditional Statements in Python**
🔔 **তাই, ভিডিওটি লাইক করুন, কমেন্ট করুন, এবং চ্যানেলটি সাবস্ক্রাইব করুন!** 🚀

👉 **CodeWithTanim - 100 Days of Python 🚀**

---

**[Note:]**  
- Strings immutable (অপরিবর্তনীয়)। তাই কোনো মেথড সরাসরি মূল স্ট্রিংকে পরিবর্তন করে না, বরং নতুন স্ট্রিং রিটার্ন করে।  
- Strings নিয়ে আরও গভীরভাবে আলোচনা করা হবে পরবর্তী ভিডিওতে।  

--- 

**Happy Coding! 😊**