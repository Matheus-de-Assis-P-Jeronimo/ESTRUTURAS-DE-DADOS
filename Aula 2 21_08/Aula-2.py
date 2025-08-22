
AnoAtual = int(input("Qual o ano atual? "))
AnoNasc = int(input("Qual o ano de nascimento? "))
ResultadoAno = AnoAtual - AnoNasc
if ResultadoAno <=9:
    print("Você é uma criança.")
elif ResultadoAno > 9 and ResultadoAno <= 19:
    print("Você é um adolescente.")
elif ResultadoAno > 19 and ResultadoAno <= 60:
    print("Você é um adulto.")
elif ResultadoAno > 60:
    print("Você é um idoso.") 