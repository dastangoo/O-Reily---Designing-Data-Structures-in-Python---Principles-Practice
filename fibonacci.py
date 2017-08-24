def fibonacci(n):
    """Return n >= 2 Fibonacci numbers."""
    a = b = 1
    result = [a, b]
    while n > 2:
        n = n - 1
        a, b = b, a + b
        result.append(b)
    return result
def fibonacciGen(n):
    a = b = 1
    yield a
    yield b
    while n > 2:
        n = n - 1
        a, b = b, a + b
        yield b
