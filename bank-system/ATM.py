balance = 10000
pin = "4321"
attempts = 3

def login():
    global attempts
    while attempts > 0:
        enter_pin = input("Enter PIN: ")
        if enter_pin == pin:
            print(" Access granted, welcome!")
            return True
        else:
            attempts -= 1
            print(" Incorrect PIN. Attempts left:", attempts)
    print(" You are blocked.")
    return False


def show_balance():
    print(" Your balance is:", balance)


def deposit():
    global balance
    amount = float(input("Enter amount: "))
    if amount > 0:
        balance += amount
        print(" Deposit successful. New balance:", balance)
    else:
        print(" Invalid amount.")


def withdraw():
    global balance
    amount = float(input("Enter amount: "))
    if amount <= 0:
        print(" Invalid amount.")
    elif amount > balance:
        print(" Not enough money.")
    else:
        balance -= amount
        print(" Withdrawal successful. New balance:", balance)


def menu():
    while True:
        
        print("1. Check balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Exit")

        choice = input("Choose operation: ")

        if choice == '1':
            show_balance()
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdraw()
        elif choice == '4':
            print(" Thank you for choosing our bank!")
            break
        else:
            print(" Invalid option, try again.")



if login():
    menu()
