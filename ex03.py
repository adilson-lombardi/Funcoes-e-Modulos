# Definição da função que encontra o maior número
def encontrar_maior(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Fluxo principal do código
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 = int(input("Digite o terceiro número inteiro: "))

# Chamada da função e exibição do resultado
maior_numero = encontrar_maior(num1, num2, num3)
print(f"O maior número digitado foi: {maior_numero}")