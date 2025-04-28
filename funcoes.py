import random

def rolar_dados(n):
    return [random.randint(1,6) for i in range(n)]

def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    dados_rolados_atualizado = dados_rolados
    dados_no_estoque_atualizado = dados_no_estoque
    dados_no_estoque_atualizado.append(dados_rolados[dado_para_guardar])
    del dados_rolados_atualizado[dado_para_guardar]
    return [dados_rolados_atualizado,dados_no_estoque_atualizado]

def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    dados_rolados_atualizado = dados_rolados
    dados_no_estoque_atualizado = dados_no_estoque
    dados_rolados.append(dados_no_estoque[dado_para_remover])
    del dados_no_estoque_atualizado[dado_para_remover]
    return [dados_rolados_atualizado,dados_no_estoque_atualizado]

def calcula_pontos_regra_simples(dados):
    pontuacao = {1:0,2:0,3:0,4:0,5:0,6:0}
    for dado in dados:
        pontuacao[dado] += dado
    return pontuacao

def calcula_pontos_soma(dados):
    pontuacao = 0
    for dado in dados:
        pontuacao += dado
    return pontuacao

def calcula_pontos_sequencia_baixa(lista):
    analisado = calcula_pontos_regra_simples(lista)
    if analisado[1] != 0 and analisado[2] != 0 and analisado[3] != 0 and analisado[4] != 0:
        return 15
    elif analisado[5] != 0 and analisado[2] != 0 and analisado[3] != 0 and analisado[4] != 0:
        return 15
    elif analisado[5] != 0 and analisado[6] != 0 and analisado[3] != 0 and analisado[4] != 0:
        return 15
    else: 
        return 0
    
def calcula_pontos_sequencia_alta(lista):
    analisado = calcula_pontos_regra_simples(lista)
    if analisado[1] != 0 and analisado[2] != 0 and analisado[3] != 0 and analisado[4] != 0 and analisado[5] != 0:
        return 30
    elif analisado[5] != 0 and analisado[2] != 0 and analisado[3] != 0 and analisado[4] != 0 and analisado[6] != 0:
        return 30
    else: 
        return 0

# Função extra para contar a quantidade de cada dado
def conta_dados(lista):
    qtde_dados = {1:0,2:0,3:0,4:0,5:0,6:0}
    for dado in lista:
        qtde_dados[dado] += 1
    return qtde_dados

def calcula_pontos_full_house(lista):
    analisado = conta_dados(lista)
    dados = []
    for qtd in analisado.values():
        dados.append(qtd)
    if 2 in dados and 3 in dados:
        return calcula_pontos_soma(lista)
    else:
        return 0
    
def calcula_pontos_quadra(dados):
    analisado = conta_dados(dados)
    for qtde in analisado.values():
        if qtde >= 4:
            return calcula_pontos_soma(dados)
    return 0

def calcula_pontos_quina(dados):
    analisado = conta_dados(dados)
    for qtde in analisado.values():
        if qtde >= 5:
            return 50
    return 0

def calcula_pontos_regra_avancada(dados):
    saida = {}
    saida['cinco_iguais'] = calcula_pontos_quina(dados)
    saida['full_house'] = calcula_pontos_full_house(dados)
    saida['quadra'] = calcula_pontos_quadra(dados)
    saida['sem_combinacao'] = calcula_pontos_soma(dados)
    saida['sequencia_alta'] = calcula_pontos_sequencia_alta(dados)
    saida['sequencia_baixa'] = calcula_pontos_sequencia_baixa(dados)
    return saida

def faz_jogada(dados, categoria, cartela):
    simples = calcula_pontos_regra_simples(dados)
    avancada = calcula_pontos_regra_avancada(dados)
    if categoria in avancada:
        pontuacao = avancada[categoria]
        cartela["regra_avancada"][categoria] = pontuacao
    else:
        categoria = int(categoria)
        if categoria in simples:
            pontuacao = simples[categoria]
            cartela["regra_simples"][categoria] = pontuacao
    
    return cartela