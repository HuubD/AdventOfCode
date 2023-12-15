def part1():
    with open("input.txt") as file:
        result = 0
        value = 0

        while 1:
            char = file.read(1)
            if char == ',':
                result += value
                value = 0
            elif not char:
                result += value
                value = 0
                break
            else:
                value += ord(char)
                value *= 17
                value %= 256
                
        print(result)

# part1()

def part2():
    with open("test.txt") as file:
        i = 0
        boxes = []
        while i < 256:
            boxes.append([])
            i += 1

        result = 0
        value = 0
        string = ''

        while 1:
            char = file.read(1)
            if char == ',':
                result += value
                value = 0
            elif char == '=':
                char = file.read(1)
                string += ' ' + char
                boxes[value].append(string)
                print(string)
                print(boxes)
                string = ''
            elif char == '-':
                filtered = [x for x in boxes[value] if not string in x]
                boxes[value] = filtered
                print(string)
                print(boxes)
                string = ''
            elif not char:
                result += value
                value = 0
                break
            else:
                string += char
                value += ord(char)
                value *= 17
                value %= 256
                
        print(result)

part2()