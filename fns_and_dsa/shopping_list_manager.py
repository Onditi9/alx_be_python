shopping_list = []
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Shopping List")
    print("4. Exit")

def add_item():
    item = input("Enter the item to add: ").strip()
    if item:
        shopping_list.append(item)
        print(f"{item} added to shopping list.")
    else:
        print("Item name cannot be empty.")

def remove_item():
    item = input("Enter the item to remove: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed from shopping list.")
    else:
        print(f"{item} not found in shopping list.")

def view_list():
    if shopping_list:
        print("Shopping List:")
        for i, item in enumerate(shopping_list, start=1):
            print(f"{i}. {item}")
    else:
        print("Your shopping list is empty.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()
        if choice == '1':
            add_item()
        elif choice == '2':
            remove_item()
        elif choice == '3':
            view_list()
        elif choice == '4':
            print("Exiting Shopping List Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()