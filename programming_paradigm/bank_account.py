import sys
from bank_account import BankAccount

account = BankAccount(initial_balance=100)

def main():
    if len(sys.argv) != 2:
        print("Usage: python main-0.py [deposit:<amount> | withdraw:<amount> | display]")
        return

    command = sys.argv[1]

    if command.startswith("deposit:"):
        try:
            amount = float(command.split(":")[1])
            if account.deposit(amount):
                print(f"Deposited: ${amount}")
            else:
                print("Invalid deposit amount.")
        except ValueError:
            print("Invalid amount for deposit.")

    elif command.startswith("withdraw:"):
        try:
            amount = float(command.split(":")[1])
            if account.withdraw(amount):
                print(f"Withdrew: ${amount}")
            else:
                print("Insufficient funds.")
        except ValueError:
            print("Invalid amount for withdrawal.")

    elif command == "display":
        account.display_balance()

    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()