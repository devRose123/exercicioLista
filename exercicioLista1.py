lista = []
soma = 0
mult = 1
maior = 0
menor = 0
while True:
    numero = int(input("Digite um número para lista (Para sair digite 0)"))
    if(numero==0):
        print(lista)
        break
    else:
        lista.append(numero)
        continue

for num in lista:
    soma = soma+num
    mult = mult*num

    if(num==lista[0]):
        maior= num
        menor = num
    elif(num>maior):
        maior = num
    elif(num < menor):
        menor = num




print(f" O Resultado da soma é: {soma}, o Resultado da multiplicação é: {mult}\n")
print(f" O maior número é: {maior} o menor número é: {menor}")





