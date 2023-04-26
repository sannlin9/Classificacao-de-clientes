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

### Grupo 1 👉 Generosos

- O grupo dos Generosos procuram o site de e-commerce durante o mês de Maio, durante este mês acontecem duas datas comemorativas importantes, o Dia das Mães e Dia dos Pais nos estados unidos.
st.image('https://png.pngtree.com/png-clipart/20221023/original/pngtree-two-men-giving-presents-each-other-png-image_8714932.png')

### Grupo 2 👉 Cliente fiel

- O grupo dos Fiéis sempre compra no nosso e-commerce durante todo o ano.
st.image('https://hotsite-cdn.s3.amazonaws.com/wp-content/uploads/2017/08/06124709/Motivos-fideliza%C3%A7%C3%A3o-de-clientes.jpg')

### Grupo 3 👉 Caçadores de descontos

- Os caçadores adoram promoções especialmente durante a black friday e cyber monday durante o mês de novembro.
st.image('https://static.vecteezy.com/ti/vetor-gratis/p1/1372982-desconto-cacador-on-cyber-segunda-feira-venda-ilustracao-vetor.jpg')

# Estratégias aplicadas aos grupos.

## Conclusões quanto ao perfil de consumo.

### Fiéis

- Os consumidores fiéis são a maior parte dos nossos clientes.

- Tem o menor bounce rate (taxa de rejeição) entre os grupos.

### Generosos
- Tem taxas de rejeição maiores, pois são mais criteriosos.

### Caçadores
- Tem a maior propensão a realizar a compra.

- Já sabem o que querem comprar, pois dentre os visitantes que realizam compras tem o maior valor de bounce rate, ou seja clicam no produto que querem e não visitam o restante do site.

# Ações

### Fiéis:

- *Programa de fidelidade:* ofereça benefícios exclusivos, descontos e recompensas para os clientes fiéis.

- *Conteúdo personalizado:* forneça conteúdo exclusivo e personalizado para os clientes fiéis, como dicas, guias e informações relevantes relacionadas aos seus interesses.

- *Comunicação frequente:* mantenha contato frequente com os clientes fiéis por meio de e-mails, mensagens de texto, notificações de aplicativos, entre outros.

### Generosos:

- *Atenção aos detalhes:* preste atenção aos detalhes do produto, incluindo descrição, imagens e informações sobre o uso e manutenção.

- *Experiência de compra personalizada:* ofereça uma experiência de compra personalizada com base nas preferências e histórico de compras dos clientes generosos.

- *Marketing de influência:* utilize influenciadores para promover seus produtos para os clientes generosos, já que eles são mais criteriosos.

### Caçadores

- *Anúncios direcionados:* utilize anúncios direcionados para apresentar os produtos que os clientes caçadores estão procurando.

- *Descontos exclusivos:* ofereça descontos exclusivos para os produtos que os clientes caçadores já demonstraram interesse.

- *Facilidade de navegação:* facilite a navegação do site e torne mais fácil para os clientes caçadores encontrar o que estão procurando.

'''
st.sidebar.image('https://www.hostinger.com.br/tutoriais/wp-content/uploads/sites/12/2021/01/O-Que-e-e-commerce-Todos-os-Detalhes-Como-Comecar-o-seu.webp')