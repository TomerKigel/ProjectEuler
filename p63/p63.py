import math



if __name__ == '__main__':
    result = 0
    lower = 0
    n = 1

    while (lower < 10) :
        lower = math.ceil(math.pow(10, (n-1) / n))
        result += 10 - lower
        n+= 1
    print(result)