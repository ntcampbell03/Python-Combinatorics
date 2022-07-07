def fib(n):
    if n == 0:
        return 0
    a, b = 1, 1
    for i in range(n-2):
        a, b = b, a + b
    return b
