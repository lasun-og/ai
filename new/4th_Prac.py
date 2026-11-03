
while True:
    print("\n===== BANK CHATBOT =====")
    print("1. Account Types")
    print("2. Loan Types")
    print("3. Card Types")
    print("4. Banking Services")
    print("5. Contact")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        print("\n--- Account Types ---")
        print("1. Savings Account")
        print("2. Current Account")
        print("3. Fixed Deposit Account")

        ch = input("Enter your choice: ")

        if ch == "1":
            print("Savings Account: Best for personal savings.")
            print("Minimum balance: Rs. 1000")
        elif ch == "2":
            print("Current Account: Suitable for business transactions.")
        elif ch == "3":
            print("Fixed Deposit Account: Offers interest for a fixed period.")
        else:
            print("Invalid choice!")

    elif choice == "2":
        print("\n--- Loan Types ---")
        print("1. Home Loan")
        print("2. Personal Loan")
        print("3. Education Loan")

        ch = input("Enter your choice: ")

        if ch == "1":
            print("Home Loan: Loan for purchasing a house.")
        elif ch == "2":
            print("Personal Loan: Loan for personal expenses.")
        elif ch == "3":
            print("Education Loan: Loan for education expenses.")
        else:
            print("Invalid choice!")

    elif choice == "3":
        print("\n--- Card Types ---")
        print("1. Debit Card")
        print("2. Credit Card")

        ch = input("Enter your choice: ")

        if ch == "1":
            print("Debit Card: Payments are made using your bank balance.")
        elif ch == "2":
            print("Credit Card: Allows you to borrow money up to a limit.")
        else:
            print("Invalid choice!")

    elif choice == "4":
        print("\n--- Banking Services ---")
        print("1. ATM")
        print("2. Mobile Banking")
        print("3. Internet Banking")

        ch = input("Enter your choice: ")

        if ch == "1":
            print("ATM: Cash withdrawal and balance inquiry.")
        elif ch == "2":
            print("Mobile Banking: Transfer funds and pay bills.")
        elif ch == "3":
            print("Internet Banking: Access banking services online.")
        else:
            print("Invalid choice!")

    elif choice == "5":
        print("\n--- Contact Details ---")
        print("Customer Care: 1800-123-4567")
        print("Email: support@bank.com")
        print("Working Hours: Monday to Saturday, 9 AM to 6 PM")

    elif choice == "6":
        print("Thank you for using the Bank Chatbot!")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 6.")
