vetor = []

for i in range(15):
    vetor.append(int(input('Digite um número: ')))
if 0 in vetor:
    vetor.remove(0)
print(vetor)