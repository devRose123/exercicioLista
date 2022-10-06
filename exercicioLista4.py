listaPar = []
listaImpar = []

while True:
    numero = int(input("Digite um número para lista (Para sair digite 0)"))

    if(numero==0):
        break
    elif(numero%2==0):
        listaPar.append(numero)
    else:
        listaImpar.append(numero)


print(f"Pares: {listaPar}")
print(f"Impar: {listaImpar}")