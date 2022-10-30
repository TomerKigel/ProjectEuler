import copy

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
        if i - 1 < 0:
            number.insert(0,0)
            i = 1
        number[i - 1] += 1
        i -= 1
    return number


def listToDigit(number):
    res = []
    while number >= 1:
        res.insert(0,number % 10)
        number /= 10
        number = int(number)
    return res


if __name__ == '__main__':
    number = [1]
    found = False
    while not found:
        found = True
        copy_number = copy.deepcopy(number)
        cn = digits_to_dec(copy_number)
        for i in range(2,7):
            cur_num = cn * i
            cur_num = listToDigit(cur_num)
            for elem in cur_num:
                if elem not in number:
                    found = False
                    continue
        incListNumber(number)
    number[-1] -= 1
    print(number)