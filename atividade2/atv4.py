'''Calculadora de Consumo de Combustível
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

* Distância percorrida: 300 km
* Combustível gasto: 25 litros
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.'''

# Calculadora de Consumo de Combustível

# Variáveis
distancia = 300  # Distância percorrida em km
combustivel_gasto = 25  # Combustível gasto em litros

# Cálculo do consumo médio
consumo_medio = distancia / combustivel_gasto  # Consumo em km/l
consumo_medio_arredondado = round(consumo_medio, 2)  # Arredonda para duas casas decimais

# Resultados
print(f"Distância percorrida: {distancia} km")
print(f"Combustível gasto: {combustivel_gasto} litros")
print(f"Consumo médio: {consumo_medio_arredondado:.2f} km/l")