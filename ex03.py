vetor = []
valores = 0
maior = 0
pares = []
impares = []

while True:
    valores = int(input('Informe um valor:'))
    vetor.append(valores)
    if valores < 0:
        break
    if valores > 5:
        maior += 1
    if valores % 2 == 0:
        pares.append(valores)
    elif valores % 2 != 0:
        impares.append(valores)


print(vetor)
print('-' * 30)
print(f'Quantidade de valores maiores que 5 é {maior}')
print('-' * 30)
print(f'A soma dos valores pares é {sum(pares)}')
print('-' * 30)
print(f'A soma dos valores ímpares é {sum(impares)}')
print('-' * 30)
print(f'A quantidade total do valores é {len(vetor)}')