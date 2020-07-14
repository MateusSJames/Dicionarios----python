aux = {}
dic = {}
ranking = []
menor = 10000
pos = 0

for i in range(0, 6):
    voltas = []
    soma = 0.0
    nome = input("Digite o nome do piloto: ")
    for j in range(0, 10):
        tempo = float(input("Digite o tempo da "+ str((j+1))+ "° volta: "))
        soma += tempo
        if(tempo < menor):
            menor = tempo
        voltas.append(tempo)
        if(voltas[j] == menor):
            pos = j+1
    dic[nome] = voltas 
    aux[nome] = soma

print()
ranking = sorted(aux, key= aux.get)
for k,v in dic.items():
    if(menor in v):
        print("A melhor volta foi de " + k + " na " + str(pos) + "° volta")

print("======= RANKING =======")
print(str(1) + "° lugar -> " + ranking[0] + " -------> CAMPEAO!!")
for i in range(1, len(ranking)):
    print(str(i+1) + "° lugar -> " + ranking[i])
print("=======================")