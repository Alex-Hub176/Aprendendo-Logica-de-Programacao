valores = (int(input("Digite o Valor 1° ")),int(input("Digite O Valor 2° ")),int(input("Digite O Valor 3° ")),int(input("Digite O Valor 4° ")))
print(f"Vai aparecer o Valor 9 {valores.count(9)}° vezes")
if 3 in valores:
    print(f"O valor 3 vai aparecer na posição {valores.index(3)+1}°")
for n in valores:
    if n %2 == 0:
        print(f"Os valores Pares Declarados é o números {n}")