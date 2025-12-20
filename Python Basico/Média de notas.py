print(f"Cálculo da Média de Notas".center(40, "="))
quantidade = int(input("Quantas notas você quer calcular a média? "))
notas = 0
for i in range(quantidade):
    nota = float(input(f"Digite a {i+1} nota: "))
    notas += nota
media = notas /quantidade
if media >= 7:
    print("Aluno Aprovado")
if media <7:
    print("Aluno Reprovado")
print(f"A Média das {quantidade} Notas, é {media}")