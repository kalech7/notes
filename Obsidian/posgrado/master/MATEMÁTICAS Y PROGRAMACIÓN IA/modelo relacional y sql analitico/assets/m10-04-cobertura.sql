-- Incluye cobertura cero: partir del diseño config x semillas.
WITH expected_seeds(seed) AS (VALUES (11), (22))
SELECT c.config_id,
       COUNT(DISTINCT CASE WHEN m.metric_value BETWEEN 0 AND 1
                           THEN es.seed END) AS observed_seeds,
       (SELECT COUNT(*) FROM expected_seeds) AS expected_seeds
FROM configs AS c
CROSS JOIN expected_seeds AS es
LEFT JOIN runs AS r
  ON r.config_id = c.config_id AND r.seed = es.seed
 AND r.dataset_id = 'd1' AND r.status = 'completed'
LEFT JOIN metrics AS m
  ON m.run_id = r.run_id AND m.split = 'validation'
 AND m.metric_name = 'accuracy'
GROUP BY c.config_id
HAVING COUNT(DISTINCT CASE WHEN m.metric_value BETWEEN 0 AND 1
                          THEN es.seed END)
       < (SELECT COUNT(*) FROM expected_seeds)
ORDER BY c.config_id;
