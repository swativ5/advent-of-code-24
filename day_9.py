from queue import PriorityQueue

f = open("input/day9_input.txt", "r")
puzzle = f.read().strip()
puzzle = "2333133121414131402"

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

memory = []
id = 0
for index in range(0, len(puzzle) - 1, 2):
    block = []
    for _ in range(int(puzzle[index])):
        block.append(str(id))
    if block != []:
        memory.append(block)
    free = []
    for _ in range(int(puzzle[index + 1])):
        free.append(".")
    if free != []:
        memory.append(free)
    id += 1
block = []
for _ in range(int(puzzle[len(puzzle) - 1])):
    block.append(str(id))
if block != []:
    memory.append(block)
print(memory)

pq = PriorityQueue()
for index in range(len(memory)):
    if memory[index][0] == ".":
        pq.put(index)

for mindex in range(len(memory) - 1, -1, -1):
    if memory[mindex][0] == ".":
        continue
    print(memory[mindex])
    pindex = pq.get(0)
    
    plen = memory[pindex]
    mlen = memory[mindex]

    pass
print(memory)
# 00 99 2111777.44.333....5555.6666.....8888..
