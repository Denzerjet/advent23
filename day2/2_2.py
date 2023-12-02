sum = 0

while True:
    red_max = -1
    green_max = -1
    blue_max = -1
    str = input()
    if str == "":
        break

    game, hands = str.split(":")
    #game_num = int(game[5: ])

    for rolls in hands.split(";"):
        for cube_type in rolls.split(","):
            cube_type = cube_type[1: ]
            num_type, color_type = cube_type.split(" ")
            num_type = int(num_type)

            if color_type == "blue":
                if num_type > blue_max:
                    blue_max = num_type
            if color_type == "green":
                if num_type > green_max:
                    green_max = num_type
            if color_type == "red":
                if num_type > red_max:
                    red_max = num_type

    power = (blue_max * red_max * green_max)
    sum += power
print(sum)
