def combination(start, length, lst = []):
    print(lst)

    for i in range(start, length):


        combination(i + 1, length, lst + [pair[i]])






line = list(input())

pair = []

stack = []

answer = []

for index in range(len(line)):
    if line[index] == "(":
        stack.append(index)
    elif line[index] == ")":
        first = stack.pop()
        pair.append((first, index))

combination(0, len(pair))
