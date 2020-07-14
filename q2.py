vogal = ('a','e','i','o','u')
vogalM = ('A','E','I','O','U')
dic = {}
quantity = [0, 0, 0, 0, 0]

a = input("Digite um texto: ")
for i in range(0, len(vogal)) :
    for j in range(0, len(a)) :
        if(vogal[i] == a[j] or vogalM[i] == a[j]) :
            quantity[i] += 1

for i in range(0, 5) :
    dic[vogal[i]] = quantity[i]

print("")
print("OCORRENCIAS DAS VOGAIS:")

print(dic)    