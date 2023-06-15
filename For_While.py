qtde = int(input('Informe a quantidade de alunos: '))

for i in range(qtde):
    nome = input('Informe o nome do aluno: ')
    print(f'Seja bem-vindo, {nome}!')

#While

num = 0

while num != -1:
    num = int(input('Informe um número (-1 para encerrar): '))