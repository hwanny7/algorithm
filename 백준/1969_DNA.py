N, M = map(int, input().split()) # 유전자 갯수, 길이
dna = [input() for _ in range(N)]

sentence = ''
count = 0
for i in range(M):
    dic = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for j in range(N):
        dic[dna[j][i]] += 1

    c = 0
    s = ''
    total = 0

    for spell, cnt in dic.items():
        total += cnt
        if c < cnt:
            c = cnt
            s = spell

    sentence += s
    count += total - c

print(sentence)
print(count)






