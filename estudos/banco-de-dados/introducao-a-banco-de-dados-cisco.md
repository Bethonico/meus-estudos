---
titulo: "Introdução a Banco de dados Cisco"
categoria: "Banco de Dados"
subcategoria: "Ciência de dados"
nivel: "Iniciante"
status: "Estudando"
atualizado_em: "2026-08-28T18:31:00.000Z"
---

# Introdução a Banco de dados Cisco


# BIG DATA

Como big data funciona, eu sei que uma big data tem as seguintes caracteristicas:

 **VOLUME: **Quantidade absurda de dados

**VELOCIDADE: **Rapido na coleta de dados e no seu armazenamento

**VARIEDADE: **Os dados vem de varias fontes diferentes

**VERACIDADE: **Os dados devem ser veridicos e relacionados



Piperline de dados

FLuxograma de como os dados fluem.

 **ETL**, que significa **E**xtract, **T**ransform e **L**oad. A extração é equivalente à ingestão e o armazenamento é equivalente à carga.




**EXTRACT**

Os dados obtidos devem ter fontes as principais são servidores ou bancos de dados (ingestão de lote) e eventos em tempo real que acontecem no mundo e streaming do mundo dos dispositivos (ingestão de streaming) eles são obtidos de uma variedades de formas e são armazenados temporariamente para serem tranformados em informações uteis.



**TRANSFORM**

Premeiro os dados são limpos e colocados em padrões e formatos corretos essa limpeza busca tembem aumentar a veracidade das informações e atualizalas tambem essa parte e fundamentao para a leitura posterior.

Depois essas informaçoes podem ser usadas, alguns exemplos:

**Principais Formas de Utilizar os DadosTomada de decisões:** Substituir a intuição por fatos reais e métricas comprovadas no dia a dia do negócio.

**Previsão de demanda:** Analisar o histórico de vendas e sazonalidades para controlar estoques e evitar produtos parados. 

**Personalização do marketing:** Entender o comportamento e os hábitos dos clientes para criar campanhas direcionadas e ofertas específicas.

**Melhoria da experiência do cliente:** Mapear preferências e canais de atendimento preferidos (como WhatsApp ou e-mail) para um contato mais humanizado.

 **Otimização de processos:** Acompanhar indicadores em tempo real para corrigir falhas rapidamente e alocar recursos onde dão mais retorno. 



**LOAD:**

Depois de transformar os dados, eles precisam ser armazenados em locais e formulários, facilitando para os analistas a execução de relatórios sobre vendas semanais e para os cientistas de dados para criar modelos de recomendação preditivos. Segurança de dados ou gerenciamento de acesso a dados para que as pessoas que devem acessar os dados possam acessar de forma eficiente e impedir a entrada de pessoas que não devem.

Há dois locais principais para as empresas armazenarem os dados, no local ou na nuvem.



**Big Data Warehouse** é uma plataforma centralizada de armazenamento de dados projetada para gerenciar e analisar volumes massivos de informações (os chamados *Big Data*).

Diferente de um banco de dados tradicional, ele é otimizado para a realização de consultas complexas, geração de relatórios e análises de inteligência de negócios (Business Intelligence).

### Principais Características

  - **Alta Escala:** Capacidade de processar petabytes ou exabytes de dados sem perder desempenho.

  - **Integração de Fontes:** Consolida dados provenientes de múltiplos sistemas (CRMs, sites, aplicativos, dispositivos IoT, bancos de dados transacionais).

  - **Estruturação:** Organiza e transforma dados brutor em formatos otimizados para leitura e análise rápida.

  - **Orientação ao Tempo:** Mantém o histórico dos dados ao longo dos anos para análise de tendências históricas.









# CONCEITOS DE IA E MACHINE LEANING






Machine learning é um subconjunto da IA que utiliza dados e resultados passados para treinar um programa para reconhecer padrões e executar tarefas sem a necessidades de programa-lo de uma maneira especifica.

## Os 3 Principais Tipos de Aprendizado

### **Supervisionado**

Utilizar dados tratados por humanos esses dados são de entrada e saída já existentes para a IA reconhecer os padrões e ter uma previsibilidade de dados futuros, esse método depende muito da veracidade dos dados tanto de entrada quanto os de saida.

