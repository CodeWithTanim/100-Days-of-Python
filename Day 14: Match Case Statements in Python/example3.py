# Example 3: Match Case with Conditions
def check_age(age):
    match age:
        case age if age < 18:
            return "You are a minor."
        case age if 18 <= age < 60:
            return "You are an adult."
        case age if age >= 60:
            return "You are a senior citizen."
        case _:
            return "Invalid age!"

# Testing the function
print(check_age(15))  # Output: You are a minor.
print(check_age(25))  # Output: You are an adult.
print(check_age(65))  # Output: You are a senior citizen.
print(check_age(-65))