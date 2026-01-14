lista = [[],[]]
for cont in range(1,8):
    numeros = int(input(f"Digite o {cont}° Valor "))
    if numeros % 2 == 0:
        lista[0].append(numeros)
    else:
        lista[1].append(numeros)
print(f"Os números Pares foram, {sorted(lista[0])}")
print(f"Os números Impares foram, {sorted(lista[1])}")