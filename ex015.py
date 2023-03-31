# ESCREVA UM PROGRAMA QUE PERGUNTE A QUANTIDADE DE KM PERCORRIDOS POR UM CARRO ALUGADO E A QUANTIDADE DE DIAS PELOS QUAIS ELE FOI ALUGADO. CALULE O PREÇO A PAGAR, SABENDO QUE O CARRO CUSTA R$60 POR DIA E R$0,15 KM RODADO

quantidade_dias = int(input('Digite quantos dias o carro foi alugado: '))
quantidade_kmRodado = int(input('Digite quantos kms o carro rodou: '))

preco_dia = 60
km_rodado = 0.15

preco_carro_usado = quantidade_dias * preco_dia
preco_km_rodado = quantidade_kmRodado * km_rodado

valor_total = preco_km_rodado + preco_carro_usado

print(f'O preço a ser pago será de R$ {valor_total:.2f}')


