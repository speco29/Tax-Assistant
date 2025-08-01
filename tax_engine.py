# tax_engine.py

def calculate_tax_old_regime(income, deductions):
    taxable_income = income - sum(deductions.values())

    # Old regime slabs
    if taxable_income <= 250000:
        tax = 0
    elif taxable_income <= 500000:
        tax = 0.05 * (taxable_income - 250000)
    elif taxable_income <= 1000000:
        tax = 12500 + 0.2 * (taxable_income - 500000)
    else:
        tax = 112500 + 0.3 * (taxable_income - 1000000)

    return round(tax, 2)


def calculate_tax_new_regime(income):
    # New regime slabs (FY2023–24)
    if income <= 300000:
        tax = 0
    elif income <= 600000:
        tax = 0.05 * (income - 300000)
    elif income <= 900000:
        tax = 15000 + 0.1 * (income - 600000)
    elif income <= 1200000:
        tax = 45000 + 0.15 * (income - 900000)
    elif income <= 1500000:
        tax = 90000 + 0.2 * (income - 1200000)
    else:
        tax = 150000 + 0.3 * (income - 1500000)

    return round(tax, 2)
