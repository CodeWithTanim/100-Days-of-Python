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