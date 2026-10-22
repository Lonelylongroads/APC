# banking/transaction.py
def deposit(acc, amount):
    acc["balance"] += amount
    return acc["balance"]

def withdraw(acc, amount):
    acc["balance"] -= amount
    return acc["balance"]