def sieve_of_eratosthenes(limit):
    primes = []
    is_prime = [True] * (limit + 1)

    for num in range(2, limit + 1):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False

    return primes

limit = int(input("Please enter a number to calculate prime numbers up to: "))
primes = sieve_of_eratosthenes(limit)
print(f"Prime numbers up to {limit}: {primes}")
