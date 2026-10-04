import pandas as pd

df = pd.read_csv("data/transacoes.csv", parse_dates=["data"])

print(df.dtypes)

aprovacao = df.groupby("forma_pagamento")["status"].apply(
    lambda s: (s == "aprovado").mean()
)
print(aprovacao)
print(df["forma_pagamento"].value_counts())