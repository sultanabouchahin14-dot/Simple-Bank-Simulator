balance = 500

print("Welcome to My Bank")

print("1 - Check Balance")
print("2 - Deposit")
print("3 - Withdraw")
print("4 - Exit")

choice = input("Choose: ")

if choice == "1":
    print("Your balance is:", balance)

elif choice == "2":
    money = int(input("Enter money: "))
    balance = balance + money
    print("New balance:", balance)

elif choice == "3":
    money = int(input("Enter money: "))

    if money <= balance:
        balance = balance - money
        print("New balance:", balance)
    else:
        print("Not enough money")

elif choice == "4":
    print("Goodbye!")

else:
    print("Wrong choice")
