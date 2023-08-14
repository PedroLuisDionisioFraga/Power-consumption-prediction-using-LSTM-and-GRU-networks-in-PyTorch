import random
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt

# Definindo o consumo médio (kW/h) e o desvio médio de consumo
# Referência: Geladeira/Refrigerador Brastemp Frost Free Duplex - 462L BRM55
averageConsumption = 66
detour = 11

# Dias e quantidade de medições por dia
days = 365
measurementsPerDay = 24
initialYear = 2010
initialDay = 1
initialMonth = 1

actualYear = datetime.now().year

print(f"Quantidade de dias analisados: {(actualYear - initialYear) * days}")

# Calculando a diferença de dias entre o ano inicial e o ano atual
numDays = (actualYear - initialYear) * 365

# Gerando os dados de data e hora
start_date = datetime(initialYear, initialMonth, initialDay)
end_date = start_date + timedelta(days=numDays)
date = pd.date_range(start_date, end_date, freq='H')

# Criando uma lista para armazenar os dados
data = []

# Gerando os dados para cada hora
current_date = start_date
while current_date < end_date:
  # Gerando um consumo aleatório com desvio médio de 100 W/h
  consumption = round(random.uniform(64.1, 67.5), 3)
  # Criando um registro com a data e o consumo
  record = {
    'Datetime': current_date.strftime('%Y-%m-%d %H:%M:%S'),
    'kWh': consumption
  }

  # Adicionando o registro à lista de dados
  data.append(record)

  # Avançando para a próxima hora
  current_date += timedelta(hours=1)

# Criando um DataFrame com os dados
df = pd.DataFrame(data)

# Plotando o gráfico
plt.figure(figsize=(10, 6))
plt.plot(df['Datetime'], df['kWh'], label='Consumo de Energia')
plt.xlabel('Data e Hora')
plt.ylabel('Consumo (kWh)')
plt.title('Refrigerador')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# Exibindo o gráfico
plt.show()

# Salvando o DataFrame em um arquivo Excel
df.to_csv('./data/consumo_geladeira.csv', index=False)
