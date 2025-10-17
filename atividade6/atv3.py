'''Crie um programa que consulte informações de um  na API , retorne logradouro, bairro, cidade e estado do CEP digitado, caso o CEP não existir ou houver erro na requisição, mostre uma mensagem de falha.'''

import requests

def consultar_cep(cep):
    
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        resposta = requests.get(url, timeout=5)

        
        if resposta.status_code == 200:
            dados = resposta.json()

            
            if "erro" in dados:
                print("❌ CEP não encontrado.")
            else:
                print(f"\n✅ Resultado da consulta:")
                print(f"Logradouro: {dados.get('logradouro', 'Não informado')}")
                print(f"Bairro: {dados.get('bairro', 'Não informado')}")
                print(f"Cidade: {dados.get('localidade', 'Não informado')}")
                print(f"Estado: {dados.get('uf', 'Não informado')}")
        else:
            print("❌ Erro na requisição. Tente novamente mais tarde.")

    except requests.exceptions.RequestException as e:
        print("❌ Falha ao conectar à API:", e)



if __name__ == "__main__":
    cep = input("Digite o CEP (somente números): ").strip()

    
    if len(cep) == 8 and cep.isdigit():
        consultar_cep(cep)
    else:
        print("❌ CEP inválido! Digite exatamente 8 números.")
