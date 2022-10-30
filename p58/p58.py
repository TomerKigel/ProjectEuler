import math
def isPrime(n):
  for i in range(2,int(math.sqrt(n))+1):
    if (n%i) == 0:
      return False
  return True

if __name__ == '__main__':
    primes_count = 0
    total_count = 1
    prob = 1
    num = 1
    j = 1
    while prob > 0.1:
        for i in range(4):
            num += 2 * j
            if isPrime(num):
                primes_count+=1
            total_count+=1
        j+=1
        prob = primes_count/total_count
    print((j-1)*2+1)