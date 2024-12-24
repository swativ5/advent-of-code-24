from queue import PriorityQueue

f = open("input/day9_input.txt", "r")
puzzle = f.read().strip()
# puzzle = "2333133121414131402"

def part1():
    memory = []
    id = 0
    for index in range(0, len(puzzle) - 1, 2):
        for _ in range(int(puzzle[index])):
            memory.append(id)
        for _ in range(int(puzzle[index + 1])):
            memory.append(".")
        id += 1
    for _ in range(int(puzzle[len(puzzle) - 1])):
        memory.append(id)

    pq = PriorityQueue()
    for index in range(len(memory)):
        if memory[index] == ".":
            pq.put(index)

    for index in range(len(memory) - 1, -1, -1):
        if memory[index] != "." and pq:
            new_index = pq.get(0)
            memory[new_index] = memory[index]
            memory[index] = "."
            pq.put(index)

    disk = [value for value in memory if value != "."]

    s = sum(index * disk[index] for index in range(len(disk)))

    print(s)

part1()

files = {}
blanks = []

id = 0
position = 0

for i in range(len(puzzle)):
    char = puzzle[i]
    x = int(char)
    if i % 2 == 0:
        files[id] = (position, x)
        id += 1
    else:
        blanks.append((position, x))
    position += x


while id > 0:
    id -= 1
    position, size = files[id]
    for i in range(len(blanks)):
        start, length = blanks[i]
        if start >= position:
            blanks = blanks[:i]
            break
        if size <= length:
            files[id] = (start, size)
            if size == length:
                blanks.pop(i)
            else:
                blanks[i] = (start + size, length - size)
            break
total = 0

for id, (position, size) in files.items():
    for x in range(position, position + size):
        total += id * x

print(total)
#6398065450842