import numpy as np
import pandas as pd

np.random.seed(42)

n = 1000

datas = pd.date_range("2025-01-01", "2025-12-31", freq="D")
estados = ["SP", "RJ", "MG", "RS", "PR"]
lojas = [f"Loja {i}" for i in range(1, 11)]

df = pd.DataFrame({
    "id_transacao": range(1, n + 1),
    "data": np.random.choice(datas, size=n),
    "forma_pagamento": np.random.choice(
        ["pix", "cartao", "boleto"], size=n, p=[0.5, 0.4, 0.1]
    ),
    "status": np.random.choice(
        ["aprovado", "recusado", "estornado"], size=n, p=[0.85, 0.10, 0.05]
    ),
    "valor": np.random.lognormal(mean=4.5, sigma=0.8, size=n).round(2),
    "estado": np.random.choice(estados, size=n, p=[0.40, 0.20, 0.15, 0.13, 0.12]),
    "loja": np.random.choice(lojas, size=n),
})

# validação
print(df.info())
print(df.isna().sum())
print(df["valor"].describe())

df.to_csv("data/transacoes.csv", index=False)
print("Arquivo salvo!")