import pandas as pd

# Lê uma planilha de vendas
df = pd.read_excel("vendas.xlsx")

# Calcula o total vendido por produto
resumo = df.groupby("Produto")["Valor"].sum().reset_index()

# Salva em uma nova planilha
resumo.to_excel("resumo_vendas.xlsx", index=False)

print("Resumo gerado com sucesso!")