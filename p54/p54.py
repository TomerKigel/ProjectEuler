
def convertToNum(i):
    if ord(i) - ord('0') < 10:
        return int(i) - int('0')
    elif i == 'T':
        return 10
    elif i == 'J':
        return 11
    elif i == 'Q':
        return 12
    elif i == 'K':
        return 13
    elif i == 'A':
        return 14

def numConvert(i):
    if i < 10:
        return str(i)
    elif i == 10:
        return 't'
    elif i == 11:
        return 'j'
    elif i == 12:
        return 'q'
    elif i == 13:
        return 'k'
    elif i == 14:
        return 'a'


def convertToType(i):
    if i == 'C':
        type = 0
    if i == 'H':
        type = 1
    if i == 'D':
        type = 2
    if i == 'S':
        type = 3
    return type

def typeConvert(i):
    if i == 0:
        type = 'c'
    if i == 1:
        type = 'h'
    if i == 2:
        type = 'd'
    if i == 3:
        type = 's'
    return type

def emptyMatrix():
    matrix = []
    for i in range(0,4):
        matrix.append([])
        for j in range(2,15):
            matrix[i].append("".join((typeConvert(i),numConvert(j))))
    return matrix


def cardConvert(card):
    column = convertToNum(card[0])
    row = convertToType(card[1])
    return (row,column)

def tickMatrix(matrix,card):
    loc = cardConvert(card)
    matrix[loc[0]][loc[1]-2] = 1
    return matrix

def sameSuit(line):
    count = 0
    max_consecutive = 0
    consecutive = 0
    royal = False
    highest = 0
    index = 0
    for i in line:
        if i == 1:
            count += 1
            consecutive += 1
        else:
            if consecutive > max_consecutive:
                highest = index+2
                max_consecutive = consecutive
            consecutive = 0
        index += 1
    if consecutive > max_consecutive:
        max_consecutive = consecutive
        highest = index+2
        if consecutive == 5:
            royal = True
    return (count,max_consecutive,royal,highest)

def sameValue(column):
    count = 0
    for i in column:
        if i == 1:
            count +=1
    return count


def lineStuff(matrix):
    for line in matrix:
        suit_count = sameSuit(line)
        if suit_count[2]:
            return ["rf",0,0]
        if suit_count[1] == 5:
            return ["sf",suit_count[3],0]
        if suit_count[0] == 5:
            return ["f",suit_count[3],0]
        return None


def calculateScore(matrix):
    x = lineStuff(matrix)
    if x != None:
        return x
    in_rank = 0
    out_rank = 0
    consecutive = 0
    max_consecutive = 0

    reval = ["hv",0,0]

    for col in range(len(matrix[0])):
        column = []
        for row in range(len(matrix)):
            column.append(matrix[row][col])
        val_count = sameValue(column)
        column.clear()

        if val_count == 1:
            consecutive += 1
            if col+2 > out_rank:
                out_rank = col+2
        elif val_count == 2:
            if reval[0] == "tok":
                reval[0] = "fh"
                out_rank = col + 2
            elif reval[0] == "op":
                reval[0] = "tp"
                if in_rank < col + 2:
                    in_rank = col + 2
            else:
                reval[0] = "op"
                in_rank = col + 2
        elif val_count == 3:
            if reval[0] == "op":
                out_rank = in_rank
                in_rank = col + 2
                reval[0] = "fh"
            else:
                reval[0] = "tok"
                in_rank = col + 2
        elif val_count == 4:
            reval[0] = "4ok"
            in_rank = col + 2
        else:
            if consecutive > max_consecutive:
                max_consecutive = consecutive
            if max_consecutive == 5:
                return ["st",out_rank,out_rank]
            consecutive = 0
    if in_rank == 0:
        in_rank = out_rank
    reval[1] = in_rank
    reval[2] = out_rank
    return reval

def compare(o1,o2):
    order = ["hv", "op", "tp", "tok", "st", "f", "fh", "4ok", "sf", "rf"]
    val_dict = {}
    for key,value in enumerate(order):
        val_dict[value] = key
    if val_dict[o1[0]] > val_dict[o2[0]]:
        print(o1," comp ", o2 ,end = " ")
        print("o1")
        return True
    elif val_dict[o1[0]] < val_dict[o2[0]]:
        return False
    else:
        if o1[1] > o2[1]:
            print(o1," comp ", o2 ,end = " ")
            print("o1")
            return True
        elif o1[1] < o2[1]:
            return False
        else:
            if o1[2] > o2[2]:
                print(o1," comp ", o2 ,end = " ")
                print("o1")
            else:
                return o1[2] > o2[2]



if __name__ == '__main__':
    f = open("p054_poker.txt", "r")
    p1_wins = 0
    for line in f:
        p1_score = 0
        p1_matrix = emptyMatrix()
        p2_matrix = emptyMatrix()
        p2_score = 0
        line = line.split(" ")
        for i in range(0,5):
            tickMatrix(p1_matrix,line[i])

        for i in range(5,10):
            tickMatrix(p2_matrix,line[i])

        if compare(calculateScore(p1_matrix), calculateScore(p2_matrix)):
            p1_wins += 1
            print(p1_wins)


    print(p1_wins)

