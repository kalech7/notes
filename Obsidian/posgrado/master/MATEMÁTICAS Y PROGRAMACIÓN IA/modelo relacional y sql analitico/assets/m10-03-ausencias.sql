-- Detectar ausencia de fila, conservando los runs objetivo.
WITH expected_seeds(seed) AS (VALUES (11), (22))
SELECT r.run_id, r.config_id, r.seed
FROM runs AS r
JOIN expected_seeds AS es ON es.seed = r.seed
LEFT JOIN metrics AS m
  ON m.run_id = r.run_id
 AND m.split = 'validation'
 AND m.metric_name = 'accuracy'
WHERE r.dataset_id = 'd1' AND r.status = 'completed'
  AND m.run_id IS NULL;
