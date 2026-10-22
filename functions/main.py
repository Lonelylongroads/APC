#1
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

#2
def check_even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

#3
def greater_number(a, b):
    return a if a > b else b

#4
def simple_interest(p, r, t):
    return (p * r * t) / 100

#5
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

#6
def circle_area(radius):
    return 3.14159 * radius * radius

#7
def sum_natural(n):
    return n * (n + 1) // 2

#8
def power(base, exponent):
    return base ** exponent

#9
def largest_element(lst):
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest

#10
def count_vowels(s):
    return sum(1 for c in s.lower() if c in "aeiou")

#11
def reverse_string(s):
    return s[::-1]

#12
def is_palindrome(val):
    s = str(val)
    return s == s[::-1]

#13
def list_average(lst):
    return sum(lst) / len(lst) if lst else 0

#14
def element_frequency(lst, elem):
    return lst.count(elem)

#15
def unique_elements(lst):
    return list(set(lst))

#16
def second_largest(lst):
    unique = list(set(lst))
    unique.sort()
    return unique[-2] if len(unique) >= 2 else None

#17
def fibonacci_series(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

#18
def student_report(marks):
    total = sum(marks)
    percentage = total / len(marks)
    if percentage >= 85:
        grade = 'A'
    elif percentage >= 70:
        grade = 'B'
    elif percentage >= 50:
        grade = 'C'
    else:
        grade = 'F'
    return percentage, grade

#19
def calculate_electricity_bill(units):
    if units <= 100:
        bill = units * 1.5
    elif units <= 300:
        bill = 100 * 1.5 + (units - 100) * 3.0
    else:
        bill = 100 * 1.5 + 200 * 3.0 + (units - 300) * 5.0
    return bill

#20
def gross_salary(basic):
    hra = basic * 0.4
    da = basic * 0.2
    return basic + hra + da

#21
def total_bill(prices, quantities, discount_pct):
    subtotal = sum(p * q for p, q in zip(prices, quantities))
    discount = subtotal * (discount_pct / 100)
    return subtotal - discount

#22
def list_statistics(lst):
    return min(lst), max(lst), sum(lst), sum(lst) / len(lst)

#23
def process_students(students_data):
    results = []
    total_class_marks = 0
    highest = -1
    lowest = float('inf')
    high_scorer = low_scorer = ""
    
    for name, roll, marks in students_data:
        tot = sum(marks)
        pct = tot / len(marks)
        total_class_marks += tot
        if tot > highest:
            highest = tot
            high_scorer = name
        if tot < lowest:
            lowest = tot
            low_scorer = name
        results.append((name, roll, tot, pct))
        
    class_avg = total_class_marks / len(students_data)
    return results, class_avg, high_scorer, low_scorer

#24
balance = 0
history = []

def deposit(amount):
    global balance
    balance += amount
    history.append(f"Deposited: {amount}")

def withdraw(amount):
    global balance
    if amount > balance:
        return "Insufficient Balance"
    balance -= amount
    history.append(f"Withdrawn: {amount}")

def balance_enquiry():
    return balance

def transaction_history():
    return history

#25
library = {}

def add_book(book_id, title):
    library[book_id] = {"title": title, "status": "Available"}

def issue_book(book_id):
    if book_id in library and library[book_id]["status"] == "Available":
        library[book_id]["status"] = "Issued"
        return True
    return False

def return_book(book_id):
    if book_id in library:
        library[book_id]["status"] = "Available"

def search_book(title):
    return [b_id for b_id, details in library.items() if details["title"].lower() == title.lower()]

def display_available():
    return {b_id: details for b_id, details in library.items() if details["status"] == "Available"}

#26
def compute_energy_charge(units):
    return units * 4.5

def compute_fixed_charges():
    return 100

def compute_taxes(amount):
    return amount * 0.05

def apply_discount(amount):
    return amount * 0.95

def final_electricity_bill(units):
    energy = compute_energy_charge(units)
    fixed = compute_fixed_charges()
    subtotal = energy + fixed
    tax = compute_taxes(subtotal)
    return apply_discount(subtotal + tax)

#27
def consultation_fee(cat):
    return 1000 if cat == "VIP" else 500

def lab_charges(tests):
    return len(tests) * 300

def medicine_charges(cost):
    return cost

def room_charges(days):
    return days * 2000

def final_hospital_bill(cat, tests, med_cost, days):
    sub = consultation_fee(cat) + lab_charges(tests) + medicine_charges(med_cost) + room_charges(days)
    discount = 0.2 if cat == "Senior" else (0.1 if cat == "VIP" else 0)
    return sub - (sub * discount)

#28
def subtotal_func(prices, quantities):
    return sum(p * q for p, q in zip(prices, quantities))

def apply_coupon(sub, coupon):
    return sub * 0.9 if coupon == "SAVE10" else sub

def calculate_gst(sub):
    return sub * 0.18

def generate_invoice(prices, quantities, coupon):
    sub = subtotal_func(prices, quantities)
    discounted = apply_coupon(sub, coupon)
    gst = calculate_gst(discounted)
    return discounted + gst

#29
def binary_search(lst, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if lst[mid] == x:
            return mid
        elif lst[mid] > x:
            return binary_search(lst, low, mid - 1, x)
        else:
            return binary_search(lst, mid + 1, high, x)
    return -1

#30
def decimal_to_binary(n):
    if n == 0:
        return ""
    return decimal_to_binary(n // 2) + str(n % 2)

#31
def recursive_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return recursive_palindrome(s[1:-1])

#32
def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b

def calculate(func, a, b):
    return func(a, b)

#lambda functions
square = lambda x: x ** 2
cube = lambda x: x ** 3
is_even = lambda x: x % 2 == 0
max_two = lambda a, b: a if a > b else b
si = lambda p, r, t: (p * r * t) / 100

squares = list(map(lambda x: x ** 2, [1, 2, 3, 4]))
cubes = list(map(lambda x: x ** 3, [1, 2, 3, 4]))
list_sum = list(map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6]))
evens = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))

