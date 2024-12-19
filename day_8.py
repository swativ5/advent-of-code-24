f = open("day8_input.txt", "r")
raw_grid = f.read().strip()
raw_grid = raw_grid.split("\n")
grid = [list(row) for row in raw_grid]
rows = len(grid)
cols = len(grid[0])

antennas = {}

for r in range(rows):
    for c in range(cols):
        char = grid[r][c]
        if char != ".":
            if char not in antennas:
                antennas[char] = []
            antennas[char].append((r, c))

antinodes = set()

for coords in antennas.values():
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            r1, c1 = coords[i]
            r2, c2 = coords[j]
            # midpoint r1 = ((ar1 + r2) / 2, (ac1 + c2) / 2))
            # antinode a1 (ar1, ac1) = (((2 * r1) - r2), ((2 * c1) - c2))
            antinodes.add(((2 * r1) - r2, (2 * c1) - c2))
            antinodes.add(((2 * r2) - r1, (2 * c2) - c1))

valid = 0
for r, c in antinodes:
    if 0 <= r < rows and 0 <= c < cols:
        valid += 1

print(valid)


antinodes = set()
for coords in antennas.values():
    for i in range(len(coords)):
        for j in range(len(coords)):
            if i == j: continue
            r1, c1 = coords[i]
            r2, c2 = coords[j]
            dr = r2 - r1
            dc = c2 - c1
            r = r1
            c = c1
            while 0 <= r < rows and 0 <= c < cols:
                antinodes.add((r, c))
                r += dr
                c += dc
            r = r1
            c = c1
            while 0 <= r < rows and 0 <= c < cols:
                antinodes.add((r, c))
                r -= dr
                c -= dc
            
print(len(antinodes))