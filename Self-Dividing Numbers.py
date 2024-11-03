def is_self_dividing(num):
    for digit in str(num):
        if digit == '0' or num % int(digit) != 0:
            return False
    return True

def self_dividing_numbers(left, right):
    result = []
    for num in range(left, right + 1):
        if is_self_dividing(num):
            result.append(num)
    return result
left = int(input())
right = int(input())
print(*self_dividing_numbers(left, right))
