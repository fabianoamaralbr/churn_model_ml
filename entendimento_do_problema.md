# Compreendendo o Problema de Negócio
**Problema de negócio** é um **resultado indesejado no processo**, podendo ser uma limitação, uma falha, ou uma consequência de fatos em série. Quando um **Modelo de Machine Learning** está sendo desenvolvido, uma boa definição do que é o Problema de Negócio é fundamental, pois quando a solução é desenvolvida sem estar claro qual é o problema a ser solucionado, provavelmente será gasto mais recursos do que o necessário, para talvez não chegar a um produto final que será efetivo.

### Qual é o Problema de Negócio desse projeto?
Aqui estamos lidando com um problema de Churn de uma instituição financeira, que tem perdido muitos clientes ultimamente. O objetivo é poder prever quais os clientes atuais estão prestes a trocar o serviço da empresa por outra e realizar interverções personalizadas para evitar o desligamento do cliente.

### O que é Churn?
Como explicado na primeira parte deste projeto, Churn é uma métrica que indica o quanto uma empresa perdeu de clientes em determinado período, podendo ter um parâmetro anual, semestral ou mensal. O índice de cancelamento tem importância significativa para o caixa da empresa, pois quanto maior o Churn, maior será a redução da receita da mesma. Isso acaba provocando desequilibrio no Fluxo de Caixa, mesmo que o time de vendas esteja batendo todas as metas.\
\
Para calcular o índice de cancelamento ou índice de Churn (C), dentro do período que está sendo analisado, é preciso dividir o total de cancelamentos de todo o período (Tcan), pelo total de clientes no início do período (Tini).
<center>

* #### **C = Tcan / Tini**

<center>
Exemplo: Uma empresa quer calcular o índice de Churn do mês anterior. No primeiro dia do mês, havia em seu portfólio 1.500 clientes. Ao longo desse mesmo mês, houve 215 cancelamentos de seus serviços. Aplicando a fórmula, fica: $C = 215/1500 = 0,1433$. Portanto o índice de Churn daquele mês apurado foi de 14,33%.\
\
Obviamente, quanto menor for esse percentual, melhor para a empresa, pois a mesma está realizando um bom trabalho de retenção.

### Qual o motivo do Churn nas empresas?

### Como reduzir o Churn?

### Como podemos resolver esse problema com Machine Learning?

O primeiro passo é realizar uma coleta de dados dos clientes. Através dos dados, é possível encontrar padrões que indicam os clientes que estão prestes a deixar a empresa, com base no perfil dos que já executaram o cancelamento anteriormente. No presente projeto, os dados representam o comportamento dos clientes dentro do banco (número de serviços, saldo, cartão de crédito, se são ativos ou não...).\
\
Um Modelo de Machine Learning pode ajudar na solução desse problema, analizando o padrão de comportamento dos clientes e realizando a previsão dos que tem uma tendência a deixar a empresa e consequentemente aumentar o índice de Churn. Para esse projeto, as etapas para desenvolvimento da solução serão:

**1. Análise Exploratória dos Dados (e Feature Engineering)**
Nesse momento é realizado uma análise exploratória para compreender melhor os dados. Começar a preparação dos dados para o Modelo, considerando os que tem relevância conceitual para o problema de negócio. Verifcicar qual a correlação entre as variáveis, a relação das variáveis com a variável álvo (a que classifica que o cliente deu churn ou não), ver qual é distribuição de cada variável.

A análise exploratória permite ao Cientista de Dados o entendimento de como podemos melhorar o desempenho da previsão do Modelo, fazendo uma tranformação nos dados brutos em características que representam melhor o problema ao modelo preditivo. Também nessa fase, é identificado erros nos dados e faz parte da transformação adequa-los caso haja dados faltantes e/ou discrepantes.

**2. Análise do melhor modelo para a solução do problema**
Para o problema de Churn, será utilizado um modelo de classificação. Os mais conhecidos são Regressão Logísitca, Árvore de Decisão, Floresta Aleatória, KNN e XGBoost. Qual é o melhor? Essa é a pergunta norteadora para essa fase, onde através de teste será verificado o melhor modelo para que a solução seja implementada.\
\
Após a análise dos modelos de maior eficácia, o trabalho consiste em realizar ajuste de hiperparâmetros (configurações de cada modelo) e testa-los para verificar qual a configuração mais se adequa como solução para o problema de negócio.

**3. Monitoramento e avaliação do modelo**
Os modelos com melhor performance precisam ser colocados em produção, seja incorporando à um software já utilizado na empresa ou criando um novo programa. Independete de como será realizado essa entrega (deploy), os modelos precisam estar em periódico monitoramento para valiar seu desempenho, e melhora-lo quando for necessário.
<<<<<<< HEAD

[<< Voltar para a homepage do Projeto](README.md) | [Análise Exploratória dos Dados >>](analise_exploratoria.ipynb)
