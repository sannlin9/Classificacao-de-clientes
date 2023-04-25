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
'''
# Nomeando os grupos.

 **Grupo 1 --> Generosos**
 
 - O grupo dos Generosos procuram o site de e-commerce durante o mês de Maio, durante este mês acontecem duas datas comemorativas importantes, o dia das mães e dia dos pais nos estados unidos.
 
 **Grupo 2 --> Cliente fiel**
 
 - O grupo dos Fieis sempre compra no nosso e-commerce durante todo o ano.
 
 **Grupo 3 --> Caçadores de descontos**
 
 - Os caçadores adoram promoções especialmente durante a black friday e cyber monday durante o mês de novembro.
'''

'''
# Estrategias aplicadas aos grupos.

### Concluções quanto ao perfil de consumo. 

**Fieis**
    
- Os consumidores fieis são a maior parte dos nossos clientes;
- Tem o menor bounce rate (taxa de rejeição) entre os grupos;
    
**Generosos**

- Tem taxas de rejeição maiores, pois são mais criteriosos.
    
**Caçadores**
    
- Tem a maior propensão a realizar a  compra.
- Já sabem o que querem comprar, pois dentre os visitantes que realizam compras tem o maior valor de bounce rate, ou seja clicam no produto que querem e não visitam o restante do site.
  
### Ações


**Fieis:**
   

- *Programa de fidelidade:* ofereça benefícios exclusivos, descontos e recompensas para os clientes fieis. 
- *Conteúdo personalizado:* forneça conteúdo exclusivo e personalizado para os clientes fieis, como dicas, guias e informações relevantes relacionadas aos seus interesses. 
- *Comunicação frequente:* mantenha contato frequente com os clientes fieis por meio de e-mails, mensagens de texto, notificações de aplicativos, entre outros.

**Generosos:**


- *Atenção aos detalhes:* preste atenção aos detalhes do produto, incluindo descrição, imagens e informações sobre o uso e manutenção. 
- *Experiência de compra personalizada:* ofereça uma experiência de compra personalizada com base nas preferências e histórico de compras dos clientes generosos. 
- *Marketing de influência:* utilize influenciadores para promover seus produtos para os clientes generosos, já que eles são mais criteriosos.

**Caçadores**


- *Anúncios direcionados:* utilize anúncios direcionados para apresentar os produtos que os clientes caçadores estão procurando.
- *Descontos exclusivos:* ofereça descontos exclusivos para os produtos que os clientes caçadores já demonstraram interesse.
- *Facilidade de navegação:* facilite a navegação do site e torne mais fácil para os clientes caçadores encontrar o que estão procurando.
'''
