# Greeting using function on user name and age 
name = input("Enter your name: ")
age = int(input("Enter your age: "))
message = "Have a good day" #default message

def make_card(name, age): 
    return f"Hello {name}, ({age} years old)!\n{message}"

print(make_card(name, age))