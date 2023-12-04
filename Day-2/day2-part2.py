# Open file and loop through each line
with open('input.txt') as f:
    result = 0
    for game in f:
        redCubes, greenCubes, blueCubes = 0, 0, 0
        gameId = game.split(':')[0]
        game = game.split(':')[1].strip()

        gameRounds = game.split(';')

        # Loop through all cubes and set the max count
        for gameRound in gameRounds:
            for cube in gameRound.split(','):
                cube = cube.strip()
                color = cube.split(' ')[1]
                count = int(cube.split(' ')[0])

                if color == 'red':
                    redCubes = max(redCubes, count)
                elif color == 'green':
                    greenCubes = max(greenCubes, count)
                elif color == 'blue':
                    blueCubes = max(blueCubes, count)
       
        power = redCubes * greenCubes * blueCubes

        result += power
    print(result)