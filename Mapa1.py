def cadastrar(lista):
    Agenda = { 
      "nome": input("Digite nome da pessoa: "),
      "telefone": input("Digita o telefone: "),
      "cidade": input("Digite a cidade: "),
      "estado": input("Digite o estado: "),
      "status": input("Digite P-> Pessoal) ou (C-> Comercial: ")
    }
    lista.append(Agenda)
  
def alterar():
  pass
def listar():
  pass
def procurar():
  pass
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
      alterar()
    elif opção == 3:
      listar()  
    elif opção == 4:
      procurar()
    elif opção == 5:
      excluir()
    elif opção == 6:  
      print("Saindo do sistema")
      break
    else:
      print("opção invalida. Escolha outra opção da lista. ")
Menu()
