SELECT
  DATE_TRUNC(
    'month',
    CAST(
      "Silver_D_Time - DATA_KEY"."DATA_KEY" AS timestampntz
    )
  ) AS "Silver_D_Time - DATA_KEY__DATA_KEY",
  count(distinct "source"."ORDER_ID") AS "count"
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
 
LEFT JOIN (
    SELECT
      DISTINCT order_purchase_timestamp:: DATE as data_key,
      EXTRACT(
        YEAR
        FROM
          order_purchase_timestamp:: DATE
      ) as ano,
      EXTRACT(
        MONTH
        FROM
          order_purchase_timestamp:: DATE
      ) as mes,
      TO_CHAR(order_purchase_timestamp:: DATE, 'Month') as nome_mes
    FROM
      TB__FRWC16__PUBLIC__VENDAS_OLIST_RAW
  ) AS "Silver_D_Time - DATA_KEY" ON DATE_TRUNC('month', CAST("source"."DATA_KEY" AS timestampntz)) = DATE_TRUNC(
    'month',
    CAST(
      "Silver_D_Time - DATA_KEY"."DATA_KEY" AS timestampntz
    )
  )
GROUP BY
  DATE_TRUNC(
    'month',
    CAST(
      "Silver_D_Time - DATA_KEY"."DATA_KEY" AS timestampntz
    )
  )
ORDER BY
  DATE_TRUNC(
    'month',
    CAST(
      "Silver_D_Time - DATA_KEY"."DATA_KEY" AS timestampntz
    )
  ) ASC