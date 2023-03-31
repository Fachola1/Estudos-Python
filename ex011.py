# FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS, CALCULE A SUA ÁREA E A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTÁ-LA, SABENDO QUE CADA LITRO DE TINTA PINTA UMA AREA DE 2M²

largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))

area = largura * altura

quantidade_tinta = area / 2

print(f"Você precisará de {quantidade_tinta} litros para pintar a parede completa.")