## Introdução
Este Notebook tem como intuito demonstrar e documentar o desenvolvimento de um modelo de predição de consumo de energia no município de Florianópolis utilizando redes neurais recorrentes, mais especificamente LSTMs.

Serão abordados temas como a obtenção do banco de dados utilizado e também a limpeza, organização e padronização destes dados.

Será feita uma análise exploratória da série temporal utilizando métodos clássicos estatísticos, juntamente com aplicação de modelos clássicos para fins de comparação e por fim avaliação de resultados.

## Dataset

O dataset utilizado foi retirado da [página de informações de mercado de energia da CELESC (Centrais Elétricas de Santa Catarina S.A.).](https://www.celesc.com.br/home/mercado-de-energia/dados-de-consumo) Ele é composto pelos seguintes dados:
 * Número de unidades consumidoras atendidas por região.
 * Consumo, em MWh, de energia elétrica por região.
Os dados tem frequência de amostragem de 30 dias, e o intervalo total é de **01/01/1994** à **01/09/2022**.