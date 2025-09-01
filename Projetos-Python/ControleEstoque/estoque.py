estoque = {
    "Parafuso": 100,
    "Porca": 150,
    "Arruela": 200
}

def entrada(produto, quantidade):
    estoque[produto] += quantidade
    print(f"{quantidade} unidades de {produto} adicionadas.")

def saida(produto, quantidade):
    if estoque[produto] >= quantidade:
        estoque[produto] -= quantidade
        print(f"{quantidade} unidades de {produto} retiradas.")
    else:
        print(f"Estoque insuficiente de {produto}.")

entrada("Parafuso", 50)
saida("Porca", 20)
print("Estoque atual:", estoque)