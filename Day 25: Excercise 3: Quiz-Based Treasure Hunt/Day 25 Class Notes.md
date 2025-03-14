# Python Programming - Day 25: Quiz-Based Treasure Hunt

## কুইজ-ভিত্তিক ট্রেজার হান্ট

### **পরিচিতি**
স্বাগতম **100 Days of Python** সিরিজের ২৫তম দিনে! আজকে আমরা তৈরি করবো এক রোমাঞ্চকর গেইম:

🔹 **লিস্ট** ব্যবহার করে মাল্টিপল চয়েস কুইজ সিস্টেম 📜  
🔹 সঠিক উত্তরে ভার্চুয়াল গোল্ড কয়েন জমা করা 💰  
🔹 ভুল উত্তরে কয়েন পেনাল্টি 😱  
🔹 গেইম শেষে টোটাল ট্রেজার দেখানো 🏆

---

## **প্রোগ্রাম রিকোয়ারমেন্টস**

### **মূল ধাপসমূহ:**
1. প্রশ্ন ও অপশন স্টোর করতে **লিস্টের মধ্যে লিস্ট** ব্যবহার করুন  
   ```python
   questions = [
       ["What is Python?", ["A. Snake", "B. Language", "C. OS"], "B"],
       # আরো প্রশ্ন যোগ করুন...
   ]
   ```

2. **কয়েন ট্র্যাকিং সিস্টেম**  
   - সঠিক উত্তরে +১০ কয়েন 🟡
   - ভুল উত্তরে -৫ কয়েন 🔴

3. **ইউজার ইন্টারঅ্যাকশন**  
   ```python
   user_ans = raw_input("আপনার উত্তর (A/B/C): ").upper()  # Python 3-এ input() ব্যবহার করুন
   ```

4. **গেইম সমাপ্তিতে ফাইনাল স্কোর**  
   ```python
   print("🏁 টোটাল ট্রেজার: {} কয়েন!".format(coins))
   ```

---

## **চ্যালেঞ্জ স্ট্রাকচার**

| কম্পোনেন্ট | বর্ণনা | উদাহরণ |
|------------|---------|---------|
| **প্রশ্ন স্টোরেজ** | নেস্টেড লিস্টে প্রশ্ন+অপশন+সঠিক উত্তর | `[Q1, [A,B,C], Ans]` |
| **স্কোরিং** | ডাইনামিক কয়েন ক্যালকুলেশন | `coins = coins + 10` |
| **ফিডব্যাক** | ইনস্ট্যান্ট রেসপন্স সিস্টেম | `print("✅ সঠিক! +" + str(reward) + " কয়েন!")` |
| **গেইম ফ্লো** | লুপ ব্যবহার করে সব প্রশ্ন দেখানো | `while question_no < total_questions:` |

---

## **আজকের চ্যালেঞ্জ! 🏴‍☠️**

```
Create a Python program that simulates a quiz-based treasure hunt. The program should display a series of multiple-choice questions stored using the list data type. Each correct answer allows the player to move forward and collect virtual gold coins, while an incorrect answer results in a penalty. At the end of the game, display the total treasure (coins) collected by the player.
```

**চ্যালেঞ্জ:**  
➤ প্রতিটি প্রশ্নের জন্য আলাদা কয়েন ভ্যালু সেট করুন  
➤ ইউজারকে ৩ বার চান্স দিন (৩ স্টেজের গেইম)  
➤ টাইমার যোগ করুন (ঐচ্ছিক) ⏳

---

**কোড কমপ্লিট করার পর:**  
📢 কমেন্টে লিখুন আপনার সর্বোচ্চ স্কোর!  
🐞 কোনো বাগ পেলে রিপোর্ট করুন - আমরা একসাথে ফিক্স করব!

---

**🎥 লাইক করুন ★ শেয়ার করুন 🔔 নোটিফিকেশন অন করুন**  
**🚀 CodeWithTanim - 100 Days of Python**