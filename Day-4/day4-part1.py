result = 0

with open('input.txt') as f:
    for line in f:
        gameResult = 0
        game = line.split(': ')[1].strip()
        winNums = game.split(' | ')[0].split(' ')
        myNums = game.split(' | ')[1].split(' ')

        while '' in winNums:
            winNums.remove('')

        while '' in myNums:
            myNums.remove('')

        for myNum in myNums:
            if myNum in winNums:
                if gameResult == 0:
                    gameResult = 1
                else:
                    gameResult *= 2

        result += gameResult
print(result)