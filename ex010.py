# CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS DÓLARES ELA PODE COMPRAR

valor = float(input('Digite um valor: '))
dollar = 3.27
valor_real_dollar = valor / dollar


print(f"Com esse valor inserido {valor}, você pode comprar US$ {valor_real_dollar:.2f}")