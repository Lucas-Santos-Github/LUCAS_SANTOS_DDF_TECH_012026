SELECT
  "source"."CATEGORIA" AS "CATEGORIA",
  SUM("source"."PRICE") AS "sum"
FROM
  (
    SELECT
      order_id,
      COALESCE(product_category_name, 'Nao Informado') as categoria,
      price,
      freight_value,
      order_purchase_timestamp:: DATE as data_key
    FROM
      TB__FRWC16__PUBLIC__VENDAS_OLIST_RAW
  ) AS "source"
GROUP BY
  "source"."CATEGORIA"
ORDER BY
  "sum" DESC,
  "source"."CATEGORIA" ASC
LIMIT
  10;