senha = input("Digite sua senha: ").strip()
if len(senha) <8:
    print("Senha tem que ter no mínimo 8 caracteres")

if not any(char.isdigit() for char in senha):
    print("Senha tem que ter no mínimo um número")

if len(senha) >8 and any(char.isdigit() for char in senha):
    print("Senha Válida")
else:
    print("Senha Inválida")

