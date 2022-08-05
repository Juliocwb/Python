from traceback import print_tb

def existe_pessoa(lista, nome):
   if len(lista) > 0:
     for pessoa in lista:
       if pessoa ['nome'] == nome:
          return True
   return False
def cadastrar(lista):
    Agenda = { 
      'nome': input("Digite nome da pessoa: "),
      'telefone': input("Digita o telefone: "),
      'cidade': input("Digite a cidade: "),
      'estado': input("Digite o estado: "),
      'status': input("Digite (P-> Pessoal) ou (C-> Comercial): ")
    }
    lista.append(Agenda)
  
def alterar(lista):
    print ("Atlerar cadastro")
    if len(lista) > 0:
       nome = input("Digita o nome da pessoa para ser alterado: ")
       if existe_pessoa(lista, nome):
          print("O cadastro encontrado. As informaçõe segue abaixo: ")
          for pessoa in lista:
            if pessoa['nome'] == nome:
               print("Nome: ",pessoa['nome'])
               print("telefone: ",pessoa['telefone'])
               print("cidade: ",pessoa['cidade'])
               print("estado: ",pessoa['estado'])
               print("status: ",pessoa['status'])

               pessoa['nome'] = input("digite o novo nome do cadastro:")
               pessoa['telefone'] = input("Digite o novo telefone:")
               pessoa['cidade'] = input("Digite o novo cidade:")
               pessoa['estado'] = input("Digite o novo estado:")
               pessoa['status'] = input("Digite o novo status:")
               break
       else:
          print(f"Não existe esse nome {nome} no cadastro do sistema")
    else:
       print("nao existe nenhum cadastro no sistema.")

def listar(lista):
    print("Lista cadastrado")
    if len(lista) > 0:
        for i, pessoa in enumerate(lista):
            print("Pessoa ",(i+1))
            print("Nome:  ", pessoa['nome'])
            print("telefone: ",pessoa['telefone'])
            print("cidade:  ",pessoa['cidade'])
            print("estado: ",pessoa['estado'])
            print("status: ",pessoa['status'])
        print("Quantidade de pessoa cadastrada: ", (len(lista)))
    else:
      print("Nao existe nenhuma pessoa cadastrada no sistema. ")
      
def procurar(lista):
    print ("Listar cadastro")
    if len(lista) > 0:
       nome = input("Digita nome da pessoa que deseja procurar  ")
       if existe_pessoa(lista, nome):
          print("O cadastro encontrado. As informaçõe segue abaixo: ")
          for pessoa in lista:
            if pessoa['nome'] == nome:
               print("Nome: ",pessoa['nome'])
               print("telefone: ",pessoa['telefone'])
               print("cidade: ",pessoa['cidade'])
               print("estado: ",pessoa['estado'])
               print("status: ",pessoa['status'])               
               break
       else:
          print(f"Não existe esse nome {nome} no cadastro do sistema")
    else:
       print("nao existe nenhum cadastro no sistema.")
  
def excluir(lista):
    if len(lista) > 0:
       nome = input("Digita nome da pessoa que deseja excluir  ")
       if existe_pessoa(lista, nome):
          print("O cadastro encontrado. As informaçõe segue abaixo: ")
          for i, pessoa in enumerate (lista):
            if pessoa['nome'] == nome:
               print("Nome: ",pessoa['nome'])
               print("telefone: ",pessoa['telefone'])
               print("cidade: ",pessoa['cidade'])
               print("estado: ",pessoa['estado'])
               print("status: ",pessoa['status'])

               del lista[i]

               print("Pessoa foi apagada com sucesso!")
       else:
          print(f"Não existe esse nome {nome} no cadastro do sistema")
    else:
       print("nao existe nenhum cadastro no sistema.")

def Menu ():

  lista=[]

  while True:
    print("1. Cadastrar Pessoa na Agenda")
    print("2. Alterar dados da pessoa")
    print("3. Listar agenda")
    print("4. Procurar pessoa na Agenda")
    print("5. Excluir pessoa na Agenda")
    print("6. Sair do sistema")
    opção = int(input("> "))

    if opção == 1:
      cadastrar(lista)
    elif opção == 2:
      alterar(lista)
    elif opção == 3:
      listar(lista)
    elif opção == 4:
      procurar(lista)
    elif opção == 5:
      excluir(lista)
    elif opção == 6:  
      print("Saindo do sistema")
      break
    else:
      print("opção invalida. Escolha outra opção da lista. ")
Menu()