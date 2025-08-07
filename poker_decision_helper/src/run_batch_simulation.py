from game_logic import simular_rodada
from database import criar_banco
from tqdm import tqdm

def simular_varias_rodadas(qtd_rodadas=1, num_oponentes=5):
    criar_banco()

    print(f"Simulando {qtd_rodadas} rodadas com {num_oponentes} oponentes...\n")
    for _ in tqdm(range(qtd_rodadas)):
        simular_rodada(num_oponentes=num_oponentes)

if __name__ == "__main__":
    simular_varias_rodadas(qtd_rodadas=10000, num_oponentes=5)

