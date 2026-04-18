def sum_to_n(n):
    if n <= 0:
        return 0
    return n + sum_to_n(n - 1)

# print(sum_to_n(10))


def product_to_n(n):
    if n <= 0:
        return 1
    return n * product_to_n(n - 1)

# print(product_to_n(5))


def fabonacci (a):
    if a <= 0:
        return 0
    elif a == 1:
        return 1
    else:
        return fabonacci(a - 1) + fabonacci(a - 2)

print(fabonacci(8))
