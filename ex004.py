# FAÇA UM PROGRAMA QUE LEIA ALGO PELO TECLADO E MOSTRE NA TELA O SEU TIPO PRIMITIVO E TODAS AS INFORAÇÕES POSSÍVEIS SOBRE ELE.

algo = input("Digite algo: ")

print(f"O tipo primitivo desse valor é: {type(algo)}")
print(f"Tem espaços? {algo.isspace()}")
print(f"É numérico? {algo.isnumeric()}")
print(f"É alfabético? {algo.isalpha()}")
print(f"Está em maiúsculas? {algo.isupper()}")
print(f"Está em minúsculas? {algo.islower()}")
print(f"Está capitalizada? {algo[0].isupper()}")
