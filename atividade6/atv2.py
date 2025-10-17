'''Crie um programa que  acesse a API  para buscar um usuário fictício aleatório. exibindo o nome, e-mail e país desse usuário, caso houver erro na conexão, mostre uma mensagem de falha.
'''

import requests

def buscar_usuario_ficticio():
   
    api_url = "https://randomuser.me/api/"

    try:
        
        response = requests.get(api_url, timeout=10) 
        
        
        response.raise_for_status() 
        
        
        dados = response.json()
        
        
        usuario = dados['results'][0]
        
        
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']
        
       
        print("--- Usuário Fictício Aleatório ---")
        print(f"Nome: {nome}")
        print(f"E-mail: {email}")
        print(f"País: {pais}")

    except requests.exceptions.RequestException as e:
        
        print("--- ERRO NA CONEXÃO OU REQUISIÇÃO ---")
        print("Falha ao buscar o usuário fictício. Verifique sua conexão com a internet ou o status da API.")
        

if __name__ == "__main__":
    buscar_usuario_ficticio()