import copy
import math


primes = []
def isPrime(n):
  if n in primes:
    return True
  for i in range(2,int(math.sqrt(n))+1):
    if (n%i) == 0:
      return False
  primes.append(n)
  return True

def next_prime(prime):
    prime += 1
    while not isPrime(prime):
            prime+=1
    return prime


def concat(num, connum):
    count = 0
    c = copy.copy(connum)
    while  c >= 1:
        c /= 10
        count += 1
    while count > 0:
        num *= 10
        count -= 1
    return num + connum


def concatStillPrime(groupa, groupb):
    for i in range(len(groupa)):
        for j in range(len(groupb)):
            if not isPrime(concat(groupa[i],groupb[j])) or not isPrime(concat(groupb[j],groupa[i])):
                return False
    return True

if __name__ == '__main__':
   prime = 3
   nprime = 5
   chosen = [3]
   while prime < 20000:
       candidates = []
       while nprime < 20000:
           if concatStillPrime([prime],[nprime]):
               candidates.append(nprime)
           nprime = next_prime(nprime)
       last = prime
       while candidates:
           for candidate in candidates:
               if candidate > last:
                   if concatStillPrime(chosen,[candidate]):
                       chosen.append(candidate)
                       if len(chosen) == 5:
                           print(chosen, end = ' ')
                           print(sum(chosen))
           if len(chosen) == 1:
               break
           last = chosen[-1]
           chosen.remove(chosen[-1])
       prime = next_prime(prime)
       chosen = [prime]
       nprime = next_prime(prime)

