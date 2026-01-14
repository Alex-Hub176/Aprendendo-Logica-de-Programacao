aluno = {}

aluno["nome"] = str(input("Nome: ")).title()
aluno["media"] = float(input("Média: "))

print(f"Nome do aluno e {aluno["nome"]}")
print(f"A média do aluno e {aluno["media"]}")
if aluno["media"] >= 7:
    print(f"{aluno["nome"]} está Aprovado")
elif 5 <=  aluno["media"] < 7:
    print(f"{aluno["nome"]} está de Recuperação")
else:
    print(f"{aluno["nome"]} Está Reprovado")