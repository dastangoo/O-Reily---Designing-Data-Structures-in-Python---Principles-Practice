def fib(n):
    # Base case
    if n < 2:
        return 1
    # Action and recursive step
    return fib(n-1) + fib(n-2)
    
