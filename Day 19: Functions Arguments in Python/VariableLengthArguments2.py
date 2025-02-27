def user_profile(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

user_profile(name="Bob", age=25, city="NYC")
user_profile(name="fgdfg", age=65, city="India")
user_profile(name="dfg", age=15, city="Dhaka")