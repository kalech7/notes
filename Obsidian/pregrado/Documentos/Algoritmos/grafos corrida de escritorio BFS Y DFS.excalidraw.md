---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠==


# Text Elements
cola [] +[1,6]
cola[1,6]
nodo=0,1 ^0u77kAcc

grafo[0]=[1,6]
grafo[1]=[0,2,4]
grafo[2]=[1,3]
grafo[3]=[2,5]
grafo[4]=[1,5,6]
grafo[5]=[3,4]
grafo[6]=[0,4]
searched=[0] ^wE8vbzM2

Decolo 1 y encolamos los vecinos  del nodo 1
grafo[1]=>[0,2,4]
cola[1,6,0,2,4]
searched[0,1]
busquedanodo=false,false
 ^Fo1zbQO7

en este grafo se marca el nodo de inicio  ^Ic90E0uj

cola[6,02,4]
nodo=0,1,6
decolo 6 y encolamos los vecinos del nodo 6
grafo[6]=> [0,4]
cola[6,0,2,4,0,4]
searched[0,1,6]
busqueda nodo= false false false
 ^5MkXHzJK

cola[0,2,4]
nodo=0,1,6
no se ejecuta ya que esta la lista de searched se sigue al siguiente nodo ^QEMSQifQ

cola[2,4]
nodo=0,1,6
grafo[2]=[1,3]
cola[2,4,1,3]
searched[0,1,6,2]
busqueda nodo= false false false flase ^3g4tXNGK

cola[4,1,3]
nodo=0,1,6,4
grafo[4]=[1,5,6]
cola[4,1,3,1,5,6]
searched[0,1,6,2]
busqueda nodo= false false false false  false ^ll2NzF0O

cola[1,3]
nodo=0,1,6,4
se salta al siguiente de la cola ya que esta el 1 en searched
busqueda nodo= false false false false  false false

 ^zeIm2tpC

cola[3]
nodo=0,1,6,4
es el nodo que se busca y se para el algoritmo
busqueda nodo= false false false false  false false true ^rQRJ8tEo

Algoritmo BFS ^OfOJOzfZ

grafo[0]=[1,6]
grafo[1]=[0,2,4]
grafo[2]=[1,3]
grafo[3]=[2,5]
grafo[4]=[1,5,6]
grafo[5]=[3,4]
grafo[6]=[0,4]
grafp[7]=[] ^s4Gc4Hf5

Algoritmo DFS ^84jpJmk9

5 ^vDIFQ8FF

