f = open(".gitignore/day4_input.txt","r")
txtinput1 = f.read().split("\n")
txtinput = [list(row) for row in txtinput1]


xmas = "XMAS"
count = 0
rows, cols = len(txtinput), len(txtinput[0])
wlength = len(xmas)


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



def search(x, y, di, dj):
    for i in range(len(xmas)):
        nx, ny = x + (di * i), y + (dj * i)
        if not (0 <= nx < rows and 0 <= ny < cols):
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

