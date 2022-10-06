lista = []
repetidos = set()
naoRepetido = []
while True:
    numero = int(input("Digite um número para lista (Para sair digite 0)"))
    if (numero == 0):

        break
    else:
        lista.append(numero)
        continue


for dado in lista:
    if dado not in naoRepetido:
        naoRepetido.append(dado)
    else:
        repetidos.add(dado)

print(f'Números informados: {lista}')
print(f'Números sem repetição: {naoRepetido}')
print(f'Somente números que se repetiram:  {repetidos}')


