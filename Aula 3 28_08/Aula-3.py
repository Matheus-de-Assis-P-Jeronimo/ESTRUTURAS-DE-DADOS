import math

def calcularSeno():#funçãozinha de leicomo sempre
    a = 0
    while a <= 360:
        r = 3.1415 * a / 180
        s = math.sin(r)
        print("Angulo: ", a,"Seno igual a: ",s)