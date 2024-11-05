def is_neon_number(n):
    square = n ** 2
    digit_sum = sum(int(digit) for digit in str(square))
    return digit_sum == n
N = int(input())
if is_neon_number(N):
    print("Neon Number")
else:
    print("Not Neon Number")
