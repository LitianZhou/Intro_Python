right_pin = 1234
saving = 0.0
checking = 0.0
# control everything, not much complex structure like a while loop
def main():
    contin = 1
    stop = False
    pin_number = input("Welcome, please enter pin: ")
    while not is_authorized(int(pin_number)) and stop == False:
        pin_number = input("enter pin: ")
        if int(pin_number) == 0:
            stop = True

    while contin == 1 and is_authorized(int(pin_number)):
        print("This is a start of an operation")
        choice = show_menu()

        if choice == 1:
            check_amount()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        contin = int(input("1 for continue, 0 for stop: "))
    print("Thanks for using my ATM, goodbye!")

def show_menu():
    print("----------menu----------")
    print("[1] check amount")
    print("[2] deposit")
    print("[3] withdraw")
    choice = int(input("enter choice: "))

    return choice

def is_authorized(pin_number):
    if pin_number == right_pin:
        return True
    elif pin_number == 0:
        print("Exiting...")
    else:
        print("Wrong pin, please input again")
        return False

def check_amount():
    print("checking: " + str(checking))
    print("saving: " + str(saving))

def deposit():
    global checking
    global saving
    account = int(input("Deposit in checking or saving? 1 for checking, 2 for saving: "))
    amount = float(input("Deposit amount: "))
    if account == 1:
        checking += amount
    elif account == 2:
        saving += amount
    else:
        print("invalid account number, start over")


def withdraw():
    global checking
    global saving
    account = int(input("Withdraw from saving or checking? 1 for deposit, 2 for saving: "))
    amount = float(input("Withdraw amount: "))
    if account == 1:
        if checking >= amount:
            checking -= amount
        else:
            print("Error, you do not have that much money")
    elif account == 2:
        if saving >= amount:
            saving -= amount
        else:
            print("Error, you do not have that much money")
    else:
        print("invalid account number, start from the beginning...")

main()