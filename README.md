# Previsão de consumo de energia usando redes LSTM/GRU no PyTorch

## O que são redes neurais recorrentes?

As RNNs mostraram grande sucesso em muitas tarefas de Processamento de Linguagem Natural. Neste ponto, devo mencionar que os tipos de RNN mais usados são as LSTMs, que são muito melhores na captura de dependências de longo prazo do que as RNNs em sua arquitetura padrão.

Redes neurais recorrentes são redes com loops, permitindo que as informações persistam, pode ser imaginada como múltiplas cópias da mesma rede, cada uma passando uma mensagem a um sucessor e estão intimamente relacionadas a sequências e listas, uma arquitetura natural da rede neural a ser usada para esses dados.

## O que são redes LSTM e GRU?

GRU(Gated Recurrent Unit) é um modelo de rede neural recorrente (RNNs) que pode ser considerada uma variação da LSTM(Long Short Term Memory), que é do mesmo tipo também.

A LSTM é uma arquitetura de rede neural recorrente (RNN) que “lembra” valores em intervalos arbitrários. A LSTM é bem adequada para classificar, processar e prever séries temporais com intervalos de tempo de duração desconhecida.

Em uma rede LSTM, cada unidade de memória é composta de três "portas"(gates) que controlam a entrada, saída e esquecimento de informações. Essas portas são compostas de camadas de neurônios com funções de ativação específicas que permitem que a rede aprenda a reter informações importantes e descartar informações irrelevantes ao longo do tempo.
As redes de memória de longo prazo (LSTMs) têm ótimas memórias e podem lembrar informações que os vanilla RNNs não conseguem.
A Gated Recurrent Unit (GRU) é o irmão mais novo da mais popular rede LSTM, e também um tipo de Rede Neural Recorrente(RNN). Eles podem resolver o problema de “memória de curto prazo” que afeta as vanilla RNNs.

As GRUs, propostas pela primeira vez em 2014, são versões simplificadas das LSTMs.

Em uma rede GRU, cada unidade de memória é composta de duas portas (reset e update) que controlam o quanto de informações antigas e novas serão consideradas na atualização da memória. Assim como a rede LSTM, a rede GRU também é capaz de lidar com informações de longo prazo em sequências.

OBS: Segue o link da fonte sobre [LSTM](https://www.deeplearningbook.com.br/arquitetura-de-redes-neurais-long-short-term-memory/) e [GRU](https://www.deeplearningbook.com.br/arquitetura-de-redes-neurais-gated-recurrent-unit-gru/#:~:text=LSTM%20e%20GRU%20foram%20criadas,para%20manter%20ou%20jogar%20fora.)

## Iniciando o uso

Primeiramente vamos instalar as versões das bibliotecas necessárias para rodar nossa RMM.

Rode no CMD o seguinte comando para facilitar a instalação:
```
pip install -r requirements.txt
```
O parâmetro "-r" especifica um arquivo de requisitos, no caso "requirements.txt", que lista todos os pacotes que precisam ser instalados, juntamente com suas versões.
O Todo o comando  instalará todos os pacotes listados no arquivo "requirements.txt" e suas respectivas versões, facilitando a instalação de todos os pacotes necessários para um projeto Python.

### Explicando as bibliotecas de uso

 * **Matplotlib**: É uma biblioteca de visualização de dados para Python que permite criar gráficos, histogramas, dispersões, gráficos de barras e muito mais. Ela é amplamente usada em ciência de dados e análise exploratória de dados. A versão "~=3.5.2" indica que deve ser instalada a versão 3.5.2 ou uma versão mais recente, mas não uma versão anterior.
 * **Torch**: É uma biblioteca de aprendizado de máquina de código aberto desenvolvida principalmente pela equipe do Facebook. Ela fornece uma ampla gama de algoritmos de aprendizado de máquina e redes neurais profundas para a construção de modelos de aprendizado de máquina. A versão "~=1.8.1" indica que deve ser instalada a versão 1.8.1 ou uma versão mais recente, mas não uma versão anterior.
 * **Torchvision**: É uma biblioteca complementar ao Torch para visão computacional. Ela fornece uma variedade de ferramentas e conjuntos de dados para ajudar a treinar e avaliar modelos de visão computacional. A versão "~=0.9.1" indica que deve ser instalada a versão 0.9.1 ou uma versão mais recente, mas não uma versão anterior.
 * **Numpy**: É uma biblioteca fundamental para computação numérica em Python. Ela fornece uma ampla variedade de funções e operações para trabalhar com matrizes e outros objetos matemáticos. A versão "1.23.3" indica que deve ser instalada exatamente essa versão.
 * **Tqdm**: É uma biblioteca para criar barras de progresso em loops e outras estruturas iterativas em Python. Ela fornece uma maneira fácil de acompanhar o progresso de um processo em tempo real. A versão "~=4.64.0" indica que deve ser instalada a versão 4.64.0 ou uma versão mais recente, mas não uma versão anterior.
 * **Jupyter**: É uma plataforma web para a criação e compartilhamento de documentos que contêm código executável, visualizações de dados e texto explicativo. Ela é muito utilizada em ciência de dados e análise de dados. A versão "1.0.0" indica que deve ser instalada exatamente essa versão.
 * **Pandas**: É uma biblioteca para manipulação e análise de dados em Python. Ela fornece ferramentas para ler, escrever e trabalhar com dados tabulares, como arquivos CSV e Excel. A versão "1.3.5" indica que deve ser instalada exatamente essa versão.
 * **Scikit-learn**: É uma biblioteca para aprendizado de máquina em Python que fornece uma ampla gama de algoritmos de aprendizado de máquina supervisionados e não supervisionados. Ela é amplamente utilizada em tarefas de classificação, regressão e agrupamento. A versão "1.0.2" indica que deve ser instalada exatamente essa versão.

## Objetivos

 * O objetivo dessa implementação é criar um modelo que possa prever com precisão o uso de energia na próxima hora com dados históricos de uso.
 * No final compararemos o desempenho do modelo GRU com um modelo LSTM.
