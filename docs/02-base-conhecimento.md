# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Função |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores para ter continuidade nas conversas |
| `perfil_investidor.json` | JSON | Personalizar as explicações para dúvidas do usuário |
| `produtos_financeiros.json` | JSON | Apresentar diferentes produtos financeiros e explicar quando são utilizados e/ou recomendados |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente para personalizar as consultas didaticamente |

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os JSON/CSV são carregados no início da sessão e incluídos no contexto do prompt

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Para tornar a solução mais simples, os dados são "injetados" no prompt. Dessa forma, o Agente terá todo o contexto disponibilizado. O código fica da seguinte maneira para a "injeção":

```python
import json
import pandas as pd

perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/historico_atendimento.json'))
```
---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

O exemplo a seguir mostra alguns dos dados mais relevantes para a construção do contexto do cliente baseado na base de dados disponibilizados, como uma forma de economizar tokens sem prejudicar a capacidade do Agente.
```
Dados do Cliente:
- Nome: João Silva
- Profissão: Analista de Sistemas
- Renda Mensal": 5000.00
- Perfil investidor: Moderado
- Patrimonio total": 15000.00

Últimas transações:
- 2025-10-01,Salário,receita,5000.00,entrada
- 2025-10-02,Aluguel,moradia,1200.00,saida
- 2025-10-03,Supermercado,alimentacao,450.00,saida
- 2025-10-05,Netflix,lazer,55.90,saida
- 2025-10-07,Farmácia,saude,89.00,saida
- 2025-10-10,Restaurante,alimentacao,120.00,saida
- 2025-10-12,Uber,transporte,45.00,saida
- 2025-10-15,Conta de Luz,moradia,180.00,saida
- 2025-10-20,Academia,saude,99.00,saida
- 2025-10-25,Combustível,transporte,250.00,saida

Produtos Disponíveis:
- Tesouro Selic (risco baixo)
- CDB Liquidez Diária (risco baixo)
- LCI/LCA (risco baixo)
- Fundo Multimercado (risco médio)
```
