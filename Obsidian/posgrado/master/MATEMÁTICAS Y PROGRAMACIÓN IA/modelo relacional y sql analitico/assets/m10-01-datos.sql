-- Datos sintéticos de estudio. Ejecutar en una base nueva.
PRAGMA foreign_keys = ON;
CREATE TABLE datasets (
  dataset_id TEXT PRIMARY KEY NOT NULL,
  version TEXT NOT NULL
);
CREATE TABLE configs (
  config_id TEXT PRIMARY KEY NOT NULL,
  hidden_units INTEGER NOT NULL,
  learning_rate REAL NOT NULL
);
CREATE TABLE runs (
  run_id TEXT PRIMARY KEY NOT NULL,
  dataset_id TEXT NOT NULL REFERENCES datasets(dataset_id),
  config_id TEXT NOT NULL REFERENCES configs(config_id),
  seed INTEGER NOT NULL,
  status TEXT NOT NULL,
  UNIQUE(dataset_id, config_id, seed)
);
CREATE TABLE metrics (
  run_id TEXT NOT NULL REFERENCES runs(run_id),
  split TEXT NOT NULL,
  metric_name TEXT NOT NULL,
  metric_value REAL NOT NULL,
  PRIMARY KEY(run_id, split, metric_name)
);
INSERT INTO datasets VALUES ('d1','v1'),('d2','v2');
INSERT INTO configs VALUES
 ('A',128,0.1),('B',128,0.01),('C',64,0.1),('D',64,0.01),('E',32,0.1);
INSERT INTO runs VALUES
 ('a11','d1','A',11,'completed'),('a22','d1','A',22,'completed'),
 ('b11','d1','B',11,'completed'),('b22','d1','B',22,'completed'),
 ('c11','d1','C',11,'completed'),('c22','d1','C',22,'completed'),
 ('d11','d1','D',11,'completed'),('d22','d1','D',22,'completed'),
 ('e11','d1','E',11,'failed'),('e22','d1','E',22,'failed'),
 ('a99','d1','A',99,'completed'),('a2v','d2','A',11,'completed');
INSERT INTO metrics VALUES
 ('a11','validation','accuracy',0.75),('a22','validation','accuracy',0.95),
 ('b11','validation','accuracy',0.85),('b22','validation','accuracy',0.85),
 ('c11','validation','accuracy',0.92),
 ('d11','validation','accuracy',0.70),('d22','validation','accuracy',0.80),
 ('e11','validation','accuracy',0.99),
 ('a99','validation','accuracy',0.99),('a2v','validation','accuracy',0.99),
 ('a11','train','accuracy',0.99),('a11','validation','loss',0.4);
