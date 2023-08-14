## Introdução
Este Notebook tem como intuito demonstrar e documentar o desenvolvimento de um modelo de predição de consumo de energia utilizando redes neurais recorrentes, mais especificamente LSTMs e GRUs.

Será feita uma análise exploratória da série temporal utilizando métodos clássicos estatísticos, juntamente com aplicação de modelos clássicos para fins de comparação e por fim avaliação de resultados.

## Dataset

O dataset utilizado foi criado pelos scripts, já respeitando o tipo de entrada que a I.A. entende, dentro da pasta **generator** que consta com uma documentação informando quais produtos foram usados como referência para criar os dados de consumo. Ele é composto pelos seguintes dados:
 * Data e hora da medição.
 * Consumo, em kWh, de energia elétrica por equipamento.
Os dados tem frequência de amostragem de 30 dias, e o intervalo total é de **01/01/2010** à **28/12/2022**.
