import math

# Solicita ao usuário um número decimal positivo
numero = float(input("Digite um número decimal positivo: "))

# Calcula as operações solicitadas
raiz_quadrada = math.sqrt(numero)
arredondado_cima = math.ceil(numero)
arredondado_baixo = math.floor(numero)

# Exibe os resultados na tela
print(f"Raiz quadrada: {raiz_quadrada}")
print(f"Arredondado para cima: {arredondado_cima}")
print(f"Arredondado para baixo: {arredondado_baixo}")