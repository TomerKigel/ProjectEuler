if __name__ == '__main__':
    f = open("p059_cipher.txt")
    f = str(f.read())
    chars = f.split(",")
    password = ['a','a','a']
    while True:
        i = 0
        res = ""
        for char in chars:
            tres = int(char) ^ ord(password[i])
            i += 1
            if i > 2:
                i = 0
            res += chr(tres)

        if " the " in res:
            sum = 0
            for ch in res:
                sum += ord(ch)
            print(res)
            print(sum)


        password[0] = chr(ord(password[0])+1)
        if ord(password[0]) > ord('z'):
            password[1] = chr(ord(password[1]) + 1)
            password[0] = 'a'
            if ord(password[1]) > ord('z'):
                password[2] = chr(ord(password[2]) + 1)
                password[1] = 'a'
                if ord(password[2]) > ord('z'):
                    break


