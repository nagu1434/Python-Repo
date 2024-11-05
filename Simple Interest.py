def simple_interest(P, T, R):
    return (P * T * R) // 100
P, T, R = map(int, input().split())
interest = simple_interest(P, T, R)
print(interest)
