'''Crie um programa que realize consultas a  em relação ao Real (BRL) usando a API mostre valor atual, máxima, mínima e data/hora da última atualização, caso a moeda não existir ou houver erro na requisição, retorne uma mensagem de erro.'''

import requests

def consultar_cotacao(moeda):
    try:
        
        moeda = moeda.upper()

        
        url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

        
        resposta = requests.get(url, timeout=10)

        
        if resposta.status_code != 200:
            print("❌ Erro na requisição. Código de status:", resposta.status_code)
            return

        dados = resposta.json()

        
        chave = f"{moeda}BRL"

        
        if chave not in dados:
            print("❌ Moeda não encontrada. Verifique o código e tente novamente.")
            return

        info = dados[chave]

        print(f"\n💱 Cotação de {moeda} em relação ao Real (BRL):")
        print(f"➡ Valor atual: R$ {float(info['bid']):.2f}")
        print(f"📈 Máximo do dia: R$ {float(info['high']):.2f}")
        print(f"📉 Mínimo do dia: R$ {float(info['low']):.2f}")
        print(f"🕓 Última atualização: {info['create_date']}")
    
    except requests.exceptions.RequestException as erro:
        print("❌ Erro na conexão com a API:", erro)
    except Exception as e:
        print("❌ Ocorreu um erro inesperado:", e)



if __name__ == "__main__":
    moeda = input("Digite o código da moeda (ex: USD, EUR, BTC): ")
    consultar_cotacao(moeda)
