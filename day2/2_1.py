sum = 0
while True:
    str = input()
    if str == "":
        break

    game, hands = str.split(":")
    game_num = int(game[5: ])

    possible = True

    for rolls in hands.split(";"):
        for cube_type in rolls.split(","):
            cube_type = cube_type[1: ]
            num_type, color_type = cube_type.split(" ")
            num_type = int(num_type)

            if color_type == "blue":
                if num_type > 14:
                    possible = False
            if color_type == "green":
                if num_type > 13:
                    possible = False
            if color_type == "red":
                if num_type > 12:
                    possible = False

    if possible:
        sum += game_num
print(sum)
