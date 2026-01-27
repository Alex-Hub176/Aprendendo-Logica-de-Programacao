def validacao(senha):
    if len(senha) >=8:
        return True
    else:
        return False
    

resp = input("Digite uma senha de até 8 caracteres: ")
print(validacao(resp))