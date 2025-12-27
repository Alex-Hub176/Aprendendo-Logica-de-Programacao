times = ('Grêmio','Corinthians','Flamengo','Vasco da Gama','Fluminense','Internacional','Cruzeiro','Santos','Atlético Paranaense','Palmeiras',
'Botafogo','Coritiba','Atlético Mineiro','Vitória','Bahia',
'Ponte Preta','São Paulo','Portuguesa','Atlético Goianiense','Chapecoense')
print(f"Os 5 primeiro colocados e {times[0:5]}")
print("=-="*30)
print(f"Os 4 últimos colocados são {times[-4:]}")
print("=-="*30)
print(f"Em ordem alfabética {sorted(times)}")
print("=-="*30)
posicao = str(input("Você quer ver a posição de qual time? ")).strip().title()
print(f"O {posicao} está na {times.index(posicao)+1}° Colocado")