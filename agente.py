import os

from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_groq import ChatGroq

load_dotenv()

SYSTEM_PROMPT = (
    "Você é um assistente prestativo. Responda sempre em português do Brasil, "
    "de forma clara e objetiva."
)


def _criar_llm() -> ChatGroq:
    api_key = os.getenv("GROQ_API_KEY", "").strip()
    if not api_key:
        raise ValueError(
            "GROQ_API_KEY não definida. Copie .env.example para .env e informe a chave."
        )
    model = os.getenv("GROQ_MODEL", "openai/gpt-oss-20b").strip()
    return ChatGroq(model=model, groq_api_key=api_key, temperature=0.7)


def responder(historico: list[tuple[str, str]], pergunta: str) -> str:
    """historico: lista de (papel, texto) com papel 'user' ou 'assistant'."""
    llm = _criar_llm()
    mensagens = [SystemMessage(content=SYSTEM_PROMPT)]
    for papel, texto in historico:
        if papel == "user":
            mensagens.append(HumanMessage(content=texto))
        elif papel == "assistant":
            mensagens.append(AIMessage(content=texto))
    mensagens.append(HumanMessage(content=pergunta))
    resposta = llm.invoke(mensagens)
    return resposta.content or ""
