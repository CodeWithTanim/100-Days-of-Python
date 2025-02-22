secret_number = 7
guess = 0

while guess != secret_number:
    guess = int(input("Guess between 1-10: "))
    if guess != secret_number:
        print("Wrong! Try again!")
print("You're a genius!")