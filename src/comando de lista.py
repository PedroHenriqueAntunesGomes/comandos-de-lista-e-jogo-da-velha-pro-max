notas = 7.5, 8.0, 6.5, 9.0
texto = "Pedro"
nomes = "Ana", "Bruno", "Carla"
vazia = []
print(f"notas = {notas}")
print(f"nomes = {nomes}")
print(f"vazia = {vazia}")

print(f"len(notas) = {len(notas)}")
print(f"len(nomes) = {len(nomes)}")

mista = 42, {texto}, 3.14, True
print(f"\nmista = {mista}")

print (f"nomes [0] = {nomes[0]}")
print (f"nomes [1] = {nomes[1]}")
print (f"nomes [2] = {nomes[2]}")

print(f"\nnomes      = {nomes}")
print(f"nomes[1:2] = {nomes[1:2]}")

print(f"\nnomes      = {nomes}")
print(f"nomes[1:]  = {nomes[1:]}")

#RESULTADOS///

notas = (7.5, 8.0, 6.5, 9.0)
nomes = ('Ana', 'Bruno', 'Carla')
vazia = []
len(notas) = 4
len(nomes) = 3

mista = (42, {'Pedro'}, 3.14, True)
nomes [0] = Ana
nomes [1] = Bruno
nomes [2] = Carla

nomes      = ('Ana', 'Bruno', 'Carla')
nomes[1:2] = ('Bruno',)

nomes      = ('Ana', 'Bruno', 'Carla')
nomes[1:]  = ('Bruno', 'Carla')
