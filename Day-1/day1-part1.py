import re

total = 0

with open('input.txt') as f:
    for line in f:
        numbers = re.findall(r'\d+', line)

        first = numbers[0]
        last = numbers[-1]
        
        firstChar = first[0]
        lastChar = last[-1]
    

        fullNumber = firstChar + lastChar
        total += int(fullNumber)

        
print(total)