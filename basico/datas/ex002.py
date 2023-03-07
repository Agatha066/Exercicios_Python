# 2. Carregue a data atual do computador e apresente somente a data

from datetime import datetime

data_atual = datetime.now()
print(data_atual.date())