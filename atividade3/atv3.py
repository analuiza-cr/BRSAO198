'''Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
'''

# Conversor de Temperatura

try:
    # Solicita a temperatura do usuário
    temperatura_str = input("Digite a temperatura: ")
    temperatura = float(temperatura_str)  # Converte para float
    
    # Solicita a unidade de origem
    unidade_origem = input("Digite a unidade de origem (C, F ou K): ").upper()
    
    # Solicita a unidade de destino
    unidade_destino = input("Digite a unidade de destino (C, F ou K): ").upper()
    
    # Verificar se as unidades são válidas
    if unidade_origem not in ['C', 'F', 'K'] or unidade_destino not in ['C', 'F', 'K']:
        print("Erro: Unidades inválidas. Use apenas C, F ou K.")
    else:
        # Converter para Celsius primeiro, se necessário
        if unidade_origem == 'F':
            celsius = (temperatura - 32) * 5/9
        elif unidade_origem == 'K':
            celsius = temperatura - 273.15
        else:  
            celsius = temperatura
        
        # Agora converter de Celsius para a unidade de destino
        if unidade_destino == 'C':
            resultado = celsius
        elif unidade_destino == 'F':
            resultado = celsius * 9/5 + 32
        elif unidade_destino == 'K':
            resultado = celsius + 273.15
        
        # Arredonda o resultado para duas casas decimais
        resultado_arredondado = round(resultado, 2)
        
        # Resultado
        print(f"A temperatura {temperatura} {unidade_origem} convertida para {unidade_destino} é: {resultado_arredondado} {unidade_destino}")
    
except ValueError:
    print("Erro: Por favor, digite um valor numérico válido para a temperatura.")
