vetor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
vetor2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

vetor = [0] * 10

for i in range(len(vetor)):
    if i % 2 == 0:
        vetor[i] = vetor1[i]
    if i % 2 != 0:
        vetor[i] = vetor2[i]

print(vetor)