# salary_utils.py
def calculate_gross(basic):
    da = basic * 0.40
    hra = basic * 0.20
    return basic + da + hra

def calculate_deductions(basic):
    return basic * 0.10

def calculate_net(basic):
    gross = calculate_gross(basic)
    deductions = calculate_deductions(basic)
    return gross - deductions