lista = []
repeticao = 0
while True:
    palavras = input("Digite uma palavra (Zero para finalizar)")
    if (palavras == "0"):
        #print(palavras)
        break
    else:
        lista.append(palavras)
        continue

busca = input("Informa a palavra que deseja contar:")

qtd_palavra = lista.count(busca)

print(f"Temos {qtd_palavra} ocorrência de {busca}")
