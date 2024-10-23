# Write a Python function monthly_payment(principal, rate, years) that
# calculates the monthly mortgage payment for a given principal loan amount, annual
# interest rate, and loan term in years. Use the formula

def monthly_payment(principal, rate, years):
    monthly_rate = rate / 100 / 12
    number_of_payments = years*12
    payment = (principal*monthly_rate) / (1 -(1 + monthly_rate)** -number_of_payments)
    return payment

result = monthly_payment(200000, 5, 30)
print(result)