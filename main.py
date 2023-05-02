import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("USD_BRL_hist.csv", sep=",")# le o arquivo e separa por ,

df["Data"] = pd.to_datetime(df["Data"], format="%d.%m.%Y") # busca a data e formata a data para melhor visualização

fig, ax = plt.subplots()
ax.plot(df["Data"], df["USD_BRL"], marker="o", linestyle="-", color="blue")# introduz o indice de moeda/data com cor azul

ax.set_xlabel("Data") # datas expostas no rodapé do grafico
ax.set_ylabel("USD/BRL") # informação lateral do grafico
ax.set_title("Cotação do USD/BRL em dezembro de 2019") # titulo do grafico

plt.xticks(rotation=45)

plt.show() # abertura do sistema
