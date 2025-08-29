import math

def calcularSeno():#funçãozinha de leicomo sempre
    a=0
    while a <= 360:
        r = 3.1415 * a / 180
        s = math.sin(r)
        print("Angulo: ", a,"Seno igual a: ",s)
        a+=10        
# calcularSeno()
#---------------------------------------------------
def esruturaFor1():
    for i in ["1º", "2º", "3º", "4º", "5º"]:
        print("Estamos no ", i,"item da lista")
# esruturaFor1()        
def estruturaFor2():
    for frutas in ["Banana", "Maçã", "Pera", "Uva", "Abacaxi"]:
        print("Fruta: ", frutas)
# estruturaFor2()        
def estruturaFor3():
    frutas =["Banana", "Maçã", "Pera", "Uva", "Abacaxi"]
    for fruta in frutas:
        print("Fruta: ", fruta)
        if fruta == "Pera":
            break
#estruturaFor3()  
def estruturaFor4():
    for frutas in ["Banana", "Maçã", "Pera", "Uva", "Abacaxi"]:
        for fruta in frutas:
            print("Fruta: ", fruta)
            if fruta == "Pera":
                continue
#estruturaFor4()
def estruturaFor5(inicio, limite, passo):
    for i in range(inicio, limite + 1, passo):  #(inicio, fim, passo)
        # Sempre adicionar 1 no fim, pois o valor final não é incluso Ex: range(0,10,2) = 0,2,4,6,8
        print("Número: ", i)
#estruturaFor5(
#     int(input("Digite o valor inicial: ")),
#     int(input("Digite o limite: ")),
#     int(input("Digite de quanto em quanto vai ser contado o valor: "))
# )
#---------------------------------------------------
#Exercicio 1
def exercicio1():# MMais uma de minhas brizas tortas
    soma = 0
    totalSoma = 0
    for i in range(100):
        for j in range(100):
            soma = i + j
            print(f"A soma de {i} com {j} é {soma}")
            totalSoma += soma
    print("O total de todas as somas é: ", totalSoma) 
def ex1():# resolução correta do que foi peço
    soma = 0
    for i in range(100):
        soma += i
        print(soma)
# ex1()
#---------------------------------------------------
#Exercicio 2
def ex2():
    for i in range(0, 51, 5):
        print(i)
# ex2()
#---------------------------------------------------
#Exercicio 3
def ex3(): #tabuada
    n = int(input("Digite um número para ver sua tabuada: "))
    maximo = int(input("Digite o maximo multiplicador: "))
    for i in range(1, maximo):
        print(f"{n} x {i} = {n * i}")
def exercicio3():# resolução correta do que foi peço
    multiplicado = int(input("Digite o numero que deseja ver a tabuada: "))
    multiplo = int(input("Digite o numero maximo que deseja ver a tabuada: "))
    if multiplo == 0 or multiplicado == 0:
        print("É ZERO SABIÇÃO, NÃO TEM TABUADA NÃO")
        return
    for i in range(1, multiplicado+1):
        print("-==-==-==- Tabuada do ",i, "-==-==-==-")
        for j in range(1, multiplo+1):
            print(f"{i} x {j} = {j*i}")
            if j*i ==0: # só pra garantir
                print("É ZERO SABIÇÃO, NÃO TEM TABUADA NÃO")
                return
exercicio3()
#---------------------------------------------------
# Lista
l = [x **2 for x in range(10)] # lista de quadrados