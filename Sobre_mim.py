import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.app_logo import add_logo
import pandas as pd


if "data" not in st.session_state:
    df = pd.read_csv("programming_languages_with_normal.csv")
    df = df.sort_values(by="popularity", ascending=False)
    st.session_state["data"] = df

st.set_page_config(page_title="um pouco sobre Micael e suas perguntas", layout="wide")

pages = st.sidebar.selectbox("Habilidades:", [
    "Sobre Mim",
    "Skills, Formações e Experiências"
])

if pages == "Sobre Mim":
    st.image("LinkedIn banner elegante bold cinza.png", width=1900)
    st.title("Um pouco sobre mim")
    st.write("""Olá! Meu nome é Micael e sou estudante de Engenharia de Software da FIAP.
        Tenho paixão por tecnologia e programação, e estou sempre em busca de aprender novas ferraentas e linguagens que possa, agregar ao meu conhecimento. O que me levou a ingressar neste curso foi a minha curiosidade por tudo, desde sempre 
        tive curiosidade para saber como as coisas funcionam e o que trem por trás delas e desde emtão me encontrei neste curso, pois além de responder as minhas curiosidades ele me ajuda a achar outras.""")
    st.write("""Por mais que eu mexa com a parte de programação, gosto muito de praticar esportes, estar reunido coma a minha familia e amigos, gosto de ir a igraja toda semana, e de estar junto de quem eu amo, gosto de aprender novas linguas atualmente eu falo português, esapnhol e estou aprendendo inglês. Tenho uma cachorrinha chamada Frida que tem 4 anos de idade, ela ama passear e brincar.""")

elif pages == "Skills, Formações e Experiências":
    st.image("Micael Azarias currículo .png", width=2100)