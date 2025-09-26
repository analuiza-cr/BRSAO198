#calculadora de preço total

'''Calculadora de Preço Total
* Desenvolva um programa que calcula o preço total de uma compra. Use as seguintes informações:

* Nome do produto: "Cadeira Infantil"
* Preço unitário: R$ 12.40
* Quantidade: 3
O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final. '''

#variáveis

nome_produto= "Cadeira infantil"
preço_unitário = 12.40
quantidade = 3

#calculo do preço total

total = preço_unitário * quantidade

#resultado

print("Produto:", nome_produto)
print(f"Preço unitário: R$ {preço_unitário:.2f}")
print("Quantidade:", quantidade)
print(f"O preço total é: R$ {total:.2f}")