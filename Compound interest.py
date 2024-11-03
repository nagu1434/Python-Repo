def calculate_total_amount(P, R, T):
    rate_decimal = R / 100
    amount = P * (1 + rate_decimal) ** T
    return amount

# Input reading
P, R, T = map(float, input().split())

# Calculate total amount
total_amount = calculate_total_amount(P, R, T)
print(f"{total_amount:.2f}")
