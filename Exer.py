class Televisao:
  def __init__(self):    
    self.name = input("marca da TV:")
    self.tamanho = input("polegada da TV:")

tv = Televisao()
print(tv.name, tv.tamanho)

tv_sala =Televisao()
print(tv_sala.name,tv_sala.tamanho)
