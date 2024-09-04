# Inicializa duas listas vazias que são referenciadas pela mesma variável
lista = lista2 = []

print("Digite [-1] para sair.")

while True:
    try:
        # Solicita ao usuário um número e tenta converter para inteiro
        n = int(input("Digite um número: "))
    except ValueError:
        # Captura erros de conversão e continua o loop
        print("Por favor, digite um número válido.")
        continue

    if n == -1:
        # Encerra o loop se o número digitado for -1
        break
    else:
        # Adiciona o número à lista
        lista.append(n)

# Exibe a lista e realiza cálculos
print("\nLista:", lista)
print("Quantidade de Elementos:", len(lista))
print("Soma:", sum(lista))
print("Maior valor:", max(lista), "\tMenor valor:", min(lista))

# Verifica se um número está na lista
n2 = int(input("\nDigite um número para ver se está na lista: "))
if n2 in lista:
    print(f"Está na lista na posição {lista.index(n2)}.")
else:
    print("Não está na lista.")

# Ordena a lista e imprime em ordem crescente
lista.sort()
print("\nOrdem crescente:", lista)

# Insere o número 33 na segunda posição da lista
lista.insert(1, 33)
print("Com 33:", lista)

# Inverte a ordem da lista e imprime em ordem decrescente
lista.reverse()
print("Ordem decrescente:", lista)

# Calcula e imprime a média dos valores na lista
media = sum(lista) / len(lista)
print(f"\nMédia: {media:.3f}")

# Conta e imprime a porcentagem de valores maiores que 10
maior_que_10 = 0
for x in lista:
    if x > 10:
        maior_que_10 += 1
print(f"Maior que 10: {(maior_que_10 / len(lista)) * 100:.2f}%")