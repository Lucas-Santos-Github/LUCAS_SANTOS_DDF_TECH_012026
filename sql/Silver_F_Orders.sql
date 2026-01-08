SELECT 
    order_id,
    COALESCE(product_category_name, 'Nao Informado') as categoria,
    price,
    freight_value,
    order_purchase_timestamp::DATE as data_key
FROM TB__FRWC16__PUBLIC__VENDAS_OLIST_RAW;