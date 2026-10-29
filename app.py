import streamlit as st

from agente import responder

st.set_page_config(page_title="Meu Agente de IA", page_icon="💬")
st.title("Meu Agente de IA")

if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

if st.sidebar.button("Nova conversa"):
    st.session_state.mensagens = []
    st.rerun()

for papel, texto in st.session_state.mensagens:
    with st.chat_message("user" if papel == "user" else "assistant"):
        st.markdown(texto)

pergunta = st.chat_input("Digite sua pergunta…")
if pergunta:
    st.session_state.mensagens.append(("user", pergunta))
    with st.chat_message("user"):
        st.markdown(pergunta)

    resposta = None
    with st.chat_message("assistant"):
        with st.spinner("Pensando…"):
            try:
                historico = st.session_state.mensagens[:-1]
                resposta = responder(historico, pergunta)
                st.markdown(resposta)
            except ValueError as e:
                st.error(str(e))
            except Exception as e:
                st.error(f"Erro ao chamar o modelo: {e}")

    if resposta is not None:
        st.session_state.mensagens.append(("assistant", resposta))
