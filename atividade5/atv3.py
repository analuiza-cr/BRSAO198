'''Crie um programa que serve para calcular o preço final de um produto após aplicar um desconto percentual.
a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
b - Preço final: Determina o novo preço após o desconto.
c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado.
'''

def calcular_preco_com_desconto():
    
    print("--- Calculadora de Desconto de Produto ---")

    
    try:
        
        preco_original = float(input("Digite o preço original do produto (R$): "))
        
        
        percentual_desconto = float(input("Digite a porcentagem de desconto a ser aplicada (%): "))
        
    except ValueError:
        
        print("\nERRO: Por favor, digite valores numéricos válidos.")
        return 
    
    
    if preco_original < 0 or percentual_desconto < 0:
        print("\nERRO: O preço e o percentual de desconto devem ser valores positivos.")
        return

    
    fator_desconto = percentual_desconto / 100
    
    
    valor_desconto = preco_original * fator_desconto
    
    preco_final = preco_original - valor_desconto
    

    valor_desconto_formatado = round(valor_desconto, 2)
    preco_final_formatado = round(preco_final, 2)
    
   
    print("\n--- Resultado do Cálculo ---")
    print(f"Preço Original: R$ {preco_original:.2f}") 
    print(f"Desconto Aplicado: {percentual_desconto:.2f}%")
    print(f"Valor do Desconto: R$ {valor_desconto_formatado:.2f}")
    print(f"=====================================")
    print(f"Preço Final com Desconto: R$ {preco_final_formatado:.2f}")
    print("=====================================")


if __name__ == "__main__":
    calcular_preco_com_desconto()