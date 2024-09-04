# Inicializa listas para armazenar números pares e ímpares
numeros_pares = []
numeros_impares = []

print("Digite [0] para sair.")

while True:
    try:
        numero = int(input("Digite um número: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        continue

    if numero == 0:
        break
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)

# Calcula a média dos números pares e ímpares, com checagem para listas vazias
media_pares = sum(numeros_pares) / len(numeros_pares) if numeros_pares else 0
media_impares = sum(numeros_impares) / len(numeros_impares) if numeros_impares else 0

print("♀♂ Média dos números pares:", media_pares)
print("Média dos números ímpares:", media_impares)