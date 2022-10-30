def digits(num):
    return len(str(num))

if __name__ == '__main__':
    count = 0
    numerator  = 1
    denominator = 2
    for expansion in range(1,1000):
         numerator = 2 * denominator + numerator
         temp = numerator
         numerator = denominator
         denominator = temp
         if digits(numerator + denominator) > digits(denominator):
             count += 1
    print(count)

