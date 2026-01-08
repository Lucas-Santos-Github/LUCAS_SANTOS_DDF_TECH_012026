import pandas as pd
from sqlalchemy import create_engine

# Configurações do seu RDS AWS
DB_USER = 'postgres'
DB_PASSWORD = 'DDFTECH012026'
DB_HOST = 'ddf-tech-012026.cmxemg2wqxm7.us-east-1.rds.amazonaws.com'
DB_PORT = '5432'
DB_NAME = 'ddfsource'

# Criar conexão
engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

# Carregar o CSV gerado anteriormente
df = pd.read_csv('vendas_olist_dadosfera.csv')

# Enviar para o banco (isso criará a tabela automaticamente)
print("Enviando dados para o RDS AWS...")
df.to_sql('vendas_olist_raw', engine, if_exists='replace', index=False)
print("Dados carregados com sucesso!")