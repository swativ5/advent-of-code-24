f = open("day5_input.txt", "r")
txtinput = f.read().strip()
conditions, values = txtinput.split("\n\n")
conditions, values = conditions.split("\n"), values.split("\n")

c = []
for condition in conditions:
    n1, n2 = condition.split("|")
    c.append([int(n1),int(n2)])

def check_valid_row(value):
    for n1, n2 in c:
        if n1 in value and n2 in value:
            index1, index2 = value.index(n1), value.index(n2)
            if index1 > index2:
                return False
    return True

sum = 0
wrong_rows = []
for row in values:
    value = [int(v) for v in row.split(",")]
    if check_valid_row(value):
        m = len(value) // 2
        sum += value[m]
    else:
        wrong_rows.append(value)
print(sum)


# Part 2
after = dict()
for c1, c2 in c:
    if c1 not in after:
        after[c1] = []
    if c2 not in after:
        after[c2] = []
    after[c1].append(c2)

# may god help i give up
def custom_sort(row):
    pass
