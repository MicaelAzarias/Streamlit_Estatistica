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

df = pd.read_csv("programming_languages_with_normal.csv")

st.title("Análise de Linguagens de Programação")
st.markdown("""
    Como um estudante de Engenharia de Software, algumas perguntas me surgiram e eu espero usar gráficos e números para respondê-las.
    A programação está em constante evolução, e entender as tendências pode ajudar tanto na escolha de uma linguagem quanto na análise de oportunidades no mercado de trabalho.

    Para isso, proponho explorar três questões principais:
    1. Quais linguagens estão crescendo mais rápido atualmente e por quê?
    2. Será que as linguagens mais populares têm relação com o salário oferecido?
    3. Quais são as linguagens de programação mais populares atualmente?
    """)
st.markdown("Vamos analisar os dados de 2020 até 2023.")

st.header("Análise Descritiva")
st.write("Analisando o conjunto de dados completo:")
st.dataframe(df)


st.header("Crescimento das Linguagens de Programação")
fig1, ax1 = plt.subplots(figsize=(10, 5))
growth = df.sort_values(by="growth_rate", ascending=False)
sns.barplot(data=growth, x="language", y="growth_rate", ax=ax1, palette="viridis")
ax1.set_title("Taxa de Crescimento das Linguagens de Programação")
ax1.set_xlabel("Linguagem")
ax1.set_ylabel("Taxa de Crescimento (%)")
st.pyplot(fig1)
st.write("""
    No gráfico acima, conseguimos ver um tipo de dado quantitativo, pois os valores numéricos representam taxas de crescimento. 
    Junto com o nosso objetivo, que é comparar o crescimento relativo das linguagens de programação ao longo do tempo, o gráfico 
    mostra a taxa de crescimento anual de cada linguagem, permitindo uma análise comparativa e identificação das que estão se destacando.

    **Linguagens com Maior Crescimento Atual:**

    - **TypeScript**  
        - Crescimento: 6,3% ao ano.  
        - Motivos: Adoção em grandes projetos, tipagem estática e integração com JavaScript.  

    - **Python**  
        - Crescimento: 5% ao ano.  
        - Motivos: Popularidade em Data Science, IA e simplicidade de aprendizado.  

    - **Go (Golang)**  
        - Crescimento: 4,2% ao ano.  
        - Motivos: Desempenho, concorrência e adoção em cloud computing.  

    - **Rust**  
        - Crescimento: 1,2% ao ano.  
        - Motivos: Segurança, desempenho e uso em sistemas críticos.  

    - **Kotlin**  
        - Crescimento: 3,1% ao ano.  
        - Motivos: Desenvolvimento Android e interoperabilidade com Java.  

    **Por Que Estão Crescendo?**

    - **TypeScript**: Segurança e produtividade em projetos JavaScript.  
    - **Python**: Dominância em IA, análise de dados e automação.  
    - **Go**: Ideal para aplicações de alta performance e cloud.  
    - **Rust**: Combina segurança e performance para sistemas críticos.  
    - **Kotlin**: Linguagem preferida para desenvolvimento Android.  
    """)

st.header("Popularidade x Salário")
fig3, ax3 = plt.subplots(figsize=(10, 5))
sns.scatterplot(data=df, x="popularity", y="salary_max", size="salary_min", hue="language", ax=ax3, palette="cool")
ax3.set_title("Relação entre Popularidade e Salário Máximo")
ax3.set_xlabel("Popularidade (%)")
ax3.set_ylabel("Salário Máximo (USD)")
st.pyplot(fig3)

st.markdown("""
As linguagens de programação mais populares atualmente, com base nos dados de 2020 até 2023 são:

1. **Python**  
   - **Popularidade**: 24% (2023).  
   - **Motivos**: Amplamente utilizado em Data Science, Machine Learning, automação e desenvolvimento web. Sua simplicidade e versatilidade o tornam a linguagem mais popular.

2. **JavaScript**  
   - **Popularidade**: 16% (2023).  
   - **Motivos**: Essencial para desenvolvimento web (front-end e back-end com Node.js). Frameworks como React e Vue.js impulsionam sua adoção.

3. **Java**  
   - **Popularidade**: 10% (2023).  
   - **Motivos**: Amplamente utilizado em aplicações empresariais, sistemas corporativos e desenvolvimento Android (com Kotlin).

4. **C#**  
   - **Popularidade**: 8% (2023).  
   - **Motivos**: Popular no desenvolvimento de jogos (Unity) e aplicações Windows.

5. **TypeScript**  
   - **Popularidade**: 9% (2023).  
   - **Motivos**: Crescimento acelerado devido à sua tipagem estática e integração com JavaScript.
    """)