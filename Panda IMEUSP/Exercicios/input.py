alunos = int(input("Digite a quantidade de alunos: "))
alunos_reprovados = 0
i = 0
while i < alunos:
    notafinal = int(input("Digite a nota do aluno: "))
    if notafinal < 5.0:
            alunos_reprovados += 1      
    i += 1
print("Quantidade de alunos reprovados:", alunos_reprovados)
