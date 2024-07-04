balance = 10000

while True:
    print("\nMenu:")
    print("1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        print(f"Your current balance is: Ksh.{balance}")
        break

    
    elif choice == '2':
        deposit_amount = float(input("Enter amount: Ksh. "))
        balance += deposit_amount
        print(f"You have successfully deposited Ksh.{deposit_amount}. Your new balance is: Ksh.{balance}. Thank you for using our service")
        break
    
    elif choice == '3':
        withdraw_amount = float(input("Enter amount to withdraw: Ksh. "))
        if withdraw_amount <= balance:
            balance -= withdraw_amount
            print(f"You have successfully withdrawn Ksh.{withdraw_amount}. Your new balance is: Ksh.{balance}. Thank you for using our service")
        else:
            print("Insufficient balance. Withdrawal denied.")
        break
    
    elif choice == '4':
        print("Thank you for using our service. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")