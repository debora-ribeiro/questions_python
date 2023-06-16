valor_venda = int(input("Ola! Qual o valor da venda? "))
valor_a_vista = valor_venda - valor_venda * 10 / 100
print("Esse será o valor com 10% de desconto:",valor_a_vista)
valor_3x = valor_venda / 3
print("A venda pacelada em 3x terá parcelas no valor de:",valor_3x)
comissao_a_vista = valor_a_vista * 5 / 100
print("Sua comissão com a venda a vista é de:", comissao_a_vista)
comissao_valor_parcelado = valor_venda * 5 / 100
print("Sua comissão no valor parcelado é de :",comissao_valor_parcelado)

