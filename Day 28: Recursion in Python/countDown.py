def countdown(num):
    if num <= 0:  # Base Case
        print("Blastoff! 🚀")
    else:
        print(num)
        countdown(num - 1)

countdown(5)