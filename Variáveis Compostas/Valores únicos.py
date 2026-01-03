valores = []
while True:
    numeros = (int(input("Digite um valor ")))
    if numeros not in valores:
        valores.append(numeros)
    else:
        print("Valor Duplicado, Não será adicionado")

    continuar = str(input("Que continuar? [S/N] ")).strip().lower()[0]
    if continuar == 'n':
        break
print(f"Em ordem Crescente, {sorted(valores)}")
