produto ={
  'codigo': 0,
  'descricao': "",
  'preço': 0,
  'quantidade': 0 
}

produto['codigo'] = int(input("Digite o codigo: \n"))
produto['descricao'] = str(input("Digite o Nome: \n"))	
produto['preço'] = float(input("Digite o preço: \n")) 
produto['quantidade'] = int(input("Digite o quantidade: \n"))

print(produto['codigo'])
print(produto['descricao'])
print(produto['preço'])
print(produto['quantidade'])