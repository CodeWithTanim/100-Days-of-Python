# Example 1: Basic Match Case
def check_number(num):
    match num:
        case 1:
            return "You entered One"
        case 2:
            return "You entered Two"
        case 3:
            return "You entered Three"
        case _:
            return "You entered something else!"

# Testing the function
print(check_number(9))  # Output: You entered Two
print(check_number(1))  # Output: You entered something else!