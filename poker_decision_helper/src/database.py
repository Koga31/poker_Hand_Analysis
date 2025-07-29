import sqlite3

def criar_banco(nome_banco='poker.db'):
    conn = sqlite3.connect(nome_banco)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS rodadas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tipo_jogador TEXT,
        mao_jogador TEXT,
        cartas_mesa TEXT,
        nome_mao TEXT,
        forca_mao INTEGER,
        ganhou INTEGER
    );
    """)
    conn.commit()
    conn.close()


def salvar_rodada_multijogador(jogadores, mesa, nome_banco='poker.db'):
    conn = sqlite3.connect(nome_banco)
    cursor = conn.cursor()

    mesa_str = ','.join([f'{v}{n}' for v, n in mesa])

    for jogador in jogadores:
        mao_str = ','.join([f'{v}{n}' for v, n in jogador['mao']])
        cursor.execute("""
        INSERT INTO rodadas (mao_jogador, cartas_mesa, nome_mao, forca_mao, ganhou, tipo_jogador)
        VALUES (?, ?, ?, ?, ?, ?);
        """, (mao_str, mesa_str, jogador['nome_mao'], jogador['forca'], int(jogador['ganhou']), jogador['tipo']))

    conn.commit()
    conn.close()
