import re

total = 0
strNumbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

with open('input.txt') as f:
    for line in f:
        indexes = []

        for strNumber in strNumbers:
            matches = re.finditer(strNumber, line)
            indexes.extend([{'value': strNumber, 'index': match.start()} for match in matches])

        for index, char in enumerate(line):
            if char.isdigit():
                indexes.append({'value': char, 'index': index})

        if indexes:
            first = min(indexes, key=lambda x: x['index'])
            last = max(indexes, key=lambda x: x['index'])

            firstChar = first['value']
            lastChar = last['value']

            if firstChar.isdigit() and lastChar.isdigit():
                fullNumber = firstChar + lastChar
            elif not firstChar.isdigit() and lastChar.isdigit():
                fullNumber = str(strNumbers.index(firstChar) + 1) + lastChar
            elif firstChar.isdigit() and not lastChar.isdigit():
                fullNumber = firstChar + str(strNumbers.index(lastChar) + 1)
            else:
                fullNumber = str(strNumbers.index(firstChar) + 1) + str(strNumbers.index(lastChar) + 1)
        
            total += int(fullNumber)
print(total)