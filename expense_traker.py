# ===========================
# Expense Tracker
# DecodeLabs - Project 2
# ===========================

print("===== Expense Tracker =====")

total_expense = 0

while True:
    expense = float(input("Enter expense amount: ₹"))
    total_expense += expense

    choice = input("Do you want to add another expense? (yes/no): ").lower()

    if choice != "yes":
        break

print("\n----- Expense Summary -----")
print(f"Total Expense: ₹{total_expense:.2f}")
print("Thank you for using Expense Tracker!")