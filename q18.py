valor_produto = float(input("Qual o valor do produto?  "))
porcentagem_desconto = float(input("Insira o valor do desconto: "))
desconto =(valor_produto * porcentagem_desconto)/100
print("O valor do desconto é: ", desconto)
produto_desconto = valor_produto - desconto
print("O valor do produto com desconto é: ", produto_desconto )