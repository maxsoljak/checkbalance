balance = 0

def get_choice():
    print("1 check balance")
    print("2 Deposit")
    print("3 Withdraw")
    
    try:
        choice = int(input("Enter a number:"))
    except ValueError:
        print("That's not a number.")
        return get_choice()
    
    if choice < 0 or choice > 3:
        print("Thats not a valid number.")
        return get_choice()
    
    return choice

def check_balance():
    
print("Your balance is:", balance)
    choice = get_choice()

