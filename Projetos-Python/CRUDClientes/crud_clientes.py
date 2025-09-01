clientes = []

def adicionar(nome, email):
    clientes.append({"nome": nome, "email": email})
    print("Cliente adicionado!")

def listar():
    for i, c in enumerate(clientes, 1):
        print(f"{i}. {c['nome']} - {c['email']}")

def remover(indice):
    if 0 < indice <= len(clientes):
        clientes.pop(indice - 1)
        print("Cliente removido!")
    else:
        print("Índice inválido.")

adicionar("João", "joao@email.com")
adicionar("Maria", "maria@email.com")
listar()
remover(1)
listar()