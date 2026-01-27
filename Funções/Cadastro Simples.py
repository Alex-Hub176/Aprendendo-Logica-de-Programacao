def cadastro_nome_idade(nome,idade):
    return {"nome": nome, "idade": idade}

pessoas = []

def maior(idade):
    if idade >= 18:
        return "Maior de idade"
    return "Menor de Idade"

while True:    
    nome = str(input("Nome: ")).strip().title()
    idade = int(input("idade: "))

    pessoa = cadastro_nome_idade(nome,idade)
    pessoas.append(pessoa)

    resp = str(input("Quer continuar? [S/N] ")).upper()[0]
    
    while resp not in "SN":
        resp = str(input("ERRADO! Digite: [S/N] ")).upper()[0]
    if resp == 'N':
        break

print("-"*30)
for p in pessoas:
    print(f"- Nome: {p["nome"]}")
    print(f"- Idade: {p["idade"]}")
    print(maior(p["idade"]))
    print("-"*30)