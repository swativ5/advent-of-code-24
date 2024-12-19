f = open("input/day7_input.txt", "r")
text = f.read()
# text = """190: 10 19
# 3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20"""
text = text.strip().split("\n")
records = []
for record in text:
    answer, numbers_str = record.split(":")
    numbers_int = [int(number) for number in numbers_str.strip().split()]
    records.append([int(answer.strip()), numbers_int])

def evaluate(numbers, operation):
    sum = 0
    numbers = list(numbers)
    while numbers and operation:
        n1 = numbers.pop(0)
        n2 = numbers.pop(0)
        op =  operation.pop(0)
        if op == "+":
            sum = (n1 + n2)
        elif op == "*":
            sum = (n1 * n2)
        else:
            sum = int(str(n1)+str(n2))
        numbers.insert(0, sum)
    return sum

def generate_operations(n):
    result = []
    for i in range(2 ** n):
        binary_representation = format(i, f'0{n}b')
        result.append(binary_representation)
    ops = []
    for val in result:
        op = list()
        for c in val:
            if c == '0':
                op.append("+")
            else:
                op.append("*")
        ops.append(op)
    return ops

def check_valid(answer, record):
    operations = generate_operations(len(record) - 1)
    for operation in operations:
        if answer == evaluate(record, operation):
            return True
    return False

sum = 0
for answer, record in records:
    if check_valid(answer, record):
        sum += answer
print(sum)


def check_valid_2(answer, record):
    operations = generate_operations_2(len(record) - 1)
    for operation in operations:
        if answer == evaluate(record, operation):
            return True
    return False


def generate_operations_2(n):
    queue = []
    queue.append("+")
    queue.append("*")
    queue.append("|")
    
    count = 1

    while len(queue) < (3**n):
        element = queue.pop(0)
        queue.append(element+"+")
        queue.append(element+"*")
        queue.append(element+"|")
        count += 2
    
    ops = []
    for val in queue:
        op = list()
        for c in val:
            op.append(c)
        ops.append(op)
    return ops

sum = 0
for answer, record in records:
    if check_valid_2(answer, record):
        sum += answer
print(sum)