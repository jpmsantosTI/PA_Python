# Definir as porcentagens fixas
IMPOSTOS = 0.45  # 45% de impostos
DISTRIBUIDOR = 0.28  # 28% do distribuidor

# Entrada do usuário
custo_fabrica = float(input("Digite o custo de fábrica do carro: R$ "))

# Cálculo dos impostos
valor_impostos = custo_fabrica * IMPOSTOS
custo_com_impostos = custo_fabrica + valor_impostos

# Cálculo do distribuidor
valor_distribuidor = custo_com_impostos * DISTRIBUIDOR
custo_final = custo_com_impostos + valor_distribuidor

# Exibir resultados
print("\nCálculo do custo ao consumidor:")
print("Custo de fábrica: R$", custo_fabrica)
print("Impostos (45%): R$", valor_impostos, "(Total: R$", custo_com_impostos, ")")
print("Distribuição (28%): R$", valor_distribuidor, "(Total: R$", custo_final, ")")
print("Preço final ao consumidor: R$", custo_final)