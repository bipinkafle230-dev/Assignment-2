# scope of variable

number = 10
print("Initial value of global variable:", number)

def my_function():
    global number 
    number1 = 5   # local variable
    print("Local variable:", number1)
    number= 20  # modify global variable

my_function()

print("Final value of global variable:", number)

