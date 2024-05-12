def menu():
    print("=-=-=-=-Menu-=-=-=-=-=")
    print("1.Cadastro" )
    print("2.Consultar Notas")
    print("3.Listar Alunos")
    print("4.Sair")

while True:
  
  print(menu())
  escolha=int(input("Escolha um valor de 1-4:"))

  if escolha==1:
    nome=(input("Digite seu nome:"))
    disciplina=(input("Escolha uma diciplina(ou -1 para encerrar):"))
    if disciplina=="-1":
       print("Fim...")
       break
    n1=int(input(f'Digite a primeira nota de {disciplina}(ou -1 para encerrar):'))
    if n1=="-1" :
       print("Fim...")
       break
    elif n1<=10 and n1>=0 :
       print(n1)
    else:
       print("Erro")
    
    n2=int(input(f'Digite a segunda nota de {disciplina}(ou -1 para encerrar):'))
    if n2=="-1" :
       print("Fim...")
       break
    elif n2<=10 and n2>=0 :
       print(n2)
    else:
       print("Erro")
    print(f'Aluno {nome} cadastrado com sucesso!')
  elif escolha==2:
    cadastro=[]

    aluno=(input("Digite o nome do aluno que quer consultar:"))
    if aluno!=nome:
       print("Aluno não cadastrado!")
    else:
      media=(n1+n2)/2
      cadastro.append(n1)
      cadastro.append(n2)
      
      print(f'{disciplina}: notas {cadastro} sua média é:{media} ')
       
  elif escolha==3:
    lista={
       'nome':nome,
      'disciplina':disciplina,
      'notas':cadastro
    }
    
    for v,i in lista.items():
       print(f'{v}:{i}')
  elif escolha==4:
     print("Saindo do Sistema")
     break
  else:
     print("Erro")
