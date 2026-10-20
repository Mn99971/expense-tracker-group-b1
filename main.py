
from expenses import (
    add_expense,
    edit_expense,
    delete_expense,
    load_expenses,
    save_expenses,
)


def show_menu():
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Edit expense")
    print("4. Delete expense")
    print("5. Spending analysis (coming soon)")
    print("6. Budget management (coming soon)")
    print("0. Save and exit")


def main():
    expenses = load_expenses()

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

            elif choice in ("5", "6"):
                print("This feature is under development.")

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
