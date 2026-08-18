es la ruta mas corta porque tiene el menor numero de segmentos (saltos)
si tiene pesos en las aritstas quiere decir que tiene un camino mas rapido  o costo o tiempo
## Pasos  
* primero se encuentra con el nodo mas barato 
* actualizo los costos de los vecino de este nodo (se usara una tabla de costos)
* repito hasta que haya hecho esto para cada nodo 
* calcula la ruta final


bfs no toma en cuenta los pesos solo los saltos pequeños entre nodos 
con dijkstra buscamos la  ruta con el peso mas pequeño 
con dijstra no se puede trabajar con grafos no dirigidos solo se usan en grafos dirigidos ponderados y aciclicos

1. se hace una tabla del costo de cada nodo el costo de un nodo es lo caro que es llegar 
2. esta tabla se va a actualizando a medida que se recorren los vecinos
ver la ejecucion paso a paso
[[Grafo Dijkstra corrida de escritorio.excalidraw]]





Relacionado con: [[grafos corrida de escritorio BFS Y DFS.excalidraw]]
