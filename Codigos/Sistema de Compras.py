print('------'*20)
valor = int(input("Qual o valor do produto: "))
print("""Qual a forma de pagamento? 
    [1] a vista 10% de desconto
    [2] a vista no cartão 5% de desconto
    [3] em ate 2x no cartão, sem desconto
    [4] 3x ou mais no cartão, com juros""")
escolha = int(input('Qual você escolhe? '))
while escolha not in (1,2,3,4):
    escolha = int(input("Qual você prefere? "))
if escolha == 1:
    desconto = valor - (valor*10/100)
    print(f"Valor pago de, {valor} R$, vai ficar por, {desconto} R$")
elif escolha == 2:
    desconto = valor - (valor*5/100)
    print(f"A compra pago de, {valor} R$, vai ficar por, {desconto} R$")
elif escolha == 3:
    print(f"A compra vai ficar, {valor} R$")
elif escolha == 4:
    juros = valor + (valor*20/100)
    print(f"Compra vai ficar {juros} R$")
print('----'*20)
