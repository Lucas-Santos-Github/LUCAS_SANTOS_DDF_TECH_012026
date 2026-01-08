import pandas as pd
import numpy as np

print("🚀 Iniciando Validação de Qualidade de Dados (Data Quality Report)...\n")

# 1. Carregamento
df = pd.read_csv("vendas_olist_dadosfera.csv")

def validate_data(df):
    results = []
    
    # Regra 1: order_id não nulo
    null_orders = df['order_id'].isnull().sum()
    results.append({
        "coluna": "order_id",
        "regra": "expect_column_values_to_not_be_null",
        "sucesso": null_orders == 0,
        "detalhe": f"{null_orders} nulos encontrados"
    })
    
    # Regra 2: Preço positivo
    invalid_prices = (df['price'] <= 0).sum()
    results.append({
        "coluna": "price",
        "regra": "expect_column_values_to_be_between(min=0.01)",
        "sucesso": invalid_prices == 0,
        "detalhe": f"{invalid_prices} preços inválidos encontrados"
    })
    
    # Regra 3: Status válidos
    status_validos = ['delivered', 'shipped', 'canceled', 'invoiced', 'processing', 'unavailable', 'approved', 'created']
    invalid_status = (~df['order_status'].isin(status_validos)).sum()
    results.append({
        "coluna": "order_status",
        "regra": "expect_column_values_to_be_in_set",
        "sucesso": invalid_status == 0,
        "detalhe": f"{invalid_status} status desconhecidos"
    })
    
    # Regra 4: Categorias preenchidas (Aceitamos 5% de nulos)
    null_cats = df['product_category_name'].isnull().sum()
    pct_null = (null_cats / len(df))
    results.append({
        "coluna": "product_category_name",
        "regra": "expect_column_values_to_not_be_null(mostly=0.95)",
        "sucesso": pct_null <= 0.05,
        "detalhe": f"{null_cats} categorias nulas ({pct_null:.2%})"
    })
    
    return results

# Executar Validação
report = validate_data(df)

# Exibição do Relatório (Formatado para o GitHub)
print("="*60)
print("📊 RELATÓRIO DE QUALIDADE DE DADOS (Data Quality) - CASE DADOSFERA")
print("="*60)

for r in report:
    emoji = "✔️" if r['sucesso'] else "⚠️"
    status = "PASS" if r['sucesso'] else "FAIL"
    print(f"{emoji} [{status}] Coluna: {r['coluna'].ljust(22)} | Regra: {r['regra']}")
    if not r['sucesso'] or "nulas" in r['detalhe']:
        print(f"   👉 Detalhe: {r['detalhe']}")

print("="*60)
print("Ação Sugerida: Tratamento de valores nulos em 'product_category_name' na camada Silver.")