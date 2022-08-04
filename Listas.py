from cgi import print_environ


nome = input("Digite um nome: \n")
sobrenome = input("Digite seu sobrenome: \n")

tamanho =len(nome)
print("O comprimento do nome é ", tamanho)

nome = nome + " " + sobrenome

print("Apos concatenar as strings temos : ", nome)

if sobrenome in nome:
   print("o sobrenome ", sobrenome, "esta contido no nome", nome, ".")
print("O nome completo em miniusculo é:", nome.lower())
print("O nome completo em maiusculo é:", nome.upper())