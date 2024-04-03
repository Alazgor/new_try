import pickle
import os

def load_data():
    if os.path.exists("budget.pkl"):
        with open("budget.pkl", "rb") as file:
            return pickle.load(file)
    else:
        return {"income": [], "expenses": []}

def save_data(data):
    with open("budget.pkl", "wb") as file:
        pickle.dump(data, file)

def add_income(amount, data):
    data["income"].append(amount)

def add_expense(amount, data):
    data["expenses"].append(amount)

def calculate_balance(data):
    total_income = sum(data["income"])
    total_expenses = sum(data["expenses"])
    return total_income - total_expenses

def display_balance(data):
    print("Income:")
    for income in data["income"]:
        print(f"+ {income}")
    print("Expenses:")
    for expense in data["expenses"]:
        print(f"- {expense}")
    print(f"Balance: {calculate_balance(data)}")

def main():
    data = load_data()
    while True:
        print("\n1. Add income")
        print("2. Add expense")
        print("3. Display balance")
        print("4. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            amount = float(input("Enter income amount: "))
            add_income(amount, data)
        elif choice == "2":
            amount = float(input("Enter expense amount: "))
            add_expense(amount, data)
        elif choice == "3":
            display_balance(data)
        elif choice == "4":
            save_data(data)
            print("Data saved. Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
