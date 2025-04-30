import funcoes as fun
import random

# Cartela inicial vazia
cartela_de_pontos = {
    'regra_simples':  {
        1:-1,
        2:-1,
        3:-1,
        4:-1,
        5:-1,
        6:-1
    },
    'regra_avancada' : {
        'sem_combinacao':-1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

fun.imprime_cartela(cartela_de_pontos)
rolagem = fun.rolar_dados(5)
print(f'Dados rolados: {rolagem}')
guardados = []
print(f'Dados guardados: {guardados}')

print('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:')
ordem = input('>')
i = 0
rerrolar = 0
while i < 12:
    if str(ordem) == '4':
        fun.imprime_cartela(cartela_de_pontos)
        print(f'Dados rolados: {rolagem}')
        print(f'Dados guardados: {guardados}')
        print('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:')
        ordem = input('>')
    elif str(ordem) == '1':
        print('Digite o índice do dado a ser guardado (0 a 4):')
        guardar = int(input('>'))
        lista_provisoria = fun.guardar_dado(rolagem, guardados, guardar)
        rolagem = lista_provisoria[0]
        guardados = lista_provisoria[1]
        print(f'Dados rolados: {rolagem}')
        print(f'Dados guardados: {guardados}')
        print('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:')
        ordem = input('>')
    elif str(ordem) == '2':
        print("Digite o índice do dado a ser removido (0 a 4):")
        remover = int(input(">"))
        lista_provisoria = fun.remover_dado(rolagem,guardados,remover)
        rolagem = lista_provisoria[0]
        guardados = lista_provisoria[1]
        print(f'Dados rolados: {rolagem}')
        print(f'Dados guardados: {guardados}')
        print('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:')
        ordem = input('>')
    elif str(ordem) == '3':
        if rerrolar < 2:
            n = len(rolagem)
            rolagem = fun.rolar_dados(n)
            print(f'Dados rolados: {rolagem}')
            print(f"Dados guardados: {guardados}")
            print('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:')
            ordem = input('>')
            rerrolar += 1
        else:
            print("Você já usou todas as rerrolagens.")
            print(f'Dados rolados: {rolagem}')
            print(f"Dados guardados: {guardados}")
            print('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:')
            ordem = input(">")
    elif str(ordem) == '0':
        print("Digite a combinação desejada:")
        combinacao = input(">")
        valida = False
        while not valida: 
            if combinacao not in str(cartela_de_pontos['regra_simples']) and combinacao not in cartela_de_pontos['regra_avancada']:
                print("Combinação inválida. Tente novamente.")
                combinacao = input(">")
            elif combinacao in str(cartela_de_pontos['regra_simples']) and cartela_de_pontos['regra_simples'][int(combinacao)] != -1:
                print('Essa combinação já foi utilizada.')
                combinacao = input(">")
            elif combinacao in cartela_de_pontos['regra_avancada'] and cartela_de_pontos['regra_avancada'][combinacao] != -1:
                print('Essa combinação já foi utilizada.')
                combinacao = input(">")
            else:
                valida = True
        atualizado = fun.faz_jogada(rolagem+guardados,combinacao,cartela_de_pontos)
        cartela_de_pontos = atualizado
        i += 1
        if i != 12:
            rerrolar = 0
            rolagem = fun.rolar_dados(5)
            print(f'Dados rolados: {rolagem}')
            guardados = []
            print(f'Dados guardados: {guardados}')
            print('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:')
            ordem = input('>')
    else:
        print('Opção inválida. Tente novamente.')
        ordem = int(input('>'))
soma = 0
for pontos in cartela_de_pontos["regra_simples"].values(): 
    soma += pontos
if soma >= 63:
    soma += 35
for pontos1 in cartela_de_pontos["regra_avancada"].values():
    soma += pontos1
fun.imprime_cartela(cartela_de_pontos)
print(f"Pontuação total: {soma}")