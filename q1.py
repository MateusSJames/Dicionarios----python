from random import randint

dados = (1, 2, 3, 4, 5, 6)
lista = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
quantity = [0, 0, 0, 0, 0, 0]
n = 0

for i in range(0, len(lista)) :        
    n = randint(1, 6)
    lista[i] = n
    
for i in range(0, len(dados)) :
    for j in range(0, len(lista)) :
        if(lista[j] == dados[i]) :
            quantity[i] += 1

print(lista)
print(quantity)            