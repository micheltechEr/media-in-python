classe = {}

print('Sistema de notas para os alunos, digite uma das opções abaixo')
print('---- SESSÃO DE CALCULO DE MÉDIA ----')   
nome_classe = input("Digite o nome da classe: ")
classe[nome_classe] = []
while True:
        opAluno = input('Cadastrar novo aluno? : ')
        if opAluno.upper() =='N':
         break
        aluno ={}
        nomeAluno= input('Digite o nome do aluno : ')
        idadeAluno= int(input('Digite a idade : '))
        notaUnidadeI = int(input('Digite a nota da unidade I : '))
        notaUnidadeII = int(input('Digite a nota da unidade II : '))
        notaUnidadeIII = int(input('Digite a nota da unidade III : '))

        media = ((notaUnidadeI * 2 ) + (notaUnidadeII * 2) + (notaUnidadeIII * 3))/7

        if(media >= 7):
             situacao = 'APROVADO'
        else:
             situacao = 'REPROVADO'

        aluno['Nome'] =nomeAluno
        aluno['Idade'] = idadeAluno
        aluno['UniI'] = notaUnidadeI
        aluno['UniII'] = notaUnidadeII
        aluno['UniIII'] = notaUnidadeIII
        aluno['Media'] = "{:.2f}".format(media)
        aluno['situacao'] = situacao
        
        classe[nome_classe].append(aluno) 
        if classe[nome_classe]:
            print(nome_classe)
            print('--------------------------------------------')
        for aluno in classe[nome_classe]:
              print(' NOME : ',aluno['Nome'],'\n','IDADE : ',aluno['Idade'])
              print(' MÉDIA : ',aluno['Media'],',',aluno['situacao'])
              print('--------------------------------------------')    
     
# age = 36
# txt = "My name is John, and I am {}"
# print(txt.format(age)) Format pode ser usado para concatenar

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "a" in x]

# print(newlist)

