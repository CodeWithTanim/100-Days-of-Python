
# Exercise 1: Greeting Machine | Python Tutorial - Day #12  

## **আজকের টপিক: সময় অনুযায়ী গ্রিটিং মেসেজ**  

### **প্রোজেক্টের লক্ষ্য**  
এমন একটি Python প্রোগ্রাম বানানো যেটা বর্তমান সময় চেক করে আপনাকে স্বয়ংক্রিয়ভাবে **Good Morning**, **Good Afternoon**, বা **Good Evening** বলে দেবে!  

---

## **Time মডিউল: সময়ের সাথে খেলা**  
Python-এর `time` মডিউল ব্যবহার করে আমরা বর্তমান সময়ের হিসেব পাবো।  

### **কোড স্নিপেট:**  
```python
import time  
current_hour = int(time.strftime("%H"))  # 24-hour ফরম্যাটে ঘণ্টা (০-২৩)
print("Now Time is:", current_hour)
```  
🔹 **`%H`**: 24-ঘণ্টা ফরম্যাটে বর্তমান ঘণ্টা রিটার্ন করে।  
🔹 **`%M`**: মিনিট।  
🔹 **`%S`**: সেকেন্ড।  

---

## **গ্রিটিং লজিক**  
সময় অনুযায়ী শর্ত (`if-elif-else`) সেট করুন:  

| সময় রেঞ্জ       | গ্রিটিং মেসেজ                  | ইমোজি |
|------------------|--------------------------------|--------|
| 4 AM – 12 PM     | Good Morning! ☕               | 🌅     |
| 12 PM – 5 PM     | Good Afternoon! 🥪             | ☀️     |
| 5 PM – 9 PM      | Good Evening! 🌙               | 🌆     |
| 9 PM – 4 AM      | Late Night Coder Alert! 😴     | 🌃     |  

```python
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)

# https://docs.python.org/3/library/time.html#time.strftime
```


### **Solve কোড:**  
```python
import time

# বর্তমান সময় HH:MM:SS ফরম্যাটে প্রিন্ট করুন
timestamp = time.strftime('%H:%M:%S')
print("Now time is:", timestamp)

# ঘণ্টা, মিনিট, সেকেন্ড আলাদাভাবে প্রিন্ট করুন
timestamp = time.strftime('%H')
print("Hour:", timestamp)
current_hour = int(timestamp) # ইন্টিজারে কনভার্ট করুন

timestamp = time.strftime('%M')
print("Minute:", timestamp)

timestamp = time.strftime('%S')
print("Second:", timestamp)

# সময় অনুযায়ী গ্রিটিং লজিক
if 4 <= current_hour < 12:
    greeting = "Good Morning! ☕️"
elif 12 <= current_hour < 17:
    greeting = "Good Afternoon 🥪"
elif 17 <= current_hour < 21:
    greeting = "Good Evening 🌙"
else:
    greeting = "Now the Nightshift 😴"

print("\n" + greeting)
```  

---

## **ডেমো আউটপুট**  
```
Good Afternoon 🥪
Now Time is: 14:30:45
Hour: 14 
Minute: 30 
Second: 45
```

---

📢 **কমেন্টে জানান আপনার মেশিন কেমন কাজ করছে!**  

---


**Happy Coding!** 🚀  
