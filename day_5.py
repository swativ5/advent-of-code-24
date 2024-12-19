f = open("input/day5_input.txt", "r")
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
for row in values:
    value = [int(v) for v in row.split(",")]
    if check_valid_row(value):
        m = len(value) // 2
        sum += value[m]
print(sum)


# Part 2
def isLessThan(a, b):
    for condition in c:
        if a in condition and b in condition:
            if a == condition[0] and b == condition[1]:
                return True
            if b == condition[0] and a == condition[1]:
                return False
    return 0;

def customSort(record):
    temp = 0
    for i in range(len(record)):
        for j in range(i + 1, len(record)):
            if not isLessThan(record[i], record[j]):
                record[i], record[j] = record[j], record[i]
    return record


sum = 0
for row in values:
    value = [int(v) for v in row.split(",")]
    if not check_valid_row(value):
        corrected_row = customSort(value)
        m = len(corrected_row) // 2
        sum += corrected_row[m]
print(sum)
#5377
#5200