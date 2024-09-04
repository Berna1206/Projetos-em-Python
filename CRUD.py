# Lista global para armazenar nomes
l_nome = []

def menu():
    """
    Exibe o menu de opções para o usuário.
    """
    print("[c] - Create")  # Opção para criar (adicionar) um novo nome
    print("[r] - Read")    # Opção para ler (exibir) a lista de nomes
    print("[u] - Update")  # Opção para atualizar (alterar) um nome existente
    print("[d] - Delete")  # Opção para deletar um nome existente
    print("[e] - Exit")    # Opção para sair do programa
    opcao = input("Opção: ")  # Captura a opção escolhida pelo usuário
    return opcao

def create():
    """
    Adiciona um novo nome à lista l_nome.
    """
    nome = input("Nome: ")  # Captura o nome a ser adicionado
    l_nome.append(nome)     # Adiciona o nome à lista

def read():
    """
    Exibe a lista de nomes armazenados em l_nome.
    """
    print(l_nome)  # Imprime a lista de nomes

def update():
    """
    Atualiza um nome existente na lista l_nome.
    """
    try:
        antigo = int(input("Posição do Item: "))  # Captura a posição do item a ser atualizado
        if antigo < 0 or antigo >= len(l_nome):  # Verifica se a posição é válida
            print("Posição inválida.")
            return
        novo = input("Novo Item: ")  # Captura o novo nome
        l_nome[antigo] = novo  # Atualiza o nome na posição especificada
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")

def delete():
    """
    Remove um nome da lista l_nome.
    """
    remover = input("Remover Item: ")  # Captura o nome a ser removido
    if remover in l_nome:  # Verifica se o nome está na lista
        l_nome.remove(remover)  # Remove o nome da lista
    else:
        print("O item não está na lista.")  # Mensagem de erro se o nome não for encontrado

if __name__ == '__main__':
    """
    Loop principal do programa que exibe o menu e executa a opção escolhida pelo usuário.
    """
    while True:
        op = menu()  # Exibe o menu e obtém a opção do usuário
        if op == "c":
            create()  # Cria um novo nome
        elif op == "r":
            read()  # Lê e exibe a lista de nomes
        elif op == "u":
            update()  # Atualiza um nome existente
        elif op == "d":
            delete()  # Deleta um nome existente
        elif op == "e":
            break  # Encerra o loop e o programa
        else:
            print("Opção inválida.")  # Mensagem de erro para opções não reconhecidas
