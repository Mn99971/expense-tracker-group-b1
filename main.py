
from expenses import (
    add_expense,
    edit_expense,
    delete_expense,
    load_expenses,
    save_expenses,
)

from analysis import (
    calculate_total,
    total_by_category,
    largest_expense,
)

from budget import (
    set_budget,
    remaining_budget,
    is_over_budget,
)


def show_menu():
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Edit expense")
    print("4. Delete expense")
    print("5. Spending analysis")
    print("6. Budget management")
    print("0. Save and exit")


def analysis_menu(expenses):
    while True:
        print("\n===== SPENDING ANALYSIS =====")
        print("1. Total spending")
        print("2. Spending by category")
        print("3. Largest expense")
        print("0. Back to main menu")

        choice = input("\nChoose an option: ").strip()

        try:
            if choice == "1":
                total = calculate_total(expenses)
                print(f"Total spending: {total:.2f}")

            elif choice == "2":
                category = input("Category: ").strip()
                total = total_by_category(expenses, category)
                print(f"Spending in {category}: {total:.2f}")

            elif choice == "3":
                expense = largest_expense(expenses)

                if expense is None:
                    print("No expenses recorded.")
                else:
                    print(
                        f"#{expense['id']} | "
                        f"{expense['amount']:.2f} | "
                        f"{expense['category']} | "
                        f"{expense['description']}"
                    )

            elif choice == "0":
                break

            else:
                print("Invalid menu option.")

        except ValueError as error:
            print(f"Invalid input: {error}")


def budget_menu(expenses, budget):
    while True:
        print("\n===== BUDGET MANAGEMENT =====")
        print("1. Set budget")
        print("2. View remaining budget")
        print("3. Check if over budget")
        print("0. Back to main menu")

        choice = input("\nChoose an option: ").strip()

        try:
            if choice == "1":
                amount = float(input("Budget amount: "))
                budget = set_budget(amount)
                print(f"Budget set to: {budget:.2f}")

            elif choice == "2":
                if budget is None:
                    print("Please set a budget first.")
                else:
                    remaining = remaining_budget(budget, expenses)
                    print(f"Remaining budget: {remaining:.2f}")

            elif choice == "3":
                if budget is None:
                    print("Please set a budget first.")
                else:
                    if is_over_budget(budget, expenses):
                        print("You have exceeded your budget!")
                    else:
                        print("You are within your budget.")

            elif choice == "0":
                break

            else:
                print("Invalid menu option.")

        except ValueError as error:
            print(f"Invalid input: {error}")

    return budget


def main():
    expenses = load_expenses()
    budget = None

    while True:
        show_menu()
        choice = input("\nChoose an option: ").strip()

        try:
            if choice == "1":
                amount = float(input("Amount: "))
                category = input("Category: ").strip()
                description = input("Description: ").strip()

                expense_id = max(
                    (expense["id"] for expense in expenses),
                    default=0
                ) + 1

                add_expense(
                    expenses, expense_id,
                    amount, category, description
                )
                save_expenses(expenses)
                print("Expense added successfully!")

            elif choice == "2":
                if not expenses:
                    print("No expenses recorded.")
                else:
                    for expense in expenses:
                        print(
                            f"#{expense['id']} | "
                            f"{expense['amount']:.2f} | "
                            f"{expense['category']} | "
                            f"{expense['description']}"
                        )

            elif choice == "3":
                expense_id = int(input("Expense ID to edit: "))
                amount = float(input("New amount: "))
                category = input("New category: ").strip()
                description = input("New description: ").strip()

                edit_expense(
                    expenses, expense_id,
                    amount, category, description
                )
                save_expenses(expenses)
                print("Expense updated successfully!")

            elif choice == "4":
                expense_id = int(input("Expense ID to delete: "))
                delete_expense(expenses, expense_id)
                save_expenses(expenses)
                print("Expense deleted successfully!")

            elif choice == "5":
                analysis_menu(expenses)

            elif choice == "6":
                budget = budget_menu(expenses, budget)

            elif choice == "0":
                save_expenses(expenses)
                print("Expenses saved. Goodbye!")
                break

            else:
                print("Invalid menu option.")

        except ValueError as error:
            print(f"Invalid input: {error}")


if __name__ == "__main__":
    main()
