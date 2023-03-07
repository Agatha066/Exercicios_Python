#1. Carregue a data atual do computador e, com base na data atual, apresente a data de dois dias no futuro
from datetime import datetime, timedelta

data_atual = datetime.now()
print('data atual: ',data_atual)
data_futura = data_atual = timedelta(2)
print('data futura: ',data_futura)
