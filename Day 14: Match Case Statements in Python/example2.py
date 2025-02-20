# Example 2: Match Case with Patterns
def check_data(data):
    match data:
        case [name, age]:
            return f"Name: {name}, Age: {age}"
        case {"name": name, "age": age}:
            return f"Name: {name}, Age: {age}"
        case _:
            return "Unknown data format!"

# Testing the function
print(check_data(["Alice", 25]))  # Output: Name: Alice, Age: 25
print(check_data({"name": "Bob", "age": 30}))  # Output: Name: Bob, Age: 30
print(check_data("Hello, 50, 52"))  # Output: Unknown data format!