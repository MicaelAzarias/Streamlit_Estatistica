import streamlit as st
import pandas as pd
import numpy as np
import scipy.stats as stats
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotnine import *
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import poisson, norm

st.set_page_config(page_title="Dados e respostas de perguntas", layout="wide")

df = pd.read_csv("programming_languages_with_normal.csv")

st.title("Distribuição Normal - Popularidade")
st.markdown("""
    A distribuição normal é usada para modelar dados que se distribuem simetricamente em torno de uma média. 
    Aqui, aplicamos essa distribuição para analisar a popularidade das linguagens de programação.
    """)

mean_popularity = df["popularity"].mean()
std_popularity = df["popularity"].std()
x_norm = range(0, int(df["popularity"].max()) + 1)
normal_dist = norm.pdf(x_norm, mean_popularity, std_popularity)

    # Limpar o gráfico anterior (se houver)
plt.clf()

fig4, ax4 = plt.subplots(figsize=(8, 5))
ax4.plot(x_norm, normal_dist, color="green")
ax4.set_title("Distribuição Normal - Popularidade")
ax4.set_xlabel("Popularidade (%)")
ax4.set_ylabel("Densidade de Probabilidade")
st.pyplot(fig4)

st.write("""
### Interpretação do Gráfico de Distribuição Normal:
                
O gráfico de **Distribuição Normal** modela a distribuição da popularidade das linguagens de programação. A Distribuição Normal é adequada para analisar dados que se distribuem simetricamente em torno de uma média.

#### **O que o Gráfico Responde:**
**"Como a popularidade das linguagens de programação está distribuída em torno da média?"**

#### **Análise Estatística:**
**Média (μ)**:  
   A média da distribuição (μ) representa o valor central de popularidade. No gráfico, a popularidade média está em torno de **10-15%**, indicando que a maioria das linguagens tem uma popularidade moderada.

**Desvio Padrão (σ)**:  
    O desvio padrão (σ) mede a dispersão dos dados em torno da média. Um desvio padrão menor indica que os dados estão mais concentrados perto da média, enquanto um desvio padrão maior sugere maior variabilidade. No gráfico, a curva é relativamente estreita, o que indica que a maioria das linguagens tem popularidade próxima à média.

**Simetria**:  
    A distribuição é simétrica em torno da média, o que significa que a probabilidade de uma linguagem ter popularidade acima ou abaixo da média é igual.

**Eventos Raros**:  
   As caudas da distribuição (popularidade muito baixa ou muito alta) têm probabilidade decrescente. Isso significa que linguagens com popularidade extrema (muito alta ou muito baixa) são **raras**.

**Conclusão**:  
    A distribuição normal confirma que a popularidade das linguagens de programação tende a se concentrar em torno de uma média, com poucas linguagens sendo extremamente populares ou extremamente pouco populares. Isso sugere que a maioria das linguagens tem uma popularidade equilibrada, enquanto apenas algumas se destacam como exceções.
""")

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)


st.title("Distribuição de Poisson - Crescimento das Linguagens")
st.markdown("""
    A distribuição de Poisson é usada para modelar eventos raros ou a taxa de ocorrência de eventos em um intervalo de tempo. 
    Aqui, aplicamos essa distribuição para analisar a taxa de crescimento das linguagens de programação.
    """)

mean_growth = df["growth_rate"].mean()
x = range(0, int(df["growth_rate"].max()) + 1)
poisson_dist = poisson.pmf(x, mean_growth)

    # Limpar o gráfico anterior (se houver)


fig2, ax2 = plt.subplots(figsize=(8, 5))
ax2.bar(x, poisson_dist, color="blue", alpha=0.7)
ax2.set_title("Distribuição de Poisson - Taxa de Crescimento")
ax2.set_xlabel("Taxa de Crescimento (%)")
ax2.set_ylabel("Probabilidade")
st.pyplot(fig2)
    
st.markdown("""
    ### Interpretação do Grafico de Poisson:

    O gráfico de **Distribuição de Poisson** modela a probabilidade de ocorrência de diferentes taxas de crescimento das linguagens de programação. A Distribuição de Poisson é adequada para analisar eventos raros ou a taxa de ocorrência de eventos em um intervalo de tempo, como o crescimento anual das linguagens.

    #### **O que o Gráfico Responde:**
    **"Qual é a probabilidade de uma linguagem de programação ter uma determinada taxa de crescimento anual?"**

    #### **Análise Estatística:**
    **Média (λ)**:  
        A média da distribuição (λ) representa a taxa de crescimento média das linguagens. No gráfico, a maior probabilidade ocorre em torno de **2-3%**, indicando que a maioria das linguagens cresce nessa faixa.

    **Probabilidade Decrescente**:  
        Conforme a taxa de crescimento aumenta, a probabilidade diminui rapidamente. Isso significa que linguagens com taxas de crescimento muito altas (acima de 4%) são **raras** e podem ser consideradas **outliers**.

    **Eventos Raros**:  
        A cauda longa à direita do gráfico (taxas de crescimento acima de 4%) mostra que, embora seja possível encontrar linguagens com crescimento excepcional, essas ocorrências são **pouco frequentes**.

    **Conclusão**:  
        A distribuição confirma que o crescimento das linguagens de programação tende a se concentrar em valores moderados (em torno da média), com poucas linguagens apresentando taxas de crescimento excepcionais. Isso sugere que a maioria das linguagens evolui de forma consistente, enquanto apenas algumas se destacam com crescimento acelerado.
""")

plt.clf()