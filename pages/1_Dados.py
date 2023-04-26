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

# Função gráficos
def plot_data(tipo, x, y, hue, xlabel, ylabel):
    fig, ax = plt.subplots(figsize=(8, 6))
    if tipo == 'scatterplot':
        sns.scatterplot(data=df, x=x, y=y, hue=hue, alpha=0.7)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        st.pyplot(fig=plt)
    elif tipo == 'countplot':
        ax = sns.countplot(data=df, x=x, hue=hue)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        st.pyplot(fig=plt)
    else:
        raise ValueError('Tipo de gráfico inválido. Use "scatterplot" ou "countplot".')

df= load_data(r'https://raw.githubusercontent.com/sannlin9/Classificacao-de-clientes/main/input/online_shoppers_intention.csv?token=GHSAT0AAAAAACABPH7VN5ZKXV6L73BBGQDKZCIHRAA')

#Titulo da pagina

st.title('Entendendo os dados.')

''' 
Classificar clientes em clusters significa agrupá-los em grupos com características e comportamentos semelhantes. Isso é importante porque permite que as empresas criem estratégias de marketing e vendas mais direcionadas e personalizadas, o que pode ajudar a aumentar as vendas e a fidelidade do cliente.

Por exemplo, ao agrupar os clientes com base em suas compras anteriores, as empresas podem enviar ofertas personalizadas para cada grupo, oferecer descontos para clientes que compram com frequência ou para aqueles que estão inativos há muito tempo, e até mesmo prever a demanda futura para ajustar seus estoques e produção.

Essas estratégias ajudam as empresas a entender melhor seus clientes, o que pode levar a melhores resultados de negócios e a uma experiência mais satisfatória para o cliente.
'''

#checkbox para mostrar os dados
st.markdown("Gostaria de visualizar os dados? clique em mostrar dados.")

if st.checkbox('Mostrar dados'):
    st.subheader('Base de dados completa.')
    st.write(df)
    
st.markdown('# Analise exploratória')

    
# Plots
'''
# Proporção de visitantes que efetivam compra.
'''
plot_data('countplot', 'Revenue', None, None, 'Efetivação da compra por visita', 'Frequência')

'''
# Mes que ocorreu a visita.
'''
plot_data('countplot', 'Month', None, 'Revenue', 'Mes da visita', 'Frequencia')

'''
# Visitas em paginas administrativas.
'''
plot_data('scatterplot','Administrative', 'Administrative_Duration', 'Revenue', 'Quantidade de paginas administrativas visitadas', 'Duração das visitas')

'''
# Visitas em paginas informativas.
'''
plot_data('scatterplot', 'Informational', 'Informational_Duration', 'Revenue', 'Quantidade de paginas informativas visitadas', 'Duração das visitas')

'''
# Visitas em paginas de produtos.
'''
plot_data('scatterplot', 'ProductRelated', 'ProductRelated_Duration', 'Revenue', 'Quantidade de paginas de produto visitadas', 'Duração das visitas')

'''
# Porporção de visitas em finais de semana.
'''
plot_data('countplot', 'Weekend', None, 'Revenue', 'Fim de semana', 'Frequência')
