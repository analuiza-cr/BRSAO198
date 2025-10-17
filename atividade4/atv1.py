'''Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/)'''

# Calculadora Básica

try:
    # Solicita o primeiro número
    num1_str = input("Digite o primeiro número: ")
    num1 = float(num1_str)  
    
    # Solicita a operação
    operacao = input("Digite a operação (+, -, *, /): ")
    
    # Solicita o segundo número
    num2_str = input("Digite o segundo número: ")
    num2 = float(num2_str)  
    
    # Realiza a operação
    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        if num2 != 0:  
            resultado = num1 / num2
        else:
            print("Erro: Divisão por zero não é permitida.")
            exit()  
    else:
        print("Erro: Operação inválida. Use apenas +, -, * ou /.")
        exit()  
    
    # Resultado
    print(f"Resultado: {resultado}")
    
except ValueError:
    print("Erro: Por favor, digite valores numéricos válidos.")
