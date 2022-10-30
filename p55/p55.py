def isPolindrom(num):
    if revNum(num) == num:
        return True
    return False

def revNum(num):
    res = 0
    while num >= 1:
        res *= 10
        res += (num % 10)
        num /= 10
        num = int(num)
    return res

if __name__ == '__main__':
    count = 0
    for num in range(0,10000):
        x_num = num
        revNnum = revNum(num)
        num = num + revNnum
        iterations = 0
        while not isPolindrom(num) and iterations < 50:
            revNnum = revNum(num)
            num = num+revNnum
            iterations += 1
        if not isPolindrom(num):
            count += 1
            print(x_num)
    print(count)
