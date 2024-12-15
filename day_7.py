f = open("day7_input.txt", "r")
text = f.read().strip().split("\n")
records = []
for record in text:
    answer, numbers_str = record.split(":")
    numbers_int = [int(number) for number in numbers_str.strip().split()]
    records.append([int(answer.strip()), numbers_int])
# for answer, numbers in records:
#     print(answer, numbers)

def evaluate(numbers, operations):
    sum = 0
    numbers = list(numbers)
    while numbers and operations:
        n1 = numbers.pop(0)
        n2 = numbers.pop(0)
        op =  operations.pop(0)
        if op == "+":
            sum = (n1 + n2)
        else:
            sum = (n1 * n2)
        numbers.insert(0, sum)
    return sum

print(evaluate([81,40,27], ["*","+"]))

def check_valid(answer, numbers):

    # star = 0
    # operations = []
    # for star in range(len(numbers) - 1):


    # n = 5
    # for i in range(n):
    #     for j in range(i, n):
    #         print(j,end="")
    #     print()
    pass
check_valid(0,0)

# 01234
# 1234
# 234
# 34
# 4

def print_boolean():
    pass