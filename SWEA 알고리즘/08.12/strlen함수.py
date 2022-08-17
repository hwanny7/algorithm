def strlen(arr):

    i = 0
    while arr[i] != '\0':
        i += 1
    return i


arr = ['s', 's', 'a', 'f', 'y', '\0']
print(strlen(arr))
