# List to store all bank accounts (each account is a dictionary)
accounts = []

# Get the number of accounts the user wants to create
num_account = int(input("How many accounts do you want to open? "))

# Loop to collect information for each account
for i in range(num_account):
    print(f"account informaition {i + 1} : ")
    name = input("\nPlease enter the account owner's name. :")

    # Get initial balance with validation (non-negative and valid number)
    while True:
        try:
            balance = float(input("Initial balance : "))
            print("---------------------------------------")

            if balance < 0:
                print("The number cannot be negative.!")
                continue
            break
        except ValueError as e:
            print("Please enter a valid value." , e)

    accounts.append({"name" : name , "balance" : balance})

# Main menu loop - keeps running until the user chooses to exit
while True:
    print("========== Banking operations menu ==========")
    print("1 .Show balance of all accounts")
    print("2 .Deposit into account")
    print("3 .Withdrawal from the account")
    print("4 .Show accounts with higher than average balances")
    print("5 .Exit")
    print("=============================================")

    chose = int(input("\nPlease select the desired option : "))

    # Option 1: Display all accounts and their balances
    if chose == 1:
        print("Accounts informaition")
        for acc in accounts:
            print(f"{acc['name']} : {acc['balance']} Toman \n")
    
    # Option 2: Deposit money into a specific account
    elif chose == 2 :
        name = input("Account Name :")
        found = False
        
        for acc in accounts:
            if acc['name'] == name:
                found = True
                while True:
                    try:
                        amount = float(input("Deposit amount :"))

                        if amount < 0:
                            print("The deposit amount cannot be negative!!")
                            continue
                        acc['balance'] += amount
                        print(f"{acc['name']} : {acc['balance']} Toman")
                        break
                    except ValueError as e:
                        print("Please enter a valid value." , e)
                    
        if not found:
            print("No account with this name found.")
    
    # Option 3: Withdraw money from a specific account
    elif chose == 3:
        name = input("Account Name :")
        found = False

        for acc in accounts:
            if acc['name'] == name:
                found = True
                while True:
                    try:
                        amount = float(input("withdrawal amount : "))

                        if amount < 0:
                            print("The deposit amount cannot be negative!!")
                            continue
                        elif amount > acc['balance']:
                            print("Low balance!!")
                            continue
                        acc['balance'] -= amount
                        print(f"{acc['name']} : {acc['balance']} Toman")
                        break

                    except ValueError as e:
                        print("Please enter a valid value." , e)
                    
                    
        if not found:
            print("No account with this name found.")
    
    # Option 4: Show accounts with balance above the average
    elif chose == 4:
        
        total_balance = sum(acc['balance'] for acc in accounts)
        avg_balance = total_balance / len(accounts)
        print(f"\nAverage accounts balance : {avg_balance :.2f} ")
        print("Accounts with higher than average balances : \n")
        for acc in accounts:
            if acc['balance'] > avg_balance:
                print(f"{acc['name']} : {acc['balance']} Toman")

    # Option 5: Exit the program
    elif chose == 5 :
        print("Byeee :)")
        break
    # Invalid menu choice
    else:
        print("Please select a valid option. Try again")

    # Ask user to return to menu; exit if answer is not 'y'        
    if chose in [1, 2, 3, 4]:
        back = input("\nDo you want to return to the menu? (Y/N): ").strip().lower()
        if back != 'y':
            print("Byeee :)")
            break

