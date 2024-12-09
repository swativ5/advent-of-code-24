import re
f = open("day3_input.txt", "r")
txt = f.read()

# Part 1
# txt = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
valid = re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", txt)
answer = 0
for i in valid:
    a, b = i
    answer += int(a)*int(b)
print(answer)

# Part 2
valid = re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)|(do\(\))|(don't\(\))", txt)
n1, n2, condition1, condition2 = [],[],[],[]
for i in valid:
    n1.append(i[0])
    n2.append(i[1])
    condition1.append(i[2])
    condition2.append(i[3])

flag = True
answer = 0
for i in valid:
    if i[3] == "don't()":
        flag = False
        continue
    if i[2] == "do()":
        flag = True
        continue
    if flag:
        a, b = i[0], i[1]
        answer += int(a)*int(b)
print(answer)
