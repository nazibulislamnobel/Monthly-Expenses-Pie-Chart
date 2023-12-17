import matplotlib.pyplot as plt

def main():
    categories = ["Rent", "Gas", "Food", "Clothing", "Car Payment", "Misc"]
    expenses = []

    print("Enter the expenses for last month in the following categories:")
    
    for category in categories:
        expense = float(input(f"{category}: "))
        expenses.append(expense)

    plt.figure(figsize=(8, 8))
    plt.pie(expenses, labels=categories, startangle=140)
    plt.axis('equal')

    plt.title("Monthly Expenses")
    plt.show()

if __name__ == "__main__":
    main()