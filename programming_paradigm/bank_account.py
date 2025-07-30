import sys
from bank_account import BankAccount

def print_usage():
    print("Usage:")
    print("  python main-0.py deposit <amount>")
    print("  python main-0.py withdraw <amount>")
    print("  python main-0.py balance")

def main():
    if len(sys.argv) < 2:
        print("Error: Missing operation.")
        print_usage()
        return

    account = BankAccount()

    operation = sys.argv[1].lower()

    if operation == "deposit":
        if len(sys.argv) != 3:
            print("Error: Deposit requires an amount.")
            print_usage()
            return
        amount = float(sys.argv[2])
        account.deposit(amount)
        print(f"Deposited ${amount:.2f}")
        account.display_balance()

    elif operation == "withdraw":
        if len(sys.argv) != 3:
            print("Error: Withdraw requires an amount.")
            print_usage()
            return
        amount = float(sys.argv[2])
        success = account.withdraw(amount)
        if success:
            print(f"Withdrew ${amount:.2f}")
        else:
            print("Insufficient funds. Withdrawal failed.")
        account.display_balance()

    elif operation == "balance":
        account.display_balance()

    else:
        print(f"Error: Unknown operation '{operation}'")
        print_usage()

if __name__ == "__main__":
    main()