import random
from hand_evaluator import avaliar_mao
from database import criar_banco, salvar_rodada_multijogador

VALORES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
NAIPES = ['♠', '♥', '♦', '♣']

"""Função para criação do baralho - 52 cartas (sem o coringa)"""
def criar_baralho():
    return [(valor, naipe) for valor in VALORES for naipe in NAIPES]

"""Função para embaralhar as cartas"""
def embaralhar(baralho):
    random.shuffle(baralho)
    return baralho

"""Função para mostrar as cartas do jogador e da mesa"""
def exibir_cartas(cartas):
    return ' | '.join([f'{v}{n}' for v, n in cartas]) 

def simular_rodada(num_oponentes=3):
    baralho = embaralhar(criar_baralho())

    # Jogador principal
    mao_jogador = [baralho.pop(), baralho.pop()]

    # Oponentes
    maos_oponentes = []
    for _ in range(num_oponentes):
        maos_oponentes.append([baralho.pop(), baralho.pop()])

    # Cartas da mesa
    flop = [baralho.pop(), baralho.pop(), baralho.pop()]
    turn = [baralho.pop()]
    river = [baralho.pop()]
    cartas_mesa = flop + turn + river

    # Avaliar todas as mãos
    jogadores = [{'tipo': 'principal', 'mao': mao_jogador}]
    for i, mao_oponente in enumerate(maos_oponentes):
        jogadores.append({'tipo': f'oponente_{i+1}', 'mao': mao_oponente})

    for jogador in jogadores:
        forca, nome_mao = avaliar_mao(jogador['mao'], cartas_mesa)
        jogador['forca'] = forca
        jogador['nome_mao'] = nome_mao

    # Descobrir quem venceu
    vencedor = max(jogadores, key=lambda j: j['forca'])
    for jogador in jogadores:
        jogador['ganhou'] = (jogador == vencedor)

    # Registrar no banco
    salvar_rodada_multijogador(jogadores, cartas_mesa)

# Execução de teste
if __name__ == "__main__":
    criar_banco()
    simular_rodada(num_oponentes=3)