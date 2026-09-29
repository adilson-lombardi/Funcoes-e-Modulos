# 1. Imports
import math


# 2. Funções
def calcular_hipotenusa(cateto_a, cateto_b):
    hipotenusa = math.sqrt(cateto_a**2 + cateto_b**2)
    return hipotenusa


# 3. Código Principal
cateto_a = float(input("Digite o valor do primeiro cateto: "))
cateto_b = float(input("Digite o valor do segundo cateto: "))

resultado = calcular_hipotenusa(cateto_a, cateto_b)

print(f"A hipotenusa do triângulo retângulo é: {resultado:.2f}")
