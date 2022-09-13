def sugar(C, Kg, sec):
    div = (N // Kg) - C
    if div == 0:
        if Kg == 5:
            return sugar(0, 3, 5)
        elif Kg == 3:
            return -1
    elif (N % (Kg * div)) % sec == 0:
        return div + N % (Kg * div) // sec
    else:
        return sugar(C + 1, Kg, sec)

N = int(input())
print(sugar(0, 5, 3))