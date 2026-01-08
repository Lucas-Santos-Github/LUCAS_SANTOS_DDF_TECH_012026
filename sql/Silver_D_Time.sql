SELECT 
    DISTINCT order_purchase_timestamp::DATE as data_key,
    EXTRACT(YEAR FROM order_purchase_timestamp::DATE) as ano,
    EXTRACT(MONTH FROM order_purchase_timestamp::DATE) as mes,
    TO_CHAR(order_purchase_timestamp::DATE, 'Month') as nome_mes
FROM TB__FRWC16__PUBLIC__VENDAS_OLIST_RAW;
