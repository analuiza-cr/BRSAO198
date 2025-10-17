'''Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.'''

# Calculadora de Desconto

# Variáveis
nome_produto = "Camiseta"  # Nome do produto
preco_original = 50.00     # Preço original em reais
porcentagem_desconto = 20  # Porcentagem de desconto

# Cálculos
valor_desconto = (preco_original * porcentagem_desconto) / 100  # Calcula o valor do desconto
preco_final = preco_original - valor_desconto  # Calcula o preço final

# Arredonda os valores para duas casas decimais (para moeda)
valor_desconto = round(valor_desconto, 2)
preco_final = round(preco_final, 2)

# Resultados
print(f"Nome do produto: {nome_produto}")
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Porcentagem de desconto: {porcentagem_desconto}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")
