sum = 0

while True:
    str = input()
    if str == "":
        break
    
    numbers = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}
    first = 0
    for i in range(len(str)):
        if str[i] in numbers:
            first = int(str[i])
            break
    second = 0
    for i in range(len(str) - 1, -1, -1):
        if str[i] in numbers:
            second = int(str[i])
            break
    num = (first * 10) + second
    sum += num
print(sum)
