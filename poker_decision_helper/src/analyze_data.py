import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Conectar ao banco
conn = sqlite3.connect('poker.db')

# Carregar os dados em um DataFrame
df = pd.read_sql_query("SELECT * FROM rodadas", conn)
conn.close()

# Exibir primeiras linhas
print(df.head())

#exibir o número de vitórias por tipo de mão
vitorias_por_mao = df[df['ganhou'] == 1].groupby('nome_mao').size().reset_index(name = 'Vitória')
vitorias_por_mao = vitorias_por_mao.sort_values(by='Vitória',ascending=False)
print(vitorias_por_mao)

#plotar gráfico de vitórias
vitorias_por_mao_plot = df[df['ganhou'] == 1].groupby('nome_mao').size()
vitorias_por_mao_plot = vitorias_por_mao_plot.sort_values(ascending=False)
plt.figure(figsize=(8,4.5))
sns.barplot(x=vitorias_por_mao_plot.index, y=vitorias_por_mao_plot.values, palette='viridis')
plt.title('Vitórias por tipo de mão')
plt.xlabel('Tipo de mão')
plt.ylabel('Número de vitórias')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Contar quantas vezes cada mão apareceu
contagem_maos = df['nome_mao'].value_counts()
print("\nFrequência das mãos:")
print(contagem_maos)
