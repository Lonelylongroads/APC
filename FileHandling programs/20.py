with open("transactions.txt", "w") as f:
    f.write("Deposit, 1000\n")
    f.write("Withdrawal, 200\n")
    f.write("Deposit, 500\n")

total_dep = 0
total_with = 0
max_txn = 0
with open("transactions.txt", "r") as f:
    for line in f:
        t_type, amt = [p.strip() for p in line.split(",")]
        amt = float(amt)
        if t_type == "Deposit":
            total_dep += amt
        else:
            total_with += amt
        if amt > max_txn:
            max_txn = amt

print("Total deposits:", total_dep)
print("Total withdrawals:", total_with)
print("Final balance:", total_dep - total_with)
print("Largest transaction:", max_txn)