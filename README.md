# Clusters - Classificação de clientes de e-commerce.
<img alt="GitHub top language" src="https://img.shields.io/github/languages/top/sannlin9/Classificacao-de-clientes?style=for-the-badge">



*Este é um projeto idealizado durante o curso de ciencia de dados | EBAC.*

Neste projeto vamos usar a base [online shoppers purchase intention](https://archive.ics.uci.edu/ml/datasets/Online+Shoppers+Purchasing+Intention+Dataset) de Sakar, C.O., Polat, S.O., Katircioglu, M. et al. Neural Comput & Applic (2018). [Web Link](https://doi.org/10.1007/s00521-018-3523-0).

A base trata de registros de 12.330 sessões de acesso a páginas, cada sessão sendo de um único usuário em um período de 12 meses, para posteriormente estudarmos a relação entre o design da página e o perfil do cliente - "Será que clientes com comportamento de navegação diferentes possuem propensão a compra diferente?" 

Nosso objetivo é tentar agrupar os clientes conforme seu comportamento de navegação entre páginas administrativas, informativas e de produtos. 

As variáveis estão descritas abaixo (em tradução livre do link indicado).

Por este motivo, o escopo desta análise estará fechado as variáveis referentes a quantidade e tempo de acesso por tipo de página, atributos que falam mais do comportamento de navegação do cliente e de temporalidade como época do ano (informações da data, como a proximidade a uma data especial, fim de semana e o mês).

## As variáveis do dataset são descritas abaixo:

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

## Aplicativo web - Streamlit.

Você pode conferir o aplicativo [aqui](https://sannlin9-classificacao-de-clientes-inicio-q2eaeg.streamlit.app/).

## Desenvolvimento do projeto.

Toda a documentação do desenvolvimento deste projeto esta disponibilizada em [Neste notebook](https://github.com/sannlin9/Classificacao-de-clientes/blob/main/Projeto%20clusteriza%C3%A7%C3%A3o.ipynb).

## Ajuda

É possível que você encontre lentidão na aplicação principalmente durante a geração do agrupamento, por se tratar de um algoritmo de cluster para diversos tipos de variaveis(númericas e categoricagas) o algoritmo demora certa de 10 segundos para processar todas as informações. 

## Autores

Sandra Lin Costa [@SandraLin](https://www.linkedin.com/in/sandra-lin-costa/)

## Histórico de versões.

* 0.3
  * Modificações no readme e inclusão de icones de páginas.
* 0.2
	* Deploy no streamlit community cloud.
* 0.1
    * Primeira versão.

## Licença de uso
Livre

