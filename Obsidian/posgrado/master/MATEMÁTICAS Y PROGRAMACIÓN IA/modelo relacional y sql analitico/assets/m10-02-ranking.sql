-- Dialecto SQLite. Población objetivo: dataset d1, semillas 11 y 22.
WITH expected_seeds(seed) AS (VALUES (11), (22)),
eligible_runs AS (
  SELECT d.dataset_id, d.version AS dataset_version,
         c.config_id, r.run_id, r.seed, m.metric_value
  FROM datasets AS d
  JOIN runs AS r ON r.dataset_id = d.dataset_id
  JOIN configs AS c ON c.config_id = r.config_id
  JOIN expected_seeds AS es ON es.seed = r.seed
  JOIN metrics AS m
    ON m.run_id = r.run_id
   AND m.split = 'validation'
   AND m.metric_name = 'accuracy'
  WHERE d.dataset_id = 'd1'
    AND r.status = 'completed'
    AND m.metric_value BETWEEN 0 AND 1
),
config_summary AS (
  SELECT dataset_id, dataset_version, config_id,
         AVG(metric_value) AS mean_accuracy,
         COUNT(DISTINCT seed) AS n_seeds
  FROM eligible_runs
  GROUP BY dataset_id, dataset_version, config_id
  HAVING COUNT(DISTINCT seed) = (SELECT COUNT(*) FROM expected_seeds)
),
ranked_configs AS (
  SELECT *, RANK() OVER (
    PARTITION BY dataset_id ORDER BY mean_accuracy DESC
  ) AS performance_rank
  FROM config_summary
)
SELECT dataset_id, config_id, ROUND(mean_accuracy, 4) AS mean_accuracy,
       n_seeds, performance_rank
FROM ranked_configs
ORDER BY dataset_id, performance_rank, config_id;
