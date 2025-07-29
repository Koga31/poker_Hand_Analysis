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

# Contar quantas vezes cada mão apareceu
contagem_maos = df['nome_mao'].value_counts()
print("\nFrequência das mãos:")
print(contagem_maos)

# Plotar gráfico de barras
plt.figure(figsize=(10,6))
sns.barplot(x=contagem_maos.index, y=contagem_maos.values, palette='viridis')
plt.title("Frequência das Mãos de Poker")
plt.xlabel("Tipo de Mão")
plt.ylabel("Frequência")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
