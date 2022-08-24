AutonomiaVeiculo=int(input("Autonomia do Veiculo: "))

kmPercorrer=int(input("km a Percorrer: "))

precoCombustivel=float(input("Preço do Combustivel: "))

custoViagem = float(((kmPercorrer * 2) / AutonomiaVeiculo) * precoCombustivel)



print("Km a percorrer", kmPercorrer * 2)

print("Litros gastos", (kmPercorrer * 2) / AutonomiaVeiculo)

print("Custo da Viagem R$ ", custoViagem)