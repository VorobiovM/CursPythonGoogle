# 1. Să se scrie o funcție care primește un număr nedefinit de parametrii și să se calculeze suma parametrilor care
# reprezintă numere întregi sau reale.
def sum_function(*args, **kwargs):
    total = 0
    for arg in args:
        if type(arg) is int:
            total += arg
    return total


print(sum_function(1, 5, -3, 'abc', [12, 56, 'cad']))  # 3
print(sum_function())                                  # 0
print(sum_function(2, 4, 'abc', param_1=2))            # 6


# 2. Să se scrie o funcție recursivă care primește ca parametru un număr întreg și returnează:
# a. suma tuturor numerelor de la [0, n]
def rec_sum_all(n):
    if not n:
        return 0
    return n + rec_sum_all(n - 1)


print(rec_sum_all(6))  # 0 + 1 + 2 + 3 + 4 + 5 + 6 = 21
print(rec_sum_all(3))  # 0 + 1 + 2 + 3 = 6
print(rec_sum_all(1))  # 0 + 1 = 1


# b. suma numerelor pare de la [0, n]
def rec_sum_even(n):
    if not n:
        return 0
    if n % 2:
        return rec_sum_even(n - 1)
    else:
        return n + rec_sum_even(n - 1)


print(rec_sum_even(6))  # 0 + 2 + 4 + 6 = 12
print(rec_sum_even(3))  # 0 + 2 = 2
print(rec_sum_even(1))  # 0 = 0


# c. suma numerelor impare de la [0, n]
def rec_sum_odd(n):
    if not n:
        return 0
    if not n % 2:
        return rec_sum_odd(n - 1)
    else:
        return n + rec_sum_odd(n - 1)


print(rec_sum_odd(6))  # 1 + 3 + 5 = 9
print(rec_sum_odd(3))  # 1 + 3 = 4
print(rec_sum_odd(1))  # 1 = 1


# 3. Să se scrie o funcție care citește de la tastatură și returnează valoarea dacă aceasta este un număr întreg,
# altfel returnează valoarea 0.
def read_int():
    user_input = input("Scrie un numar intreg: ")
    try:
        sanitized_data = int(user_input)
        return sanitized_data
    except ValueError:
        return 0


print(read_int())
