
# Part 1
f = open("input/day2_input.txt", "r")
txtinput = f.read().split("\n")
input = []
for i in range(len(txtinput) - 1):
    value = txtinput[i].split()
    for j in range(len(value)):
        value[j] = int(value[j])
    input.append(value)

# input = [[7,6,4,2,1],
#          [1, 2, 7, 8, 9],
#          [9, 7, 6, 2, 1],
#          [1, 3, 2, 4, 5],
#          [8, 6, 4, 4, 1],
#          [1, 3, 6, 7, 9]]

def is_safe(row):
    increasing = all(row[i] < row[i+1] for i in range(len(row)-1))
    decreasing = all(row[i] > row[i+1] for i in range(len(row)-1))

    if not (increasing or decreasing):
        return False

    for i in range(len(row) - 1):
        difference = row[i] - row[i+1]
        if abs(difference) > 3 or abs(difference) < 1:
            return False
    return True

# Part 1
count = 0
for r in range(len(input)):
    row = input[r]
    value =  is_safe(row)
    count += 1 if value else 0
print(count)

# Part 2
count = 0
for r in range(len(input)):
    row = input[r]
    value =  is_safe(row)
    if not value:
        for i in range(len(row)):
            mrow = row[:i] + row[i+1:]
            if is_safe(mrow):
                value = True
    count += 1 if value else 0
print(count)