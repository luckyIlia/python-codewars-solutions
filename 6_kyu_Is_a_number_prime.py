def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1))

print(is_prime(5))

def is_prime2(num):
    if num < 2:
        return False
    
    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            return False
    return True


print(is_prime2(5))