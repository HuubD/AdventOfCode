import re

total = 0
strNumbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

# Open file and loop through each line
with open('input.txt') as f:
    for line in f:
        indexes = []

        # Find all written numbers in the line
        for strNumber in strNumbers:
            matches = re.finditer(strNumber, line)
            indexes.extend([{'value': strNumber, 'index': match.start()} for match in matches])

        # Find all numbers in the line
        for index, char in enumerate(line):
            if char.isdigit():
                indexes.append({'value': char, 'index': index})

        if indexes:
            first = min(indexes, key=lambda x: x['index'])['value']
            last = max(indexes, key=lambda x: x['index'])['value']

            # Concatenate the first and last numbers
            if first.isdigit() and last.isdigit():
                fullNumber = first + last
            elif not first.isdigit() and last.isdigit():
                fullNumber = str(strNumbers.index(first) + 1) + last
            elif first.isdigit() and not last.isdigit():
                fullNumber = first + str(strNumbers.index(last) + 1)
            else:
                fullNumber = str(strNumbers.index(first) + 1) + str(strNumbers.index(last) + 1)
        
            total += int(fullNumber)
print(total)