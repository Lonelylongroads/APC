# main.py
from banking import account, transaction, loan

acc = account.create_account("Alice", 1000)
transaction.deposit(acc, 500)
print("Balance:", acc["balance"])
print("Loan Amount:", loan.calculate_loan(5000))