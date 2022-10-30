import copy
import math

primes = [2]
def populate_primes():
    for i in range(0,100000):
        primes.append(next_prime(primes[i]))

def next_prime(prime):
    if prime == 1:
        return 2
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
    sum = 0
    lst = []
    maxa = {}
    found = False
    start_index = 0
    while not found:
        pr = 1
        index = 0
        while sum < 1000000:
            pr = next_prime(pr)
            if index >= start_index:
                lst.append(pr)
                sum += pr
            index += 1

        maxa[len(lst)] = (sum-pr,copy.deepcopy(lst))
        start_index += 1

        if start_index >= len(lst):
            found = True

        lst.clear()
        sum = 0

    max_val = 0
    max_len = 0
    for key in maxa.keys():
        if maxa[key][0] in primes and key > max_len:
            max_val = maxa[key][0]
            max_len = key

    print(max_val,max_len,max_lst)








