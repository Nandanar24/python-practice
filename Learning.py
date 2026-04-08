name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello {name}!")
if age < 13:
    print("You are a child")
elif age < 18:
    print("You are a teen")
else:
    print("You are an adult")