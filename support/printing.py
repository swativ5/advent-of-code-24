f = open("day6_input.txt")
text = f.read().strip().split("\n")
#print(text)
for r in range(len(text)):
    row = text[r]
    print("{", end = "")
    for c in range(len(row)):        
        char = row[c]
        if c == len(row) - 1:
            print("'",char,"'", end="")
            continue
        print("'",char,"',", end="")
    print("},")
print(len(text))
print(len(text[0]))
s = "........#.............................#......#................#..................#..................#.........#.#.#..............."
print(len(s))