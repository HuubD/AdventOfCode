result = 0

with open('test.txt') as f:
    copies = []
    gameIndex = -1
    for line in f:
        x = 0
        i = 0
        winNumsCount = 0
        game = line.split(': ')[1].strip()
        winNums = game.split(' | ')[0].split(' ')
        myNums = game.split(' | ')[1].split(' ')

        while '' in winNums:
            winNums.remove('')

        while '' in myNums:
            myNums.remove('')

        for myNum in myNums:
            if myNum in winNums:
                winNumsCount += 1

        if len(copies) > 0:
            while x < 1 + copies[gameIndex]:
                print(copies)
                i = 0
                while i < winNumsCount:
                    if gameIndex + i < len(copies):
                        copies[gameIndex + i] += 1
                    else:
                        copies.append(1)
                    
                    i += 1
                x += 1
        else:
            while i < winNumsCount:
                copies.append(1)
                i += 1

        print(copies)

        gameIndex += 1

print("Result:", result)
