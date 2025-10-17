'''Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação). Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.'''

import re

def eh_palindromo(texto):

    texto_lower = texto.lower()


    texto_filtrado = re.sub(r'[^a-z0-9]', '', texto_lower)

    
    return texto_filtrado == texto_filtrado[::-1]



palavra_ou_frase = "A man, a plan, a canal: Panama" 

if eh_palindromo(palavra_ou_frase):
    resposta = "Sim"
else:
    resposta = "Não"


print(f'O texto "{palavra_ou_frase}" é um palíndromo?')
print(resposta)