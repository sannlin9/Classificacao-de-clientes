import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

import warnings
warnings.filterwarnings('ignore')

# Set no tema do seaborn para melhorar o visual dos plots
custom_params = {"axes.spines.right": False, "axes.spines.top": False}
sns.set_palette(sns.color_palette("pastel"))

st.set_page_config (layout= 'wide', 
                    page_title ='Classicação de clientes',
                    initial_sidebar_state="expanded",
                    menu_items={ 
         'Get Help': 'https://www.linkedin.com/in/sandra-lin-costa-894a05174/',
         'Report a bug': "https://github.com/sannlin9/Streamlit-app/issues",
        'About': "# Este aplicativo foi criado como projeto por Sandra Lin Costa!"},
                    page_icon= '👋')


# Função para ler os dados

@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df

df= load_data(r'https://raw.githubusercontent.com/sannlin9/Classificacao-de-clientes/main/input/online_shoppers_intention.csv?token=GHSAT0AAAAAACABPH7VN5ZKXV6L73BBGQDKZCIHRAA')

#Titulo da pagina

st.title('Entendo os dados.')

#checkbox para mostrar os dados
st.markdown("Gostaria de visualizar os dados? clique em mostrar dados.")

if st.checkbox('Mostrar dados'):
    st.subheader('Amostra do dataframe.')
    st.write(df.head(20))
    
st.markdown('# Analise exploratória')

# Função gráficos
def plot_data(tipo, x, y, hue, xlabel, ylabel):
    fig, ax = plt.subplots(figsize=(8, 6))
    if tipo == 'scatterplot':
        sns.scatterplot(data=df, x=x, y=y, hue=hue, alpha=0.7)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
    elif tipo == 'countplot':
        ax = sns.countplot(data=df, x=x, hue=hue)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
    else:
        raise ValueError('Tipo de gráfico inválido. Use "scatterplot" ou "countplot".')
    plt.show()

# Plot
'''
Proporção de visitantes que efetivam compra.
'''
plot_data('countplot', 'Revenue', None, None, 'Efetivação da compra por visita', 'Frequência')

'''
# Mes que ocorreu a visita.
'''
sns.countplot(data=df, x='Month', hue='Revenue')
plt.xlabel('Mes da visita')
plt.ylabel('Frequencia')
st.pyplot(fig=plt)

'''
# Visitas em paginas administrativas.
'''
sns.scatterplot(data=df, x='Administrative', y='Administrative_Duration', hue='Revenue', alpha=0.7)
plt.xlabel('Quantidade de paginas administrativas visitadas')
plt.ylabel('Duração das visitas')
st.pyplot(fig=plt)

'''
# Visitas em paginas informativas.
'''
sns.scatterplot(data=df, x='Informational', y='Informational_Duration', hue='Revenue', alpha=0.7)
plt.xlabel('Quantidade de paginas informativas visitadas')
plt.ylabel('Duração das visitas')
st.pyplot(fig=plt)

'''
# Visitas em paginas de produtos.
'''
sns.scatterplot(data=df, x='ProductRelated', y='ProductRelated_Duration', hue='Revenue',alpha=0.7)
plt.xlabel('Quantidade de paginas de produto visitadas')
plt.ylabel('Duração das visitas')
st.pyplot(fig=plt)

'''
# Porporção de visitas em finais de semana.
'''
ax = sns.countplot(data=df, x='Weekend', hue='Revenue')
plt.title('Visitas realizadas durante finais de semana')
plt.xlabel('Fim de semana')
plt.ylabel('Frequência ')
st.pyplot(fig=plt)