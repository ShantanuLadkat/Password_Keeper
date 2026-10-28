while True:

    choice = input("Enter your choice: ")

    if choice == "1":
        account = input("Enter account name: ")
        password = input("Enter password: ")

        passwords[account] = password
        print("Password saved successfully.")

    elif choice == "2":
        account = input("Enter account name to search: ")

        if account in passwords:
            print("Password:", passwords[account])
        else:
            print("Account not found.")

    elif choice == "3":
        if len(passwords) == 0:
            print("No accounts saved.")
        else:
            print("\nSaved Accounts and Passwords:")
            for account in passwords:
                print(account, ":", passwords[account])

    elif choice == "4":
        account = input("Enter account name to delete: ")

        if account in passwords:
            del passwords[account]
            print("Account deleted successfully.")
        else:
            print("Account not found.")

    elif choice == "5":
        print("Thank you for using Password Keeper.")
        break

    else:
        print("Invalid choice. Please try again.")