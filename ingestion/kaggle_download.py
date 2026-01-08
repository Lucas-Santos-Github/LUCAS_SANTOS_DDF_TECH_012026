import pandas as pd
import os
import kagglehub

# 1. Download da base oficial via KaggleHub
print("Baixando dataset da Olist...")
path = kagglehub.dataset_download("olistbr/brazilian-ecommerce")
print("Arquivos baixados em:", path)

# 2. Carregamento das tabelas necessárias para o Case
# Usaremos Orders (Pedidos), Items (Itens) e Products (Produtos)
orders = pd.read_csv(f"{path}/olist_orders_dataset.csv")
items = pd.read_csv(f"{path}/olist_order_items_dataset.csv")
products = pd.read_csv(f"{path}/olist_products_dataset.csv")
reviews = pd.read_csv(f"{path}/olist_order_reviews_dataset.csv") 
# Importante para o Item 5 (GenAI)

# 3. Join para criar uma visão consolidada (Denormalização para Bronze/Silver)
# Isso ajuda a atingir os 100.000 registros com facilidade
df_consolidado = items.merge(orders, on='order_id', how='inner')
df_consolidado = df_consolidado.merge(products, on='product_id', how='left')

# 4. Verificação de Volumetria
total_registros = len(df_consolidado)
print(f"Total de registros consolidados: {total_registros}")

if total_registros >= 100000:
    print("✅ Requisito de > 100.000 registros atingido!")
else:
    print("⚠️ Atenção: Volume abaixo de 100k. Verifique os joins.")

# 5. Exportação para Ingestão na Dadosfera
# Vamos gerar dois arquivos: um para a Fato de Vendas e outro para os Reviews (Texto Desestruturado)
df_consolidado.to_csv("vendas_olist_dadosfera.csv", index=False)
reviews.to_csv("reviews_olist_genai.csv", index=False)

print("Arquivos prontos para upload: 'vendas_olist_dadosfera.csv' e 'reviews_olist_genai.csv'")