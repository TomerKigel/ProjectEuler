import copy
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


def digits_to_dec(digits):
    sum = 0
    for i in range(len(digits)):
        sum += digits[len(digits)-i-1] * 10**i
    return sum

def heapPermutation(id_list, size, lst):
    # if size becomes 1 then prints the obtained
    # permutation
    if size == 1:
        if digits_to_dec(id_list) in primes and digits_to_dec(id_list) not in lst:
            lst.append((digits_to_dec(id_list)))
        return

    for i in range(size):
        heapPermutation(id_list, size - 1,lst)
        # if size is odd, swap 0th i.e (first)
        # and (size-1)th i.e (last) element
        # else If size is even, swap ith
        # and (size-1)th i.e (last) element
        if size & 1:
            id_list[0], id_list[size - 1] = id_list[size - 1], id_list[0]
        else:
            id_list[i], id_list[size - 1] = id_list[size - 1], id_list[i]

if __name__ == '__main__':
    populate_primes()
    digits = [1, 2, 3, 4]
    while True:
        lst = []
        temp_digits = copy.deepcopy(digits)
        heapPermutation(digits,4,lst)
        digits = temp_digits
        lst.sort()
        if digits[0] == 1 and digits[1] == 4 and digits[2] == 7 and digits[3] == 8:
            print(lst)
        if len(lst) > 2:
            for i in range(len(lst)):
                for j in range(i+1,len(lst)):
                    for l in range(i + 1, len(lst)):
                        if lst[j] - lst[i] == lst[l] - lst[j]:
                            print(lst[i],lst[j],lst[l])
        digits[-1] +=1
        i = len(digits) - 1
        while digits[i] > 9:
            digits[i] = 1
            digits[i-1] += 1
            i -=1






