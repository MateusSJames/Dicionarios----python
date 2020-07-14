dic = {}
lista = []
print("---------------------------------MENU------------------------------------------")
print("Caso deseje encerrar a operacao pressione ENTER quando digitar o nome do aluno")
print("--------------------------------------------------------------------------------")
print("")
aluno = input("Digite o nome do aluno(a): ")
media = 0.0
soma = 0
while(aluno != "") :
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media = (nota1+nota2)/2.0
    dic[aluno] = [nota1,nota2]
    aluno = input("Digite o nome do aluno(a): ")

print("")
print(dic)    

print("")
a = input("Digite o nome do aluno(a) para consultar a media: ")
lista = dic[a]
soma = lista[0] + lista[1]
media = soma/2.0
print("A media desse aluno(a) sera: ", media)