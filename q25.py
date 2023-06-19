numero = input("Olá! Por favor digite um número de 4 digitos: ")
if len(numero) < 4 or len(numero) > 4 :
    print("O número deve ter 4 digitos, o número de digitos esta inadequada.")
else:
    print("ok!")
    for num in numero:
        print(num)

