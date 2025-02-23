fruits = ["apple", "banana", "cherry", "damaged", "mango"]

for fruit in fruits:
    if fruit == "damaged":
        print("Stopping processing!")
        break
    if fruit == "banana":
        print("Skipping banana!")
        continue
    print(f"Processing: {fruit}")