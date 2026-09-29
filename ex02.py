import math

# Definição da função que calcula a área
def calcular_area_circulo(raio):
    area = math.pi * (raio ** 2)
    return area

# Fluxo principal do código
raio_usuario = float(input("Digite o raio do círculo: "))

# Chamada da função e exibição do resultado formatado
area_calculada = calcular_area_circulo(raio_usuario)
print(f"A área do círculo é: {area_calculada:.2f}")