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

def calcula_pontos_regra_simples(lista):
    lista.sort()
    dicio_pontuacao = {}
    for i in range(len(lista)):
        if lista[i] in dicio_pontuacao:
            dicio_pontuacao[lista[i]] += lista[i]
        else: 
            dicio_pontuacao[lista[i]] = lista[i]
    for numero in range(1,7):
        if numero not in dicio_pontuacao:
            dicio_pontuacao[numero] = 0
    return dicio_pontuacao

# mesma função só que sem o .sort
def calcula_pontos_regra_simples_1(dados):
    pontuacao = {1:0,2:0,3:0,4:0,5:0,6:0}
    for dado in dados:
        pontuacao[dado] += dado
    return pontuacao