import regex
import pandas as pd
import datetime
import os

# List to store expenses
expenses = []


# validate date
def validate_date(date_string):
    try:
        # parse the date
        valid_date = datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        # if date is invalid
        return False


# add expenses
def input_expense():

    global expenses
    while True:

        while True:
            date = input("Enter the date of the expense in YYYY-MM-DD: ")
            if regex.match(r"\d{4}-\d{2}-\d{2}", date):
                if validate_date(date):
                    break
                else:
                    print("Invalid date. Please enter valid date in YYYY-MM-DD")
            else:
                print("Invalid date format. Please enter the date in YYYY-MM-DD")

            # Validate the category
        while True:
            category = input("Enter the category of the expense (Food or Travel): ")
            if category in ['Food', 'Travel']:
                break
            else:
                print("Invalid category. Please enter Food or Travel.")

            # Validate the amount
        while True:
            try:
                amount = float(input("Enter the amount spent: "))
                break
            except ValueError:
                print("Invalid amount. Please enter a valid amount.")

            # Validate the description
        while True:
            description = input("Enter a brief description of the expense (max 100 characters): ")
            if len(description) <= 100:
                break
            else:
                print("Description is too long. Please enter a description with a maximum of 100 characters.")

        # Store the expense in a dictionary
        expense = {
            'date': date,
            'category': category,
            'amount': amount,
            'description': description
        }

        # Add the expense to the list
        expenses.append(expense)
    
        # ask the user for another expense
        additionalexpense = input("Expense added. Do you want to add another expense(Y/N)")
        if additionalexpense != 'Y':
            print("Exiting expense entry.")
            # Return the list of expenses
            return expenses


# View Expenses
def view_expense():
    i = 0
    for expense in expenses:
        i += 1
        desc = expense["description"];
        if desc == "":
            print(f"Expense No.: {i} missing required details, Skipping it")
        else:
            print(f"Expense No.: {i} - {expense}")


# Function to set the monthly budget
def set_monthly_budget():
    while True:
        try:
            budget = float(input("Enter the total amount you want to budget for the month: "))
            return budget
        except ValueError:
            print("Please enter a valid number.")


# Function to track expenses and compare with the budget
def track_budget():

    budget = set_monthly_budget()
    total_amount = 0;

    # for loop to iterate through expenses and get total amount
    for expense in expenses:
        total_amount += expense["amount"];

    # Check if the expenses exceed the budget
    if total_amount > budget:
        exceeded = total_amount - budget
        print(f"Warning: You have exceeded your budget by: {exceeded} !!")
    else:
        remaining_balance = budget - total_amount
        print(f"You have {remaining_balance} left for the month.")


# Function to save expenses to a CSV file using pandas
def save_expenses():
    filename = "expenses.csv"
    df = pd.DataFrame(expenses)  # Convert the list of expenses to a DataFrame
    df.to_csv(filename, index=False)  # Save DataFrame to CSV without index
    file_path = os.path.abspath(filename)
    print(f"Expenses saved to {file_path}")


# Function to load expenses from a CSV file using pandas
def load_expenses():
    filename = "expenses.csv"
    try:
        global expenses
        df = pd.read_csv(filename)  # Load the CSV file into a DataFrame
        expenses = df.to_dict('records')  # Convert DataFrame to a list of dictionaries
        file_path = os.path.abspath(filename)
        print(f"Expenses loaded from {file_path}")
    except FileNotFoundError:
        print("No previous expenses found.")


# Main menu function
def main():
    load_expenses()

    while True:
        print("\nMenu:")
        print("1. Add an Expense")
        print("2. View Expenses")
        print("3. Track Budget")
        print("4. Save Expenses")
        print("5. Save and Exit")

        try:
            choice = int(input("Enter the number of your choice: "))
        except ValueError:
            print("Invalid choice. Please enter a number from 1 to 5.")
            continue

        if choice == 1:
            input_expense()
        elif choice == 2:
            view_expense()
        elif choice == 3:
            track_budget()
        elif choice == 4:
            save_expenses()
        elif choice == 5:
            save_expenses()
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == '__main__':
    main()


