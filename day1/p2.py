sum = 0

while True:
    str = input()
    if str == "":
        break

    numbers = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}
    first = 0
    # one
    # two, three, ten
    # four, five
    # six, seven
    # eight
    # nine
    # 0 1
    # 0 + 3 = 3 - 1
    for i in range(len(str)):
        if str[i] == "o" and i + 3 - 1 < len(str):
            if str[i+1] == "n" and str[i+2] == "e":
                first = 1
                break
        if str[i] == "t" and i + 3 - 1 < len(str):
            if str[i+1] == "w" and str[i+2] == "o":
                first = 2
                break
            if str[i+1] == "e" and str[i+2] == "n":
                first = 10
                break
        if str[i] == "t" and i + 5 - 1 < len(str):
            if str[i+1] == "h" and str[i+2] == "r" and str[i+3] == "e" and str[i+4] == "e":
                first = 3
                break
        if str[i] == "f" and i + 4 - 1 < len(str):
            if str[i+1] == "o" and str[i+2] == "u" and str[i+3] == "r":
                first = 4
                break
            if str[i+1] == "i" and str[i+2] == "v" and str[i+3] == "e":
                first = 5
                break
        if str[i] == "s" and i + 3 - 1 < len(str):
            if str[i+1] == "i" and str[i+2] == "x":
                first = 6
                break
        if str[i] == "s" and i + 5 - 1 < len(str):
            if str[i+1] == "e" and str[i+2] == "v" and str[i+3] == "e" and str[i+4] == "n":
                first = 7
                break
        if str[i] == "e" and i + 5 - 1 < len(str):
            if str[i+1] == "i" and str[i+2] == "g" and str[i+3] == "h" and str[i+4] == "t":
                first = 8
                break
        if str[i] == "n" and i + 4 - 1 < len(str):
            if str[i+1] == "i" and str[i+2] == "n" and str[i+3] == "e":
                first = 9
                break

        if str[i] in numbers:
            first = int(str[i])
            break
    # one
    # two, three, ten
    # four, five
    # six, seven
    # eight
    # nine
    # 0 1
    #
    second = 0
    for i in range(len(str) - 1, -1, -1):
        if str[i] == "e" and i - 3 + 1 >= 0:
            if str[i-1] == "n" and str[i-2] == "o":
                second = 1
                break
        if str[i] == "o" and i - 3 + 1 >= 0:
            if str[i-1] == "w" and str[i-2] == "t":
                second = 2
                break
        if str[i] == "e" and i - 5 + 1 >= 0:
            if str[i-1] == "e" and str[i-2] == "r" and str[i-3] == "h" and str[i-4] == "t":
                second = 3
                break
        if str[i] == "r" and i - 4 + 1 >= 0:
            if str[i-1] == "u" and str[i-2] == "o" and str[i-3] == "f":
                second = 4
                break
        if str[i] == "e" and i - 4 + 1 >= 0:
            if str[i-1] == "v" and str[i-2] == "i" and str[i-3] == "f":
                second = 5
                break
        if str[i] == "x" and i - 3 + 1 >= 0:
            if str[i-1] == "i" and str[i-2] == "s":
                second = 6
                break
        if str[i] == "n" and i - 5 + 1 >= 0:
            if str[i-1] == "e" and str[i-2] == "v" and str[i-3] == "e" and str[i-4] == "s":
                second = 7
                break
        if str[i] == "t" and i - 5 + 1 >= 0:
            if str[i-1] == "h" and str[i-2] == "g" and str[i-3] == "i" and str[i-4] == "e":
                second = 8
                break
        if str[i] == "e" and i - 4 + 1 >= 0:
            if str[i-1] == "n" and str[i-2] == "i" and str[i-3] == "n":
                second = 9
                break

        if str[i] in numbers:
            second = int(str[i])
            break
    num = (first * 10) + second
    sum += num
print(sum)
