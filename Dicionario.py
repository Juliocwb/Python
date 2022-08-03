produto ={
  'codigo': 0,
  'descricao': "",
  'preço': 0,
  'quantidade': 0 
}

produto['codigo'] = int(input("Digite o codigo: "))
produto['descricao'] = str(input("Digite o Nome: "))	
produto['preço'] = float(input("Digite o preço: ")) 
produto['quantidade'] = int(input("Digite o quantidade: "))

print(produto['codigo'])
print(produto['descricao'])
print(produto['preço'])
print(produto['quantidade'])