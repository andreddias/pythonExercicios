import requests
import streamlit as st
from streamlit import title


def buscar_letra(banda, musica):
    endpoint = f"https://api.lyrics.ovh/v1/{banda}/{musica}"
    response = requests.get(endpoint)
    letra = response.json()["lyrics"] if response.status_code == 200 else ""
    return letra


def limpar_campos():
    st.session_state["banda"] = ""
    st.session_state["musica"] = ""


st.image("https://i.imgur.com/SmktDIH.png")
st.title("Letras de músicas")

# Inicializa as variáveis no session_state se elas não existirem
if "banda" not in st.session_state:
    st.session_state["banda"] = ""
if "musica" not in st.session_state:
    st.session_state["musica"] = ""

# Campos de entrada usando session_state para manter o estado
banda = st.text_input("Digite o nome da banda: ", key="banda")
musica = st.text_input("Digite o nome da música: ", key="musica")

#Botões para pesquisa e limpeza
pesquisar = st.button("Pesquisar")
st.button("Limpar", on_click=limpar_campos)

if pesquisar:
    if not banda or not musica:
        st.error("Por favor, preencha ambos os campos: Banda e Música.")
    else:
        letra = buscar_letra(banda, musica)
        if letra:
            st.text(letra)
            st.success(f"letra da música:  {musica}")

        else:
            st.error(f"Não foi possível encontrar a letra da música: {musica} da banda: {banda}")
        # Para executar
        # [user]$ streamlit run /home/user/PycharmProjects/pythonTest/.venv/bin/app.py
        # Fonte: https://www.youtube.com/watch?v=_03CKMuvIxU