searched=[f,f,f,f,f,f,f]
componenteR=[0,1,2,3,5,4,6 
parent=[0,0,0,0,0,0,0]
 ^LEtY2HOt

DFS 0 ^rLINJP7c

DFS 1 ^3L0xt8J5

0 ^V8RquOMS

2 ^EN17f34Y

4 ^18HdErf2

1 ^PVz8u8UC

6 ^V6SYFOZ9

DFS 2 ^meRmkJ7U

1 ^hZcd5Qyt

3 ^o3Cc2BYB

parent=[0,0,0,2,0,0,0]
 ^sCTOut3X

parent=[0,0,1,2,0,0,0]
 ^dz8Z3TJ0

DFS 3 ^otd49krY

2 ^un65FFSS

5 ^owsMEnZd

parent=[0,0,1,2,0,3,0]
 ^jDYVEqPd

DFS 5 ^5QMVUA8w

DFS 4 ^hR1uooJF

1 ^gDLolPmd

5 ^KuIKjvNl

6 ^DclbFoh9

DFS 6 ^vJNJHylu

0 ^Js50Xmnr

4 ^pnFCxslO

parent=[0,0,1,2,5,3,0]
 ^U7OPBOzw

parent=[0,0,1,2,5,3,4]
 ^CxFoG9Wj

searched=[t,t,t,t,t,t,t] ^KAb9M4q4

parent nos ayuda aconstriur el arbol ^PfSjSwKS

0 ^OEZv8Pf4

1 ^eLgGJm5U

2 ^oHBigAS6

3 ^fFMLeNT8

5 ^3c747dzj

4 ^6vPSsRzU

6 ^5W2vtZvL

(nodos) 0 1 2 3 4 5 6   ^FUm8CTJs

El diccionario parents se utiliza para almacenar información sobre los padres
 de los nodos en el recorrido DFS. Durante el recorrido, a medida que se visita 
un nuevo nodo, se registra su padre, es decir, el nodo desde el cual se llegó a él. ^gZhW299r

%%
# Drawing
```json
{
	"type": "excalidraw",
	"version": 2,
	"source": "https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/tag/1.9.6",
	"elements": [
		{
			"type": "ellipse",
			"version": 55,
			"versionNonce": 174753093,
			"isDeleted": false,
			"id": "ivqxF77BC4n1ALxqDsnPV",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -489.6000061035156,
			"y": 349.1624984741211,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 60,
			"height": 52,
			"seed": 2028604581,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687813260283,
			"link": null,
			"locked": false
		},
		{
			"type": "line",
			"version": 46,
			"versionNonce": 190782859,
			"isDeleted": false,
			"id": "wDHFE31s7w0U_eqmYeVt9",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -431.1999816894531,
			"y": 365.9625015258789,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 159.99996948242188,
			"height": 2.399993896484375,
			"seed": 1777336683,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687813260283,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					159.99996948242188,
					-2.399993896484375
				]
			]
		},
		{
			"type": "ellipse",
			"version": 80,
			"versionNonce": 869504165,
			"isDeleted": false,
			"id": "9t4Mx5C3iCpi_Hae8qZT1",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -272.79998779296875,
			"y": 337.9625015258789,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 82.39996337890625,
			"height": 58.399993896484375,
			"seed": 1673376261,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687813260283,
			"link": null,
			"locked": false
		},
		{
			"type": "line",
			"version": 32,
			"versionNonce": 1415132203,
			"isDeleted": false,
			"id": "H-9y9obJOgdQKepww5dVD",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -228,
			"y": 396.36251068115234,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4,
			"height": 66.40000915527344,
			"seed": 1726820555,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687813260283,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					4,
					66.40000915527344
				]
			]
		},
		{
			"type": "ellipse",
			"version": 83,
			"versionNonce": 539211781,
			"isDeleted": false,
			"id": "jhbWa8cEfVQm8b8tdATjJ",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -252.79998779296875,
			"y": 460.3624954223633,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 59.20001220703125,
			"height": 67.20001220703125,
			"seed": 1223772421,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687813260283,
			"link": null,
			"locked": false
		},
		{
			"type": "ellipse",
			"version": 119,
			"versionNonce": 790066891,
			"isDeleted": false,
			"id": "9gDGpiW7V6FS2UPR7n-7t",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -468,
			"y": 490.76248931884766,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 68.00006103515625,
			"height": 64,
			"seed": 1187723205,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687813260283,
			"link": null,
			"locked": false
		},
		{
			"type": "line",
			"version": 59,
			"versionNonce": 156790629,
			"isDeleted": false,
			"id": "ToxFl2SF0sCDcFPIYNS7i",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -456.79998779296875,
			"y": 398.7625045776367,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 12.800018310546875,
			"height": 94.40000915527344,
			"seed": 775312037,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687813260283,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					12.800018310546875,
					94.40000915527344
				]
			]
		},
		{
			"type": "line",
			"version": 46,
			"versionNonce": 708076907,
			"isDeleted": false,
			"id": "NaOvlRYqOAX-6N3LGl_QI",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -402.39996337890625,
			"y": 524.3624954223633,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 156.79998779296875,
			"height": 14.399993896484375,
			"seed": 514890027,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687813260283,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					156.79998779296875,
					-14.399993896484375
				]
			]
		},
		{
			"type": "line",
			"version": 67,
			"versionNonce": 230636229,
			"isDeleted": false,
			"id": "l2FBK-nFRSK_ZVuBHcosI",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -222.39996337890625,
			"y": 523.5624771118164,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.79998779296875,
			"height": 88.80001831054688,
			"seed": 1294665285,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687813260283,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					0.79998779296875,
					88.80001831054688
				]
			]
		},
		{
			"type": "ellipse",
			"version": 75,
			"versionNonce": 486178827,
			"isDeleted": false,
			"id": "CgIdoygm_MmAbfBaVUWrZ",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -247.20001220703125,
			"y": 609.9625015258789,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 54.4000244140625,
			"height": 53.600006103515625,
			"seed": 762450475,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687813260283,
			"link": null,
			"locked": false
		},
		{
			"type": "ellipse",
			"version": 78,
			"versionNonce": 636852773,
			"isDeleted": false,
			"id": "veBgbpPdnVsky10Fo6x7O",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -100,
			"y": 429.1624984741211,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 57.60003662109375,
			"height": 53.60002136230469,
			"seed": 1528562405,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687813260283,
			"link": null,
			"locked": false
		},
		{
			"type": "line",
			"version": 47,
			"versionNonce": 291784363,
			"isDeleted": false,
			"id": "HPWuB-BbWMsB0V3dEKtJN",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -192,
			"y": 372.36251068115234,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 97.60003662109375,
			"height": 64.80000305175781,
			"seed": 1039361925,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687813260283,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					97.60003662109375,
					64.80000305175781
				]
			]
		},
		{
			"type": "ellipse",
			"version": 59,
			"versionNonce": 1525222789,
			"isDeleted": false,
			"id": "ryHQGbDey8pT_bA80R6W8",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 38.4000244140625,
			"y": 386.7625045776367,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 53.5999755859375,
			"height": 48.00001525878906,
			"seed": 1968248491,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687813260283,
			"link": null,
			"locked": false
		},
		{
			"type": "line",
			"version": 55,
			"versionNonce": 1847343435,
			"isDeleted": false,
			"id": "7F7-4KQzTqJaTxe-Dg1j-",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -42.39996337890625,
			"y": 442.7625198364258,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 86.39996337890625,
			"height": 25.600021362304688,
			"seed": 1705853029,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687813260283,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					86.39996337890625,
					-25.600021362304688
				]
			]
		},
		{
			"type": "line",
			"version": 61,
			"versionNonce": 1003951333,
			"isDeleted": false,
			"id": "2HqW3gHR8DdEv_psdL_xt",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -194.39996337890625,
			"y": 629.9625015258789,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 249.5999755859375,
			"height": 196.8000030517578,
			"seed": 171827787,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687813260283,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					249.5999755859375,
					-196.8000030517578
				]
			]
		},
		{
			"type": "freedraw",
			"version": 47,
			"versionNonce": 1618794475,
			"isDeleted": false,
			"id": "liHSUK2CLbs7hP8qCSdze",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -471.1999816894531,
			"y": 364.36251068115234,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 18.399993896484375,
			"height": 15.199996948242188,
			"seed": 1386525413,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260283,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.79998779296875
				],
				[
					0,
					1.5999908447265625
				],
				[
					0,
					4
				],
				[
					0,
					5.5999908447265625
				],
				[
					0.79998779296875,
					8
				],
				[
					1.5999755859375,
					9.599990844726562
				],
				[
					2.399993896484375,
					9.599990844726562
				],
				[
					4,
					9.599990844726562
				],
				[
					7.199981689453125,
					10.399993896484375
				],
				[
					9.5999755859375,
					10.399993896484375
				],
				[
					12.79998779296875,
					10.399993896484375
				],
				[
					14.399993896484375,
					10.399993896484375
				],
				[
					16,
					10.399993896484375
				],
				[
					16.79998779296875,
					8.79998779296875
				],
				[
					18.399993896484375,
					6.399993896484375
				],
				[
					18.399993896484375,
					4.79998779296875
				],
				[
					18.399993896484375,
					2.399993896484375
				],
				[
					18.399993896484375,
					0.79998779296875
				],
				[
					16.79998779296875,
					-1.600006103515625
				],
				[
					16.79998779296875,
					-3.20001220703125
				],
				[
					15.199981689453125,
					-4
				],
				[
					13.5999755859375,
					-4.8000030517578125
				],
				[
					11.199981689453125,
					-4.8000030517578125
				],
				[
					9.5999755859375,
					-4.8000030517578125
				],
				[
					7.199981689453125,
					-4.8000030517578125
				],
				[
					6.399993896484375,
					-3.20001220703125
				],
				[
					5.5999755859375,
					-3.20001220703125
				],
				[
					5.5999755859375,
					-2.4000091552734375
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 25,
			"versionNonce": 340602949,
			"isDeleted": false,
			"id": "UZ6WJlUU19Rys-AFpW7iJ",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -235.20001220703125,
			"y": 355.56250762939453,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.60003662109375,
			"height": 21.599990844726562,
			"seed": 670025957,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260283,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.60003662109375,
					2.399993896484375
				],
				[
					3.20001220703125,
					6.399993896484375
				],
				[
					4,
					11.199996948242188
				],
				[
					4,
					17.599990844726562
				],
				[
					4.800048828125,
					20
				],
				[
					4.800048828125,
					20.800003051757812
				],
				[
					5.60003662109375,
					21.599990844726562
				],
				[
					5.60003662109375,
					21.599990844726562
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 34,
			"versionNonce": 110142091,
			"isDeleted": false,
			"id": "pIA7bPN_vqyjgZPCqgc_Y",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -78.39996337890625,
			"y": 445.16251373291016,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 12,
			"height": 14.399993896484375,
			"seed": 1503435205,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260283,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.79998779296875
				],
				[
					0,
					1.600006103515625
				],
				[
					0.79998779296875,
					6.399993896484375
				],
				[
					0.79998779296875,
					9.600006103515625
				],
				[
					0.79998779296875,
					11.199981689453125
				],
				[
					0.79998779296875,
					12
				],
				[
					0.79998779296875,
					12.79998779296875
				],
				[
					0.79998779296875,
					13.600006103515625
				],
				[
					2.39996337890625,
					13.600006103515625
				],
				[
					5.5999755859375,
					14.399993896484375
				],
				[
					8,
					14.399993896484375
				],
				[
					8.79998779296875,
					14.399993896484375
				],
				[
					9.5999755859375,
					14.399993896484375
				],
				[
					10.39996337890625,
					14.399993896484375
				],
				[
					11.199951171875,
					14.399993896484375
				],
				[
					12,
					14.399993896484375
				],
				[
					12,
					14.399993896484375
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 27,
			"versionNonce": 1646845861,
			"isDeleted": false,
			"id": "AnrlfLlv88-cEVwgjNRpb",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -80.79998779296875,
			"y": 443.56250762939453,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.79998779296875,
			"height": 1.5999755859375,
			"seed": 1258527915,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260283,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.79998779296875,
					0
				],
				[
					-2.4000244140625,
					-0.79998779296875
				],
				[
					-4.79998779296875,
					-0.79998779296875
				],
				[
					-5.5999755859375,
					-0.79998779296875
				],
				[
					-6.4000244140625,
					-0.79998779296875
				],
				[
					-7.20001220703125,
					-0.79998779296875
				],
				[
					-8,
					-0.79998779296875
				],
				[
					-8.79998779296875,
					0
				],
				[
					-8.79998779296875,
					0.79998779296875
				],
				[
					-8.79998779296875,
					0.79998779296875
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 46,
			"versionNonce": 1494358315,
			"isDeleted": false,
			"id": "SA1OLsjxO-LA0jriGtmPb",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 59.20001220703125,
			"y": 401.1624984741211,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 24,
			"height": 17.599990844726562,
			"seed": 1398726763,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260283,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.79998779296875
				],
				[
					0.79998779296875,
					-0.79998779296875
				],
				[
					5.5999755859375,
					-0.79998779296875
				],
				[
					11.20001220703125,
					-0.79998779296875
				],
				[
					14.4000244140625,
					-0.79998779296875
				],
				[
					17.5999755859375,
					-0.79998779296875
				],
				[
					20,
					0.8000030517578125
				],
				[
					20,
					1.600006103515625
				],
				[
					20,
					2.4000091552734375
				],
				[
					17.5999755859375,
					4
				],
				[
					15.20001220703125,
					4.8000030517578125
				],
				[
					12.79998779296875,
					4.8000030517578125
				],
				[
					12,
					4.8000030517578125
				],
				[
					12.79998779296875,
					4.8000030517578125
				],
				[
					15.20001220703125,
					4.8000030517578125
				],
				[
					18.4000244140625,
					7.20001220703125
				],
				[
					20,
					7.20001220703125
				],
				[
					22.4000244140625,
					8.800003051757812
				],
				[
					23.20001220703125,
					10.400009155273438
				],
				[
					24,
					12
				],
				[
					24,
					14.400009155273438
				],
				[
					24,
					15.20001220703125
				],
				[
					23.20001220703125,
					16.800003051757812
				],
				[
					20.79998779296875,
					16.800003051757812
				],
				[
					17.5999755859375,
					16.800003051757812
				],
				[
					12.79998779296875,
					16
				],
				[
					10.4000244140625,
					15.20001220703125
				],
				[
					9.5999755859375,
					13.600006103515625
				],
				[
					9.5999755859375,
					13.600006103515625
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 60,
			"versionNonce": 194487045,
			"isDeleted": false,
			"id": "5tICQQZEUDw3c4N4FHIsx",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -235.20001220703125,
			"y": 486.7625198364258,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 28,
			"height": 36,
			"seed": 2073156197,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260283,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.79998779296875
				],
				[
					0,
					2.399993896484375
				],
				[
					0,
					4.79998779296875
				],
				[
					0,
					8.79998779296875
				],
				[
					0,
					11.199981689453125
				],
				[
					0.800048828125,
					12.79998779296875
				],
				[
					0.800048828125,
					13.5999755859375
				],
				[
					0.800048828125,
					14.399993896484375
				],
				[
					1.60003662109375,
					14.399993896484375
				],
				[
					2.4000244140625,
					14.399993896484375
				],
				[
					3.20001220703125,
					14.399993896484375
				],
				[
					6.4000244140625,
					15.199981689453125
				],
				[
					9.60003662109375,
					15.199981689453125
				],
				[
					11.20001220703125,
					15.199981689453125
				],
				[
					13.60003662109375,
					15.199981689453125
				],
				[
					14.4000244140625,
					15.199981689453125
				],
				[
					15.20001220703125,
					15.199981689453125
				],
				[
					16.800048828125,
					15.199981689453125
				],
				[
					17.60003662109375,
					15.199981689453125
				],
				[
					18.4000244140625,
					15.199981689453125
				],
				[
					18.4000244140625,
					13.5999755859375
				],
				[
					19.20001220703125,
					12
				],
				[
					19.20001220703125,
					10.399993896484375
				],
				[
					19.20001220703125,
					9.5999755859375
				],
				[
					19.20001220703125,
					8.79998779296875
				],
				[
					20,
					8
				],
				[
					20,
					7.199981689453125
				],
				[
					20,
					6.399993896484375
				],
				[
					20,
					5.5999755859375
				],
				[
					20,
					4
				],
				[
					20,
					4.79998779296875
				],
				[
					21.60003662109375,
					9.5999755859375
				],
				[
					24,
					18.399993896484375
				],
				[
					24,
					23.199981689453125
				],
				[
					24,
					24.79998779296875
				],
				[
					24.800048828125,
					27.199981689453125
				],
				[
					25.60003662109375,
					29.5999755859375
				],
				[
					25.60003662109375,
					32
				],
				[
					26.4000244140625,
					33.5999755859375
				],
				[
					26.4000244140625,
					36
				],
				[
					27.20001220703125,
					36
				],
				[
					28,
					36
				],
				[
					28,
					36
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 38,
			"versionNonce": 1433123787,
			"isDeleted": false,
			"id": "oOOq6ocljAXavEQlrxzXN",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -214.39996337890625,
			"y": 634.7625198364258,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 14.4000244140625,
			"height": 16,
			"seed": 1837754411,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260283,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.800048828125,
					0
				],
				[
					-1.60003662109375,
					0
				],
				[
					-4,
					2.399993896484375
				],
				[
					-7.20001220703125,
					4.79998779296875
				],
				[
					-8.800048828125,
					8
				],
				[
					-8.800048828125,
					10.399993896484375
				],
				[
					-10.4000244140625,
					12.79998779296875
				],
				[
					-9.60003662109375,
					12.79998779296875
				],
				[
					-6.4000244140625,
					12.79998779296875
				],
				[
					-3.20001220703125,
					12.79998779296875
				],
				[
					-0.800048828125,
					12.79998779296875
				],
				[
					0.79998779296875,
					12.79998779296875
				],
				[
					2.39996337890625,
					13.5999755859375
				],
				[
					3.199951171875,
					15.199981689453125
				],
				[
					4,
					15.199981689453125
				],
				[
					4,
					16
				],
				[
					3.199951171875,
					16
				],
				[
					-0.800048828125,
					16
				],
				[
					-5.60003662109375,
					16
				],
				[
					-8.800048828125,
					15.199981689453125
				],
				[
					-8.800048828125,
					15.199981689453125
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 50,
			"versionNonce": 1427569253,
			"isDeleted": false,
			"id": "BkRpcryqKaUXCRxhpYguK",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -432.79998779296875,
			"y": 509.9625015258789,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 16,
			"height": 26.399993896484375,
			"seed": 228684069,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260283,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.800018310546875,
					0
				],
				[
					-1.600006103515625,
					0
				],
				[
					-2.399993896484375,
					0
				],
				[
					-4.800018310546875,
					1.600006103515625
				],
				[
					-6.399993896484375,
					6.399993896484375
				],
				[
					-6.399993896484375,
					10.399993896484375
				],
				[
					-7.20001220703125,
					13.600006103515625
				],
				[
					-7.20001220703125,
					16
				],
				[
					-7.20001220703125,
					16.800018310546875
				],
				[
					-7.20001220703125,
					18.399993896484375
				],
				[
					-7.20001220703125,
					20.800018310546875
				],
				[
					-7.20001220703125,
					22.399993896484375
				],
				[
					-6.399993896484375,
					22.399993896484375
				],
				[
					-5.600006103515625,
					23.20001220703125
				],
				[
					-3.20001220703125,
					24.800018310546875
				],
				[
					-0.800018310546875,
					26.399993896484375
				],
				[
					0.79998779296875,
					26.399993896484375
				],
				[
					3.199981689453125,
					26.399993896484375
				],
				[
					4.79998779296875,
					26.399993896484375
				],
				[
					4.79998779296875,
					24
				],
				[
					6.4000244140625,
					22.399993896484375
				],
				[
					8,
					20
				],
				[
					8.79998779296875,
					17.600006103515625
				],
				[
					8.79998779296875,
					16.800018310546875
				],
				[
					8.79998779296875,
					16
				],
				[
					8.79998779296875,
					15.20001220703125
				],
				[
					8.79998779296875,
					13.600006103515625
				],
				[
					7.20001220703125,
					12.800018310546875
				],
				[
					4,
					11.20001220703125
				],
				[
					0.79998779296875,
					11.20001220703125
				],
				[
					-0.800018310546875,
					10.399993896484375
				],
				[
					-1.600006103515625,
					10.399993896484375
				],
				[
					-1.600006103515625,
					10.399993896484375
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "ellipse",
			"version": 111,
			"versionNonce": 1740114539,
			"isDeleted": false,
			"id": "QQrivuzrFVEoBXX8MwFC4",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 36,
			"y": 375.56250762939453,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"width": 61.5999755859375,
			"height": 64,
			"seed": 1036561771,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687813260283,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 277,
			"versionNonce": 703715504,
			"isDeleted": false,
			"id": "0u77kAcc",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 50,
			"angle": 0,
			"x": -500.8000183105469,
			"y": 691.5625076293945,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 189.30795288085938,
			"height": 105,
			"seed": 587590411,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687923244927,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "cola [] +[1,6]\ncola[1,6]\nnodo=0,1",
			"rawText": "cola [] +[1,6]\ncola[1,6]\nnodo=0,1",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "cola [] +[1,6]\ncola[1,6]\nnodo=0,1",
			"lineHeight": 1.25,
			"baseline": 95
		},
		{
			"type": "text",
			"version": 207,
			"versionNonce": 348226827,
			"isDeleted": false,
			"id": "wE8vbzM2",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 275.5999755859375,
			"y": 319.56250762939453,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 225.73590087890625,
			"height": 280,
			"seed": 672052837,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260283,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "grafo[0]=[1,6]\ngrafo[1]=[0,2,4]\ngrafo[2]=[1,3]\ngrafo[3]=[2,5]\ngrafo[4]=[1,5,6]\ngrafo[5]=[3,4]\ngrafo[6]=[0,4]\nsearched=[0]",
			"rawText": "grafo[0]=[1,6]\ngrafo[1]=[0,2,4]\ngrafo[2]=[1,3]\ngrafo[3]=[2,5]\ngrafo[4]=[1,5,6]\ngrafo[5]=[3,4]\ngrafo[6]=[0,4]\nsearched=[0]",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "grafo[0]=[1,6]\ngrafo[1]=[0,2,4]\ngrafo[2]=[1,3]\ngrafo[3]=[2,5]\ngrafo[4]=[1,5,6]\ngrafo[5]=[3,4]\ngrafo[6]=[0,4]\nsearched=[0]",
			"lineHeight": 1.25,
			"baseline": 270
		},
		{
			"type": "freedraw",
			"version": 36,
			"versionNonce": 154749520,
			"isDeleted": false,
			"id": "4y6g8wlr01bki7PrfBOWD",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 10,
			"angle": 0,
			"x": -442.3999938964844,
			"y": 731.5625381469727,
			"strokeColor": "#f08c00",
			"backgroundColor": "transparent",
			"width": 8,
			"height": 19.199951171875,
			"seed": 1407070437,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687923244927,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.79998779296875
				],
				[
					-1.600006103515625,
					2.39996337890625
				],
				[
					-3.20001220703125,
					4.79998779296875
				],
				[
					-4,
					5.5999755859375
				],
				[
					-4,
					6.39996337890625
				],
				[
					-4.79998779296875,
					7.199951171875
				],
				[
					-5.600006103515625,
					8
				],
				[
					-6.399993896484375,
					9.5999755859375
				],
				[
					-6.399993896484375,
					10.39996337890625
				],
				[
					-6.399993896484375,
					11.199951171875
				],
				[
					-7.20001220703125,
					12
				],
				[
					-7.20001220703125,
					12.79998779296875
				],
				[
					-8,
					13.5999755859375
				],
				[
					-8,
					14.39996337890625
				],
				[
					-8,
					15.199951171875
				],
				[
					-8,
					16
				],
				[
					-8,
					16.79998779296875
				],
				[
					-8,
					17.5999755859375
				],
				[
					-8,
					18.39996337890625
				],
				[
					-7.20001220703125,
					19.199951171875
				],
				[
					-7.20001220703125,
					19.199951171875
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 29,
			"versionNonce": 965952176,
			"isDeleted": false,
			"id": "jPTbfCvQ2T8L7IJRHNmU_",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 10,
			"angle": 0,
			"x": -437.6000061035156,
			"y": 736.3625259399414,
			"strokeColor": "#f08c00",
			"backgroundColor": "transparent",
			"width": 13.5999755859375,
			"height": 12.79998779296875,
			"seed": 1998726347,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687923244927,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.79998779296875,
					0
				],
				[
					-1.5999755859375,
					0
				],
				[
					-2.399993896484375,
					0.79998779296875
				],
				[
					-4,
					1.5999755859375
				],
				[
					-7.199981689453125,
					4.79998779296875
				],
				[
					-8,
					6.39996337890625
				],
				[
					-8,
					7.20001220703125
				],
				[
					-8.79998779296875,
					7.20001220703125
				],
				[
					-8.79998779296875,
					8
				],
				[
					-8.79998779296875,
					8.79998779296875
				],
				[
					-11.199981689453125,
					10.39996337890625
				],
				[
					-12.79998779296875,
					12
				],
				[
					-13.5999755859375,
					12.79998779296875
				],
				[
					-13.5999755859375,
					12.79998779296875
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 54,
			"versionNonce": 1312522320,
			"isDeleted": false,
			"id": "Tv2FoIOTo6G4lMpBQlLIF",
			"fillStyle": "hachure",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": -422.4000244140625,
			"y": 734.7625503540039,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 19.199981689453125,
			"height": 21.60003662109375,
			"seed": 90728907,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687923244927,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.800018310546875,
					0
				],
				[
					0,
					0.79998779296875
				],
				[
					0,
					2.4000244140625
				],
				[
					-1.5999755859375,
					4
				],
				[
					-1.5999755859375,
					5.60003662109375
				],
				[
					-4,
					8
				],
				[
					-5.5999755859375,
					9.60003662109375
				],
				[
					-5.5999755859375,
					11.20001220703125
				],
				[
					-7.199981689453125,
					13.60003662109375
				],
				[
					-8,
					15.20001220703125
				],
				[
					-9.5999755859375,
					16.79998779296875
				],
				[
					-10.399993896484375,
					17.60003662109375
				],
				[
					-11.199981689453125,
					17.60003662109375
				],
				[
					-12,
					18.4000244140625
				],
				[
					-12,
					19.20001220703125
				],
				[
					-12.79998779296875,
					20
				],
				[
					-13.5999755859375,
					20.79998779296875
				],
				[
					-13.5999755859375,
					21.60003662109375
				],
				[
					-13.5999755859375,
					20.79998779296875
				],
				[
					-7.199981689453125,
					14.4000244140625
				],
				[
					-5.5999755859375,
					12.79998779296875
				],
				[
					-4,
					12
				],
				[
					-3.199981689453125,
					10.4000244140625
				],
				[
					-2.399993896484375,
					10.4000244140625
				],
				[
					-2.399993896484375,
					9.60003662109375
				],
				[
					-1.5999755859375,
					8.79998779296875
				],
				[
					-1.5999755859375,
					8
				],
				[
					-0.79998779296875,
					8
				],
				[
					0.800018310546875,
					6.4000244140625
				],
				[
					1.600006103515625,
					6.4000244140625
				],
				[
					3.20001220703125,
					4.79998779296875
				],
				[
					5.600006103515625,
					3.20001220703125
				],
				[
					5.600006103515625,
					2.4000244140625
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "text",
			"version": 345,
			"versionNonce": 1702325424,
			"isDeleted": false,
			"id": "Fo1zbQO7",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": -501.60003662109375,
			"y": 790.3624954223633,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 607.0118408203125,
			"height": 210,
			"seed": 866130181,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687923244927,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "Decolo 1 y encolamos los vecinos  del nodo 1\ngrafo[1]=>[0,2,4]\ncola[1,6,0,2,4]\nsearched[0,1]\nbusquedanodo=false,false\n",
			"rawText": "Decolo 1 y encolamos los vecinos  del nodo 1\ngrafo[1]=>[0,2,4]\ncola[1,6,0,2,4]\nsearched[0,1]\nbusquedanodo=false,false\n",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Decolo 1 y encolamos los vecinos  del nodo 1\ngrafo[1]=>[0,2,4]\ncola[1,6,0,2,4]\nsearched[0,1]\nbusquedanodo=false,false\n",
			"lineHeight": 1.25,
			"baseline": 200
		},
		{
			"type": "freedraw",
			"version": 103,
			"versionNonce": 1636234832,
			"isDeleted": false,
			"id": "Ski-V1vzgZfQ9eA_YjHZk",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": -425.5999755859375,
			"y": 865.9625625610352,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"width": 6.4000244140625,
			"height": 22.39996337890625,
			"seed": 1593395339,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687923244927,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.79998779296875
				],
				[
					-0.800048828125,
					1.5999755859375
				],
				[
					-0.800048828125,
					3.199951171875
				],
				[
					-1.60003662109375,
					3.199951171875
				],
				[
					-2.4000244140625,
					4.79998779296875
				],
				[
					-2.4000244140625,
					5.5999755859375
				],
				[
					-2.4000244140625,
					7.199951171875
				],
				[
					-3.20001220703125,
					8.79998779296875
				],
				[
					-4,
					10.39996337890625
				],
				[
					-4,
					11.199951171875
				],
				[
					-4,
					12.79998779296875
				],
				[
					-4,
					13.5999755859375
				],
				[
					-4.800048828125,
					14.39996337890625
				],
				[
					-4.800048828125,
					15.199951171875
				],
				[
					-4.800048828125,
					16
				],
				[
					-4.800048828125,
					16.79998779296875
				],
				[
					-4.800048828125,
					18.39996337890625
				],
				[
					-4.800048828125,
					19.199951171875
				],
				[
					-5.60003662109375,
					20.79998779296875
				],
				[
					-6.4000244140625,
					20.79998779296875
				],
				[
					-6.4000244140625,
					21.5999755859375
				],
				[
					-6.4000244140625,
					22.39996337890625
				],
				[
					-6.4000244140625,
					22.39996337890625
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 34,
			"versionNonce": 390485680,
			"isDeleted": false,
			"id": "sGrOuccnxd-gys2qyOzMQ",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": -417.5999755859375,
			"y": 732.3625259399414,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"width": 14.4000244140625,
			"height": 19.20001220703125,
			"seed": 624945701,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687923244927,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.79998779296875,
					0
				],
				[
					-3.20001220703125,
					0.79998779296875
				],
				[
					-3.20001220703125,
					3.20001220703125
				],
				[
					-5.60003662109375,
					4.79998779296875
				],
				[
					-7.20001220703125,
					6.39996337890625
				],
				[
					-8,
					7.20001220703125
				],
				[
					-8.79998779296875,
					7.20001220703125
				],
				[
					-8.79998779296875,
					8
				],
				[
					-9.60003662109375,
					8.79998779296875
				],
				[
					-11.20001220703125,
					10.39996337890625
				],
				[
					-11.20001220703125,
					12
				],
				[
					-12.000030517578125,
					12.79998779296875
				],
				[
					-12.800018310546875,
					13.5999755859375
				],
				[
					-12.800018310546875,
					14.39996337890625
				],
				[
					-12.800018310546875,
					15.20001220703125
				],
				[
					-12.800018310546875,
					16
				],
				[
					-13.600006103515625,
					16.79998779296875
				],
				[
					-14.4000244140625,
					17.5999755859375
				],
				[
					-14.4000244140625,
					18.39996337890625
				],
				[
					-14.4000244140625,
					19.20001220703125
				],
				[
					-14.4000244140625,
					19.20001220703125
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "arrow",
			"version": 43,
			"versionNonce": 670280784,
			"isDeleted": false,
			"id": "clBN4fTlWBzsGKtMu1ikQ",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": -307.20001220703125,
			"y": 908.1625137329102,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"width": 405.60003662109375,
			"height": 4.79998779296875,
			"seed": 264594795,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687923244927,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": {
				"elementId": "Ic90E0uj",
				"focus": -0.3437094448570887,
				"gap": 6.4000244140625
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					405.60003662109375,
					4.79998779296875
				]
			]
		},
		{
			"type": "text",
			"version": 91,
			"versionNonce": 1135083696,
			"isDeleted": false,
			"id": "Ic90E0uj",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 104.800048828125,
			"y": 891.7624893188477,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"width": 576.603759765625,
			"height": 35,
			"seed": 1661833413,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "clBN4fTlWBzsGKtMu1ikQ",
					"type": "arrow"
				}
			],
			"updated": 1687923244927,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "en este grafo se marca el nodo de inicio ",
			"rawText": "en este grafo se marca el nodo de inicio ",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "en este grafo se marca el nodo de inicio ",
			"lineHeight": 1.25,
			"baseline": 25
		},
		{
			"type": "text",
			"version": 261,
			"versionNonce": 727294544,
			"isDeleted": false,
			"id": "5MkXHzJK",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": -511.4000244140625,
			"y": 1009.5624771118164,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 607.767822265625,
			"height": 280,
			"seed": 1903538251,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687923244927,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "cola[6,02,4]\nnodo=0,1,6\ndecolo 6 y encolamos los vecinos del nodo 6\ngrafo[6]=> [0,4]\ncola[6,0,2,4,0,4]\nsearched[0,1,6]\nbusqueda nodo= false false false\n",
			"rawText": "cola[6,02,4]\nnodo=0,1,6\ndecolo 6 y encolamos los vecinos del nodo 6\ngrafo[6]=> [0,4]\ncola[6,0,2,4,0,4]\nsearched[0,1,6]\nbusqueda nodo= false false false\n",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "cola[6,02,4]\nnodo=0,1,6\ndecolo 6 y encolamos los vecinos del nodo 6\ngrafo[6]=> [0,4]\ncola[6,0,2,4,0,4]\nsearched[0,1,6]\nbusqueda nodo= false false false\n",
			"lineHeight": 1.25,
			"baseline": 270
		},
		{
			"type": "text",
			"version": 185,
			"versionNonce": 172255920,
			"isDeleted": false,
			"id": "QEMSQifQ",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": -508.20001220703125,
			"y": 1286.5624465942383,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 1043.671630859375,
			"height": 105,
			"seed": 341842699,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687923244927,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "cola[0,2,4]\nnodo=0,1,6\nno se ejecuta ya que esta la lista de searched se sigue al siguiente nodo",
			"rawText": "cola[0,2,4]\nnodo=0,1,6\nno se ejecuta ya que esta la lista de searched se sigue al siguiente nodo",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "cola[0,2,4]\nnodo=0,1,6\nno se ejecuta ya que esta la lista de searched se sigue al siguiente nodo",
			"lineHeight": 1.25,
			"baseline": 95
		},
		{
			"type": "freedraw",
			"version": 32,
			"versionNonce": 2056312912,
			"isDeleted": false,
			"id": "N-X5xis1cfpc3AI2twy9j",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": -430.4000244140625,
			"y": 1005.9624710083008,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"width": 6.4000244140625,
			"height": 28,
			"seed": 2070172395,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687923244927,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.800018310546875
				],
				[
					-0.79998779296875,
					1.600006103515625
				],
				[
					-1.5999755859375,
					4
				],
				[
					-2.4000244140625,
					5.600006103515625
				],
				[
					-3.20001220703125,
					7.20001220703125
				],
				[
					-3.20001220703125,
					8.800018310546875
				],
				[
					-4,
					11.20001220703125
				],
				[
					-4,
					14.399993896484375
				],
				[
					-4,
					17.600006103515625
				],
				[
					-4,
					19.20001220703125
				],
				[
					-4,
					21.600006103515625
				],
				[
					-4,
					22.399993896484375
				],
				[
					-4,
					23.20001220703125
				],
				[
					-4.79998779296875,
					24.800018310546875
				],
				[
					-5.5999755859375,
					26.399993896484375
				],
				[
					-5.5999755859375,
					27.20001220703125
				],
				[
					-5.5999755859375,
					28
				],
				[
					-6.4000244140625,
					28
				],
				[
					-6.4000244140625,
					28
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 31,
			"versionNonce": 1438880944,
			"isDeleted": false,
			"id": "7fvTA1aWRYLNmOlPjD8NH",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": -433.60003662109375,
			"y": 1151.5624771118164,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"width": 4,
			"height": 28,
			"seed": 124627563,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687923244927,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.79998779296875
				],
				[
					0,
					2.399993896484375
				],
				[
					-0.79998779296875,
					4
				],
				[
					-1.5999755859375,
					7.20001220703125
				],
				[
					-1.5999755859375,
					8
				],
				[
					-1.5999755859375,
					9.600006103515625
				],
				[
					-2.39996337890625,
					11.20001220703125
				],
				[
					-2.39996337890625,
					13.600006103515625
				],
				[
					-2.39996337890625,
					16
				],
				[
					-3.20001220703125,
					16.79998779296875
				],
				[
					-4,
					17.600006103515625
				],
				[
					-4,
					19.20001220703125
				],
				[
					-4,
					20.79998779296875
				],
				[
					-4,
					22.399993896484375
				],
				[
					-4,
					24.79998779296875
				],
				[
					-4,
					27.20001220703125
				],
				[
					-4,
					28
				],
				[
					-4,
					28
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "text",
			"version": 189,
			"versionNonce": 158420560,
			"isDeleted": false,
			"id": "3g4tXNGK",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": -512.2000732421875,
			"y": 1400.162483215332,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 554.4277954101562,
			"height": 210,
			"seed": 16465733,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687923244927,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "cola[2,4]\nnodo=0,1,6\ngrafo[2]=[1,3]\ncola[2,4,1,3]\nsearched[0,1,6,2]\nbusqueda nodo= false false false flase",
			"rawText": "cola[2,4]\nnodo=0,1,6\ngrafo[2]=[1,3]\ncola[2,4,1,3]\nsearched[0,1,6,2]\nbusqueda nodo= false false false flase",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "cola[2,4]\nnodo=0,1,6\ngrafo[2]=[1,3]\ncola[2,4,1,3]\nsearched[0,1,6,2]\nbusqueda nodo= false false false flase",
			"lineHeight": 1.25,
			"baseline": 200
		},
		{
			"type": "freedraw",
			"version": 35,
			"versionNonce": 2077064880,
			"isDeleted": false,
			"id": "L3jVi4NeBPwgAZZTZOaMF",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": -426.4000244140625,
			"y": 1279.7624893188477,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"width": 4.79998779296875,
			"height": 32.79998779296875,
			"seed": 1850172939,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687923244927,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.79998779296875
				],
				[
					0,
					4
				],
				[
					-0.79998779296875,
					5.5999755859375
				],
				[
					-1.5999755859375,
					8.79998779296875
				],
				[
					-1.5999755859375,
					12
				],
				[
					-1.5999755859375,
					14.399993896484375
				],
				[
					-1.5999755859375,
					16
				],
				[
					-1.5999755859375,
					16.79998779296875
				],
				[
					-2.4000244140625,
					18.399993896484375
				],
				[
					-2.4000244140625,
					19.199981689453125
				],
				[
					-2.4000244140625,
					22.399993896484375
				],
				[
					-2.4000244140625,
					23.199981689453125
				],
				[
					-3.20001220703125,
					24.79998779296875
				],
				[
					-4,
					26.399993896484375
				],
				[
					-4,
					28
				],
				[
					-4,
					28.79998779296875
				],
				[
					-4,
					29.5999755859375
				],
				[
					-4,
					30.399993896484375
				],
				[
					-4,
					31.199981689453125
				],
				[
					-4.79998779296875,
					32
				],
				[
					-4.79998779296875,
					32.79998779296875
				],
				[
					-4.79998779296875,
					32.79998779296875
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 21,
			"versionNonce": 282264656,
			"isDeleted": false,
			"id": "btxe3IVFbTIc_wVp43cHI",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": -433.60003662109375,
			"y": 1405.3624954223633,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"width": 3.20001220703125,
			"height": 15.20001220703125,
			"seed": 846094059,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687923244927,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.79998779296875
				],
				[
					0,
					2.39996337890625
				],
				[
					-0.79998779296875,
					4.79998779296875
				],
				[
					-1.5999755859375,
					8.79998779296875
				],
				[
					-2.39996337890625,
					12.79998779296875
				],
				[
					-2.39996337890625,
					14.39996337890625
				],
				[
					-3.20001220703125,
					15.20001220703125
				],
				[
					-3.20001220703125,
					15.20001220703125
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 19,
			"versionNonce": 1560946864,
			"isDeleted": false,
			"id": "9XqXs2cvsEW_HtJv2YooJ",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": -432.800048828125,
			"y": 1510.162483215332,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 16.79998779296875,
			"seed": 1004448779,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687923244927,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					4
				],
				[
					0,
					8
				],
				[
					0,
					11.20001220703125
				],
				[
					0,
					14.4000244140625
				],
				[
					0,
					16.79998779296875
				],
				[
					0,
					16.79998779296875
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "text",
			"version": 296,
			"versionNonce": 1760178213,
			"isDeleted": false,
			"id": "ll2NzF0O",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 912.6022542317704,
			"y": 341.39580758412643,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 652.5957641601562,
			"height": 210,
			"seed": 1976310117,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260284,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "cola[4,1,3]\nnodo=0,1,6,4\ngrafo[4]=[1,5,6]\ncola[4,1,3,1,5,6]\nsearched[0,1,6,2]\nbusqueda nodo= false false false false  false",
			"rawText": "cola[4,1,3]\nnodo=0,1,6,4\ngrafo[4]=[1,5,6]\ncola[4,1,3,1,5,6]\nsearched[0,1,6,2]\nbusqueda nodo= false false false false  false",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "cola[4,1,3]\nnodo=0,1,6,4\ngrafo[4]=[1,5,6]\ncola[4,1,3,1,5,6]\nsearched[0,1,6,2]\nbusqueda nodo= false false false false  false",
			"lineHeight": 1.25,
			"baseline": 200
		},
		{
			"type": "freedraw",
			"version": 23,
			"versionNonce": 371986603,
			"isDeleted": false,
			"id": "XkhVcpL1rDv66KuJtm5tH",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 997.9353027343749,
			"y": 343.72918160756393,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"width": 5.333251953125,
			"height": 34.66667175292969,
			"seed": 568959045,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260284,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.3332112630207575,
					0
				],
				[
					-2.6666259765625,
					5.333353678385379
				],
				[
					-3.9998372395832575,
					13.333333333333314
				],
				[
					-3.9998372395832575,
					17.333348592122377
				],
				[
					-3.9998372395832575,
					21.333338419596316
				],
				[
					-3.9998372395832575,
					25.33335367838538
				],
				[
					-3.9998372395832575,
					29.333343505859375
				],
				[
					-3.9998372395832575,
					30.66668192545569
				],
				[
					-3.9998372395832575,
					33.333333333333314
				],
				[
					-3.9998372395832575,
					34.66667175292969
				],
				[
					-5.333251953125,
					34.66667175292969
				],
				[
					-5.333251953125,
					34.66667175292969
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 18,
			"versionNonce": 1054532485,
			"isDeleted": false,
			"id": "aQLXck7nq-mDzekr2cSKk",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 997.9353027343749,
			"y": 447.72919686635294,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"width": 1.3332112630207575,
			"height": 26.666666666666686,
			"seed": 158502885,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260284,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.33331298828125
				],
				[
					0,
					5.333353678385436
				],
				[
					0,
					10.666656494140625
				],
				[
					-1.3332112630207575,
					16.00001017252606
				],
				[
					-1.3332112630207575,
					21.333312988281307
				],
				[
					-1.3332112630207575,
					26.666666666666686
				],
				[
					-1.3332112630207575,
					26.666666666666686
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "text",
			"version": 200,
			"versionNonce": 1532674891,
			"isDeleted": false,
			"id": "zeIm2tpC",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 916.2685343424477,
			"y": 571.3958330154412,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 866.4877319335938,
			"height": 210,
			"seed": 1623071243,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260284,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "cola[1,3]\nnodo=0,1,6,4\nse salta al siguiente de la cola ya que esta el 1 en searched\nbusqueda nodo= false false false false  false false\n\n",
			"rawText": "cola[1,3]\nnodo=0,1,6,4\nse salta al siguiente de la cola ya que esta el 1 en searched\nbusqueda nodo= false false false false  false false\n\n",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "cola[1,3]\nnodo=0,1,6,4\nse salta al siguiente de la cola ya que esta el 1 en searched\nbusqueda nodo= false false false false  false false\n\n",
			"lineHeight": 1.25,
			"baseline": 200
		},
		{
			"type": "text",
			"version": 137,
			"versionNonce": 790506213,
			"isDeleted": false,
			"id": "rQRJ8tEo",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 917.935302734375,
			"y": 734.0625607172644,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 809.8436889648438,
			"height": 140,
			"seed": 1040276235,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260284,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "cola[3]\nnodo=0,1,6,4\nes el nodo que se busca y se para el algoritmo\nbusqueda nodo= false false false false  false false true",
			"rawText": "cola[3]\nnodo=0,1,6,4\nes el nodo que se busca y se para el algoritmo\nbusqueda nodo= false false false false  false false true",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "cola[3]\nnodo=0,1,6,4\nes el nodo que se busca y se para el algoritmo\nbusqueda nodo= false false false false  false false true",
			"lineHeight": 1.25,
			"baseline": 130
		},
		{
			"type": "text",
			"version": 490,
			"versionNonce": 2035950059,
			"isDeleted": false,
			"id": "OfOJOzfZ",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 181.93534342447919,
			"y": 53.06252511342325,
			"strokeColor": "#0040ff",
			"backgroundColor": "transparent",
			"width": 480.1714172363281,
			"height": 88.48468272701943,
			"seed": 1206360037,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260284,
			"link": null,
			"locked": false,
			"fontSize": 70.78774618161555,
			"fontFamily": 1,
			"text": "Algoritmo BFS",
			"rawText": "Algoritmo BFS",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Algoritmo BFS",
			"lineHeight": 1.25,
			"baseline": 62
		},
		{
			"type": "ellipse",
			"version": 99,
			"versionNonce": 2051114565,
			"isDeleted": false,
			"id": "fBWsz9071ENN8hDASZMoU",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -445.53261820475245,
			"y": 2144.729161262512,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 60,
			"height": 52,
			"seed": 1442760997,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687813260284,
			"link": null,
			"locked": false
		},
		{
			"type": "line",
			"version": 90,
			"versionNonce": 1765059723,
			"isDeleted": false,
			"id": "SejHSpiZJ01bOKaaMmWdk",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -387.13259379068995,
			"y": 2161.52916431427,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 159.99996948242188,
			"height": 2.399993896484375,
			"seed": 804543621,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687813260284,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					159.99996948242188,
					-2.399993896484375
				]
			]
		},
		{
			"type": "ellipse",
			"version": 124,
			"versionNonce": 1931638181,
			"isDeleted": false,
			"id": "HeJwPFUuOyY2230fThC2Y",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -228.73259989420558,
			"y": 2133.52916431427,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 82.39996337890625,
			"height": 58.399993896484375,
			"seed": 278954981,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687813260284,
			"link": null,
			"locked": false
		},
		{
			"type": "line",
			"version": 76,
			"versionNonce": 514122539,
			"isDeleted": false,
			"id": "ehfB-bhU2l3P2MXq9BEy8",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -183.93261210123683,
			"y": 2191.9291734695435,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4,
			"height": 66.40000915527344,
			"seed": 202424133,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687813260284,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					4,
					66.40000915527344
				]
			]
		},
		{
			"type": "ellipse",
			"version": 127,
			"versionNonce": 888043781,
			"isDeleted": false,
			"id": "NJVdc1rWtJWm5CYnueJzU",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -208.73259989420558,
			"y": 2255.9291582107544,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 59.20001220703125,
			"height": 67.20001220703125,
			"seed": 1487048357,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687813260284,
			"link": null,
			"locked": false
		},
		{
			"type": "ellipse",
			"version": 163,
			"versionNonce": 840254923,
			"isDeleted": false,
			"id": "HvPACQjcft1b1BWftMiwv",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -423.9326121012368,
			"y": 2286.3291521072388,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 68.00006103515625,
			"height": 64,
			"seed": 84111877,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687813260284,
			"link": null,
			"locked": false
		},
		{
			"type": "line",
			"version": 103,
			"versionNonce": 421728357,
			"isDeleted": false,
			"id": "Mr7K7K2viq9zfr5huoZ_L",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -412.7325998942056,
			"y": 2194.329167366028,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 12.800018310546875,
			"height": 94.40000915527344,
			"seed": 1848699237,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687813260284,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					12.800018310546875,
					94.40000915527344
				]
			]
		},
		{
			"type": "line",
			"version": 90,
			"versionNonce": 1252021355,
			"isDeleted": false,
			"id": "fIDRS838XJGPtnpbgZidI",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -358.3325754801431,
			"y": 2319.9291582107544,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 156.79998779296875,
			"height": 14.399993896484375,
			"seed": 1970828485,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687813260285,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					156.79998779296875,
					-14.399993896484375
				]
			]
		},
		{
			"type": "line",
			"version": 111,
			"versionNonce": 1838005189,
			"isDeleted": false,
			"id": "nAqpifvE-xClpixLwybkC",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -178.33257548014308,
			"y": 2319.1291399002075,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.79998779296875,
			"height": 88.80001831054688,
			"seed": 1987548197,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687813260285,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					0.79998779296875,
					88.80001831054688
				]
			]
		},
		{
			"type": "ellipse",
			"version": 122,
			"versionNonce": 1209044747,
			"isDeleted": false,
			"id": "H8E4T2g2AEieYo-Ill25g",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -55.93261210123683,
			"y": 2224.729161262512,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 57.60003662109375,
			"height": 53.60002136230469,
			"seed": 2098972549,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687813260285,
			"link": null,
			"locked": false
		},
		{
			"type": "line",
			"version": 91,
			"versionNonce": 1783364389,
			"isDeleted": false,
			"id": "mx7qPnz6Pw02W11XPko4d",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -147.93261210123683,
			"y": 2167.9291734695435,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 97.60003662109375,
			"height": 64.80000305175781,
			"seed": 1000509157,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687813260285,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					97.60003662109375,
					64.80000305175781
				]
			]
		},
		{
			"type": "ellipse",
			"version": 103,
			"versionNonce": 752907691,
			"isDeleted": false,
			"id": "II0t_ySYm-yurkcbx5y46",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 82.46741231282567,
			"y": 2182.329167366028,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 53.5999755859375,
			"height": 48.00001525878906,
			"seed": 1083796037,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687813260285,
			"link": null,
			"locked": false
		},
		{
			"type": "line",
			"version": 99,
			"versionNonce": 1741377157,
			"isDeleted": false,
			"id": "TA0f1DeQP_ImwHqZSl1s3",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1.6674245198569224,
			"y": 2238.329182624817,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 86.39996337890625,
			"height": 25.600021362304688,
			"seed": 1826478501,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687813260285,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					86.39996337890625,
					-25.600021362304688
				]
			]
		},
		{
			"type": "line",
			"version": 105,
			"versionNonce": 1211795531,
			"isDeleted": false,
			"id": "PxfJWQkHQppSC6Z5vjdvt",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -150.33257548014308,
			"y": 2425.52916431427,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 249.5999755859375,
			"height": 196.8000030517578,
			"seed": 698178821,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687813260285,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					249.5999755859375,
					-196.8000030517578
				]
			]
		},
		{
			"type": "freedraw",
			"version": 91,
			"versionNonce": 1422472677,
			"isDeleted": false,
			"id": "0FVnzw15qVPKmVdHCFwpP",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -427.13259379068995,
			"y": 2159.9291734695435,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 18.399993896484375,
			"height": 15.199996948242188,
			"seed": 1582658661,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260285,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.79998779296875
				],
				[
					0,
					1.5999908447265625
				],
				[
					0,
					4
				],
				[
					0,
					5.5999908447265625
				],
				[
					0.79998779296875,
					8
				],
				[
					1.5999755859375,
					9.599990844726562
				],
				[
					2.399993896484375,
					9.599990844726562
				],
				[
					4,
					9.599990844726562
				],
				[
					7.199981689453125,
					10.399993896484375
				],
				[
					9.5999755859375,
					10.399993896484375
				],
				[
					12.79998779296875,
					10.399993896484375
				],
				[
					14.399993896484375,
					10.399993896484375
				],
				[
					16,
					10.399993896484375
				],
				[
					16.79998779296875,
					8.79998779296875
				],
				[
					18.399993896484375,
					6.399993896484375
				],
				[
					18.399993896484375,
					4.79998779296875
				],
				[
					18.399993896484375,
					2.399993896484375
				],
				[
					18.399993896484375,
					0.79998779296875
				],
				[
					16.79998779296875,
					-1.600006103515625
				],
				[
					16.79998779296875,
					-3.20001220703125
				],
				[
					15.199981689453125,
					-4
				],
				[
					13.5999755859375,
					-4.8000030517578125
				],
				[
					11.199981689453125,
					-4.8000030517578125
				],
				[
					9.5999755859375,
					-4.8000030517578125
				],
				[
					7.199981689453125,
					-4.8000030517578125
				],
				[
					6.399993896484375,
					-3.20001220703125
				],
				[
					5.5999755859375,
					-3.20001220703125
				],
				[
					5.5999755859375,
					-2.4000091552734375
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 69,
			"versionNonce": 536430315,
			"isDeleted": false,
			"id": "_y_O2IxuJj5eb4wgEYGc1",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -191.13262430826808,
			"y": 2151.1291704177856,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.60003662109375,
			"height": 21.599990844726562,
			"seed": 651403205,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260285,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.60003662109375,
					2.399993896484375
				],
				[
					3.20001220703125,
					6.399993896484375
				],
				[
					4,
					11.199996948242188
				],
				[
					4,
					17.599990844726562
				],
				[
					4.800048828125,
					20
				],
				[
					4.800048828125,
					20.800003051757812
				],
				[
					5.60003662109375,
					21.599990844726562
				],
				[
					5.60003662109375,
					21.599990844726562
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 78,
			"versionNonce": 1817391429,
			"isDeleted": false,
			"id": "bZWk9Ym4OrKPOAcLB5LB9",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -34.33257548014308,
			"y": 2240.7291765213013,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 12,
			"height": 14.399993896484375,
			"seed": 1228234533,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260285,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.79998779296875
				],
				[
					0,
					1.600006103515625
				],
				[
					0.79998779296875,
					6.399993896484375
				],
				[
					0.79998779296875,
					9.600006103515625
				],
				[
					0.79998779296875,
					11.199981689453125
				],
				[
					0.79998779296875,
					12
				],
				[
					0.79998779296875,
					12.79998779296875
				],
				[
					0.79998779296875,
					13.600006103515625
				],
				[
					2.39996337890625,
					13.600006103515625
				],
				[
					5.5999755859375,
					14.399993896484375
				],
				[
					8,
					14.399993896484375
				],
				[
					8.79998779296875,
					14.399993896484375
				],
				[
					9.5999755859375,
					14.399993896484375
				],
				[
					10.39996337890625,
					14.399993896484375
				],
				[
					11.199951171875,
					14.399993896484375
				],
				[
					12,
					14.399993896484375
				],
				[
					12,
					14.399993896484375
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 71,
			"versionNonce": 447164811,
			"isDeleted": false,
			"id": "G_IkiD7IJBvvYIFKvyLj_",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -36.73259989420558,
			"y": 2239.1291704177856,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.79998779296875,
			"height": 1.5999755859375,
			"seed": 1810379397,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260285,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.79998779296875,
					0
				],
				[
					-2.4000244140625,
					-0.79998779296875
				],
				[
					-4.79998779296875,
					-0.79998779296875
				],
				[
					-5.5999755859375,
					-0.79998779296875
				],
				[
					-6.4000244140625,
					-0.79998779296875
				],
				[
					-7.20001220703125,
					-0.79998779296875
				],
				[
					-8,
					-0.79998779296875
				],
				[
					-8.79998779296875,
					0
				],
				[
					-8.79998779296875,
					0.79998779296875
				],
				[
					-8.79998779296875,
					0.79998779296875
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 90,
			"versionNonce": 734445733,
			"isDeleted": false,
			"id": "ZachxTG80mvssvGXJ_S4X",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 103.26740010579442,
			"y": 2196.729161262512,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 24,
			"height": 17.599990844726562,
			"seed": 195664357,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260285,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.79998779296875
				],
				[
					0.79998779296875,
					-0.79998779296875
				],
				[
					5.5999755859375,
					-0.79998779296875
				],
				[
					11.20001220703125,
					-0.79998779296875
				],
				[
					14.4000244140625,
					-0.79998779296875
				],
				[
					17.5999755859375,
					-0.79998779296875
				],
				[
					20,
					0.8000030517578125
				],
				[
					20,
					1.600006103515625
				],
				[
					20,
					2.4000091552734375
				],
				[
					17.5999755859375,
					4
				],
				[
					15.20001220703125,
					4.8000030517578125
				],
				[
					12.79998779296875,
					4.8000030517578125
				],
				[
					12,
					4.8000030517578125
				],
				[
					12.79998779296875,
					4.8000030517578125
				],
				[
					15.20001220703125,
					4.8000030517578125
				],
				[
					18.4000244140625,
					7.20001220703125
				],
				[
					20,
					7.20001220703125
				],
				[
					22.4000244140625,
					8.800003051757812
				],
				[
					23.20001220703125,
					10.400009155273438
				],
				[
					24,
					12
				],
				[
					24,
					14.400009155273438
				],
				[
					24,
					15.20001220703125
				],
				[
					23.20001220703125,
					16.800003051757812
				],
				[
					20.79998779296875,
					16.800003051757812
				],
				[
					17.5999755859375,
					16.800003051757812
				],
				[
					12.79998779296875,
					16
				],
				[
					10.4000244140625,
					15.20001220703125
				],
				[
					9.5999755859375,
					13.600006103515625
				],
				[
					9.5999755859375,
					13.600006103515625
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 104,
			"versionNonce": 1769916459,
			"isDeleted": false,
			"id": "OdYvLIfFozGkD5BvRFmaU",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -191.13262430826808,
			"y": 2282.329182624817,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 28,
			"height": 36,
			"seed": 830936389,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260285,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.79998779296875
				],
				[
					0,
					2.399993896484375
				],
				[
					0,
					4.79998779296875
				],
				[
					0,
					8.79998779296875
				],
				[
					0,
					11.199981689453125
				],
				[
					0.800048828125,
					12.79998779296875
				],
				[
					0.800048828125,
					13.5999755859375
				],
				[
					0.800048828125,
					14.399993896484375
				],
				[
					1.60003662109375,
					14.399993896484375
				],
				[
					2.4000244140625,
					14.399993896484375
				],
				[
					3.20001220703125,
					14.399993896484375
				],
				[
					6.4000244140625,
					15.199981689453125
				],
				[
					9.60003662109375,
					15.199981689453125
				],
				[
					11.20001220703125,
					15.199981689453125
				],
				[
					13.60003662109375,
					15.199981689453125
				],
				[
					14.4000244140625,
					15.199981689453125
				],
				[
					15.20001220703125,
					15.199981689453125
				],
				[
					16.800048828125,
					15.199981689453125
				],
				[
					17.60003662109375,
					15.199981689453125
				],
				[
					18.4000244140625,
					15.199981689453125
				],
				[
					18.4000244140625,
					13.5999755859375
				],
				[
					19.20001220703125,
					12
				],
				[
					19.20001220703125,
					10.399993896484375
				],
				[
					19.20001220703125,
					9.5999755859375
				],
				[
					19.20001220703125,
					8.79998779296875
				],
				[
					20,
					8
				],
				[
					20,
					7.199981689453125
				],
				[
					20,
					6.399993896484375
				],
				[
					20,
					5.5999755859375
				],
				[
					20,
					4
				],
				[
					20,
					4.79998779296875
				],
				[
					21.60003662109375,
					9.5999755859375
				],
				[
					24,
					18.399993896484375
				],
				[
					24,
					23.199981689453125
				],
				[
					24,
					24.79998779296875
				],
				[
					24.800048828125,
					27.199981689453125
				],
				[
					25.60003662109375,
					29.5999755859375
				],
				[
					25.60003662109375,
					32
				],
				[
					26.4000244140625,
					33.5999755859375
				],
				[
					26.4000244140625,
					36
				],
				[
					27.20001220703125,
					36
				],
				[
					28,
					36
				],
				[
					28,
					36
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 94,
			"versionNonce": 147940357,
			"isDeleted": false,
			"id": "5HAJKbz1nmOaBzyLil55a",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -388.7325998942056,
			"y": 2305.52916431427,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 16,
			"height": 26.399993896484375,
			"seed": 1968982021,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260285,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.800018310546875,
					0
				],
				[
					-1.600006103515625,
					0
				],
				[
					-2.399993896484375,
					0
				],
				[
					-4.800018310546875,
					1.600006103515625
				],
				[
					-6.399993896484375,
					6.399993896484375
				],
				[
					-6.399993896484375,
					10.399993896484375
				],
				[
					-7.20001220703125,
					13.600006103515625
				],
				[
					-7.20001220703125,
					16
				],
				[
					-7.20001220703125,
					16.800018310546875
				],
				[
					-7.20001220703125,
					18.399993896484375
				],
				[
					-7.20001220703125,
					20.800018310546875
				],
				[
					-7.20001220703125,
					22.399993896484375
				],
				[
					-6.399993896484375,
					22.399993896484375
				],
				[
					-5.600006103515625,
					23.20001220703125
				],
				[
					-3.20001220703125,
					24.800018310546875
				],
				[
					-0.800018310546875,
					26.399993896484375
				],
				[
					0.79998779296875,
					26.399993896484375
				],
				[
					3.199981689453125,
					26.399993896484375
				],
				[
					4.79998779296875,
					26.399993896484375
				],
				[
					4.79998779296875,
					24
				],
				[
					6.4000244140625,
					22.399993896484375
				],
				[
					8,
					20
				],
				[
					8.79998779296875,
					17.600006103515625
				],
				[
					8.79998779296875,
					16.800018310546875
				],
				[
					8.79998779296875,
					16
				],
				[
					8.79998779296875,
					15.20001220703125
				],
				[
					8.79998779296875,
					13.600006103515625
				],
				[
					7.20001220703125,
					12.800018310546875
				],
				[
					4,
					11.20001220703125
				],
				[
					0.79998779296875,
					11.20001220703125
				],
				[
					-0.800018310546875,
					10.399993896484375
				],
				[
					-1.600006103515625,
					10.399993896484375
				],
				[
					-1.600006103515625,
					10.399993896484375
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "ellipse",
			"version": 155,
			"versionNonce": 845843147,
			"isDeleted": false,
			"id": "Mm-NiUO6aj1NWVIz2L2QO",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 80.06738789876317,
			"y": 2171.1291704177856,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"width": 61.5999755859375,
			"height": 64,
			"seed": 1224671077,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687813260285,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 260,
			"versionNonce": 1735433061,
			"isDeleted": false,
			"id": "s4Gc4Hf5",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 319.6673634847007,
			"y": 2115.1291704177856,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 225.73590087890625,
			"height": 280,
			"seed": 974375621,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260285,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "grafo[0]=[1,6]\ngrafo[1]=[0,2,4]\ngrafo[2]=[1,3]\ngrafo[3]=[2,5]\ngrafo[4]=[1,5,6]\ngrafo[5]=[3,4]\ngrafo[6]=[0,4]\ngrafp[7]=[]",
			"rawText": "grafo[0]=[1,6]\ngrafo[1]=[0,2,4]\ngrafo[2]=[1,3]\ngrafo[3]=[2,5]\ngrafo[4]=[1,5,6]\ngrafo[5]=[3,4]\ngrafo[6]=[0,4]\ngrafp[7]=[]",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "grafo[0]=[1,6]\ngrafo[1]=[0,2,4]\ngrafo[2]=[1,3]\ngrafo[3]=[2,5]\ngrafo[4]=[1,5,6]\ngrafo[5]=[3,4]\ngrafo[6]=[0,4]\ngrafp[7]=[]",
			"lineHeight": 1.25,
			"baseline": 270
		},
		{
			"type": "ellipse",
			"version": 98,
			"versionNonce": 2047146347,
			"isDeleted": false,
			"id": "6cmSgU0xBCI35q6_R5s3I",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": -200.73133341471336,
			"y": 2415.3958737055464,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 60,
			"height": 78,
			"seed": 1968354987,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"type": "text",
					"id": "vDIFQ8FF"
				}
			],
			"updated": 1687813260285,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 10,
			"versionNonce": 1341253317,
			"isDeleted": false,
			"id": "vDIFQ8FF",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": -182.06852977023166,
			"y": 2431.818709239271,
			"strokeColor": "#be4bdb",
			"backgroundColor": "transparent",
			"width": 22.24798583984375,
			"height": 45,
			"seed": 1412816197,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260285,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "5",
			"rawText": "5",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "6cmSgU0xBCI35q6_R5s3I",
			"originalText": "5",
			"lineHeight": 1.25,
			"baseline": 32
		},
		{
			"type": "text",
			"version": 117,
			"versionNonce": 1301845003,
			"isDeleted": false,
			"id": "84jpJmk9",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 99.26866658528644,
			"y": 1857.7291460037227,
			"strokeColor": "#be4bdb",
			"backgroundColor": "transparent",
			"width": 520.7742309570312,
			"height": 95.2169678290235,
			"seed": 1758786955,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260285,
			"link": null,
			"locked": false,
			"fontSize": 76.1735742632188,
			"fontFamily": 1,
			"text": "Algoritmo DFS",
			"rawText": "Algoritmo DFS",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Algoritmo DFS",
			"lineHeight": 1.25,
			"baseline": 67
		},
		{
			"type": "text",
			"version": 192,
			"versionNonce": 1693632037,
			"isDeleted": false,
			"id": "LEtY2HOt",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": -426.39793904622377,
			"y": 2584.729268074035,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 375.39581298828125,
			"height": 140,
			"seed": 915693899,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260285,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "searched=[f,f,f,f,f,f,f]\ncomponenteR=[0,1,2,3,5,4,6 \nparent=[0,0,0,0,0,0,0]\n",
			"rawText": "searched=[f,f,f,f,f,f,f]\ncomponenteR=[0,1,2,3,5,4,6 \nparent=[0,0,0,0,0,0,0]\n",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "searched=[f,f,f,f,f,f,f]\ncomponenteR=[0,1,2,3,5,4,6 \nparent=[0,0,0,0,0,0,0]\n",
			"lineHeight": 1.25,
			"baseline": 130
		},
		{
			"type": "rectangle",
			"version": 225,
			"versionNonce": 757062315,
			"isDeleted": false,
			"id": "ebge7tOkFgqgjox1GMMqr",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 478.9354858398435,
			"y": 3220.729308764139,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 394,
			"height": 66,
			"seed": 1153245131,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "rLINJP7c"
				}
			],
			"updated": 1687813260285,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 154,
			"versionNonce": 425769349,
			"isDeleted": false,
			"id": "rLINJP7c",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 631.8355026245115,
			"y": 3236.229308764139,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 88.19996643066406,
			"height": 35,
			"seed": 455575723,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260285,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "DFS 0",
			"rawText": "DFS 0",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "ebge7tOkFgqgjox1GMMqr",
			"originalText": "DFS 0",
			"lineHeight": 1.25,
			"baseline": 25
		},
		{
			"type": "rectangle",
			"version": 211,
			"versionNonce": 645480677,
			"isDeleted": false,
			"id": "XerMy2Inlgjngwpw7qN6r",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 489.4355468749998,
			"y": 3138.229247728983,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 385,
			"height": 79,
			"seed": 1788988523,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "3L0xt8J5"
				}
			],
			"updated": 1687813260285,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 167,
			"versionNonce": 157510635,
			"isDeleted": false,
			"id": "3L0xt8J5",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 643.6735610961912,
			"y": 3160.229247728983,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 76.52397155761719,
			"height": 35,
			"seed": 647239179,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260285,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "DFS 1",
			"rawText": "DFS 1",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "XerMy2Inlgjngwpw7qN6r",
			"originalText": "DFS 1",
			"lineHeight": 1.25,
			"baseline": 25
		},
		{
			"type": "line",
			"version": 127,
			"versionNonce": 2105849483,
			"isDeleted": false,
			"id": "oUJa2liGlIcObP3V81adT",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 871.2688395182289,
			"y": 3247.729298591613,
			"strokeColor": "#e8590c",
			"backgroundColor": "transparent",
			"width": 114.666748046875,
			"height": 38.66668701171875,
			"seed": 293268715,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687813260285,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					114.666748046875,
					-38.66668701171875
				]
			]
		},
		{
			"type": "line",
			"version": 139,
			"versionNonce": 321915813,
			"isDeleted": false,
			"id": "cU5joCzZfHwFMlKq_sl7j",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 877.9355061848956,
			"y": 3259.729217211405,
			"strokeColor": "#e8590c",
			"backgroundColor": "transparent",
			"width": 109.33329264322924,
			"height": 40,
			"seed": 388035461,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687813260285,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					109.33329264322924,
					40
				]
			]
		},
		{
			"type": "line",
			"version": 214,
			"versionNonce": 6532395,
			"isDeleted": false,
			"id": "3nhSijDfRMh2U2KadCN39",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 854.9881452593884,
			"y": 3147.518732656512,
			"strokeColor": "#e8590c",
			"backgroundColor": "transparent",
			"width": 156.2106002004523,
			"height": 78.66663347210806,
			"seed": 444560389,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687813260285,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					156.2106002004523,
					-78.66663347210806
				]
			]
		},
		{
			"type": "line",
			"version": 187,
			"versionNonce": 1792626437,
			"isDeleted": false,
			"id": "53QsxOXrIpbt3h3_QC7Pq",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 875.2687784830727,
			"y": 3153.904642958389,
			"strokeColor": "#e8590c",
			"backgroundColor": "transparent",
			"width": 144.42111902069644,
			"height": 48.07002017372497,
			"seed": 1083912107,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687813260286,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					144.42111902069644,
					-48.07002017372497
				]
			]
		},
		{
			"type": "line",
			"version": 160,
			"versionNonce": 1164627915,
			"isDeleted": false,
			"id": "nwl-4hc-E5KR1W4igwjoR",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 876.6021931966144,
			"y": 3183.729257901509,
			"strokeColor": "#e8590c",
			"backgroundColor": "transparent",
			"width": 144.7720122755619,
			"height": 26.31580018160639,
			"seed": 1862190923,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687813260286,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					144.7720122755619,
					-26.31580018160639
				]
			]
		},
		{
			"type": "text",
			"version": 201,
			"versionNonce": 783588971,
			"isDeleted": false,
			"id": "V8RquOMS",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 1006.7776317931056,
			"y": 3038.764256745053,
			"strokeColor": "#e8590c",
			"backgroundColor": "transparent",
			"width": 19.263992309570312,
			"height": 35,
			"seed": 1017679563,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260286,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "0",
			"rawText": "0",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "0",
			"lineHeight": 1.25,
			"baseline": 25
		},
		{
			"type": "text",
			"version": 168,
			"versionNonce": 993726917,
			"isDeleted": false,
			"id": "EN17f34Y",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 1037.6547123423793,
			"y": 3076.2555404964237,
			"strokeColor": "#e8590c",
			"backgroundColor": "transparent",
			"width": 19.935989379882812,
			"height": 35,
			"seed": 455448587,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260286,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "2",
			"rawText": "2",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "2",
			"lineHeight": 1.25,
			"baseline": 25
		},
		{
			"type": "text",
			"version": 142,
			"versionNonce": 1997248779,
			"isDeleted": false,
			"id": "18HdErf2",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 1035.5846140008225,
			"y": 3138.939802420766,
			"strokeColor": "#e8590c",
			"backgroundColor": "transparent",
			"width": 17.919998168945312,
			"height": 35,
			"seed": 2120307019,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260286,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "4",
			"rawText": "4",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "4",
			"lineHeight": 1.25,
			"baseline": 25
		},
		{
			"type": "text",
			"version": 117,
			"versionNonce": 468336555,
			"isDeleted": false,
			"id": "PVz8u8UC",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 1040.602132161458,
			"y": 3200.06257088979,
			"strokeColor": "#e8590c",
			"backgroundColor": "transparent",
			"width": 7.5879974365234375,
			"height": 35,
			"seed": 903570021,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260286,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "1",
			"rawText": "1",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "1",
			"lineHeight": 1.25,
			"baseline": 25
		},
		{
			"type": "text",
			"version": 117,
			"versionNonce": 513483909,
			"isDeleted": false,
			"id": "V6SYFOZ9",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 1025.602132161458,
			"y": 3310.06257088979,
			"strokeColor": "#e8590c",
			"backgroundColor": "transparent",
			"width": 17.919998168945312,
			"height": 35,
			"seed": 781700389,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260286,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "6",
			"rawText": "6",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "6",
			"lineHeight": 1.25,
			"baseline": 25
		},
		{
			"type": "freedraw",
			"version": 197,
			"versionNonce": 125506123,
			"isDeleted": false,
			"id": "7dfSMoVG9KsezunfFrko7",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 985.8652365165841,
			"y": 3031.518602019861,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"width": 33.33333333333326,
			"height": 33.333333333333485,
			"seed": 382525573,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260286,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.33331298828125,
					0
				],
				[
					4.0000406901042425,
					0
				],
				[
					6.6666666666667425,
					1.333414713541515
				],
				[
					10.666707356770758,
					4.000040690104015
				],
				[
					13.333333333333258,
					6.666666666666515
				],
				[
					14.666646321614508,
					8.000081380208485
				],
				[
					17.3333740234375,
					13.333333333333485
				],
				[
					20,
					14.666748046875
				],
				[
					22.666727701822992,
					16.00006103515625
				],
				[
					25.333353678385492,
					20
				],
				[
					26.666666666666742,
					22.666727701822765
				],
				[
					26.666666666666742,
					24.000040690104015
				],
				[
					29.333394368489508,
					26.666666666666515
				],
				[
					30.666707356770758,
					29.333394368489735
				],
				[
					30.666707356770758,
					32.000020345052235
				],
				[
					32.00002034505201,
					33.333333333333485
				],
				[
					33.33333333333326,
					33.333333333333485
				],
				[
					33.33333333333326,
					33.333333333333485
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "rectangle",
			"version": 247,
			"versionNonce": 254692325,
			"isDeleted": false,
			"id": "8emhLlACgbZs4-TpxZGHc",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 485.7688191731768,
			"y": 3028.895944913227,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 387,
			"height": 107,
			"seed": 56421957,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "meRmkJ7U"
				}
			],
			"updated": 1687813260286,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 121,
			"versionNonce": 2056818923,
			"isDeleted": false,
			"id": "meRmkJ7U",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 634.8328374226885,
			"y": 3064.895944913227,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 88.87196350097656,
			"height": 35,
			"seed": 592357253,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260286,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "DFS 2",
			"rawText": "DFS 2",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "8emhLlACgbZs4-TpxZGHc",
			"originalText": "DFS 2",
			"lineHeight": 1.25,
			"baseline": 25
		},
		{
			"type": "line",
			"version": 173,
			"versionNonce": 1415468709,
			"isDeleted": false,
			"id": "nj-QjhkPdj01AB2vVA0lf",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 864.3891653773973,
			"y": 3035.7259118299394,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 312.213027819217,
			"height": 106.66335111267517,
			"seed": 794836229,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687813260286,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					312.213027819217,
					-106.66335111267517
				]
			]
		},
		{
			"type": "line",
			"version": 172,
			"versionNonce": 637942277,
			"isDeleted": false,
			"id": "ND1gsV6Bcrzzqn6TbOK1Q",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 877.9354044596352,
			"y": 3047.729298591613,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 349.3333943684894,
			"height": 72.00002034505178,
			"seed": 962902219,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687813260286,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					349.3333943684894,
					-72.00002034505178
				]
			]
		},
		{
			"type": "text",
			"version": 116,
			"versionNonce": 1343624395,
			"isDeleted": false,
			"id": "hZcd5Qyt",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 1207.2687988281245,
			"y": 2905.06257088979,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 7.5879974365234375,
			"height": 35,
			"seed": 2100284619,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260286,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "1",
			"rawText": "1",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "1",
			"lineHeight": 1.25,
			"baseline": 25
		},
		{
			"type": "text",
			"version": 116,
			"versionNonce": 766460779,
			"isDeleted": false,
			"id": "o3Cc2BYB",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 1255.602132161458,
			"y": 2971.7292375564566,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 19.0679931640625,
			"height": 35,
			"seed": 2052689739,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260286,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "3",
			"rawText": "3",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "3",
			"lineHeight": 1.25,
			"baseline": 25
		},
		{
			"type": "text",
			"version": 85,
			"versionNonce": 979975365,
			"isDeleted": false,
			"id": "sCTOut3X",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": -423.39795939127595,
			"y": 2715.7292273839307,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 312.45184326171875,
			"height": 70,
			"seed": 887070827,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260286,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "parent=[0,0,0,2,0,0,0]\n",
			"rawText": "parent=[0,0,0,2,0,0,0]\n",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "parent=[0,0,0,2,0,0,0]\n",
			"lineHeight": 1.25,
			"baseline": 60
		},
		{
			"type": "freedraw",
			"version": 17,
			"versionNonce": 1913609253,
			"isDeleted": false,
			"id": "AzZ3GVla1hSpwsyx1iq1K",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": -214.06466674804676,
			"y": 2659.7291663487745,
			"strokeColor": "#c2255c",
			"backgroundColor": "transparent",
			"width": 5.333302815755189,
			"height": 24.000040690104015,
			"seed": 178295499,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260286,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.333414713541515
				],
				[
					0,
					4.000040690104015
				],
				[
					0,
					8.000081380208485
				],
				[
					0,
					10.666707356770985
				],
				[
					0,
					14.666748046875
				],
				[
					-1.33331298828125,
					17.3333740234375
				],
				[
					-1.33331298828125,
					18.66668701171875
				],
				[
					-2.6666259765625,
					20
				],
				[
					-2.6666259765625,
					21.333414713541515
				],
				[
					-3.9999898274739394,
					21.333414713541515
				],
				[
					-3.9999898274739394,
					22.666727701822765
				],
				[
					-5.333302815755189,
					24.000040690104015
				],
				[
					-5.333302815755189,
					24.000040690104015
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "text",
			"version": 91,
			"versionNonce": 1115328389,
			"isDeleted": false,
			"id": "dz8Z3TJ0",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": -420.7313588460285,
			"y": 2750.06252002716,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 300.77581787109375,
			"height": 70,
			"seed": 1127927461,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260286,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "parent=[0,0,1,2,0,0,0]\n",
			"rawText": "parent=[0,0,1,2,0,0,0]\n",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "parent=[0,0,1,2,0,0,0]\n",
			"lineHeight": 1.25,
			"baseline": 60
		},
		{
			"type": "freedraw",
			"version": 14,
			"versionNonce": 601610059,
			"isDeleted": false,
			"id": "Lvnjbqz_Iiz4gYwEbnWJ1",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": -240.73133341471345,
			"y": 2725.0625200271597,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 18.66668701171875,
			"seed": 364511301,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260286,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.33331298828125
				],
				[
					0,
					5.33335367838572
				],
				[
					0,
					9.333394368489735
				],
				[
					0,
					12.000020345052235
				],
				[
					0,
					13.333333333333485
				],
				[
					0,
					14.666646321614735
				],
				[
					0,
					16.00006103515625
				],
				[
					0,
					17.3333740234375
				],
				[
					0,
					18.66668701171875
				],
				[
					0,
					18.66668701171875
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "rectangle",
			"version": 167,
			"versionNonce": 949532139,
			"isDeleted": false,
			"id": "QwpzcSVu8APv3znBidieZ",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 482.93551635742176,
			"y": 2943.56257088979,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 382,
			"height": 83,
			"seed": 1540333003,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "otd49krY"
				}
			],
			"updated": 1687813260287,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 119,
			"versionNonce": 1122382405,
			"isDeleted": false,
			"id": "otd49krY",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 629.9335327148436,
			"y": 2967.56257088979,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 88.00396728515625,
			"height": 35,
			"seed": 846265515,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260287,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "DFS 3",
			"rawText": "DFS 3",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "QwpzcSVu8APv3znBidieZ",
			"originalText": "DFS 3",
			"lineHeight": 1.25,
			"baseline": 25
		},
		{
			"type": "line",
			"version": 96,
			"versionNonce": 1803600011,
			"isDeleted": false,
			"id": "MKdwkYy-whvpIKKjSfMxi",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 872.6020507812501,
			"y": 2905.062494595845,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 125.33335367838527,
			"height": 41.33331298828125,
			"seed": 1796460331,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687813260287,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					125.33335367838527,
					-41.33331298828125
				]
			]
		},
		{
			"type": "line",
			"version": 146,
			"versionNonce": 441557413,
			"isDeleted": false,
			"id": "_rbcXvpfGJod7wq9mc39t",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 868.6021118164061,
			"y": 2962.3959449132276,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 226.6667683919269,
			"height": 88.00003051757812,
			"seed": 300583397,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687813260287,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					226.6667683919269,
					-88.00003051757812
				]
			]
		},
		{
			"type": "text",
			"version": 102,
			"versionNonce": 642676523,
			"isDeleted": false,
			"id": "un65FFSS",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 1015.9353841145833,
			"y": 2834.7291409174595,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 19.935989379882812,
			"height": 35,
			"seed": 1662167717,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260287,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "2",
			"rawText": "2",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "2",
			"lineHeight": 1.25,
			"baseline": 25
		},
		{
			"type": "text",
			"version": 114,
			"versionNonce": 89662725,
			"isDeleted": false,
			"id": "owsMEnZd",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 1112.2687988281245,
			"y": 2858.3959042231236,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 17.304000854492188,
			"height": 35,
			"seed": 944375141,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260287,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "5",
			"rawText": "5",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "5",
			"lineHeight": 1.25,
			"baseline": 25
		},
		{
			"type": "freedraw",
			"version": 109,
			"versionNonce": 929847755,
			"isDeleted": false,
			"id": "lOrOwJfB5NreR1qyL036r",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 1008.6020100911458,
			"y": 2834.395838101704,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"width": 33.33333333333326,
			"height": 29.333343505859375,
			"seed": 1443762373,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260287,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					2.6668294270832575,
					0
				],
				[
					6.6666666666667425,
					5.333353678385265
				],
				[
					12.0001220703125,
					10.666656494140625
				],
				[
					17.3333740234375,
					16.00001017252589
				],
				[
					22.666829427083258,
					20
				],
				[
					26.666666666666742,
					22.666676839192405
				],
				[
					29.33349609375,
					25.333353678385265
				],
				[
					32.0001220703125,
					29.333343505859375
				],
				[
					33.33333333333326,
					29.333343505859375
				],
				[
					33.33333333333326,
					29.333343505859375
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 122,
			"versionNonce": 125254757,
			"isDeleted": false,
			"id": "hh9xCMH5GnXSdEm84gbWx",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 1205.935587565104,
			"y": 2903.729257901509,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"width": 25.333251953125,
			"height": 33.333333333333485,
			"seed": 474872069,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260287,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.3332112630205302,
					1.33331298828125
				],
				[
					5.333251953125,
					6.666666666666515
				],
				[
					11.999918619791515,
					14.666646321614735
				],
				[
					18.66658528645803,
					24.000040690104015
				],
				[
					23.99983723958303,
					30.666707356770985
				],
				[
					25.333251953125,
					32.000020345052235
				],
				[
					25.333251953125,
					33.333333333333485
				],
				[
					25.333251953125,
					33.333333333333485
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 121,
			"versionNonce": 1005906027,
			"isDeleted": false,
			"id": "tIjLzPfB1W3ZFcXSNdQn-",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 1273.9354654947915,
			"y": 2962.3959449132276,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"width": 5.333251953125,
			"height": 45.333353678385265,
			"seed": 813217253,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260287,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.333211263020985,
					17.333272298177235
				],
				[
					-2.6666259765625,
					21.33331298828125
				],
				[
					-4.00004069010447,
					30.666605631510265
				],
				[
					-5.333251953125,
					35.999959309895985
				],
				[
					-5.333251953125,
					42.6666259765625
				],
				[
					-5.333251953125,
					45.333353678385265
				],
				[
					-5.333251953125,
					45.333353678385265
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 121,
			"versionNonce": 1484548037,
			"isDeleted": false,
			"id": "vG_EjO4UDAgaq9FV5G7Tv",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 1039.2689208984375,
			"y": 3205.06257088979,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"width": 34.666544596354015,
			"height": 25.333353678385265,
			"seed": 181238123,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260287,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					2.6666259765625,
					2.666727701822765
				],
				[
					9.333292643229015,
					9.333394368489735
				],
				[
					18.66658528645803,
					16.00006103515625
				],
				[
					27.999877929687045,
					22.666727701822765
				],
				[
					34.666544596354015,
					24.000040690104015
				],
				[
					34.666544596354015,
					25.333353678385265
				],
				[
					34.666544596354015,
					25.333353678385265
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "text",
			"version": 31,
			"versionNonce": 1518675749,
			"isDeleted": false,
			"id": "jDYVEqPd",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": -418.73131306966127,
			"y": 2794.39591439565,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 300.579833984375,
			"height": 70,
			"seed": 406589995,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260287,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "parent=[0,0,1,2,0,3,0]\n",
			"rawText": "parent=[0,0,1,2,0,3,0]\n",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "parent=[0,0,1,2,0,3,0]\n",
			"lineHeight": 1.25,
			"baseline": 60
		},
		{
			"type": "freedraw",
			"version": 9,
			"versionNonce": 1495271851,
			"isDeleted": false,
			"id": "EtLGc-qF9UvXKZxWs1wfn",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": -168.73131306966138,
			"y": 2757.062540372212,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 3.9999898274738825,
			"height": 14.666646321614735,
			"seed": 1312611371,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260287,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.33331298828125
				],
				[
					0,
					5.333353678385265
				],
				[
					-2.6666768391926325,
					9.333292643229015
				],
				[
					-3.9999898274738825,
					12.000020345052235
				],
				[
					-3.9999898274738825,
					14.666646321614735
				],
				[
					-3.9999898274738825,
					14.666646321614735
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "rectangle",
			"version": 164,
			"versionNonce": 1342110341,
			"isDeleted": false,
			"id": "hJTer_xAVhw36BpcQqMaL",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 476.43552652994777,
			"y": 2860.729262987772,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 387,
			"height": 82,
			"seed": 1993195819,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "5QMVUA8w"
				}
			],
			"updated": 1687813260287,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 119,
			"versionNonce": 1869061195,
			"isDeleted": false,
			"id": "5QMVUA8w",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 626.8155390421548,
			"y": 2884.229262987772,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 86.23997497558594,
			"height": 35,
			"seed": 947942245,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260287,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "DFS 5",
			"rawText": "DFS 5",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "hJTer_xAVhw36BpcQqMaL",
			"originalText": "DFS 5",
			"lineHeight": 1.25,
			"baseline": 25
		},
		{
			"type": "rectangle",
			"version": 95,
			"versionNonce": 1369924069,
			"isDeleted": false,
			"id": "ZCjzuxjXslSHI2ny5wVXK",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 480.43536376953125,
			"y": 2766.8958686192823,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 347,
			"height": 91,
			"seed": 735545349,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "hR1uooJF"
				}
			],
			"updated": 1687813260287,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 14,
			"versionNonce": 140761835,
			"isDeleted": false,
			"id": "hR1uooJF",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 610.5073776245117,
			"y": 2794.8958686192823,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 86.85597229003906,
			"height": 35,
			"seed": 1942667819,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260287,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "DFS 4",
			"rawText": "DFS 4",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "ZCjzuxjXslSHI2ny5wVXK",
			"originalText": "DFS 4",
			"lineHeight": 1.25,
			"baseline": 25
		},
		{
			"type": "line",
			"version": 37,
			"versionNonce": 76275013,
			"isDeleted": false,
			"id": "o0_n2ngILJx8QknlZi2Op",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 825.9353841145834,
			"y": 2767.062540372212,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 78.66668701171898,
			"height": 66.66666666666652,
			"seed": 947981413,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687813260287,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					78.66668701171898,
					-66.66666666666652
				]
			]
		},
		{
			"type": "line",
			"version": 17,
			"versionNonce": 1084179851,
			"isDeleted": false,
			"id": "Kl1JRc316gAkeU8HJZfUV",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 832.6020507812499,
			"y": 2789.729217211405,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 54.666646321614735,
			"height": 32.000020345052235,
			"seed": 58178725,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687813260287,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					54.666646321614735,
					-32.000020345052235
				]
			]
		},
		{
			"type": "line",
			"version": 9,
			"versionNonce": 269085861,
			"isDeleted": false,
			"id": "wPdq96JxRXJppRIxFTG7O",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 833.9353637695311,
			"y": 2821.7291866938267,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 72.00002034505223,
			"height": 10.666656494140625,
			"seed": 757401509,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687813260287,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					72.00002034505223,
					-10.666656494140625
				]
			]
		},
		{
			"type": "text",
			"version": 32,
			"versionNonce": 1062493227,
			"isDeleted": false,
			"id": "gDLolPmd",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 925.6019287109376,
			"y": 2682.3958940505972,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 7.5879974365234375,
			"height": 35,
			"seed": 229706251,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260287,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "1",
			"rawText": "1",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "1",
			"lineHeight": 1.25,
			"baseline": 25
		},
		{
			"type": "text",
			"version": 3,
			"versionNonce": 1406078981,
			"isDeleted": false,
			"id": "KuIKjvNl",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 915.2686767578124,
			"y": 2741.7291866938267,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 17.304000854492188,
			"height": 35,
			"seed": 2061019877,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260287,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "5",
			"rawText": "5",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "5",
			"lineHeight": 1.25,
			"baseline": 25
		},
		{
			"type": "text",
			"version": 3,
			"versionNonce": 1617796811,
			"isDeleted": false,
			"id": "DclbFoh9",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 921.9353434244791,
			"y": 2805.0625200271597,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 17.919998168945312,
			"height": 35,
			"seed": 343040811,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260287,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "6",
			"rawText": "6",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "6",
			"lineHeight": 1.25,
			"baseline": 25
		},
		{
			"type": "freedraw",
			"version": 9,
			"versionNonce": 1574487909,
			"isDeleted": false,
			"id": "1hOsWf1vvt-RikXv8ZWEK",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 943.2686564127604,
			"y": 2693.7292070388785,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"width": 23.99993896484375,
			"height": 6.66666666666697,
			"seed": 778020645,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260287,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-2.6666259765625,
					0
				],
				[
					-5.333251953125,
					0
				],
				[
					-13.333333333333258,
					2.66667683919286
				],
				[
					-20,
					3.99998982747411
				],
				[
					-23.99993896484375,
					6.66666666666697
				],
				[
					-23.99993896484375,
					6.66666666666697
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 14,
			"versionNonce": 512068971,
			"isDeleted": false,
			"id": "gQXdAqx0qForeW94OMx7g",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 941.9353434244791,
			"y": 2747.062540372212,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"width": 29.333292643229242,
			"height": 23.99998982747411,
			"seed": 1654942885,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260287,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-3.99993896484375,
					2.66667683919286
				],
				[
					-10.666605631510492,
					6.666666666666515
				],
				[
					-17.333272298177008,
					11.999969482421875
				],
				[
					-21.33331298828125,
					16.00001017252589
				],
				[
					-22.6666259765625,
					18.66663614908839
				],
				[
					-25.333353678385492,
					20
				],
				[
					-27.999979654947992,
					21.33331298828125
				],
				[
					-27.999979654947992,
					22.66667683919286
				],
				[
					-29.333292643229242,
					22.66667683919286
				],
				[
					-29.333292643229242,
					23.99998982747411
				],
				[
					-29.333292643229242,
					23.99998982747411
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 15,
			"versionNonce": 544510661,
			"isDeleted": false,
			"id": "BfwdCKiAj2BLZSMEV5HRr",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 944.6020711263021,
			"y": 2804.395863533019,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"width": 21.333414713541742,
			"height": 27.99997965494822,
			"seed": 287801323,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260287,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.33331298828125
				],
				[
					-1.3334147135417425,
					3.99998982747411
				],
				[
					-2.6667277018229925,
					7.99997965494822
				],
				[
					-6.6666666666667425,
					13.333333333333485
				],
				[
					-8.000081380208485,
					16.000010172526345
				],
				[
					-9.333394368489735,
					16.000010172526345
				],
				[
					-12.000020345052235,
					18.66668701171875
				],
				[
					-13.333333333333485,
					20
				],
				[
					-16.00006103515625,
					23.99998982747411
				],
				[
					-20,
					27.99997965494822
				],
				[
					-21.333414713541742,
					27.99997965494822
				],
				[
					-21.333414713541742,
					27.99997965494822
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "rectangle",
			"version": 47,
			"versionNonce": 1021749259,
			"isDeleted": false,
			"id": "xavObiDKXd6OrIllc6XsD",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 477.9354044596354,
			"y": 2660.3958737055455,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 341.33331298828125,
			"height": 106.66666666666652,
			"seed": 1281205835,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [],
			"updated": 1687813260287,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 8,
			"versionNonce": 1749021221,
			"isDeleted": false,
			"id": "vJNJHylu",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 618.6020100911459,
			"y": 2708.395853360493,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 86.85597229003906,
			"height": 35,
			"seed": 1063786725,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260287,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "DFS 6",
			"rawText": "DFS 6",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "DFS 6",
			"lineHeight": 1.25,
			"baseline": 25
		},
		{
			"type": "line",
			"version": 13,
			"versionNonce": 831221419,
			"isDeleted": false,
			"id": "9AJsROREZhrfnkYv_I8Q8",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 817.9354044596354,
			"y": 2671.062530199686,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 40,
			"height": 66.66666666666697,
			"seed": 521611013,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687813260288,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					40,
					-66.66666666666697
				]
			]
		},
		{
			"type": "line",
			"version": 21,
			"versionNonce": 304637317,
			"isDeleted": false,
			"id": "mskqxDRWmmeGclckkH7RW",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 824.6020711263021,
			"y": 2693.729156176248,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 90.66660563151027,
			"height": 61.333363850911155,
			"seed": 461060331,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687813260288,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					90.66660563151027,
					-61.333363850911155
				]
			]
		},
		{
			"type": "text",
			"version": 4,
			"versionNonce": 1327391051,
			"isDeleted": false,
			"id": "Js50Xmnr",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 868.6020100911459,
			"y": 2568.395853360493,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 19.263992309570312,
			"height": 35,
			"seed": 1170964299,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260288,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "0",
			"rawText": "0",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "0",
			"lineHeight": 1.25,
			"baseline": 25
		},
		{
			"type": "text",
			"version": 37,
			"versionNonce": 788135915,
			"isDeleted": false,
			"id": "pnFCxslO",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 915.2686767578124,
			"y": 2598.729156176248,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 17.919998168945312,
			"height": 35,
			"seed": 810025419,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260288,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "4",
			"rawText": "4",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "4",
			"lineHeight": 1.25,
			"baseline": 25
		},
		{
			"type": "freedraw",
			"version": 11,
			"versionNonce": 1435928645,
			"isDeleted": false,
			"id": "KiFpVPv1PxhIw5cxJ1GMX",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 889.9353230794271,
			"y": 2559.062509854634,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"width": 13.333333333333485,
			"height": 20,
			"seed": 1875895915,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260288,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.33336385091161
				],
				[
					-2.6666259765625,
					4.000040690104015
				],
				[
					-5.333251953125,
					8.000030517578125
				],
				[
					-7.9999796549479925,
					12.000020345052235
				],
				[
					-10.666605631510492,
					14.66669718424464
				],
				[
					-11.999918619791742,
					20
				],
				[
					-13.333333333333485,
					20
				],
				[
					-13.333333333333485,
					20
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 17,
			"versionNonce": 1529399947,
			"isDeleted": false,
			"id": "zecqfI8EJPw83Fw83TUe9",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 956.6019897460936,
			"y": 2599.062509854634,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"width": 34.66664632161451,
			"height": 22.66667683919286,
			"seed": 1977320331,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260288,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.33331298828125,
					0
				],
				[
					-3.99993896484375,
					2.66667683919286
				],
				[
					-7.999979654947765,
					5.333353678385265
				],
				[
					-14.666646321614508,
					9.333343505859375
				],
				[
					-21.33331298828125,
					12.000020345052235
				],
				[
					-26.666666666666515,
					16.00001017252589
				],
				[
					-27.999979654947765,
					18.66668701171875
				],
				[
					-29.333292643229015,
					21.33336385091161
				],
				[
					-30.666605631510265,
					21.33336385091161
				],
				[
					-31.999918619791515,
					21.33336385091161
				],
				[
					-31.999918619791515,
					22.66667683919286
				],
				[
					-33.33333333333326,
					22.66667683919286
				],
				[
					-34.66664632161451,
					22.66667683919286
				],
				[
					-34.66664632161451,
					22.66667683919286
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 14,
			"versionNonce": 1619474341,
			"isDeleted": false,
			"id": "oqDjhDN2Su0O49zLUEeTz",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 1117.935302734375,
			"y": 2851.062530199686,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"width": 4.000040690104015,
			"height": 41.333363850911155,
			"seed": 29821067,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260288,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.33331298828125
				],
				[
					1.333414713541515,
					3.999989827473655
				],
				[
					1.333414713541515,
					9.333343505859375
				],
				[
					2.66682942708303,
					17.33332316080714
				],
				[
					2.66682942708303,
					23.999989827473655
				],
				[
					2.66682942708303,
					30.666656494140625
				],
				[
					2.66682942708303,
					36.00001017252589
				],
				[
					4.000040690104015,
					38.66663614908839
				],
				[
					4.000040690104015,
					40.000050862629905
				],
				[
					4.000040690104015,
					41.333363850911155
				],
				[
					4.000040690104015,
					41.333363850911155
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "text",
			"version": 48,
			"versionNonce": 946159915,
			"isDeleted": false,
			"id": "U7OPBOzw",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": -416.7313181559243,
			"y": 2843.062499682108,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 298.619873046875,
			"height": 70,
			"seed": 779363493,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260288,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "parent=[0,0,1,2,5,3,0]\n",
			"rawText": "parent=[0,0,1,2,5,3,0]\n",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "parent=[0,0,1,2,5,3,0]\n",
			"lineHeight": 1.25,
			"baseline": 60
		},
		{
			"type": "text",
			"version": 63,
			"versionNonce": 1550514949,
			"isDeleted": false,
			"id": "CxFoG9Wj",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": -419.3979949951171,
			"y": 2887.062540372212,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 297.27587890625,
			"height": 70,
			"seed": 1023471627,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260288,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "parent=[0,0,1,2,5,3,4]\n",
			"rawText": "parent=[0,0,1,2,5,3,4]\n",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "parent=[0,0,1,2,5,3,4]\n",
			"lineHeight": 1.25,
			"baseline": 60
		},
		{
			"type": "freedraw",
			"version": 16,
			"versionNonce": 807003083,
			"isDeleted": false,
			"id": "z1nFdKoM6dPDPuv6j2NRG",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": -198.06465657552076,
			"y": 2803.062550544738,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 2.6666768391927462,
			"height": 22.6666259765625,
			"seed": 1458804939,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260288,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.3333638509114962,
					1.33331298828125
				],
				[
					1.3333638509114962,
					2.6666259765625
				],
				[
					1.3333638509114962,
					3.99998982747411
				],
				[
					1.3333638509114962,
					6.66666666666697
				],
				[
					1.3333638509114962,
					9.33329264322947
				],
				[
					1.3333638509114962,
					10.666656494140625
				],
				[
					1.3333638509114962,
					11.999969482421875
				],
				[
					1.3333638509114962,
					13.333333333333485
				],
				[
					1.3333638509114962,
					15.999959309895985
				],
				[
					1.3333638509114962,
					20
				],
				[
					2.6666768391927462,
					21.33331298828125
				],
				[
					2.6666768391927462,
					22.6666259765625
				],
				[
					2.6666768391927462,
					22.6666259765625
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 12,
			"versionNonce": 1639928421,
			"isDeleted": false,
			"id": "VOMLFGqeGiDVJDVrj9Msx",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": -139.397969563802,
			"y": 2847.062540372212,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 1.3333638509113825,
			"height": 25.33330281575536,
			"seed": 1760583941,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260288,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.3333638509113825,
					0
				],
				[
					-1.3333638509113825,
					1.33331298828125
				],
				[
					-1.3333638509113825,
					2.66667683919286
				],
				[
					-1.3333638509113825,
					7.999979654947765
				],
				[
					-1.3333638509113825,
					16.00001017252589
				],
				[
					-1.3333638509113825,
					20
				],
				[
					0,
					22.66667683919286
				],
				[
					0,
					25.33330281575536
				],
				[
					0,
					25.33330281575536
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "text",
			"version": 83,
			"versionNonce": 1178582309,
			"isDeleted": false,
			"id": "KAb9M4q4",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": -48.09777600714301,
			"y": 2883.665060705681,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 319.3118896484375,
			"height": 35,
			"seed": 828161867,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260288,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "searched=[t,t,t,t,t,t,t]",
			"rawText": "searched=[t,t,t,t,t,t,t]",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "searched=[t,t,t,t,t,t,t]",
			"lineHeight": 1.25,
			"baseline": 25
		},
		{
			"type": "text",
			"version": 96,
			"versionNonce": 209834923,
			"isDeleted": false,
			"id": "PfSjSwKS",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": -413.73653334148867,
			"y": 2999.557732516123,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 513.7998046875,
			"height": 35,
			"seed": 1572137643,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687813260288,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "parent nos ayuda aconstriur el arbol",
			"rawText": "parent nos ayuda aconstriur el arbol",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "parent nos ayuda aconstriur el arbol",
			"lineHeight": 1.25,
			"baseline": 25
		},
		{
			"type": "ellipse",
			"version": 562,
			"versionNonce": 1200148548,
			"isDeleted": false,
			"id": "ky5InVlA989EHd-YxTVA8",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": -183.97913099731932,
			"y": 3066.2272367095597,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 72,
			"height": 64,
			"seed": 1104030597,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"type": "text",
					"id": "OEZv8Pf4"
				}
			],
			"updated": 1687839463326,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 511,
			"versionNonce": 688459344,
			"isDeleted": false,
			"id": "OEZv8Pf4",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": -157.5669712748202,
			"y": 3080.59981971159,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 19.263992309570312,
			"height": 35,
			"seed": 959197093,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687923214867,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "0",
			"rawText": "0",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "ky5InVlA989EHd-YxTVA8",
			"originalText": "0",
			"lineHeight": 1.25,
			"baseline": 25
		},
		{
			"type": "ellipse",
			"version": 572,
			"versionNonce": 1645094852,
			"isDeleted": false,
			"id": "owo8MPhCSqq_PmKEmc-tS",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": -187.76858181891657,
			"y": 3201.49061429011,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 83,
			"height": 81,
			"seed": 1083106149,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"type": "text",
					"id": "eLgGJm5U"
				}
			],
			"updated": 1687839463326,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 511,
			"versionNonce": 311541424,
			"isDeleted": false,
			"id": "eLgGJm5U",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": -149.90751195642002,
			"y": 3224.352789652055,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.5879974365234375,
			"height": 35,
			"seed": 1317062789,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687923214869,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "1",
			"rawText": "1",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "owo8MPhCSqq_PmKEmc-tS",
			"originalText": "1",
			"lineHeight": 1.25,
			"baseline": 25
		},
		{
			"type": "ellipse",
			"version": 570,
			"versionNonce": 1090293572,
			"isDeleted": false,
			"id": "JWBQ7D-VDcL9youogMqH_",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": -192.62347304150944,
			"y": 3363.9308369205237,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 91,
			"height": 76,
			"seed": 245483109,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"type": "text",
					"id": "oHBigAS6"
				}
			],
			"updated": 1687839463326,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 511,
			"versionNonce": 1735574608,
			"isDeleted": false,
			"id": "oHBigAS6",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": -157.26482627543876,
			"y": 3384.560779235435,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 19.935989379882812,
			"height": 35,
			"seed": 127840459,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687923214871,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "2",
			"rawText": "2",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "JWBQ7D-VDcL9youogMqH_",
			"originalText": "2",
			"lineHeight": 1.25,
			"baseline": 25
		},
		{
			"type": "ellipse",
			"version": 559,
			"versionNonce": 347211460,
			"isDeleted": false,
			"id": "hj9CV0mfNCxwv3MuyTr3V",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": -194.4920375814463,
			"y": 3528.4241480258765,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 105,
			"height": 84,
			"seed": 1077711467,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"type": "text",
					"id": "fFMLeNT8"
				}
			],
			"updated": 1687839463326,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 511,
			"versionNonce": 289826992,
			"isDeleted": false,
			"id": "fFMLeNT8",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": -151.64914017577132,
			"y": 3552.7256632160415,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 19.0679931640625,
			"height": 35,
			"seed": 655719141,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687923214872,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "3",
			"rawText": "3",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "hj9CV0mfNCxwv3MuyTr3V",
			"originalText": "3",
			"lineHeight": 1.25,
			"baseline": 25
		},
		{
			"type": "line",
			"version": 531,
			"versionNonce": 1372360260,
			"isDeleted": false,
			"id": "fqDF99Eeltozv1WnnhvCO",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": -142.84725507349344,
			"y": 3121.3938547500647,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.4211309837505723,
			"height": 78.68725245019095,
			"seed": 1296216453,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687839463326,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					3.4211309837505723,
					78.68725245019095
				]
			]
		},
		{
			"type": "line",
			"version": 521,
			"versionNonce": 1774020604,
			"isDeleted": false,
			"id": "ov01F-8VUjof0BfdDSjz-",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": -147.97908205690123,
			"y": 3282.189490634197,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.7106959996567639,
			"height": 78.68718719630033,
			"seed": 1388947813,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687839463326,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					1.7106959996567639,
					78.68718719630033
				]
			]
		},
		{
			"type": "line",
			"version": 530,
			"versionNonce": 690628036,
			"isDeleted": false,
			"id": "pY5f3XveurWxC2-hPkT1D",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": -144.55795107315066,
			"y": 3436.142734043047,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.7106959996572186,
			"height": 90.66134140110034,
			"seed": 237909093,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687839463326,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					1.7106959996572186,
					90.66134140110034
				]
			]
		},
		{
			"type": "line",
			"version": 520,
			"versionNonce": 1917257852,
			"isDeleted": false,
			"id": "vaboxliOqOW5FgNwoARVi",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": -136.0049931059923,
			"y": 3620.8866130828883,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.4213919993139825,
			"height": 59.87077102399917,
			"seed": 664335819,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687839463326,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					3.4213919993139825,
					59.87077102399917
				]
			]
		},
		{
			"type": "ellipse",
			"version": 525,
			"versionNonce": 2145963332,
			"isDeleted": false,
			"id": "ZFAvy0wMk57zBD5_IJmCS",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": -168.75429466372248,
			"y": 3696.152734549328,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 98,
			"height": 64,
			"seed": 872068101,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"type": "text",
					"id": "3c747dzj"
				}
			],
			"updated": 1687839463326,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 511,
			"versionNonce": 1530247760,
			"isDeleted": false,
			"id": "3c747dzj",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": -128.5545273691094,
			"y": 3710.5253175513585,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 17.304000854492188,
			"height": 35,
			"seed": 1860324971,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687923214873,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "5",
			"rawText": "5",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "ZFAvy0wMk57zBD5_IJmCS",
			"originalText": "5",
			"lineHeight": 1.25,
			"baseline": 25
		},
		{
			"type": "line",
			"version": 534,
			"versionNonce": 1734771908,
			"isDeleted": false,
			"id": "yHAvKtFTkubOm8fyMU6Au",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": -117.18838117201881,
			"y": 3761.155136795063,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.4211309837505723,
			"height": 87.24014516345869,
			"seed": 2000869189,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687839463326,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-3.4211309837505723,
					87.24014516345869
				]
			]
		},
		{
			"type": "ellipse",
			"version": 537,
			"versionNonce": 197400956,
			"isDeleted": false,
			"id": "19LC0AphMs3L2XxiKZq79",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": -149.79303072957737,
			"y": 3865.4236605072374,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 96,
			"height": 72,
			"seed": 1658014795,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"type": "text",
					"id": "6vPSsRzU"
				}
			],
			"updated": 1687839463326,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 511,
			"versionNonce": 1742066352,
			"isDeleted": false,
			"id": "6vPSsRzU",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": -110.6941553110043,
			"y": 3883.9678163845215,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 17.919998168945312,
			"height": 35,
			"seed": 1980487243,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687923214875,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "4",
			"rawText": "4",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "19LC0AphMs3L2XxiKZq79",
			"originalText": "4",
			"lineHeight": 1.25,
			"baseline": 25
		},
		{
			"type": "line",
			"version": 512,
			"versionNonce": 1400605180,
			"isDeleted": false,
			"id": "iI9qERN2pqGPdlrQSdY-W",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": -50.47541343440912,
			"y": 3894.581333285845,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 104.34619160555667,
			"height": 5.131696475626086,
			"seed": 1735734789,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1687839463326,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					104.34619160555667,
					5.131696475626086
				]
			]
		},
		{
			"type": "ellipse",
			"version": 585,
			"versionNonce": 1532437444,
			"isDeleted": false,
			"id": "qT9ejwRUTuFGhcHka_zt8",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 55.50387153131419,
			"y": 3868.6341607452223,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 72,
			"height": 69,
			"seed": 1611983019,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"type": "text",
					"id": "5W2vtZvL"
				}
			],
			"updated": 1687839463326,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 563,
			"versionNonce": 120189008,
			"isDeleted": false,
			"id": "5W2vtZvL",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": 82.58802832412582,
			"y": 3885.7389767942864,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 17.919998168945312,
			"height": 35,
			"seed": 1209127173,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687923214877,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "6",
			"rawText": "6",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "qT9ejwRUTuFGhcHka_zt8",
			"originalText": "6",
			"lineHeight": 1.25,
			"baseline": 25
		},
		{
			"type": "text",
			"version": 163,
			"versionNonce": 879021252,
			"isDeleted": false,
			"id": "FUm8CTJs",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"angle": 0,
			"x": -372.22116323142967,
			"y": 2917.0086476497604,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 243.79986572265625,
			"height": 25,
			"seed": 455246404,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1687839374903,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "(nodos) 0 1 2 3 4 5 6  ",
			"rawText": "(nodos) 0 1 2 3 4 5 6  ",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "(nodos) 0 1 2 3 4 5 6  ",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"id": "gZhW299r",
			"type": "text",
			"x": -41.7219034830722,
			"y": 3416.108759595988,
			"width": 1143.855712890625,
			"height": 105,
			"angle": 0,
			"strokeColor": "#ff0000",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 40,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1075335344,
			"version": 323,
			"versionNonce": 993971280,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1687929485119,
			"link": null,
			"locked": false,
			"text": "El diccionario parents se utiliza para almacenar información sobre los padres\n de los nodos en el recorrido DFS. Durante el recorrido, a medida que se visita \nun nuevo nodo, se registra su padre, es decir, el nodo desde el cual se llegó a él.",
			"rawText": "El diccionario parents se utiliza para almacenar información sobre los padres\n de los nodos en el recorrido DFS. Durante el recorrido, a medida que se visita \nun nuevo nodo, se registra su padre, es decir, el nodo desde el cual se llegó a él.",
			"fontSize": 28,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 95,
			"containerId": null,
			"originalText": "El diccionario parents se utiliza para almacenar información sobre los padres\n de los nodos en el recorrido DFS. Durante el recorrido, a medida que se visita \nun nuevo nodo, se registra su padre, es decir, el nodo desde el cual se llegó a él.",
			"lineHeight": 1.25,
			"isFrameName": false
		}
	],
	"appState": {
		"theme": "dark",
		"viewBackgroundColor": "#f5faff",
		"currentItemStrokeColor": "#ff0000",
		"currentItemBackgroundColor": "transparent",
		"currentItemFillStyle": "hachure",
		"currentItemStrokeWidth": 4,
		"currentItemStrokeStyle": "solid",
		"currentItemRoughness": 1,
		"currentItemOpacity": 40,
		"currentItemFontFamily": 1,
		"currentItemFontSize": 28,
		"currentItemTextAlign": "left",
		"currentItemStartArrowhead": null,
		"currentItemEndArrowhead": "arrow",
		"scrollX": 363.0552368164057,
		"scrollY": -2774.921259595988,
		"zoom": {
			"value": 0.7500000000000001
		},
		"currentItemRoundness": "round",
		"gridSize": null,
		"currentStrokeOptions": null,
		"previousGridSize": null
	},
	"files": {}
}
```
%%