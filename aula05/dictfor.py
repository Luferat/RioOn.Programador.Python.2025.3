# Dicionário a ser iterado
meuCarro =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Usando somente o nome do dicionário
for carro in meuCarro:
  print(carro)
  
print('--------------')  

# Usando o método dict.keys()
for carro in meuCarro.keys():
  print(carro)
  
print('--------------')  

# Usando o método dict.values()
for carro in meuCarro.values():
  print(carro)  
  
print('--------------') 

# Usando o método dict.items()
for carroKey, carroValue in meuCarro.items():
  print(carroKey, carroValue)

