def power_e(x, n):
    ans = 1.0
    numerator = 1.0
    denominator = 1.0
    for i in range(1, n + 1):
        numerator*= x
        denominator *= i
        ans += numerator / denominator
    return ans


def Sum_S(n):
    ans = 1.0
    denominator = 1.0
    for i in range(2, n + 1):
        denominator *= i
        ans += 1 / denominator
    return ans


x = int(input())
n = int(input())

print(f"e^{x} = {power_e(x, 100)}")
print(f"S(n) = {Sum_S(n)}")