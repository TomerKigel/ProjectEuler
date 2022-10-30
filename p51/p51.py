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


def digits_to_dec(digits):
    sum = 0
    for i in range(len(digits)):
        sum += digits[len(digits)-i-1] * 10**i
    return sum

def incListNumber(number):
    number[-1] += 1
    i = len(number) - 1
    while number[i] > 9:
        number[i] = 0
        number[i - 1] += 1
        i -= 1
    return number

def valToTruthTableLine(val,inputsize):
    res = []
    if val == 1:
        res = [1]
        for i in range(len(res), inputsize):
            res.insert(0, 0)
        return res
    binary_digit= 0
    binary_value = 1
    while binary_value <= val:
        binary_value *= 2
        binary_digit+= 1
    binary_value /= 2
    binary_digit -= 1

    while binary_digit >= 0:
        if val - 2**binary_digit >= 0:
            res.append(1)
            val -= 2**binary_digit
        else:
            res.append(0)
        binary_digit -= 1

    for i in range(len(res),inputsize):
        res.insert(0,0)
    return res


def listToDigit(number):
    res = []
    while number >= 1:
        res.insert(0,number % 10)
        number /= 10
        number = int(number)
    return res


if __name__ == '__main__':
    populate_primes()
    prime = 2
    number = [2]
    amount_replaced = 1
    valplace = 1

    found = False
    max_primes = 0
    while digits_to_dec(number) < 11:
        number = listToDigit(next_prime(digits_to_dec(number)))

    while not found:
        lst = []
        for valplace in range(1,2**len(number)):
            primes_found = 0
            lst.clear()
            copy_number = copy.deepcopy(number)
            line = valToTruthTableLine(valplace,len(number))
            for replace_number in range(0,10):
                if replace_number == 0 and line[0] == 1:
                    continue
                index = 0
                for v in line:
                    if v:
                        copy_number[index] = replace_number
                    index += 1
                if digits_to_dec(copy_number) in primes and digits_to_dec(copy_number) != digits_to_dec(number):
                    primes_found+=1
                    lst.append(digits_to_dec(copy_number))

                if max_primes < primes_found:
                    print(digits_to_dec(number))
                    max_primes = primes_found
                    print(max_primes)
                    print(lst)
                if primes_found > 7:
                    found = True
                    print(digits_to_dec(number))


        number = listToDigit(next_prime(digits_to_dec(number)))
