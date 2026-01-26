def medias(notas):
    return sum(notas) / len(notas)

notas = []
for i in range(1,4):
    notas.append(float(input(f"{i}° Notas: ")))

media = medias(notas)

if media >= 7:
    print(f"Aprovado Média de, {media:.2f}")
elif 5 <= media < 7:
    print(f"Recuperação Média de, {media:.2f}")
elif media < 5:
    print(f"Reprovado Média de, {media:.2f}")
