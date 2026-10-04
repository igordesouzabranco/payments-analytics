# Payments Analytics

Projeto de estudo de análise de dados com **Python (pandas e NumPy)** e, na próxima etapa, **Power BI**. Ele simula transações de pagamento de lojas online (Pix, cartão e boleto) para praticar geração, validação e análise de dados.

> **Aviso:** os dados são totalmente **simulados**. Este projeto não tem relação com dados reais de nenhuma empresa.

## Objetivo

Praticar o ciclo completo de um projeto de dados:

1. Gerar um dataset com Python
2. Validar tipos e dados ausentes
3. Salvar em CSV
4. Analisar e criar medidas e dashboard no Power BI (em andamento)

## Estrutura do projeto

```
payments-analytics-python/
├── data/
│   └── transacoes.csv
├── src/
│   └── create_data.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Dados gerados

O script cria 1.000 transações com as colunas:

| Coluna | Tipo | Descrição |
|---|---|---|
| id_transacao | inteiro | Identificador único da transação |
| data | data | Data da transação (ano de 2025) |
| forma_pagamento | texto | pix (50%), cartao (40%) ou boleto (10%) |
| status | texto | aprovado (85%), recusado (10%) ou estornado (5%) |
| valor | decimal | Valor da compra, com distribuição lognormal |
| estado | texto | SP, RJ, MG, RS ou PR |
| loja | texto | Loja 1 a Loja 10 |

A semente aleatória (`np.random.seed(42)`) garante que qualquer pessoa que rodar o script obtenha **exatamente os mesmos dados**.

## Como executar

```bash
git clone URL_DO_REPOSITORIO
cd payments-analytics-python

python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/Mac: source .venv/bin/activate

pip install -r requirements.txt
python src/create_data.py
```

O arquivo `data/transacoes.csv` será gerado e o script imprime uma validação (tipos, valores ausentes e estatísticas).

## Primeiras observações

- Não há valores ausentes e todos os tipos estão corretos.
- A **média** do valor das transações (R$ 124,27) é maior que a **mediana** (R$ 90,40), porque poucas compras de valor alto (máximo de R$ 2.081,80) puxam a média para cima.

## Próximos passos

- [ ] Importar o CSV no Power BI
- [ ] Criar medidas em DAX (total de vendas, ticket médio, taxa de aprovação)
- [ ] Montar o dashboard e adicionar prints ao repositório
- [ ] Análises extras em Python (aprovação por forma de pagamento e por estado)

## Tecnologias

Python, pandas, NumPy, Power BI (planejado)