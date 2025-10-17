'''Criar um código que serve para analisar números digitados pelo usuário, classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos.'''

# Verificador de Senha

def verificar_senha(senha):
    # Critérios
    tem_comprimento_suficiente = len(senha) >= 8
    tem_numero = any(char.isdigit() for char in senha)  
    
    if tem_comprimento_suficiente and tem_numero:
        return True  
    else:
        return False  
# Solicita a senha do usuário
senha = input("Digite uma senha: ")
if verificar_senha(senha):
    print("Senha segura: Atende a todos os critérios.")
else:
    feedback = "Senha não segura: "
    if len(senha) < 8:
        feedback += "A senha deve ter pelo menos 8 caracteres. "
    if not any(char.isdigit() for char in senha):
        feedback += "A senha deve conter pelo menos um número."
    print(feedback)
