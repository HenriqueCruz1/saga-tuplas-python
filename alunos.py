alunos = []

while True:
    cadastro = str(input('Você quer cadastrar um aluno [S/N] ')).upper()
    if cadastro == 'N':
        break
    elif cadastro == 'S':

        nome = str(input('Qual o nome do aluno?'))
        nota1 = float(input('Qual o valor da sua primeira nota? '))
        nota2 = float(input('Qual o valor da sua segunda nota? '))
        nota3 = float(input('Qual o valor da sua terceira nota? '))

        media = (nota1+nota2+nota3)/3

        if media < 6:
            situação = 'Reprovado'
        elif media < 8 :
            situação = 'Recuperação'
        else:
            situação = 'Aprovado'

        aluno = (nome, media, situação)
        alunos.append(aluno)

        print(20*'-','QUADRO DE ALUNOS', 20*'-' )

        for indice, (nome, media, situação) in enumerate(alunos, start = 1):
            print(f'{indice} - {nome} - {media:.2f} - {situação} ')
    else:
        print('ERRO!! Digite um valor valido!')

print('Obrigado por utilizar nosso programa de cadastro')