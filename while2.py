# Inicializa listas e contadores
alturas = []
ct_homens = 0
ct_mulheres = 0

print("Digite [0] para sair.")

while True:
    try:
        altura = float(input("Digite a altura: "))
        if altura == 0:
            break
    except ValueError:
        print("Por favor, digite um valor numérico válido para a altura.")
        continue

    genero = input("Digite [m] para masculino ou [f] para feminino: ").strip().lower()
    if genero == 'm':
        ct_homens += 1
    elif genero == 'f':
        ct_mulheres += 1
    else:
        print("Gênero inválido. Digite [m] para masculino ou [f] para feminino.")
        continue

    alturas.append(altura)

# Calcula a maior e menor altura
maior_altura = max(alturas) if alturas else 0
menor_altura = min(alturas) if alturas else 0

print("\nMaior altura do grupo:", maior_altura)
print("Menor altura do grupo:", menor_altura)
print("Quantidade de homens:", ct_homens)
print("Quantidade de mulheres:", ct_mulheres)