Os métodos de aprendizado de máquina supervisionado geralmente resolvem problemas de regressão e classificação:

  - **Problemas de regressão** envolvem a estimativa das relações matemáticas entre uma variável contínua e uma ou mais outras variáveis. Essa relação matemática pode calcular os valores de uma variável desconhecida, de acordo com os valores conhecidos das outras. Exemplos de problemas que usam a regressão incluem estimar a posição e a velocidade de um carro usando GPS, prever a trajetória de um tornado usando dados climáticos ou prever o valor futuro de uma ação usando dados históricos e outros dados.

  - **Os problemas de classificação** consistem em uma variável desconhecida discreta. Normalmente, o problema envolve estimar qual amostra específica pertence a um conjunto de classes predefinidas. Exemplos de classificação são filtrar e-mail em spam ou não spam, diagnosticar patologias de exames médicos ou identificar rostos em uma imagem.

### **Sem supervisão**


Esse método não tem necessidade de dados fornecidos por especialistas pois a IA reconhece padrões nos dados de forma autônoma.  Lida principalmente com dados não rotulados encontrando padrões e informações.

Exemplos de problemas resolvidos com métodos não supervisionados são clustering e associação:

  - **Métodos de clustering** – Clustering é o agrupamento de dados que têm características semelhantes. Ele ajuda a segmentar os dados em grupos e analisa cada um para encontrar padrões. Por exemplo, algoritmos de agrupamento identificam grupos de usuários com base em seu histórico de compras online e, em seguida, enviam anúncios direcionados a cada membro.

  - **Métodos de associação** - A associação consiste em descobrir grupos de itens frequentemente observados juntos. Os varejistas on-line usam associações para sugerir compras adicionais a um usuário com base no conteúdo do carrinho de compras.



### **Reforço**

O aprendizado por reforço assume um modelo de tentativa e erro, recompensando comportamentos esperados e punindo erros, o sistema aos poucos aprende a fornecer os resultados esperados e evitar resultados inesperados.

Esse modelo e usado em videogames, robótica e automações



## **O Processo de Aprendizado de Máquina**

O desenvolvimento de uma solução de aprendizado de máquina raramente é um processo linear. Várias etapas de tentativa e erro são necessárias para ajustar a solução. Os detalhes de cada etapa realizada pelos cientistas de dados dos Data Crunchers, enquanto trabalham no novo modelo de identificação e erradicação de ervas daninhas, são os seguintes:

**Etapa 1. Preparação de dados** – Execute procedimentos de limpeza de dados, como transformação em um formato estruturado e remoção de dados ausentes e observações com ruído/corrompidas.

**Etapa 2-a. Dados de aprendizado** - Criar um conjunto de dados de aprendizado usado para treinar o modelo.

**Passo 2b. Dados de teste **– Crie um conjunto de dados de teste usado para avaliar o desempenho do modelo. Execute esta etapa apenas no caso de aprendizado supervisionado.

**Etapa 3. Loop do processo de aprendizagem **– Seleção. Um algoritmo é escolhido de acordo com o problema. Dependendo do algoritmo selecionado, podem ser necessárias etapas adicionais de pré-processamento.

**Etapa 4. Loop do processo de aprendizagem** – Avaliação. O desempenho desse algoritmo selecionado é avaliado nos dados de aprendizado. Se o algoritmo e o modelo atingirem um desempenho aceitável nos dados de aprendizado, a solução validará os dados de teste. Caso contrário, repita o processo de aprendizado com um novo modelo e algoritmo propostos.

**Etapa 5. Avaliação do modelo** – Teste a solução nos dados de teste. Os desempenhos nos dados de aprendizagem não são necessariamente transferíveis para os dados de teste. Quanto mais complexo e ajustado for o modelo, maiores serão as chances de ele se tornar propenso a overfitting, o que significa que ele não pode ter um desempenho preciso em relação a dados não vistos. O ajuste excessivo pode resultar no retorno ao processo de aprendizado do modelo.