is_p = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
primes = list(filter(is_p, range(1, 20)))

positives = list(filter(lambda x: x > 0, [-2, -1, 0, 1, 2]))
greater_than_50 = list(filter(lambda x: x > 50, [20, 60, 40, 80]))
long_words = list(filter(lambda w: len(w) > 5, ["apple", "banana", "cat"]))
sorted_words = sorted(["apple", "banana", "fig"], key=lambda w: len(w))
sorted_students = sorted([("Alice", 85), ("Bob", 92)], key=lambda x: x[1])
sorted_emps = sorted([("Alice", 50000), ("Bob", 75000)], key=lambda x: x[1])

students = [("Alice", 80), ("Bob", 65), ("Charlie", 90)]
avg_marks = sum(map(lambda x: x[1], students)) / len(students)
above_75 = list(filter(lambda x: x[1] > 75, students))
sorted_studs = sorted(students, key=lambda x: x[1], reverse=True)

emps = [("Alice", "HR", 45000), ("Bob", "IT", 60000), ("Charlie", "IT", 55000)]
rich_emps = list(filter(lambda e: e[2] > 50000, emps))
hiked_salaries = list(map(lambda e: (e[0], e[1], e[2] * 1.1), emps))
sorted_sal = sorted(emps, key=lambda e: e[2])

products = [("Laptop", 50000, 2), ("Mouse", 500, 5)]
total_vals = list(map(lambda p: (p[0], p[1] * p[2]), products))
expensive = list(filter(lambda p: p[1] > 1000, products))
sorted_prods = sorted(products, key=lambda p: p[1] * p[2], reverse=True)

words = ["python", "code", "lambda", "ai"]
lengths = list(map(lambda w: (w, len(w)), words))
long_w = list(filter(lambda w: len(w) > 5, words))
sorted_w = sorted(words, key=lambda w: len(w))


print(factorial(5))
print(check_even_odd(4))
print(greater_number(10, 20))
print(simple_interest(1000, 5, 2))
print(is_prime(11))
print(circle_area(5))
print(sum_natural(10))
print(power(2, 3))
print(largest_element([1, 5, 3, 9, 2]))
print(count_vowels("Hello World"))
print(reverse_string("python"))
print(is_palindrome("madam"))
print(list_average([10, 20, 30, 40]))
print(element_frequency([1, 2, 2, 3, 2], 2))
print(unique_elements([1, 2, 2, 3, 1]))
print(second_largest([10, 20, 5, 20, 30]))
print(fibonacci_series(5))
print(student_report([80, 90, 85]))
print(calculate_electricity_bill(250))
print(gross_salary(10000))
print(total_bill([100, 200], [2, 1], 10))
print(list_statistics([10, 20, 30, 40]))
print(process_students([("Alice", 1, [80, 90]), ("Bob", 2, [60, 70])]))
deposit(100)
withdraw(30)
print(balance_enquiry())
print(transaction_history())
add_book(1, "Python")
print(issue_book(1))
return_book(1)
print(search_book("Python"))
print(display_available())
print(final_electricity_bill(200))
print(final_hospital_bill("VIP", ["Blood", "Xray"], 5000, 3))
print(generate_invoice([100, 200], [2, 1], "SAVE10"))
print(binary_search([1, 2, 3, 4, 5], 0, 4, 3))
print(decimal_to_binary(10))
print(recursive_palindrome("racecar"))
print(calculate(add, 5, 3))
print(square(4))
print(cube(3))
print(is_even(4))
print(max_two(10, 20))
print(si(1000, 5, 2))
print(squares)
print(cubes)
print(list_sum)
print(evens)
print(primes)
print(positives)
print(greater_than_50)
print(long_words)
print(sorted_words)
print(sorted_students)
print(sorted_emps)
print(avg_marks)
print(above_75)
print(sorted_studs)
print(rich_emps)
print(hiked_salaries)
print(sorted_sal)
print(total_vals)
print(expensive)
print(sorted_prods)
print(lengths)
print(long_w)
print(sorted_w)