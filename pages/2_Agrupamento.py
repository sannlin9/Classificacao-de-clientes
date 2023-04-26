import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st
import time

from scipy.cluster.hierarchy import linkage, fcluster
from gower import gower_matrix
from scipy.spatial.distance import pdist, squareform

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



#Titulo da pagina

st.title('Agrupamento dos visitantes em clusters.')

# Função para ler os dados

@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df

# Função gráficos
def plot_data(tipo, x, y, hue, xlabel, ylabel):
    fig, ax = plt.subplots(figsize=(8, 6))
    if tipo == 'scatterplot':
        sns.scatterplot(data=df, x=x, y=y, hue=hue, alpha=0.7, palette="pastel")
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        st.pyplot(fig=plt)
    elif tipo == 'countplot':
        ax = sns.countplot(data=df, x=x, hue=hue)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        st.pyplot(fig=plt)
    elif tipo == 'barplot':
        ax = sns.barplot(data=df, x=x, y=y, hue=hue)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        st.pyplot(fig=plt)
    else:
        raise ValueError('Tipo de gráfico inválido. Use "scatterplot" ou "countplot".')

df= load_data(r'https://raw.githubusercontent.com/sannlin9/Classificacao-de-clientes/main/input/online_shoppers_intention.csv?token=GHSAT0AAAAAACABPH7VN5ZKXV6L73BBGQDKZCIHRAA')


progress_text = "Gerando o agrupamento, por favor aguarde..."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1, text=progress_text)
    
variaveis = [
    'Administrative', 'Informational', 'ProductRelated',
    'ProductRelated_Duration', 'Month'
]

variaveis_cat = variaveis[-1:]
df_1 = pd.get_dummies(df[variaveis])

vars_cat = [
    True if x in {
        'Month_Aug', 'Month_Dec', 'Month_Feb', 'Month_Jul', 'Month_June',
        'Month_Mar', 'Month_May', 'Month_Nov', 'Month_Oct', 'Month_Sep'
    } else False for x in df_1.columns
]

distancia_gower = gower_matrix(df_1, cat_features=vars_cat)

gdv = squareform(distancia_gower, force='tovector')
Z = linkage(gdv, method='complete')
Z_df = pd.DataFrame(Z, columns=['id1', 'id2', 'dist', 'n'])

#agrupamento de 3 grupos.
df['grupo'] = fcluster(Z, 3, criterion='maxclust')

st.write(df.groupby(['grupo', 'Revenue']).count().fillna(0))

'''
Como nossos grupos se comportam.
'''

'''
# Acessos a paginas administrativas x duração do acesso.
'''
plot_data('scatterplot', 'Administrative', 'Administrative_Duration', 'grupo', 'Acessos a paginas administrativas', 'duração do acesso')

'''
# Acessos a paginas informativas x duração do acesso.
'''
plot_data('scatterplot', 'Informational', 'Informational_Duration', 'grupo', 'Acessos a paginas informativas', 'duração do acesso')

'''
# Acessos a paginas de produtos x duração do acesso.
'''
plot_data('scatterplot', 'ProductRelated', 'ProductRelated_Duration', 'grupo', 'Acessos a paginas de produtos', 'duração do acesso')

'''
# Periodo do acesso.
'''
plot_data('countplot', 'Month', None, 'grupo', 'Mês', 'Frequência')

'''
# Quanto nossos grupos compram.
'''
plot_data('countplot', 'Revenue', None, 'grupo', 'Porporção de compra por acesso', 'Frequência')

'''
