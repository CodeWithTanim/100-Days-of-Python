# import time  
# current_hour = int(time.strftime("%H"))  # 24-hour ফরম্যাটে ঘণ্টা (০-২৩)
# print("Now Time is:", current_hour)

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