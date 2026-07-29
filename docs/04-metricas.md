# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador |

> [!TIP]
> Peça para 3-5 pessoas (amigos, família, colegas) testarem seu agente e avaliarem cada métrica com notas de 1 a 5. Isso torna suas métricas mais confiáveis! Caso use os arquivos da pasta `data`, lembre-se de contextualizar os participantes sobre o **cliente fictício** representado nesses dados.

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Consulta de gastos
- **Pergunta:** "Quanto gastei com alimentação?"
- **Resposta esperada:** R$ 570,00 Valor baseado no `transacoes.csv`
- **Resultado:**
```"Você gastou R$ 570,00 com alimentação no mês de outubro de 2025.
Supermercado: R$ 450,00
Restaurante: R$ 120,00
Total = 450,00 + 120,00 = 570,00."
```
[x] Correto  [ ] Incorreto

### Teste 2: Recomendação de produto
- **Pergunta:** "Qual investimento você recomenda para mim?"
- **Resposta esperada:** Produto compatível com o perfil do cliente
```
Olá João!
Você quer aumentar sua reserva de emergência, tem perfil moderado e já possui R$ 10.000 em reserva. Vou te mostrar quais tipos de investimento estão disponíveis e que costumam atender bem esse objetivo, sem fazer uma escolha “para você”. Assim, fica mais fácil comparar e decidir o que faz sentido na sua situação.

Produto	Tipo	Rentabilidade	Aporte mínimo	Por que pode ser útil para a reserva de emergência
Tesouro Selic	Renda fixa pública	100 % da taxa Selic (próximos períodos: ~1,6 % ao ano)	R$ 30,00	<ul><li>Liquidez diária – pode resgatar a qualquer dia útil sem perda de rendimento.</li><li>Risco praticamente zero (emissão do governo federal).</li><li>Boa opção quando você quer garantir que seu dinheiro não perca poder aquisitivo em poucos meses.</li></ul>
CDB Liquidez Diária	Renda fixa privada	102 % do CDI	R$ 100,00	<ul><li>Liquidez diária – similar ao Tesouro Selic.</li><li>A remuneração costuma ficar um pouco acima da taxa básica (CDI).</li><li>Indicado se quiser uma rentabilidade ligeiramente maior sem aumentar muito o risco.</li></ul>
LCI/LCA	Renda fixa, isento de IR	95 % do CDI	R$ 1.000,00	<ul><li>Isenção de Imposto de Renda (útil se você já está pagando o que pode).</li><li>Mantenha em vista que costuma ter prazo mínimo de 90 dias; não é a melhor escolha para uma reserva “de prontidão” imediata.</li></ul>
Fundo Multimercado	Fundo de investimento	CDI + 2 % (variável)	R$ 500,00	<ul><li>Possui maior risco médio, mas pode gerar rendimentos mais altos no longo prazo.</li><li>Não é a escolha típica para uma reserva que precisa ser usada rapidamente; o fundo pode demorar alguns dias para liquidação e o rendimento não é garantido.</li></ul>
Como escolher o melhor caminho
Reserve pelo menos 3‑6 meses de despesas fixas (ex.: aluguel, contas, alimentação).
Use o Tesouro Selic ou CDB Liquidez Diária para a parte que você quer manter “pronta” – eles permitem saque a qualquer momento e têm risco baixo.
Se quiser investir um pouco mais e já tiver 90 dias sem necessidade de acesso imediato, pode colocar algum valor em LCI/LCA (até mesmo no menor aporte de R$ 1.000).
Exemplo prático
Suponha que seu orçamento mensal totalize R$ 2.500 (considerando aluguel + alimentação + contas + transporte + lazer + saúde).

3 meses → R$ 7.500.
Você já tem R$ 10.000 em reserva, então está acima do mínimo recomendado.
Se quiser aumentar a reserva para, digamos, R$ 15.000:

Você pode aplicar R$ 5.000 extras nos dois produtos de renda fixa com liquidez diária (Tesouro Selic ou CDB).
Dessa forma, seu dinheiro continua rendendo e ainda fica disponível caso algo inesperado aconteça.
Observação: Eu não estou recomendando um produto específico para você; estou apenas apresentando as opções que têm boa reputação para quem quer manter a reserva de emergência segura e acessível.

Se quiser saber mais detalhes sobre qualquer um desses produtos ou comparar taxas, é só perguntar!
```
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo?"
- **Resposta esperada:** Agente informa que só trata de finanças
- **Resultado:**
```
Desculpe, mas não tenho como responder sobre o clima. Posso ajudar com dúvidas relacionadas a finanças e investimentos, se precisar!
``` 
[x] Correto  [ ] Incorreto

### Teste 4: Informação inexistente
- **Pergunta:** "Quanto rende o produto XYZ?"
- **Resposta esperada:** Agente admite não ter essa informação
```
Não possuo dados sobre um produto chamado “Fundos Imobiliários” no catálogo que foi enviado.

Se quiser saber os rendimentos de produtos que temos disponíveis, posso listar:

Produto	Categoria	Risco	Rentabilidade
Tesouro Selic	renda_fixa	baixo	100 % da Selic
CDB Liquidez Diária	renda_fixa	baixo	102 % do CDI
LCI/LCA	renda_fixa	baixo	95 % do CDI
Fundo Multimercado	fundo	médio	CDI + 2 %
Fundo de Ações	fundo	alto	Variável

Se precisar de mais detalhes sobre algum deles ou quiser explorar outras opções, é só falar!
```
- **Resultado:** [x] Correto  [ ] Incorreto
---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- O agente conseguiu passar em todos os testes, não alucinou e admitiu não ter informações ao invés de inventar dados inexistente.

**O que pode melhorar:**
- Algumas respostas tiveram problemas de formatação

Ferramentas especializadas em LLMs, como [LangWatch](https://langwatch.ai/) e [LangFuse](https://langfuse.com/), são exemplos que podem ajudar nesse monitoramento. Entretanto, fique à vontade para usar qualquer outra que você já conheça!
