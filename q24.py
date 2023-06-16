numero = input("Ola! Digite um número de três digitos para ser invertido: ")
if len(numero) > 3 or len(numero) < 3:
    print("O número precisa ter 3 digitos")
else:
    print("O número serà:",numero[::-1])