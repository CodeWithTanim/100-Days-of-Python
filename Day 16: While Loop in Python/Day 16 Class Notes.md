
# Python Programming - Day 15: While Loops

## **While Loops**  ( **যতক্ষণ লুপ**  )

## **Introduction**  
**100 Days of Python** সিরিজের ১৫তম দিনে স্বাগতম! আজকের ভিডিওতে আমরা শিখবো:  
- **While Loop** কী এবং কেন ব্যবহার করা হয় 🔄  
- While Loop-এর সিনট্যাক্স এবং ব্যবহারের নিয়ম 📜  
- **Infinite Loop** এড়ানোর টিপস 🚫  
- রিয়েল-লাইফ উদাহরণ সহ প্র্যাকটিকাল কোডিং 🎮  

---

## **While Loop কি?**  
While Loop হলো Python-এর একটি কন্ডিশন-বেসড লুপ, যেটা **যতক্ষণ** শর্ত সত্য (True) থাকে, ততক্ষণ কোড ব্লক রিপিট করে। বাংলায় বললে—*"যতক্ষণ মা ডাক দেয়নি, ততক্ষণ ভাই ফোনে বেসুরে গান গাইতে থাকো!"* 🎤  

### **সিনট্যাক্স:**  
```python  
while condition:  
    # code to execute  
```  

### **উদাহরণ (Countdown):**  
```python  
count = 5  
while count > 0:  
    print(f"Countdown: {count}")  
    count -= 1  
print("Blastoff! 🚀")  
```  
**আউটপুট:**  
```  
Countdown: 5  
Countdown: 4  
Countdown: 3  
Countdown: 2  
Countdown: 1  
Blastoff! 🚀  
```  

---

## **Infinite Loop: ভয়ঙ্কর কিন্তু মজার!**  
যদি লুপের **কন্ডিশন কখনো False না হয়**, তখন লুপ চলতেই থাকে—এটাই Infinite Loop!  
```python  
# ⚠️ সাবধান! এই কোড রান করাবেন না!  
while True:  
    print("আমি আটকে গেছি! 😱")  
```  

### **Infinite Loop এড়ানোর উপায়:**  
- লুপের ভিতরে **ভ্যারিয়েবল আপডেট** করুন।  
- **Break** স্টেটমেন্ট ব্যবহার করুন।  

---

## **প্র্যাকটিকাল উদাহরণ: Guess the Number**  
```python  
secret = 7  
guess = 0  

while guess != secret:  
    guess = int(input("1-10 এর মধ্যে সংখ্যা ধরুন: "))  
    if guess != secret:  
        print("ভুল! আবার চেষ্টা করুন! 😜")  

print("জিনিয়াস! আপনি জিতে গেছেন! 🎉")  
```  
**আউটপুট:**  
```  
1-10 এর মধ্যে সংখ্যা ধরুন: 5  
ভুল! আবার চেষ্টা করুন! 😜  
1-10 এর মধ্যে সংখ্যা ধরুন: 7  
জিনিয়াস! আপনি জিতে গেছেন! 🎉  
```  

---

## **Today's Challenge! 🎯**  
**Mission:** একটি While Loop লিখুন যেটা **1-100 পর্যন্ত জোড় সংখ্যা প্রিন্ট করে**।  

```python  
# আপনার কোড এখানে লিখুন  
num = 1  
while num <= 100:  
    if num % 2 == 0:  
        print(num)  
    num += 1  
```  
📢 **কমেন্টে জানান, আপনি কয়টি জোড় সংখ্যা পেয়েছেন!** 💬  

---

**চ্যানেলটি সাবস্ক্রাইব করুন, বেল আইকন টিপুন, এবং Python-এর সাথে থাকুন!** 🐍  
**Happy Coding!** ❤️  
```  
