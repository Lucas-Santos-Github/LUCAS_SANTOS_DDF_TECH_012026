SELECT
  "source"."Faixa_preço" AS "Faixa_preço",
  count(distinct "source"."ORDER_ID") AS "count"
FROM
  (
    SELECT
      "source"."ORDER_ID" AS "ORDER_ID",
      "source"."PRICE" AS "PRICE",
      CASE
        WHEN ("source"."PRICE" >= 0)
       
   AND ("source"."PRICE" <= 100) THEN ' Até R$100 '
        WHEN ("source"."PRICE" >= 101)
        AND ("source"."PRICE" <= 200) THEN 'De R$100 até R$200 '
        WHEN ("source"."PRICE" >= 201)
        AND ("source"."PRICE" <= 300) THEN 'De R$200 até R$300 '
        WHEN ("source"."PRICE" >= 301)
        AND ("source"."PRICE" <= 400) THEN 'De R$300 até R$400 '
        WHEN ("source"."PRICE" >= 401)
        AND ("source"."PRICE" <= 500) THEN 'De R$400 até R$500 '
        WHEN ("source"."PRICE" >= 501)
        AND ("source"."PRICE" <= 600) THEN 'De R$500 até R$600 '
        WHEN ("source"."PRICE" >= 601)
        AND ("source"."PRICE" <= 700) THEN 'De R$600 até R$700 '
        WHEN ("source"."PRICE" >= 701)
        AND ("source"."PRICE" <= 800) THEN 'De R$700 até R$800 '
        WHEN ("source"."PRICE" >= 801)
        AND ("source"."PRICE" <= 900) THEN 'De R$800 até R$900 '
        WHEN ("source"."PRICE" >= 901)
        AND ("source"."PRICE" <= 1000) THEN 'De R$900 até R$1000 '
        WHEN "source"."PRICE" > 1000 THEN 'Maior que R$1000 '
        ELSE 'Sem preço'
      END AS "Faixa_preço"
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
  ) AS "source"
GROUP BY
  "source"."Faixa_preço"
ORDER BY
  "source"."Faixa_preço" ASC