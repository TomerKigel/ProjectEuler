import math

primes = [2]
def populate_primes():
    for i in range(0,50000):
        primes.append(next_prime(primes[i]))

def next_prime(prime):
    if prime != primes[-1]:
        for i in range(0,len(primes)):
            if primes[i] == prime:
                return primes[i+1]
    prime += 1
    is_prime = False
    while not is_prime:
        is_prime = True
        for i in primes:
            if prime % i == 0:
                is_prime = False
            if i > math.sqrt(prime):
                break
        if not is_prime:
            prime+=1
    return prime

def composite(num,primes):
    factors = []
    while num != 1:
        for prime in primes:
            if num % prime == 0:
                if prime not in factors:
                    factors.append(prime)
                num /= prime
                break
    return len(factors)


if __name__ == '__main__':
    populate_primes()
    numbers = [2,3,4,5]
    for i in range(1,9999999):
        found = True
        for j in numbers:
            if composite(j,primes) != 4:
                found = False
                numbers[0] = j+1
                numbers[1] = numbers[0] + 1
                numbers[2] = numbers[0] + 2
                numbers[3] = numbers[0] + 3
                break
            else:
                print(j)
        if found:
            print(numbers)
            break
