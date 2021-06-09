def caching_fibonacci():
    cache = {0: 0, 1: 1}

    def fibonacci(n):
        if n in cache:
            resolt = cache[n]
        else:
            resolt = fibonacci(n-1) + fibonacci(n-2)
            cache[n] = resolt
        return resolt
    return fibonacci


a = caching_fibonacci()
print(a(6))
