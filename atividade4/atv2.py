''' Criar um código que registre as notas de alunos e calcular a média da turma.'''

# Registro de Notas e Cálculo da Média da Turma

try:
    # Solicita o número de alunos
    num_alunos_str = input("Digite o número de alunos na turma: ")
    num_alunos = int(num_alunos_str)  # Converte para inteiro
    
    if num_alunos > 0:  
        notas = []  
        
        for i in range(num_alunos):
            while True:  
                nota_str = input(f"Digite a nota do aluno {i+1}: ")
                try:
                    nota = float(nota_str)  
                    if nota >= 0:  
                        notas.append(nota)
                        break  
                        print("Erro: A nota deve ser um valor não negativo.")
                except ValueError:
                    print("Erro: Por favor, digite um valor numérico válido.")
        
        # Calcula a média
        if notas:  
            soma_notas = sum(notas)
            media = soma_notas / num_alunos
            media_arredondada = round(media, 2)  
            
            # Exibe as notas e a média
            print("Notas registradas:", notas)
            print(f"Média da turma: {media_arredondada}")
        else:
            print("Nenhuma nota foi registrada.")
    else:
        print("Erro: O número de alunos deve ser maior que zero.")
    
except ValueError:
    print("Erro: Por favor, digite um valor numérico válido para o número de alunos.")