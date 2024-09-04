# Cria uma lista com números de 1 a 20
lista = list(range(1, 21))

# Cria uma cópia da lista original
nova_lista = lista[:]
print("Cópia Lista:", nova_lista)

# Cria uma lista com a ordem inversa dos elementos
lista_inversa = lista[::-1]
print("\nLista Inversa:", lista_inversa)

# Cria uma lista com elementos nos índices ímpares da lista original
lista_pares = lista[1::2]
print("\nLista Pares:", lista_pares)

# Cria uma lista com elementos nos índices pares da lista original em ordem decrescente
lista_pares_decrescente = lista[::-2]
print("\nLista Pares Decrescente:", lista_pares_decrescente)

# Cria uma lista com elementos nos índices pares da lista original
lista_impares = lista[::2]
print("\nLista Impares:", lista_impares)

# Cria uma lista com elementos nos índices pares da lista original em ordem decrescente
lista_impares_decrescente = lista[::-2]
print("\nLista Impares Decrescente:", lista_impares_decrescente)

# Cria uma lista com elementos múltiplos de 3, começando a partir do terceiro elemento
lista_multiplo_3 = lista[2::3]
print("\nLista Multiplos de 3:", lista_multiplo_3)

# Cria uma lista com elementos múltiplos de 5, começando a partir do quinto elemento
lista_multiplo_5 = lista[4::5]
print("\nLista Multiplos de 5:", lista_multiplo_5)

# Cria uma lista com elementos que são múltiplos de 3 e ímpares, começando a partir do terceiro elemento
lista_3_impar = lista[2::6]
print("\nLista Multiplos de 3 ímpares", lista_3_impar)
