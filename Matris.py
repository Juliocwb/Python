mat=[]

for i in range(3):
    linha=[]
    for j in range(3):
        dado = int(input("Digete um valor: "))
        linha.append(dado)
    mat.append(linha)
for i in range(3):
    for j in range(3):
        print("Elemento da linha", i , "e Coluna",j, "é:", mat[i][j])
        