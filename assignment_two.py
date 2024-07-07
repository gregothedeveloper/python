balance = 10000

# Menu display
while True:
    print("\nMenu:")
    print("1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")

# Handling customers' choices
# Handling customers' balance choice

    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        print(f"Your current balance is: Ksh.{balance}")

# Handling customers' deposit choice

    elif choice == '2':
        deposit_amount = float(input("Enter amount to deposit: Ksh. "))
        if deposit_amount > 0:
            balance += deposit_amount
            print(f"Congratulations!, You have successfully deposited Ksh.{deposit_amount}. Your new balance is: Ksh.{balance}. Thank you for using our service.")
        else:
            print("Ooops!, Invalid deposit amount. Please enter a positive value.")

# Handling customers' withdrawal choice

    elif choice == '3':
        withdraw_amount = float(input("Enter amount to withdraw: Ksh. "))
        if withdraw_amount > 0:
            if withdraw_amount <= balance:
                balance -= withdraw_amount
                print(f"Congratulations!, You have successfully withdrawn Ksh.{withdraw_amount}. Your new balance is: Ksh.{balance}. Thank you for using our service.")
            else:
                print("Ooops!, Insufficient balance. Withdrawal denied.")
        else:
            print("Invalid withdrawal amount. Please enter a positive value.")

    # Handling customers'  exit choice

    elif choice == '4':
        print("Thank you for using our service. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")