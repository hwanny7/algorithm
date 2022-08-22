

n = input()
total = 0
final = 0
for i in range(len(n)):
    if n[i] == '(':
        total += 1
    elif n[i] == ')' and n[i-1] == '(':
        total -= 1
        final += total
    else:
        final += 1
        total -= 1
print(final)