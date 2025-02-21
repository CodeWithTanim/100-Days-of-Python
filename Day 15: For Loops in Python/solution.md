# Python Programming - Day 15: For Loop Challenge Solution

## **Problem Statement**
**প্রবলেম:** ১ থেকে ১০০ পর্যন্ত জোড় সংখ্যাগুলোর যোগফল বের করুন For Loop ব্যবহার করে।  
**Hint:** `range(start, end, step)` এর ৩য় প্যারামিটার ব্যবহার করুন!

---

## **Solution Code**
```python
total = 0  
for number in range(2, 101, 2):  # Start=2, End=101 (exclusive), Step=2  
    total += number  
print("Sub of 1 to 100 Even Numbers:", total)  
```

**আউটপুট:**
```
Sub of 1 to 100 Even Numbers: 2550
```

---

## **Explanation**
### **How It Works:**
1. **`range(2, 101, 2)`**:
   - **Start**: ২ থেকে শুরু (প্রথম জোড় সংখ্যা)।  
   - **End**: ১০১ পর্যন্ত (১০১ এক্সক্লুসিভ, মানে ১০০ পর্যন্ত)।  
   - **Step**: ২ করে বাড়বে (২, ৪, ৬, ..., ১০০)।  
2. **For Loop**:
   - প্রতিটি জোড় সংখ্যা `number` ভেরিয়েবলে ধরে `total`-এর সাথে যোগ করা হয়।  
3. **Final Output**:
   - লুপ শেষে `total`-এ জোড় সংখ্যাগুলোর যোগফল জমা হয়, যা প্রিন্ট করা হয়।

---

### **Mathematical Verification**
জোড় সংখ্যাগুলোর যোগফল গাণিতিকভাবে বের করা যায়:  
- **n = 50** (মোট জোড় সংখ্যা ১ থেকে ১০০ পর্যন্ত)।  
- **Sum = n * (first + last) / 2**  
  `= 50 * (2 + 100) / 2`  
  `= 50 * 51`  
  `= 2550`  

---

## **How to Run the Code**
1. Python ইনস্টল করা থাকলে, কোডটি কপি করে আপনার Python IDE বা কোড এডিটরে পেস্ট করুন।  
2. রান করুন এবং আউটপুট দেখুন।  

---

## **Challenge for You!**
- **Modify the Code:** বিজোড় সংখ্যাগুলোর যোগফল বের করুন For Loop ব্যবহার করে।  
- **Hint:** `range(1, 101, 2)` ব্যবহার করুন!  

---

**ভালো লেগে থাকলে ভিডিওটি শেয়ার করুন, লাইক করুন, এবং চ্যানেলটি সাবস্ক্রাইব করুন!** 🚀  
**Happy Coding!** 💻
