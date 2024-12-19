f = open("input/day4_input.txt","r")
txtinput1 = f.read().strip().split("\n")
txtinput = [list(row) for row in txtinput1]


xmas = "XMAS"
count = 0
rows, cols = len(txtinput), len(txtinput[0])

d = [
    (-1, 0), #up
    (1, 0), #down
    (0, 1), # right
    (0, -1), #left
    (-1,-1), #diagonal left up
    (1, -1), #diagonal right up
    (1, 1), #diagonal right down
    (-1, 1) #diagonal left down
]


# Part 1
def search(x, y, di, dj):
    for i in range(len(xmas)):
        nx, ny = x + (di * i), y + (dj * i)
        if not 0 <= nx < rows:
            return False
        elif not 0 <= ny < cols:
           return False
        elif txtinput[nx][ny] != xmas[i]:
            return False
    return True

for r in range(rows):
    for c in range(cols):
        for dx, dy in d:
            if search(r, c, dx, dy):
                count += 1
print(count)

# Part 2
# txtinput1 = """.M.S......
# ..A..MSMS.
# .M.S.MAA..
# ..A.ASMSM.
# .M.S.M....
# ..........
# S.S.S.S.S.
# .A.A.A.A..
# M.M.M.M.M.
# .........."""
# txtinput1 = txtinput1.strip().split("\n")
# txtinput = [list(row) for row in txtinput1]
# rows, cols = len(txtinput), len(txtinput[0])
# print("Rows:", rows, "Columns:", cols)


d2 = [(-1,-1), #diagonal left up
    (1, -1), #diagonal right up
    (1, 1), #diagonal right down
    (-1, 1) #diagonal left down
    ]

def search2(x, y):
    nx1, ny1 = x + d2[0][0], y + d2[0][1]
    nx2, ny2 = x + d2[1][0], y + d2[1][1]
    nx3, ny3 = x + d2[2][0], y + d2[2][1]
    nx4, ny4 = x + d2[3][0], y + d2[3][1]

    if txtinput[nx1][ny1] == "M" and txtinput[nx3][ny3] == "S":
        if txtinput[nx2][ny2] == "M" and txtinput[nx4][ny4] == "S":
            return True
        if txtinput[nx2][ny2] == "S" and txtinput[nx4][ny4] == "M":
            return True
    if txtinput[nx1][ny1] == "S" and txtinput[nx3][ny3] == "M":
        if txtinput[nx2][ny2] == "M" and txtinput[nx4][ny4] == "S":
            return True
        if txtinput[nx2][ny2] == "S" and txtinput[nx4][ny4] == "M":
            return True
    return False

def safe(x, y):
    for dx, dy in d2:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < rows and 0 <= ny < cols):
            return False
    return True

count = 0
for r in range(rows):
    for c in range(cols):
        if txtinput[r][c] == "A" and safe(r, c):
            if search2(r, c):
                count += 1
print(count)
