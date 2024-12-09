# Part 1
f = open("day1_input.txt", "r")
txtinput = f.read().split("\n")
lista = []
listb = []
for i in range(len(txtinput) - 1):
    a, b = txtinput[i].split()
    lista.append(int(a))
    listb.append(int(b))
lista.sort()
listb.sort()
distance = 0
for i in range(len(lista)):
    distance += abs(lista[i] - listb[i])
print(distance)

# Part 2
# creating a map because i think thats the best way to find frequency.

hashmap = dict()
for i in range(len(lista)):
    if lista[i] not in hashmap:
        hashmap[lista[i]] = 0
for i in range(len(listb)):
    if listb[i] in hashmap:
        hashmap[listb[i]] = hashmap[listb[i]] + 1
# print(hashmap)
ans = 0
for i in lista:
    #print(i, hashmap[i], i * hashmap[i])
    ans += i * hashmap[i]
print(ans)

