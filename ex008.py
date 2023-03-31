# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

valor = float(input("Digite um valor em metros: "))

cm = valor * 100
mm = valor * 1000

print(f"O valor em cm é: {cm:.2f} cm")
print(f"O valor em mm é: {mm:.2f} mm")