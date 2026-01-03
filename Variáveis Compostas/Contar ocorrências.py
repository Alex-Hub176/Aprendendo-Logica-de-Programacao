lista = []
print("Digite uma lista de 5 números")
for cont in range(5):
    lista.append(int(input(f"Digite o {cont+1} número: ")))
numero = int(input("Digite um número, para ver quantas vezes ele aparece na lista: "))
print(f"Vai paracer o  número {numero}, {lista.count(numero)} vezes")

