palavras = ('maquina','notebook','celular','filme','futebol','trabalhar','moto','amigo')
vogais = 'aeiou'
for cont in palavras:
   print(f"\nNa palavra, {cont.title()}, vai ter as vogais: ",end='')
   for letras in cont:
       if letras.lower() in vogais:
           print(letras,end=',')
           
