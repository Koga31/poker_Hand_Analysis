from itertools import combinations

VALORES_PESO = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
            '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

"""Função para definir o valor das cartas (ignorando o Naipe -> por isso o uso de '_')"""
def contar_valores(cartas):
    contagem = {}
    for valor, _ in cartas:
        contagem[valor] = contagem.get(valor, 0) + 1
    return contagem

"""Função para verificar se é um flush (Naipes iguais)"""
def is_flush(cartas):
    naipes = [n for _, n in cartas]
    return len(set(naipes)) == 1

"""Função para verificar se é uma sequência ('Numeros' em Ordem Sequencial)"""
def is_straight(cartas):
    valores = sorted(set(VALORES_PESO[v] for v, _ in cartas))
    for i in range(len(valores) - 4):
        if valores[i:i+5] == list(range(valores[i], valores[i] + 5)):
            return True
    # Ace pode ser 1 (A,2,3,4,5)
    if set([14, 2, 3, 4, 5]).issubset(set(valores)):
        return True
    return False

"""Função para classificar a mão recebida"""
def classificar_mao(cartas):
    valores = contar_valores(cartas)
    val_counts = sorted(valores.values(), reverse=True)

    is_straight_val = is_straight(cartas)
    is_flush_val = is_flush(cartas)

    if is_flush_val and is_straight_val:
        return (8, "Straight Flush")
    elif val_counts == [4, 1]:
        return (7, "Four of a Kind")
    elif val_counts == [3, 2]:
        return (6, "Full House")
    elif is_flush_val:
        return (5, "Flush")
    elif is_straight_val:
        return (4, "Straight")
    elif val_counts == [3, 1, 1]:
        return (3, "Three of a Kind")
    elif val_counts == [2, 2, 1]:
        return (2, "Two Pair")
    elif val_counts == [2, 1, 1, 1]:
        return (1, "One Pair")
    else:
        return (0, "High Card")

"""Função para avaliar a mão recebida"""
def avaliar_mao(cartas_mao, cartas_mesa):
    combinacoes = combinations(cartas_mao + cartas_mesa, 5)
    melhores = [classificar_mao(comb) for comb in combinacoes]
    return max(melhores, key=lambda x: x[0])  # retorna a mais forte