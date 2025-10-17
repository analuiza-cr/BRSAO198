'''Calculadora de IMC

Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

< 18.5: classificacao = "Abaixo do peso"
< 25: classificacao = "Peso normal"
< 30: classificacao = "Sobrepeso"
Para os demais cenários: classificacao = "Obeso"'''

# Calculadora de IMC

try:
    # Solicita o peso do usuário
    peso_str = input("Digite seu peso em kg: ")
    peso = float(peso_str)  # Converte para float
    
    # Solicita a altura do usuário
    altura_str = input("Digite sua altura em metros: ")
    altura = float(altura_str)  # Converte para float
    
    # Verifica se os valores são positivos (pois peso e altura não podem ser negativos)
    if peso > 0 and altura > 0:
        # Cálculo do IMC
        imc = peso / (altura ** 2)  # Fórmula: IMC = peso / (altura ao quadrado)
        imc_arredondado = round(imc, 2)  # Arredonda para duas casas decimais
        
        # Classificação do IMC
        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif imc < 25:
            classificacao = "Peso normal"
        elif imc < 30:
            classificacao = "Sobrepeso"
        else:
            classificacao = "Obeso"
        
        # Exibição do resultado
        print(f"Seu IMC é: {imc_arredondado} - {classificacao}")
    else:
        print("Erro: Peso e altura devem ser valores positivos.")
    
except ValueError:
    print("Erro: Por favor, digite valores numéricos válidos para peso e altura.")