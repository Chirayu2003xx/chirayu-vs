def prit(n, isPrime):
    isPrime[0] = isPrime[1] = False
    for i in range(2, n + 1):
        isPrime[i] = True
    for p in range(2, int(n**0.5) + 1):
        if isPrime[p]:
            for i in range(p * p, n + 1, p):
                isPrime[i] = False

def superPrimes(n):
    isPrime = [1 for i in range(n + 1)]
    prit(n, isPrime)
    primes = []
    for p in range(2, n + 1):
        if isPrime[p]:
            primes.append(p)
    for k in range(len(primes)):
        if isPrime[primes[k]]:
            print(primes[k], end=" ")

n = 241
print("Super-Primes less than or equal to", n, "are:")
superPrimes(n)
