import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

import streamlit as st

import warnings
warnings.filterwarnings('ignore')

# Set no tema do seaborn para melhorar o visual dos plots
custom_params = {"axes.spines.right": False, "axes.spines.top": False}
sns.set_palette(sns.color_palette("pastel"))

st.sidebar.success("Selecione uma pagina para navegar.")

st.set_page_config (layout= 'wide', 
                    page_title ='Classicação de clientes',
                    initial_sidebar_state="expanded",
                    menu_items={ 
         'Get Help': 'https://www.linkedin.com/in/sandra-lin-costa-894a05174/',
         'Report a bug': "https://github.com/sannlin9/Streamlit-app/issues",
        'About': "# Este aplicativo foi criado como projeto por Sandra Lin Costa!"},
                    page_icon= '👋')

#Titulo da pagina

st.title('Classificação de clientes.')


'''
    Neste projeto, vamos analisar uma base de dados chamada "Online Shoppers Purchase Intention" de Sakar et al. 
    
    Essa base contém informações sobre 12.330 sessões de acesso a páginas de um site, cada sessão de um usuário diferente em um período de 12 meses. O objetivo é entender se o design da página afeta a propensão de compra do cliente, dependendo de como ele navega pelo site. 
    Para isso, vamos agrupar os clientes de acordo com seu comportamento de navegação entre páginas administrativas, informativas e de produtos. 
    
    As variáveis que usaremos são a quantidade e o tempo de acesso por tipo de página, bem como informações de temporalidade, como a época do ano. 
    
    Em resumo, vamos analisar como o comportamento de navegação dos clientes está relacionado à propensão de compra e como isso pode ser influenciado pelo design da página.
  
 -------------------------------------------
    
|Variavel                |Descrição          | 
|------------------------|:-------------------| 
|Administrative          | Quantidade de acessos em páginas administrativas| 
|Administrative_Duration | Tempo de acesso em páginas administrativas | 
|Informational           | Quantidade de acessos em páginas informativas  | 
|Informational_Duration  | Tempo de acesso em páginas informativas  | 
|ProductRelated          | Quantidade de acessos em páginas de produtos | 
|ProductRelated_Duration | Tempo de acesso em páginas de produtos | 
|BounceRates             | *Percentual de visitantes que entram no site e saem sem acionar outros *requests* durante a sessão  | 
|ExitRates               | * Soma de vezes que a página é visualizada por último em uma sessão dividido pelo total de visualizações | 
|PageValues              | * Representa o valor médio de uma página da Web que um usuário visitou antes de concluir uma transação de comércio eletrônico | 
|SpecialDay              | Indica a proximidade a uma data festiva (dia das mães etc) | 
|Month                   | Mês  | 
|OperatingSystems        | Sistema operacional do visitante | 
|Browser                 | Browser do visitante | 
|Region                  | Região | 
|TrafficType             | Tipo de tráfego                  | 
|VisitorType             | Tipo de visitante: novo ou recorrente | 
|Weekend                 | Indica final de semana | 
|Revenue                 | Indica se houve compra ou não |

\* variávels calculadas pelo google analytics
    '''
'''
--------------------------------
'''




