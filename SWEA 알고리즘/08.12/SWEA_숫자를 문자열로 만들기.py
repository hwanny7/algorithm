def itoa(n):
    lst = []
    while n != 0:
        lst.append(chr(n % 10 + 48))
        n //= 10
    return(''.join(lst[::-1]))

print(itoa(1555555666667))



