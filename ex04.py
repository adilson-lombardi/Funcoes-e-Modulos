# ==========================================
# EXERCÍCIO 4: Compreendendo Escopo de Variáveis
# ==========================================

# --- CÓDIGO DO EXERCÍCIO ---

x = 10  # Variável global


def alterar_valor():
    x = 5  # Variável local
    print(f"Valor dentro da função: {x}")


alterar_valor()
print(f"Valor fora da função: {x}")


# ==========================================
# RESPOSTAS DA QUESTÃO
# ==========================================

"""
a) Qual será a saída exata impressa no console ao executar este código?

RESPOSTA A:
Valor dentro da função: 5
Valor fora da função: 10


b) Explique por que o valor de x fora da função não é alterado para 5,
utilizando o conceito de Escopo de Variáveis.

RESPOSTA B:
A variável x = 10 (definida fora da função) pertence ao escopo global,
enquanto a atribuição x = 5 dentro da função criar_valor() cria uma nova
variável no escopo local da função.

Como não foi utilizada a palavra-chave `global x`, a alteração afeta apenas
o escopo local durante a execução da função, mantendo a variável do escopo
global intacta com o valor 10.
"""