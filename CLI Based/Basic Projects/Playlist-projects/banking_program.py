import time


def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")


def deposit():
    amount = float(input("Enter an amount to be deposited: "))
    if amount <= 0:
        print("Invalid amount! Amount must be greater than zero.")
        return 0
    else:
        return amount


def withdraw(balance):
    amount = float(input("Enter an amount to be withdrawn: "))

    if amount > balance:
        print("Insufficient balance!")
        return balance
    elif amount <= 0:
        print("Amount must be greater than zero.")
        return balance
    else:
        balance -= amount
        return balance


def main():
    balance = 0
    is_running = True

    while is_running:
        print("\n--- Banking Program ---")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("-----------------------\n")

        choice = int(input("Enter your choice (1-4): "))

        match choice:
            case 1:
                show_balance(balance)

            case 2:
                balance += deposit()

            case 3:
                balance = withdraw(balance)

            case 4:
                print("Exiting....")
                time.sleep(0.5)
                is_running = False

            case _:
                print("Invalid choice!")
                time.sleep(0.5)

    print("\nThank you!\n")
    time.sleep(0.5)


if __name__ == "__main__":
    main()