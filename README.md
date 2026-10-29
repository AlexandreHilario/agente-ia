# Meu Agente de IA

Chat em linguagem natural com LLM (Groq) via LangChain e interface Streamlit, com histórico da conversa na sessão.

## Pré-requisitos

- Python 3.10+
- Conta gratuita na [Groq Console](https://console.groq.com)

## Configuração

1. Crie uma API key em [console.groq.com](https://console.groq.com).
2. Copie o exemplo de ambiente e preencha a chave:

```bash
cp .env.example .env
```

3. Instale as dependências:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Executar

```bash
streamlit run app.py
```

Abra a URL exibida no terminal (geralmente `http://localhost:8501`).

Modelo padrão: `openai/gpt-oss-20b`. Altere `GROQ_MODEL` no `.env` se necessário.

## Roteiro da demonstração

1. Envie: `Meu nome é [seu nome].`
2. Envie: `Qual é o meu nome?`
3. O agente deve usar o contexto da conversa anterior.
4. Use **Nova conversa** na barra lateral para limpar o histórico.

## Estrutura

| Arquivo      | Função                          |
| ------------ | ------------------------------- |
| `agente.py`  | Integração LangChain + ChatGroq |
| `app.py`     | Interface Streamlit             |
