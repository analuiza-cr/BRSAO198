'''Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.'''

# Conversor de Moeda

# Variáveis
valor_reais = 100.00  # Valor em reais
taxa_dolar = 5.20     # Taxa de câmbio: 1 dólar = R$ 5.20
taxa_euro = 6.15      # Taxa de câmbio: 1 euro = R$ 6.15

# Cálculos de conversão
dolares = round(valor_reais / taxa_dolar, 2)  # Converte para dólares e arredonda
euros = round(valor_reais / taxa_euro, 2)     # Converte para euros e arredonda

# Exibição dos resultados
print(f"O valor em dólares é: {dolares:.2f}")
print(f"O valor em euros é: {euros:.2f}")
