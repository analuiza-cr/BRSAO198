'''Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia'''

from datetime import date
from datetime import datetime

def calcular_dias_vivo():

    print("--- Calculadora de Dias de Vida ---")
    
    
    while True:
        data_nascimento_str = input("Por favor, digite sua data de nascimento (DD/MM/AAAA): ")
        try:
            
            data_nascimento = datetime.strptime(data_nascimento_str, '%d/%m/%Y').date()
            break  
        except ValueError:
            print("Formato de data inválido. Use o formato DD/MM/AAAA (ex: 25/08/1990).")

    
    data_hoje = date.today()
    
    
    if data_nascimento > data_hoje:
        print("Sua data de nascimento não pode ser no futuro! Por favor, tente novamente.")
        return

    
    diferenca = data_hoje - data_nascimento
    
    
    dias_vivos = diferenca.days
    
    
    print(f"\n--- Resultado ---")
    print(f"Data de Nascimento: {data_nascimento.strftime('%d/%m/%Y')}")
    print(f"Data Atual:         {data_hoje.strftime('%d/%m/%Y')}")
    print(f"\nParabéns! Você está vivo há {dias_vivos:,} dias!".replace(",", "."))


if __name__ == "__main__":
    calcular_dias_vivo()