dic = {}

def adicionar(dic):
    lista = []
    nome = input("Digite o nome do contato: ")
    numero = int(input("Digite o numero do contato: "))
    lista.append(numero)
    while True:
        op = input("Deseja acrescentar mais algum numero (S/N)? ").upper()[0]
        if(op == 'S'):
            numero = int(input("Digite o numero do contato: "))
            lista.append(numero)
        elif(op == 'N'):
            break
        else:
            print("ERRO. Operacao invalida, por favor tente novamente.")    

    dic[nome] = lista
    return dic

def adicionarNum(dic):
    nome = input("Digite o nome do contato para adicionar a ele um novo numero: ")
    if(nome not in dic):
        op = input("Esse contato nao existe. Deseja incluir ele (S/N)? ").upper()[0]
        if(op == 'S'):
            adicionar(dic)
        elif(op == 'N'):
            print("Operacao 2 encerrada!")
            
        while(op != 'S' and op != 'N'):
            print("Operacao invalida. Tente novamente.")
            op = input("Esse contato nao existe. Deseja incluir ele (S/N)? ").upper()[0]
            if(op == 'S'):
                adicionar(dic)
            elif(op == 'N'):
                print("Operacao 2 encerrada!")
                break    
    else:
        num = int(input("Digite o novo numero: "))
        dic[nome].append(num)        
    return dic

def removerNum(dic):
    num = int(input("Digite o numero desejado para excluir: "))
    if(num not in dic):
        print("Esse numero nao existe na lista.")
    for k,v in dic.items():
        for i in range(0, len(v)):
            if(v[i] == num):
                del(v[i])
        
    return dic    

def removerCon(dic):
    nome = input("Digite o nome do contato para excluir: ")
    if(nome not in dic):
        while(nome not in dic):
            print("Esse contato nao existe na lista. Por favor tente novamente.")
            nome = input("Digite o nome do contato para excluir: ")
    else:
        dic.pop(nome)

    return dic   

def consultar(dic):
    nome = input("Digite o nome do contato para ver os seus numeros: ")
    while(nome not in dic):
        print("Esse contato nao existe. Tente novamente.")
        nome = input("Digite o nome do contato para ver os seus numeros: ")
    return dic[nome]

print("======= MENU DE OPCOES =======")
print("Digite 1 para adicionar um novo contato.")
print("Digite 2 para adicionar um novo numero.")
print("Digite 3 para excluir um numero.")
print("Digite 4 para excluir um contato.")
print("Digite 5 para consultar o numero de um contato.")
print("Digite 6 para encerrar a aplicacao.")
print("==============================")                

while True:
    n = int(input("Digite o numero da operacao desejada: "))
    if(n == 1):
        print(adicionar(dic))
    elif(n == 2):
        print(adicionarNum(dic))
    elif(n == 3):
        print(removerNum(dic))    
    elif(n == 4):
        print(removerCon(dic))
    elif(n == 5):
        print(consultar(dic))
    elif(n == 6):
        print("Fim da operacao!!")
        break
    else:
        print("Operacao invalida. Por favor, tente novamente.")

print()
print("============= LISTA FINAL ============")
for k, v in dic.items():
    print("Contato: " + str(k) + "    Telefone(s): " + str(v))


print("======================================")            