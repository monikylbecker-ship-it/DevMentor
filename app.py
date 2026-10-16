import os
import streamlit as st
from google import genai
from google.genai import errors
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="DevMentor AI", page_icon="💻")

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("Configure GOOGLE_API_KEY no arquivo .env antes de iniciar o bot.")
    st.stop()

client = genai.Client(api_key=api_key)

SYSTEM_PROMPT = """
Você é a DevMentor AI, uma mentora e especialista em programação.
Seu objetivo é me ajudar a me tornar uma programadora melhor.

Você deve:
- Ensinar conceitos teóricos de linguagens de programação;
- Explicar lógica de programação de forma didática;
- Revisar e melhorar códigos;
- Sugerir boas práticas;
- Explicar erros e como corrigi-los;
- Guiar projetos práticos passo a passo;
- Adaptar as explicações ao meu nível de conhecimento;
- Incentivar meu raciocínio em vez de apenas entregar respostas prontas.

Seja clara, didática, prática e objetiva.
"""

st.title("💻 DevMentor AI")
st.caption("Sua mentora de programação, código por código.")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

for message in st.session_state["messages"]:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

if prompt := st.chat_input("Pergunte sobre programação..."):
    st.session_state["messages"].append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    contents = [
        {
            "role": "user" if message["role"] == "user" else "model",
            "parts": [{"text": message["content"]}],
        }
        for message in st.session_state["messages"]
        if message["role"] != "system"
    ]

    response = None
    for model in (
        "gemini-3.8-flash",
        "gemini-3.7-flash",
        "gemini-flash-lite-latest",
    ):
        try:
            response = client.models.generate_content(
                model=model,
                contents=contents,
                config={"system_instruction": SYSTEM_PROMPT},
            )
            break
        except errors.ServerError:
            continue

    if response is None:
        st.error("Os modelos do Google estão temporariamente indisponíveis. Tente novamente em alguns instantes.")
        st.stop()

    answer = response.text

    st.session_state["messages"].append(
        {"role": "assistant", "content": answer}
    )

    with st.chat_message("assistant"):
        st.markdown(answer)