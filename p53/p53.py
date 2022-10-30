def factorial(num):
    res = 1
    for i in range(1,num+1):
        res *= i
    return res

if __name__ == '__main__':
   count = 0
   for n in range(23,101):
       for r in range(1,n):
           if factorial(n) / (factorial(r) * factorial(n-r)) > 1000000:
               count +=1
   print(count)