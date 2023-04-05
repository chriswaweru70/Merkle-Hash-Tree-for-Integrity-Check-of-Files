import random

# Miller-Rabin primality test function
def is_prime(n, k=10):
    # Check if n is 2 or 3
    if n <= 3:
        return n >= 2

    # Check if n is even
    if n % 2 == 0:
        return False

    # Write n-1 as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Perform k iterations of the Miller-Rabin test
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True

# Test all numbers between 500000 and 1000000
primes = [num for num in range(500000, 1000001) if is_prime(num)]

# Print the list of primes found
print(primes)
