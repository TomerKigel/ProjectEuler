def deconNum(num):
    res = [int(x) for x in str(num)]
    sum = 0
    for i in res:
        sum += i
    return sum

if __name__ == '__main__':
    num = 0
    largest = 0
    for a in range(20,101):
        for b in range(5,101):
            num = a**b
            if deconNum(num) > largest:
                largest = deconNum(num)
    print(largest)

