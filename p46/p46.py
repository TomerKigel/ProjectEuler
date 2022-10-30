import math

primes = [2]
def populate_primes():
    for i in range(0,10000):
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


if __name__ == '__main__':
    populate_primes()
    prime = 2
    current_number = 35
    square = 1
    while True:
        if current_number == prime + 2 * pow(square,2):
            print(current_number, "=", prime, "+2*", square,"^2")
            current_number += 2
            while current_number in primes:
                current_number+=2
            prime = 2
            square = 1
        elif current_number < prime + 2 * pow(square,2):
            if prime < current_number:
                square = 1
                prime = next_prime(prime)
            else:
                print(current_number)
                break
        else:
            square += 1