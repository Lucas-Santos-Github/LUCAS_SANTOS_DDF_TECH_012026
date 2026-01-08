import pandas as pd
from sqlalchemy import create_engine

# 1. Suas credenciais do RDS AWS (as mesmas que usamos antes)
DB_USER = 'postgres'
DB_PASSWORD = 'DDFTECH012026'
DB_HOST = 'ddf-tech-012026.cmxemg2wqxm7.us-east-1.rds.amazonaws.com'
DB_PORT = '5432'
DB_NAME = 'ddfsource'

# 2. Conectar ao Banco
engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

print("🔍 Lendo dados diretamente do PostgreSQL na AWS para validação...")

# 3. Executar a consulta de validação
# Dica: Já trazemos os dados prontos para o relatório
df_val = pd.read_sql("SELECT order_id, price, order_status, product_category_name FROM vendas_olist_raw", engine)

# 4. Aplicar a lógica de qualidade (Reaproveitando nossa lógica anterior)
total = len(df_val)
price_errors = (df_val['price'] <= 0).sum()
null_orders = df_val['order_id'].isnull().sum()
null_cats = df_val['product_category_name'].isnull().sum()

print("\n" + "="*50)
print("📊 RELATÓRIO DE QUALIDADE - CAMADA TRANSACIONAL (AWS)")
print("="*50)
print(f"✔️ Total de registros analisados no banco: {total}")
print(f"{'✔️' if price_errors == 0 else '⚠️'} Erros de Preço: {price_errors}")
print(f"{'✔️' if null_orders == 0 else '⚠️'} Pedidos sem ID: {null_orders}")
print(f"{'✔️' if (null_cats/total) < 0.05 else '⚠️'} Categorias Nulas: {null_cats} ({ (null_cats/total):.2%})")
print("="*50)