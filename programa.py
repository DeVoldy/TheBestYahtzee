import funcoes as fun

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

if ordem == '4':
    fun.imprime_cartela(cartela_de_pontos)
elif ordem == '1':
    print('Digite o índice do dado a ser guardado (0 a 4):')
    guardar = int(input('>'))
    lista_provisoria = fun.guardar_dado(rolagem, guardados, guardar)
    rolagem = lista_provisoria[0]
    guardados = lista_provisoria[1]
    print(f'Dados rolados: {rolagem}')
    print(f'Dados guardados: {guardados}')
elif ordem == '2':
    print("Digite o índice do dado a ser removido (0 a 4):")
    remover = int(input(">"))
    lista_provisoria = fun.remover_dado(rolagem,guardados,remover)
    rolagem = lista_provisoria[0]
    guardados = lista_provisoria[1]
    print(f'Dados rolados: {rolagem}')
    print(f'Dados guardados: {guardados}')
elif ordem == '3':
    n = len(rolagem)
    rolagem = fun.rolar_dados(n)
    print(f'Dados rolados: {rolagem}')
    print(f"Dados guardados: {guardados}")
elif ordem =="0":
    print("Digite a combinação desejada:")
    combinacao = input(">")
    atualizado = fun.faz_jogada(rolagem+guardados,combinacao,cartela_de_pontos)
    cartela_de_pontos = atualizado
    fun.imprime_cartela(cartela_de_pontos)