**Etapa 6. Implementação do modelo** – Depois que o modelo atingir um desempenho satisfatório nos dados de teste, implemente o modelo. Implementar o modelo significa realizar as tarefas necessárias para dimensionar a solução de aprendizado de máquina para Big Data.



As etapas do processo de aprendizado de máquina na ordem são:

**Etapa 1** – Prepare a data com procedimentos de limpeza de dados

**Etapa 2** – Criar um conjunto de dados de aprendizado usado para treinar o modelo e testar um conjunto de dados para avaliar o modelo

**Etapa 3** – O algoritmo é escolhido de acordo com o problema a ser resolvido

**Etapa 4** – O algoritmo é avaliado nos dados de aprendizagem

**Etapa 5** – A solução é testada em relação aos dados de teste

**Etapa 6** – O modelo é implementado.



## **Treinando Máquinas para Reconhecer Padrões**

O reconhecimento de padrões usa o conceito de aprendizado para classificar dados com base nas informações estatísticas obtidas com os padrões e suas representações. O aprendizado permite que os sistemas de reconhecimento de padrões sejam "treinados" e adaptáveis para fornecer resultados mais precisos. Ao treinar o sistema de reconhecimento de padrões, uma parte do conjunto de dados prepara o sistema, e o restante testa a precisão do sistema. Conforme mostrado na figura abaixo, o conjunto de dados é dividido em dois grupos: treinar o modelo e testar o modelo. O conjunto de dados de treinamento é usado para criar o modelo e consiste em cerca de 80% dos dados. Ele contém o conjunto de imagens usadas para treinar o sistema. O conjunto de dados de teste consiste em cerca de 20% dos dados e mede a precisão do modelo. Por exemplo, se o sistema que identifica categorias de aves puder identificar corretamente sete em cada dez aves, a precisão do sistema será de 70%.







Os algoritmos de reconhecimento de padrão podem ser aplicados a diferentes tipos de dados digitais, incluindo imagens, textos ou vídeos, e podem ser usados para automatizar e resolver totalmente problemas analíticos complicados. As aplicações e os casos de uso para reconhecimento de padrões são praticamente ilimitados. Alguns exemplos incluem:

  - **Segurança móvel** – Identificação de impressões digitais ou reconhecimento facial para obter acesso a um smartphone.

  - **Engenharia** – Reconhecimento de fala por sistemas de assistente digital, como Alexa, Google Assistant e Siri.

  - **Geologia** – Detecção de tipos específicos de rochas e minerais e interpretação de padrões temporais em gravações de matrizes sísmicas.

  - **Biomédica** – Uso de padrões biométricos para identificar células tumorais e cancerígenas no corpo.







### Plataformas para analises de dados e postar o portfolio

As respostas variam, mas podem incluir as seguintes plataformas.

**Plataformas de mídia social **– A publicação em mídia social (como Twitter, Quora, Reddit e LinkedIn) pode criar sua legitimidade como profissional de dados e uma boa maneira de obter mais visibilidade para seus projetos.

**DataCamp Workspace **- Um Data Notebook colaborativo baseado em nuvem onde você pode analisar dados instantaneamente, colaborar com outros e publicar uma análise. Ao criar projetos, você pode compartilhar o link para o perfil do DataCamp para que outras pessoas possam ter acesso.

**GitHub **–  Um site e serviço em nuvem que permite que os desenvolvedores armazenem, gerenciem e monitorem seus repositórios de código. Ele permite que os usuários colaborem ou publiquem projetos de código aberto.

**Kaggle **–  Uma plataforma de comunidade on-line para que os entusiastas de dados colaborem, encontrem e publiquem conjuntos de dados, publiquem notebooks e concorram com outras pessoas para resolver os desafios da ciência de dados. Para apresentar seu trabalho, crie um notebook ou kernel que ajude outras pessoas a descobrir e entender seu projeto.

**Sites para Criar e Hospedar um Site Pessoal ou Blog **-  Sites pessoais ou blogs são outra maneira de ter seus projetos todos em um só lugar e compartilhá-los de forma econômica. Esses sites permitem mais controle e personalização do conteúdo do que o DataCamp Workspace e o Kaggle. O WordPress e o Wix são boas opções para criar e hospedar um blog ou site.























