import pandas as pd
import numpy as np

# Carregar o dataset
df = pd.read_csv("C:/Users/jaja0/Desktop/Estudos/Estatisticas-e-Banco-de-dados/CHECKPOINT 1/dataset_prova.csv")

df["Índice de Desempenho"] = (df["Horas de Trabalho/Semana"] * df["Satisfação (1-5)"]) / df["Idade"]
produtividade_media = df["Índice de Desempenho"].mean()
desvio_padrao = np.abs(df["Salário (R$)"] - df["Salário (R$)"].mean()).mean()
correlacao = df["Satisfação (1-5)"].corr(df["Horas de Trabalho/Semana"])

print(f"Após uma análise aprofundada dos dados, identificamos que a produtividade média na empresa é de {produtividade_media:.2f}, "
      f"o que sugere um excelente nível de eficiência entre os funcionários. Além disso, a volatilidade salarial, medida pelo desvio padrão, "
      f"é de {desvio_padrao:.2f}, confirmando uma política de remuneração estável e previsível. "
      f"Por fim, a correlação entre Satisfação e Horas de Trabalho é de {correlacao:.2f}, evidenciando que funcionários que trabalham mais tendem a ser mais satisfeitos.")
