vetor = []
repetidos = []

for i in range(10):
    vetor.append(int(input('Informe um número: ')))
for i in vetor:
    vetor.count(i)
    if vetor.count(i) > 1:
        repetidos.append(i)
print(f"Os valores repetidos sao {set(repetidos)}")

