def somar(v1=0,v2=0):
    resultado = v1 + v2
    return resultado

def subtracao(v1=0,v2=0):
    resultado = v1 - v2
    return resultado

def multiplicar(v1=0,v2=0):
    resultado = v1 * v2
    return resultado

def divisao(v1,v2):
    if v2 == 0:
        return "ERRO! Não e possivel Divisão por zero"
    resultado = v1 / v2
    return resultado

while True:   
    try:
        valor1 = int(input("Valor 1: "))
        valor2 = int(input("Valor 2: "))
        print(""" 
        1 - Somar
        2 - Subtração
        3 - Multiplicação
        4 - Divisão
            """)
        resposta = int(input("Qual operação você que fazer? "))
        break
    except ValueError:
        print("Valor inválido Tente Novamente")
        

if resposta == 1:
    print(f"[{valor1} + {valor2 } = {somar(valor1,valor2)}]")
elif resposta == 2:
    print(f"[{valor1} - {valor2} = {subtracao(valor1,valor2)}]")
elif resposta == 3:
    print(f"[{valor1} * {valor2} = {multiplicar(valor1,valor2)}]")
elif resposta == 4:
    print(f"[{valor1} / {valor2} = {divisao(valor1,valor2)}]")



