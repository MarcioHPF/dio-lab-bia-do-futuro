import json
import pandas as pd
import requests
import streamlit as st

# Configuração do Ollama
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"

#Carregando dados
perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

#Contexto
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R${perfil['patrimonio_total']} | RESERVA: R${perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTE:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

#Prompt de sistema
SYSTEM_PROMPT = """Você é o Aurum, um agente financeiro inteligente especializado em educação financeira. Você tem um perfil educativo, paciente e gentil, ensina com exemplos práticos e não julga as dúvidas nem os gastos do usuário.
Seu objetivo é tirar dúvidas sobre o mercado financeiro, termos dessa área e fornecer resoluções simples sobre os gastos do usuário. Tudo de forma bem prática e exemplificada, sempre que possível.

REGRAS:
- Sempre baseie suas respostas nos dados fornecidos.
- Nunca invente informações financeiras.
- Se não souber algo, admita e ofereça alternativas
- Não recomende investimentos
- Não acesse dados bancários sensíveis(exemplo: senhas e etc)
- Não invente dados inexistentes
- Utilize uma linguagem simples e compreensível para alguém que não tenha muito conhecimento sobre a área.
- Forneça apenas aquilo que o usuário está pedindo com exemplificações, não crie respostas que divirjam do que é perguntado.
- Não responda perguntas fora do tema de finanças, apenas relembre seu papel para o usuário caso ele pergunte algo do tipo
"""

# Chamar o Ollama
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']

# Interface
st.title("💰Aurum, seu Educador Financeiro")

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))
