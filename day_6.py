turn = {"up":"left",
        "down":"right",
        "left":"down",
        "right":"up"
        }

direction_dict = {"up": [0, -1],
                  "down": [0, 1],
                  "left": [1, 0],
                  "right": [-1, 0]
                  }

def find_direction(s):
    if s == "^":
        return "up"
    elif s == ">":
        return "right"
    elif s == "<":
        return "left"
    elif s == "v":
        return "down"

def move_a_step(c_direction, current):
    x, y = current
    dx, dy = direction_dict[c_direction]
    nx, ny = x + dy, y + dx
    return (nx, ny)

def turn_right(c_direction):
    return turn[c_direction]

def find_start(block):
    for row in range(len(block)):
        for col in range(len(block[0])):
            c = block[row][col]
            if c != "." and c != "#":
                return (row, col)

def is_cycle(block, c_direction, current):
    visited = set()
    x, y = current
    visited.add((x, y))
    direction = c_direction

    while safe(x, y):
        nx, ny = move_a_step(direction, (x, y))
        if not safe(nx, ny):
            return False

        c = block[nx][ny]
        if c == "#" or c == "O":
            direction = turn_right(direction)

        x, y = move_a_step(direction, (x, y))
        if (x, y) in visited:
            return True
        visited.add((x, y))

    return False




f = open("day6_input.txt", "r")
raw_block = f.read().strip()
raw_block = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""
raw_block = [list(row) for row in raw_block.splitlines()]



x, y = find_start(raw_block)
direction = find_direction(raw_block[x][y])
print("start", x, y, direction)
length, width = len(raw_block[0]), len(raw_block)

def safe(cx, cy, length = len(raw_block[0]), width = len(raw_block)):
    if 0 <= cx < width and 0 <= cy < length:
        return True
    return False


# print("Part 1")
# visited = set()
# visited.add((x,y))

# while safe(x, y):
#     nx, ny = move_a_step(direction, (x,y))
#     if not safe(nx,ny):
#         break
#     c = raw_block[nx][ny]
#     if c == "#":
#         direction = turn_right(direction)
#     # raw_block[x][y] = "."
#     x, y = move_a_step(direction, (x,y))
#     raw_block[x][y] = "^"
#     visited.add((x,y))
#     for i in raw_block:
#         print(i)
#     print()
# print(len(visited))


print("part 2")

count = 0
obstacles = set()
while safe(x, y):
    nx, ny = move_a_step(direction, (x,y))
    if not safe(nx,ny):
        break
    c = raw_block[nx][ny]
    
    new_block = [list(row) for row in raw_block]
    new_block[nx][ny] = "O"
    if (nx, ny) not in obstacles and is_cycle(new_block, direction, (nx,ny)):
        count += 1
        obstacles.add((nx,ny))

    if c == "#" or c == "O":
        direction = turn_right(direction)
    x, y = move_a_step(direction, (x,y))


print(len(obstacles))
