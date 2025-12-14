while True:
    from random import randint
    computador = randint(0,10)
    print('-=-'*10)
    valor = int(input("Digite um Valor: "))
    usuario = str(input("Digite, Par ou Impar [P/I] ")).strip().lower()[0]
    while usuario not in ('p','i'):
        usuario = str(input("Digite, Par ou Impar [P/I] ")).strip().lower()[0]
        print('----'*10)
    soma = computador + valor
    print(f"Você jogou {valor}, e o computador jogou {computador}. Total foi {soma}, Deu",'Par' if soma % 2 == 0 else 'Impar')
    print('-----'*10)
    if usuario == 'p' and soma % 2 == 0:
        print("Você Venceu!!")
    if usuario == 'i' and soma % 2 == 1:
        print("Você Venceu!!")
    else:
        print("O computador venceu")
        break
    print('-=-'*10) 