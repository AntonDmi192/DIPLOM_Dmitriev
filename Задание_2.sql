SELECT DISTINCT track,
				CASE
					WHEN finished = true THEN 2
					WHEN cancelled = true THEN -1
					WHEN "inDelivery" = true THEN 1
					ELSE 0
				END AS "Status"
FROM "Orders";