class BankAccount:
    account_counter = 1000

    def __init__(self, account_holder):
        BankAccount.account_counter += 1
        self.account_number = BankAccount.account_counter
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} into Account {self.account_number}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from Account {self.account_number}")
        else:
            print(f"Insufficient funds in Account {self.account_number}")

    def display_balance(self):
        print(f"Account {self.account_number} ({self.account_holder}) Balance: {self.balance}")

    def transfer(self, amount, other_account):
        if amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            print(f"Transferred {amount} from Account {self.account_number} to Account {other_account.account_number}")
        else:
            print(f"Transfer failed: Insufficient funds in Account {self.account_number}")


acc1 = BankAccount("Sakshi")
acc2 = BankAccount("Rahul")

acc1.deposit(5000)
acc2.deposit(2000)

acc1.display_balance()
acc2.display_balance()

acc1.withdraw(1000)
acc1.transfer(1500, acc2)

acc1.display_balance()
acc2.display_balance()