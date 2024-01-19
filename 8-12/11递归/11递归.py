def age(n):
    if n == 1:
        return 1
    else:
        return age(n + 1) + 2


def peach(n):
    if n == 10:
        return 1
    else:
        return (peach(n + 1) + 1) * 2


def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n - 1) * n


def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fractional_addition(n):
    if n == 1:
        return 1
    else:
        return fractional_addition(n - 1) + ((-1) ** (n + 1)) * (11 / (2 * n - 1))


def fibonacci_sum(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return 2 * (fibonacci_sum(n - 1) + fibonacci_sum(n - 2))


print(age(1))
print(peach(1))
print(factorial(5))
print(fibonacci(4))
print(f'{fractional_addition(7):.4f}')
print(fibonacci_sum(3))
