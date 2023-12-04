# Open file and loop through each line
with open('input.txt') as f:
    idSum = 0
    for game in f:
        gameId = game.split(':')[0]
        game = game.split(':')[1].strip()
        possible = True

        gameRounds = game.split(';')

        # Loop through all cubes and check if the count is valid
        for gameRound in gameRounds:
            for cube in gameRound.split(','):
                cube = cube.strip()
                color = cube.split(' ')[1]
                count = int(cube.split(' ')[0])

                if color == 'red' and count > 12:
                    possible = False
                    break
                elif color == 'green' and count > 13:
                    possible = False
                    break
                elif color == 'blue' and count > 14:
                    possible = False
                    break

        if possible:
            idSum += int(gameId.split(' ')[1])
       
    print(idSum) 