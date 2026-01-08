SELECT
  "source"."CATEGORIA" AS "CATEGORIA",
  "source"."count" AS "count",
  "source"."sum" AS "sum",
  CAST("source"."sum" AS float) / NULLIF("source"."count", 0) AS "Ticket_Medio"
FROM
  (
    SELECT
      "source"."CATEGORIA" AS "CATEGORIA",
      count(distinct "source"."ORDER_ID") AS "count",
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
      "source"."CATEGORIA" ASC
  ) AS "source"
ORDER BY
  CAST("source"."sum" AS float) / NULLIF("source"."count", 0) DESC
LIMIT
  10;