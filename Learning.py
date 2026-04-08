password = input("Enter a password: ")
if len(password) < 5:
    print("Weak password 💀")
elif len(password) < 8:
    print("Okay password ")
else:
    print("Strong password ")