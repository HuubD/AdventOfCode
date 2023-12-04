import re

total = 0

with open('input.txt') as f:
    for line in f:
        numbers = re.findall(r'\d+', line)
        
        firstChar = numbers[0][0]
        lastChar = numbers[-1][-1]
    
        fullNumber = firstChar + lastChar
        total += int(fullNumber)

print(total)