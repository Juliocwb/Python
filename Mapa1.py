from traceback import print_tb


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
  buscar = str(input("Digite o nome da pessoa que desja alterar cadastro: "))
  achou = False
  i = 0
  while i < len(lista):
     if lista[i]['nome'] == buscar:
           achou = True
           break 
     i+=1
  if achou:
    for pessoa in lista:
        print("Nome: ",pessoa['nome'])
        print("telefone: ",pessoa['telefone'])
        print("Cidade: ",pessoa['cidade'])
        print("Estado: ",pessoa['estado'])
        print("Status: ",pessoa['status'])

        pessoa['nome'] = input("Digite o novo nome para cadastro: ")
        pessoa['telefone'] = input("Digite o novo Telefone: ")        
        pessoa['cidade'] = input("Digite o novo nome da Cidade: ")
        pessoa['estado'] = input("Digite o novo nome do Estado: ")
        pessoa['status'] = input("Digite o novo nome do Status: ") 

        print("Os dados do cadastros {} foram alterados com sucesso!", format(pessoa['nome']))
        break    
    
  else:
    print(f"{buscar} Nao encontrado")
    
  
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
  buscar = str(input("Digite o nome da pessao que desja procurar: "))
  achou = False
  i = 0
  while i < len(lista):
     if lista[i]['nome'] == buscar:
          achou = True
          break 
     i+=1
  if achou:
    print(f"{buscar} achou na posicao {i} ")
    print(f"{lista [i]}")
    
  else:
    print(f"{buscar} Nao encontrado")
  
def excluir():
  pass

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
      excluir()
    elif opção == 6:  
      print("Saindo do sistema")
      break
    else:
      print("opção invalida. Escolha outra opção da lista. ")
Menu()