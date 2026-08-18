---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠==


# Text Elements
A ^2WSjjYsi

B ^8HOF2UpX

C ^Po5JqIRg

D ^oZwEULUf

E ^cN8Yx3TC

FIN ^odZq6Mon

H ^Gknrhyel

G ^eO88zKPz

Grafo= {'A':{'B':2,'C':1,'D':5},
        'B':{'E':1},
        'C':{'E':3},
        'D':{'FIN':10},
        'E':{'G':1,'H':3}
        'G':{'FIN':5}
        'H':{'FIN':2,'G':1}
        'FIN':{}} ^Avgqlglr

2 ^fxJ76Ft0

1 ^9UOhaphD

5 ^Ma46lNcx

3 ^HCZFTySI

1 ^gYyRJpnt

10 ^4m4u7EME

2 ^fUFCOWcq

1 ^0Fzvo73W

3 ^tuALPCWh

1 ^2t3rRll8

5 ^H0gvUNym

Costs={
        'A': inf,
        'B':2,
        'C':1,
        'D':5,
        'E':inf,
        'G':inf,
        'H':inf,
        'Fin': inf
        } ^roh3Gscz

parent={
        'A': none,
        'B': 'A',
        'C':'A',
        'D':'A',
        'E':none,
        'G':none,
        'H':none,
        'Fin': none     ^84uFBHOc

start ^nCsQkqIY

find lowest_cost_node: C,B,E,G,D  ^9MsibdHM

c | cost['c']:1|  G['C']:{'E':3} | ['E']           | 'E'    |  ^4wppy0Kq

node | ^mpQPDfHW

cost | ^0X2xGOQS

neighbours | ^dCUyj71N

neighbours.keys | ^51FM39Xd

n ^cQtNyBZ6

for ^j0eahz8h

| new_cost ^70I4HrlN

| cost[n]>new_cost? ^ooqZ2vr0

| cost['n'] ^CyCeVDX1

| parents['n'] ^EvnVlCMs

El método .keys() devuelve una vista 
iterable de las claves en el diccionario. ^njkDVkUO

Dentro del bucle for, se calcula el nuevo costo 
para llegar al nodo vecino 
n desde el nodo actual node. Se suma el costo acumulado 
hasta el nodo actual (cost) con el costo de 
la arista que conecta node con n ^13wj70hQ

neighbours[n] ^ggOqmX0h

1+3=4 ^jOgTvyCI

'E' ^UB2CwQo6

cost+ ^n3Jonft4

inf>4 ^Hmw7m61Y

'E' ^XAU1uoQZ

4 ^ilaqaDOF

'E' ^AxKlzdNm

'C' ^A3wol8bu

Processed<-- C,B,E,G,D,H ^SJpEwlMo

B | cost['B']:2|  G['B']:{'E':1} | ['E']           | 'E'    |  ^lpxpa6FG

2+1=3 ^V9xSkYgt

4>3 ^8VDmAz8X

3 ^n7vNQtVN

'B' ^93npZS5I

4 ^TA7OL9Ef

3 ^tQRgSqZe

C ^YseYskhI

B ^ysOFhobq

E | cost['E']:3|  G['E']:{'G':1,'H':3} | ['G','H'] | 'G' 
                                                   | 'H' ^UsDycXVO

3+1=4 ^9dOVsYmX

3+3=6 ^NprbskNL

 inf>4 ^VX8a2zHY

'G' ^UeXF1SR8

'E' ^EUgYkOLA

4 ^tTK41cKL

'E' ^R5tNrPjZ

'H' ^nfMhdGYK

4 ^ypnekGtH

E ^0LzkYYvP

inf>6 ^UlymKvTe

6 ^RgP8JEN8

'E' ^KG1AHzMG

6 ^mUuvQ8fJ

E ^X8foqJku

G | cost['G']:4|  G['G']:{'FIN':5}   | ['FIN']     | 'FIN'    |  ^fzPREI90

4+5=9 ^dWWXK7oV

'FIN' ^CiXMlIis

inf>9 ^LmSamxFe

9 ^rpRWqqr4

'G' ^6QeWg2Jb

G ^TrnAj99U

9 ^8KTr1UgU

D | cost['D']:5|  G['D']:{'FIN':10} | ['FIN']     | 'FIN'    |  ^bjDW9YLB

5+10=15 ^uKkzIGQ4

9>15 ^39eT9GA0

H | cost['H']:6|  G['H']:{'FIN':2,'G':1}| ['FIN','G']  | 'FIN'
                                                          'G'  ^I55bZcIf

6+2=8 ^16juYYWB

6+1=7 ^mAdh9dGY

9>8 ^aIjmgKaZ

4>7 ^aqHAS4ib

8 ^lfboBWez

'H' ^fTWvdXoe

H ^Lm1PNaBM

8 ^EJNoG1ea

FIN | cost['FIN']:8|  G['FIN']:{} | []     |      |  ^LtsQQxUY

COSTO ^15BIB2ZS

A
B
C
D
E
G
H
FIN
 ^rmKmbZiS

inf
2
1
5
3
4
6
8 ^jV4GaRAk

start ^3dFOS9Yf

None
A
A
A
B
E
E
H ^YgHN5UO9

A
B
C
D
E
G
H
FIN
 ^eOJcRUmb

Ruta(A,Fin):A, B, E, H, FIN ^Un68vqRl

Costo:8 ^Thf0zKyx

ruta mas barata ^7lFYZFHA

2 ^YndUoNW8

1 ^RKSJzLn9

3 ^3ucve8OS

2 ^6Gr2zkQt

Parents ^TrbPAoHa

start ^cNngK4UB


# Embedded files
7c13b1cb2d9cb220911191bebb79cbd5c53394e6: [[Pasted Image 20230811161921_265.png]]

%%
# Drawing
```json
{
	"type": "excalidraw",
	"version": 2,
	"source": "https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/tag/1.9.12",
	"elements": [
		{
			"type": "ellipse",
			"version": 427,
			"versionNonce": 66467514,
			"isDeleted": false,
			"id": "sYUjRzZ6F_xEtVepXNEcy",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -657.3877965774329,
			"y": -524.8197553056985,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 51,
			"height": 58,
			"seed": 879063404,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"id": "W0Mt2enDsmtIzCyj9HBoA",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "2WSjjYsi"
				},
				{
					"id": "AUq3JKr9kWKLZMXi8bl0z",
					"type": "arrow"
				}
			],
			"updated": 1691799689178,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 367,
			"versionNonce": 112798182,
			"isDeleted": false,
			"id": "2WSjjYsi",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -640.0402963531586,
			"y": -511.3020424362989,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 16.2425537109375,
			"height": 30.952380952380956,
			"seed": 1942227796,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1691799689178,
			"link": null,
			"locked": false,
			"fontSize": 24.761904761904766,
			"fontFamily": 1,
			"text": "A",
			"rawText": "A",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "sYUjRzZ6F_xEtVepXNEcy",
			"originalText": "A",
			"lineHeight": 1.25,
			"baseline": 21
		},
		{
			"type": "ellipse",
			"version": 386,
			"versionNonce": 1009995642,
			"isDeleted": false,
			"id": "rP4lPyCsqZMIQchRDMiwf",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -497.2476509343396,
			"y": -603.3517786661785,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 43,
			"height": 59,
			"seed": 1483535444,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"id": "96vzFljbGtIyMbpoSHImy",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "8HOF2UpX"
				},
				{
					"id": "rGA1Q0OYeuEtAQe36AJJF",
					"type": "arrow"
				}
			],
			"updated": 1691799689178,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 353,
			"versionNonce": 1325858086,
			"isDeleted": false,
			"id": "8HOF2UpX",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -485.0379406263348,
			"y": -589.3364287111816,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 18.17498779296875,
			"height": 31.25,
			"seed": 1917235308,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1691799689178,
			"link": null,
			"locked": false,
			"fontSize": 25,
			"fontFamily": 1,
			"text": "B",
			"rawText": "B",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "rP4lPyCsqZMIQchRDMiwf",
			"originalText": "B",
			"lineHeight": 1.25,
			"baseline": 22
		},
		{
			"type": "ellipse",
			"version": 378,
			"versionNonce": 1187991610,
			"isDeleted": false,
			"id": "oRZ55M-x48aY9QZh0aLKJ",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -488.27485862280514,
			"y": -503.56989834890356,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 50,
			"height": 59,
			"seed": 1352796140,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"id": "clRVOV052M2zJmGSwRPzp",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "Po5JqIRg"
				},
				{
					"id": "W0Mt2enDsmtIzCyj9HBoA",
					"type": "arrow"
				}
			],
			"updated": 1691799689178,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 380,
			"versionNonce": 1287153766,
			"isDeleted": false,
			"id": "Po5JqIRg",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -471.50252357483214,
			"y": -489.5545483939067,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 16.099990844726562,
			"height": 31.250000000000004,
			"seed": 144254444,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1691799689178,
			"link": null,
			"locked": false,
			"fontSize": 25.000000000000004,
			"fontFamily": 1,
			"text": "C",
			"rawText": "C",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "oRZ55M-x48aY9QZh0aLKJ",
			"originalText": "C",
			"lineHeight": 1.25,
			"baseline": 22
		},
		{
			"type": "ellipse",
			"version": 323,
			"versionNonce": 1202534650,
			"isDeleted": false,
			"id": "hySP6iaejUyzn_PKm6fN0",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -485.8129477336316,
			"y": -409.33144212094305,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 46,
			"height": 58,
			"seed": 748278380,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"id": "77-bpmY0rV773FwGT-h9a",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "oZwEULUf"
				},
				{
					"id": "AUq3JKr9kWKLZMXi8bl0z",
					"type": "arrow"
				}
			],
			"updated": 1691799689178,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 334,
			"versionNonce": 1067084710,
			"isDeleted": false,
			"id": "oZwEULUf",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -472.1080046530706,
			"y": -395.6153165531307,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 19.063201904296875,
			"height": 30.555555555555554,
			"seed": 844675924,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1691799689178,
			"link": null,
			"locked": false,
			"fontSize": 24.444444444444443,
			"fontFamily": 1,
			"text": "D",
			"rawText": "D",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "hySP6iaejUyzn_PKm6fN0",
			"originalText": "D",
			"lineHeight": 1.25,
			"baseline": 22
		},
		{
			"type": "ellipse",
			"version": 422,
			"versionNonce": 1850739130,
			"isDeleted": false,
			"id": "5M4bcqUiLbfRY8F7dEHO1",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -356.9660390813592,
			"y": -597.8083193326332,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 47,
			"height": 59,
			"seed": 1325261652,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"id": "96vzFljbGtIyMbpoSHImy",
					"type": "arrow"
				},
				{
					"id": "clRVOV052M2zJmGSwRPzp",
					"type": "arrow"
				},
				{
					"id": "r9fiZK8MD2iQNB8OnMp5B",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "cN8Yx3TC"
				}
			],
			"updated": 1691799689178,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 370,
			"versionNonce": 1708787430,
			"isDeleted": false,
			"id": "cN8Yx3TC",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -342.19339237234857,
			"y": -584.1401915998586,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 17.220687866210938,
			"height": 31.944444444444443,
			"seed": 551108564,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1691799689178,
			"link": null,
			"locked": false,
			"fontSize": 25.555555555555554,
			"fontFamily": 1,
			"text": "E",
			"rawText": "E",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "5M4bcqUiLbfRY8F7dEHO1",
			"originalText": "E",
			"lineHeight": 1.25,
			"baseline": 22
		},
		{
			"type": "ellipse",
			"version": 386,
			"versionNonce": 31113850,
			"isDeleted": false,
			"id": "E0s7j1lh00Arhhc_fz878",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -324.70540643489574,
			"y": -480.6775363350671,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 49,
			"height": 57,
			"seed": 1689400428,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"id": "7w-EBIWMTyTQiOAduSeox",
					"type": "arrow"
				},
				{
					"id": "JuvlYgOE6HCuRgKtXYT60",
					"type": "arrow"
				},
				{
					"id": "O7rF3xAlIxi0AIoiXz9CB",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "Gknrhyel"
				}
			],
			"updated": 1691799689178,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 306,
			"versionNonce": 805583398,
			"isDeleted": false,
			"id": "Gknrhyel",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -306.6415220856849,
			"y": -467.3300795988837,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 13.2239990234375,
			"height": 30,
			"seed": 1729991532,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1691799689178,
			"link": null,
			"locked": false,
			"fontSize": 24,
			"fontFamily": 1,
			"text": "H",
			"rawText": "H",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "E0s7j1lh00Arhhc_fz878",
			"originalText": "H",
			"lineHeight": 1.25,
			"baseline": 21
		},
		{
			"type": "ellipse",
			"version": 442,
			"versionNonce": 1829790522,
			"isDeleted": false,
			"id": "whYN5RrC1cwmBeBf2mvWY",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -215.86195604588778,
			"y": -385.34382178887984,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 92,
			"height": 59,
			"seed": 1636813652,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"id": "77-bpmY0rV773FwGT-h9a",
					"type": "arrow"
				},
				{
					"id": "5xYwwyyE2SvUncyGqY6H1",
					"type": "arrow"
				},
				{
					"id": "JuvlYgOE6HCuRgKtXYT60",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "odZq6Mon"
				}
			],
			"updated": 1691799689178,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 509,
			"versionNonce": 1963328870,
			"isDeleted": false,
			"id": "odZq6Mon",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -190.96552050732444,
			"y": -370.64912400779605,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 42.15330505371094,
			"height": 29.891304347826093,
			"seed": 467285332,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1691799689178,
			"link": null,
			"locked": false,
			"fontSize": 23.913043478260875,
			"fontFamily": 1,
			"text": "FIN",
			"rawText": "FIN",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "whYN5RrC1cwmBeBf2mvWY",
			"originalText": "FIN",
			"lineHeight": 1.25,
			"baseline": 21
		},
		{
			"type": "ellipse",
			"version": 338,
			"versionNonce": 1247013882,
			"isDeleted": false,
			"id": "XHUEwoA--O0mtUggFtx0E",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -202.20092971563764,
			"y": -562.6999021525522,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 71,
			"height": 58,
			"seed": 150583148,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"id": "r9fiZK8MD2iQNB8OnMp5B",
					"type": "arrow"
				},
				{
					"id": "5xYwwyyE2SvUncyGqY6H1",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "eO88zKPz"
				}
			],
			"updated": 1691799689178,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 290,
			"versionNonce": 640444582,
			"isDeleted": false,
			"id": "eO88zKPz",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -176.3658959238343,
			"y": -548.8575139584773,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 19.125350952148438,
			"height": 30.303030303030305,
			"seed": 1609969132,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1691799689178,
			"link": null,
			"locked": false,
			"fontSize": 24.242424242424242,
			"fontFamily": 1,
			"text": "G",
			"rawText": "G",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "XHUEwoA--O0mtUggFtx0E",
			"originalText": "G",
			"lineHeight": 1.25,
			"baseline": 21
		},
		{
			"type": "arrow",
			"version": 850,
			"versionNonce": 959909414,
			"isDeleted": false,
			"id": "rGA1Q0OYeuEtAQe36AJJF",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -607.6325695445445,
			"y": -501.0539478271753,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 105.22179637854322,
			"height": 68.14771688931535,
			"seed": 872136404,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"type": "text",
					"id": "fxJ76Ft0"
				}
			],
			"updated": 1691800161002,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": {
				"elementId": "rP4lPyCsqZMIQchRDMiwf",
				"gap": 5.402957430392154,
				"focus": 0.3868173880972096
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
					105.22179637854322,
					-68.14771688931535
				]
			]
		},
		{
			"type": "text",
			"version": 199,
			"versionNonce": 52716518,
			"isDeleted": false,
			"id": "fxJ76Ft0",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -575.7904665812658,
			"y": -556.8158665989097,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 14.239990234375,
			"height": 25,
			"seed": 556804716,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1691799689178,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "2",
			"rawText": "2",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "rGA1Q0OYeuEtAQe36AJJF",
			"originalText": "2",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "arrow",
			"version": 960,
			"versionNonce": 934952102,
			"isDeleted": false,
			"id": "W0Mt2enDsmtIzCyj9HBoA",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -603.3403342416832,
			"y": -491.8206075599173,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 108.86157085668708,
			"height": 16.186048798921377,
			"seed": 116358100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"type": "text",
					"id": "9UOhaphD"
				}
			],
			"updated": 1691800161003,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "sYUjRzZ6F_xEtVepXNEcy",
				"gap": 3.269247746036076,
				"focus": -0.008391442209222354
			},
			"endBinding": {
				"elementId": "oRZ55M-x48aY9QZh0aLKJ",
				"gap": 6.233860794794037,
				"focus": -0.10341557216360156
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
					108.86157085668708,
					16.186048798921377
				]
			]
		},
		{
			"type": "text",
			"version": 164,
			"versionNonce": 1308292902,
			"isDeleted": false,
			"id": "9UOhaphD",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -566.1078290514192,
			"y": -512.2636242438364,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.4199981689453125,
			"height": 25,
			"seed": 2056658516,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1691799689178,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "1",
			"rawText": "1",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "W0Mt2enDsmtIzCyj9HBoA",
			"originalText": "1",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "arrow",
			"version": 864,
			"versionNonce": 1294191398,
			"isDeleted": false,
			"id": "AUq3JKr9kWKLZMXi8bl0z",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -615.1105675913656,
			"y": -465.57591058198176,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 125.00728801228558,
			"height": 79.08154161166124,
			"seed": 2072150252,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"type": "text",
					"id": "Ma46lNcx"
				}
			],
			"updated": 1691800161005,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "sYUjRzZ6F_xEtVepXNEcy",
				"gap": 6.511696719541109,
				"focus": 0.5915450792062676
			},
			"endBinding": {
				"elementId": "hySP6iaejUyzn_PKm6fN0",
				"gap": 4.756835980319473,
				"focus": -0.34215459377274615
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
					125.00728801228558,
					79.08154161166124
				]
			]
		},
		{
			"type": "text",
			"version": 198,
			"versionNonce": 2132615782,
			"isDeleted": false,
			"id": "Ma46lNcx",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -572.6557924594338,
			"y": -462.23444906775364,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 12.3599853515625,
			"height": 25,
			"seed": 1747144404,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1691799689178,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "5",
			"rawText": "5",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "AUq3JKr9kWKLZMXi8bl0z",
			"originalText": "5",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "arrow",
			"version": 1051,
			"versionNonce": 1242265190,
			"isDeleted": false,
			"id": "96vzFljbGtIyMbpoSHImy",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -452.0133424934917,
			"y": -564.7633257495918,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 93.9178487364909,
			"height": 0.6691154045886378,
			"seed": 490003436,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"type": "text",
					"id": "gYyRJpnt"
				}
			],
			"updated": 1691800161006,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "rP4lPyCsqZMIQchRDMiwf",
				"gap": 3.207330185005739,
				"focus": 0.3138109362376855
			},
			"endBinding": {
				"elementId": "5M4bcqUiLbfRY8F7dEHO1",
				"gap": 1.2379667978556603,
				"focus": -0.09153772014920644
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
					93.9178487364909,
					-0.6691154045886378
				]
			]
		},
		{
			"type": "text",
			"version": 164,
			"versionNonce": 2035803558,
			"isDeleted": false,
			"id": "gYyRJpnt",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -441.49256002022054,
			"y": -582.7288817564557,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.4199981689453125,
			"height": 25,
			"seed": 1708597204,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1691799689178,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "1",
			"rawText": "1",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "96vzFljbGtIyMbpoSHImy",
			"originalText": "1",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "arrow",
			"version": 1098,
			"versionNonce": 2069608870,
			"isDeleted": false,
			"id": "clRVOV052M2zJmGSwRPzp",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -442.91902168414975,
			"y": -495.3172039487139,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 86.20995291524252,
			"height": 56.30514408279316,
			"seed": 595605868,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"type": "text",
					"id": "HCZFTySI"
				}
			],
			"updated": 1691800161006,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "oRZ55M-x48aY9QZh0aLKJ",
				"gap": 2.3349683955598883,
				"focus": -0.23586087308975012
			},
			"endBinding": {
				"elementId": "5M4bcqUiLbfRY8F7dEHO1",
				"gap": 3.4537300797052684,
				"focus": -0.04527490257321932
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
					86.20995291524252,
					-56.30514408279316
				]
			]
		},
		{
			"type": "text",
			"version": 164,
			"versionNonce": 1037582566,
			"isDeleted": false,
			"id": "HCZFTySI",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -441.0680183537164,
			"y": -546.7366669480416,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 13.6199951171875,
			"height": 25,
			"seed": 46681940,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1691799689178,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "3",
			"rawText": "3",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "clRVOV052M2zJmGSwRPzp",
			"originalText": "3",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "arrow",
			"version": 1170,
			"versionNonce": 1742124710,
			"isDeleted": false,
			"id": "77-bpmY0rV773FwGT-h9a",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -437.8133603782642,
			"y": -393.1379195564633,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 219.52643168936012,
			"height": 24.752809125046724,
			"seed": 87562324,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"type": "text",
					"id": "4m4u7EME"
				}
			],
			"updated": 1691800161010,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "hySP6iaejUyzn_PKm6fN0",
				"gap": 4.109592177780801,
				"focus": -0.5366624586439717
			},
			"endBinding": {
				"elementId": "whYN5RrC1cwmBeBf2mvWY",
				"gap": 5.803844353008936,
				"focus": 0.2364112122561793
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
					219.52643168936012,
					24.752809125046724
				]
			]
		},
		{
			"type": "text",
			"version": 164,
			"versionNonce": 539702310,
			"isDeleted": false,
			"id": "4m4u7EME",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -382.96348208841823,
			"y": -415.71545967238245,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 19.17999267578125,
			"height": 25,
			"seed": 982516820,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1691799689178,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "10",
			"rawText": "10",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "77-bpmY0rV773FwGT-h9a",
			"originalText": "10",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "arrow",
			"version": 864,
			"versionNonce": 1442518138,
			"isDeleted": false,
			"id": "7w-EBIWMTyTQiOAduSeox",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -337.74357291701705,
			"y": -540.4999356780512,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 21.80817485935694,
			"height": 60.25197539526721,
			"seed": 729651052,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"type": "text",
					"id": "tuALPCWh"
				}
			],
			"updated": 1691800161008,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": {
				"elementId": "E0s7j1lh00Arhhc_fz878",
				"gap": 4.780654468658933,
				"focus": -0.20952846272833753
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
					21.80817485935694,
					60.25197539526721
				]
			]
		},
		{
			"type": "text",
			"version": 163,
			"versionNonce": 2050867046,
			"isDeleted": false,
			"id": "tuALPCWh",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -377.91575007750805,
			"y": -535.243711673054,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 13.6199951171875,
			"height": 25,
			"seed": 649113964,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1691799689178,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "3",
			"rawText": "3",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "7w-EBIWMTyTQiOAduSeox",
			"originalText": "3",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "arrow",
			"version": 939,
			"versionNonce": 1308766310,
			"isDeleted": false,
			"id": "r9fiZK8MD2iQNB8OnMp5B",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -305.95978150606584,
			"y": -570.4202881657518,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 105.24033908150682,
			"height": 25.807151879599587,
			"seed": 112681428,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"type": "text",
					"id": "2t3rRll8"
				}
			],
			"updated": 1691800161012,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "5M4bcqUiLbfRY8F7dEHO1",
				"gap": 4.060883899680048,
				"focus": -0.29467046008494374
			},
			"endBinding": {
				"elementId": "XHUEwoA--O0mtUggFtx0E",
				"gap": 1.0174191196394333,
				"focus": 0.084917787415053
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
					105.24033908150682,
					25.807151879599587
				]
			]
		},
		{
			"type": "text",
			"version": 163,
			"versionNonce": 1616700070,
			"isDeleted": false,
			"id": "2t3rRll8",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -310.30223373357916,
			"y": -576.1795442076522,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.4199981689453125,
			"height": 25,
			"seed": 2108725484,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1691799689179,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "1",
			"rawText": "1",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "r9fiZK8MD2iQNB8OnMp5B",
			"originalText": "1",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "arrow",
			"version": 1150,
			"versionNonce": 74134438,
			"isDeleted": false,
			"id": "5xYwwyyE2SvUncyGqY6H1",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -156.31654824340146,
			"y": -504.62244730967404,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.96022667539475,
			"height": 121.51032122493893,
			"seed": 1146964820,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"type": "text",
					"id": "H0gvUNym"
				}
			],
			"updated": 1691800161012,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "XHUEwoA--O0mtUggFtx0E",
				"gap": 1.3086019276151342,
				"focus": -0.23851776265475738
			},
			"endBinding": {
				"elementId": "whYN5RrC1cwmBeBf2mvWY",
				"gap": 1.1424827794091599,
				"focus": 0.5059015626026918
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
					7.96022667539475,
					121.51032122493893
				]
			]
		},
		{
			"type": "text",
			"version": 249,
			"versionNonce": 1429577190,
			"isDeleted": false,
			"id": "H0gvUNym",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -228.50842965814695,
			"y": -469.53135330579653,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 12.3599853515625,
			"height": 25,
			"seed": 1687138412,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1691799689179,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "5",
			"rawText": "5",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "5xYwwyyE2SvUncyGqY6H1",
			"originalText": "5",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "arrow",
			"version": 1114,
			"versionNonce": 1743373606,
			"isDeleted": false,
			"id": "JuvlYgOE6HCuRgKtXYT60",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -280.2181565891161,
			"y": -426.09661014564153,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 66.85700090080732,
			"height": 50.64243227984133,
			"seed": 1402453996,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"type": "text",
					"id": "fUFCOWcq"
				}
			],
			"updated": 1691800161011,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "E0s7j1lh00Arhhc_fz878",
				"gap": 6.015230222689211,
				"focus": 0.3217063334587955
			},
			"endBinding": {
				"elementId": "whYN5RrC1cwmBeBf2mvWY",
				"gap": 6.1120089989567745,
				"focus": -0.2921755687378067
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
					66.85700090080732,
					50.64243227984133
				]
			]
		},
		{
			"type": "text",
			"version": 163,
			"versionNonce": 2111107366,
			"isDeleted": false,
			"id": "fUFCOWcq",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -310.7581796689484,
			"y": -432.873142799431,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 14.239990234375,
			"height": 25,
			"seed": 1708552812,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1691799689179,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "2",
			"rawText": "2",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "JuvlYgOE6HCuRgKtXYT60",
			"originalText": "2",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "arrow",
			"version": 801,
			"versionNonce": 1096946534,
			"isDeleted": false,
			"id": "O7rF3xAlIxi0AIoiXz9CB",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -271.8942494341743,
			"y": -457.1842058051276,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 80.29262375077279,
			"height": 56.0473522198046,
			"seed": 266823508,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"type": "text",
					"id": "0Fzvo73W"
				}
			],
			"updated": 1691800161009,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "E0s7j1lh00Arhhc_fz878",
				"gap": 4.1500026479586625,
				"focus": 0.44394565832008226
			},
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					80.29262375077279,
					-56.0473522198046
				]
			]
		},
		{
			"type": "text",
			"version": 163,
			"versionNonce": 1437064294,
			"isDeleted": false,
			"id": "0Fzvo73W",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -291.64841558593633,
			"y": -513.5085425712035,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.4199981689453125,
			"height": 25,
			"seed": 641858028,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1691799689179,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "1",
			"rawText": "1",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "O7rF3xAlIxi0AIoiXz9CB",
			"originalText": "1",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "text",
			"version": 433,
			"versionNonce": 513737978,
			"isDeleted": false,
			"id": "Avgqlglr",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -112.39998590378525,
			"y": -550.3899067470005,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 279.1997985839844,
			"height": 200,
			"seed": 806593108,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1691799689179,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Grafo= {'A':{'B':2,'C':1,'D':5},\n        'B':{'E':1},\n        'C':{'E':3},\n        'D':{'FIN':10},\n        'E':{'G':1,'H':3}\n        'G':{'FIN':5}\n        'H':{'FIN':2,'G':1}\n        'FIN':{}}",
			"rawText": "Grafo= {'A':{'B':2,'C':1,'D':5},\n        'B':{'E':1},\n        'C':{'E':3},\n        'D':{'FIN':10},\n        'E':{'G':1,'H':3}\n        'G':{'FIN':5}\n        'H':{'FIN':2,'G':1}\n        'FIN':{}}",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Grafo= {'A':{'B':2,'C':1,'D':5},\n        'B':{'E':1},\n        'C':{'E':3},\n        'D':{'FIN':10},\n        'E':{'G':1,'H':3}\n        'G':{'FIN':5}\n        'H':{'FIN':2,'G':1}\n        'FIN':{}}",
			"lineHeight": 1.25,
			"baseline": 193
		},
		{
			"type": "text",
			"version": 496,
			"versionNonce": 1652252582,
			"isDeleted": false,
			"id": "roh3Gscz",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 229.0761268252419,
			"y": -554.1708501180012,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 112.109375,
			"height": 230,
			"seed": 1206044884,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1691799689179,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 2,
			"text": "Costs={\n        'A': inf,\n        'B':2,\n        'C':1,\n        'D':5,\n        'E':inf,\n        'G':inf,\n        'H':inf,\n        'Fin': inf\n        }",
			"rawText": "Costs={\n        'A': inf,\n        'B':2,\n        'C':1,\n        'D':5,\n        'E':inf,\n        'G':inf,\n        'H':inf,\n        'Fin': inf\n        }",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Costs={\n        'A': inf,\n        'B':2,\n        'C':1,\n        'D':5,\n        'E':inf,\n        'G':inf,\n        'H':inf,\n        'Fin': inf\n        }",
			"lineHeight": 1.15,
			"baseline": 225
		},
		{
			"type": "text",
			"version": 319,
			"versionNonce": 489182650,
			"isDeleted": false,
			"id": "84uFBHOc",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 515.6000526064918,
			"y": -560.3041465395972,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 157.705078125,
			"height": 207,
			"seed": 358310100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1691799689179,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 2,
			"text": "parent={\n        'A': none,\n        'B': 'A',\n        'C':'A',\n        'D':'A',\n        'E':none,\n        'G':none,\n        'H':none,\n        'Fin': none    ",
			"rawText": "parent={\n        'A': none,\n        'B': 'A',\n        'C':'A',\n        'D':'A',\n        'E':none,\n        'G':none,\n        'H':none,\n        'Fin': none    ",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "parent={\n        'A': none,\n        'B': 'A',\n        'C':'A',\n        'D':'A',\n        'E':none,\n        'G':none,\n        'H':none,\n        'Fin': none    ",
			"lineHeight": 1.15,
			"baseline": 202
		},
		{
			"type": "text",
			"version": 97,
			"versionNonce": 1752988390,
			"isDeleted": false,
			"id": "nCsQkqIY",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 5.548183597278572,
			"x": -686.007206871396,
			"y": -532.6493751889182,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 55.39994812011719,
			"height": 25,
			"seed": 1883062612,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1691799689179,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "start",
			"rawText": "start",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "start",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "text",
			"version": 113,
			"versionNonce": 1204391546,
			"isDeleted": false,
			"id": "9MsibdHM",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -602.3881563459125,
			"y": -273.7922730218796,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 307.9296875,
			"height": 23,
			"seed": 400327764,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1691799689179,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 2,
			"text": "find lowest_cost_node: C,B,E,G,D ",
			"rawText": "find lowest_cost_node: C,B,E,G,D ",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "find lowest_cost_node: C,B,E,G,D ",
			"lineHeight": 1.15,
			"baseline": 18
		},
		{
			"type": "text",
			"version": 177,
			"versionNonce": 506998310,
			"isDeleted": false,
			"id": "4wppy0Kq",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -581.7024234590076,
			"y": -208.2684169950939,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 581.25,
			"height": 19.2,
			"seed": 602624596,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "J96ONNTtT4iHfJkN-sDwH",
					"type": "arrow"
				}
			],
			"updated": 1691799689179,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 3,
			"text": "c | cost['c']:1|  G['C']:{'E':3} | ['E']           | 'E'    | ",
			"rawText": "c | cost['c']:1|  G['C']:{'E':3} | ['E']           | 'E'    | ",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "c | cost['c']:1|  G['C']:{'E':3} | ['E']           | 'E'    | ",
			"lineHeight": 1.2,
			"baseline": 15
		},
		{
			"type": "text",
			"version": 113,
			"versionNonce": 591769402,
			"isDeleted": false,
			"id": "mpQPDfHW",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -608.22743334089,
			"y": -226.36371321905222,
			"strokeColor": "#c2255c",
			"backgroundColor": "transparent",
			"width": 56.25,
			"height": 19.2,
			"seed": 253891692,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1691799689179,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 3,
			"text": "node |",
			"rawText": "node |",
			"textAlign": "center",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "node |",
			"lineHeight": 1.2,
			"baseline": 15
		},
		{
			"type": "text",
			"version": 115,
			"versionNonce": 1620801894,
			"isDeleted": false,
			"id": "0X2xGOQS",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -486.13222721644814,
			"y": -227.88747042701357,
			"strokeColor": "#c2255c",
			"backgroundColor": "transparent",
			"width": 56.25,
			"height": 19.2,
			"seed": 565569644,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1691799689179,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 3,
			"text": "cost |",
			"rawText": "cost |",
			"textAlign": "center",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "cost |",
			"lineHeight": 1.2,
			"baseline": 15
		},
		{
			"type": "text",
			"version": 147,
			"versionNonce": 603961338,
			"isDeleted": false,
			"id": "dCUyj71N",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -374.25721268426804,
			"y": -231.12558891659694,
			"strokeColor": "#c2255c",
			"backgroundColor": "transparent",
			"width": 112.5,
			"height": 19.2,
			"seed": 1578089836,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1691799689179,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 3,
			"text": "neighbours |",
			"rawText": "neighbours |",
			"textAlign": "center",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "neighbours |",
			"lineHeight": 1.2,
			"baseline": 15
		},
		{
			"type": "text",
			"version": 130,
			"versionNonce": 1727224998,
			"isDeleted": false,
			"id": "51FM39Xd",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -252.55177416120256,
			"y": -227.8874704270135,
			"strokeColor": "#c2255c",
			"backgroundColor": "transparent",
			"width": 159.375,
			"height": 19.2,
			"seed": 867717740,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1691799689179,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 3,
			"text": "neighbours.keys |",
			"rawText": "neighbours.keys |",
			"textAlign": "center",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "neighbours.keys |",
			"lineHeight": 1.2,
			"baseline": 15
		},
		{
			"type": "text",
			"version": 52,
			"versionNonce": 972728506,
			"isDeleted": false,
			"id": "cQtNyBZ6",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -75.45658256894058,
			"y": -230.55415453229637,
			"strokeColor": "#c2255c",
			"backgroundColor": "transparent",
			"width": 9.375,
			"height": 19.2,
			"seed": 1406813524,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "J96ONNTtT4iHfJkN-sDwH",
					"type": "arrow"
				}
			],
			"updated": 1691799689179,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 3,
			"text": "n",
			"rawText": "n",
			"textAlign": "center",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "n",
			"lineHeight": 1.2,
			"baseline": 15
		},
		{
			"id": "U2fGi_VxxRWhQUNMNZgWk",
			"type": "image",
			"x": 540.6545852532522,
			"y": -329.75246561909773,
			"width": 335.74808075928604,
			"height": 215.4000244140625,
			"angle": 0,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 334473210,
			"version": 350,
			"versionNonce": 1995233254,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689179,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "7c13b1cb2d9cb220911191bebb79cbd5c53394e6",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "j0eahz8h",
			"type": "text",
			"x": -43.574368199756236,
			"y": -253.41388200161106,
			"width": 28.125,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#c2255c",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1856018234,
			"version": 77,
			"versionNonce": 1557758330,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "J96ONNTtT4iHfJkN-sDwH",
					"type": "arrow"
				}
			],
			"updated": 1691799689179,
			"link": null,
			"locked": false,
			"text": "for",
			"rawText": "for",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "for",
			"lineHeight": 1.2
		},
		{
			"id": "J96ONNTtT4iHfJkN-sDwH",
			"type": "arrow",
			"x": -44.574368199756236,
			"y": -236.66053381278255,
			"width": 19.055147058823422,
			"height": 8.59598154239211,
			"angle": 0,
			"strokeColor": "#c2255c",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 1864576826,
			"version": 61,
			"versionNonce": 412412710,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689179,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-19.055147058823422,
					8.59598154239211
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "j0eahz8h",
				"focus": -0.019917021059222228,
				"gap": 1
			},
			"endBinding": {
				"elementId": "cQtNyBZ6",
				"focus": -0.3320359494391013,
				"gap": 2.452067310360917
			},
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "70I4HrlN",
			"type": "text",
			"x": -12.892767068092553,
			"y": -231.28961756500144,
			"width": 93.75,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#c2255c",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 638399782,
			"version": 43,
			"versionNonce": 400507450,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "Pwu3SeQbZoguqp_33YaNW",
					"type": "arrow"
				}
			],
			"updated": 1691799689179,
			"link": null,
			"locked": false,
			"text": "| new_cost",
			"rawText": "| new_cost",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "| new_cost",
			"lineHeight": 1.2
		},
		{
			"id": "ooqZ2vr0",
			"type": "text",
			"x": 116.9196718967512,
			"y": -229.28961756500144,
			"width": 178.125,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#c2255c",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1290954278,
			"version": 93,
			"versionNonce": 1247319654,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689179,
			"link": null,
			"locked": false,
			"text": "| cost[n]>new_cost?",
			"rawText": "| cost[n]>new_cost?",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "| cost[n]>new_cost?",
			"lineHeight": 1.2
		},
		{
			"id": "CyCeVDX1",
			"type": "text",
			"x": 306.2197207248762,
			"y": -230.0896358755483,
			"width": 103.125,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#c2255c",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1204121702,
			"version": 73,
			"versionNonce": 367979258,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689179,
			"link": null,
			"locked": false,
			"text": "| cost['n']",
			"rawText": "| cost['n']",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "| cost['n']",
			"lineHeight": 1.2
		},
		{
			"id": "EvnVlCMs",
			"type": "text",
			"x": 424.5572451389387,
			"y": -232.08960535797019,
			"width": 131.25,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#c2255c",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1657498598,
			"version": 125,
			"versionNonce": 889510310,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689180,
			"link": null,
			"locked": false,
			"text": "| parents['n']",
			"rawText": "| parents['n']",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "| parents['n']",
			"lineHeight": 1.2
		},
		{
			"id": "njkDVkUO",
			"type": "text",
			"x": 567.3421572483137,
			"y": -103.53045712324948,
			"width": 245.15670776367188,
			"height": 31.64086397231057,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 295610874,
			"version": 141,
			"versionNonce": 764115898,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689180,
			"link": null,
			"locked": false,
			"text": "El método .keys() devuelve una vista \niterable de las claves en el diccionario.",
			"rawText": "El método .keys() devuelve una vista \niterable de las claves en el diccionario.",
			"fontSize": 12.656345588924228,
			"fontFamily": 1,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 26,
			"containerId": null,
			"originalText": "El método .keys() devuelve una vista \niterable de las claves en el diccionario.",
			"lineHeight": 1.25
		},
		{
			"id": "13wj70hQ",
			"type": "text",
			"x": 536.390085104759,
			"y": -70.39387418164887,
			"width": 338.3756408691406,
			"height": 71.90436647992865,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1718506598,
			"version": 133,
			"versionNonce": 1606857958,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689180,
			"link": null,
			"locked": false,
			"text": "Dentro del bucle for, se calcula el nuevo costo \npara llegar al nodo vecino \nn desde el nodo actual node. Se suma el costo acumulado \nhasta el nodo actual (cost) con el costo de \nla arista que conecta node con n",
			"rawText": "Dentro del bucle for, se calcula el nuevo costo \npara llegar al nodo vecino \nn desde el nodo actual node. Se suma el costo acumulado \nhasta el nodo actual (cost) con el costo de \nla arista que conecta node con n",
			"fontSize": 11.504698636788584,
			"fontFamily": 1,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 67,
			"containerId": null,
			"originalText": "Dentro del bucle for, se calcula el nuevo costo \npara llegar al nodo vecino \nn desde el nodo actual node. Se suma el costo acumulado \nhasta el nodo actual (cost) con el costo de \nla arista que conecta node con n",
			"lineHeight": 1.25
		},
		{
			"id": "ggOqmX0h",
			"type": "text",
			"x": -67.33102237815115,
			"y": -294.0896053579702,
			"width": 99.328125,
			"height": 15.650131944444446,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1620666982,
			"version": 204,
			"versionNonce": 1826092154,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "Pwu3SeQbZoguqp_33YaNW",
					"type": "arrow"
				},
				{
					"id": "axyqDG4VI_SHuIwTB79S4",
					"type": "arrow"
				}
			],
			"updated": 1691799689180,
			"link": null,
			"locked": false,
			"text": "neighbours[n]",
			"rawText": "neighbours[n]",
			"fontSize": 13.041776620370372,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 12,
			"containerId": null,
			"originalText": "neighbours[n]",
			"lineHeight": 1.2
		},
		{
			"id": "Pwu3SeQbZoguqp_33YaNW",
			"type": "arrow",
			"x": -57.58243398561578,
			"y": -277.28961756500144,
			"width": 78.74106619841015,
			"height": 40,
			"angle": 0,
			"strokeColor": "#c2255c",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 149678970,
			"version": 289,
			"versionNonce": 1680549926,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689180,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					78.74106619841015,
					40
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "ggOqmX0h",
				"focus": 0.8818367495024151,
				"gap": 1.1498558485243109
			},
			"endBinding": {
				"elementId": "70I4HrlN",
				"focus": 0.27192699567168654,
				"gap": 6
			},
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "jOgTvyCI",
			"type": "text",
			"x": 18.744623068626197,
			"y": -205.28955652984519,
			"width": 46.875,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 214432422,
			"version": 54,
			"versionNonce": 630674746,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689180,
			"link": null,
			"locked": false,
			"text": "1+3=4",
			"rawText": "1+3=4",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "1+3=4",
			"lineHeight": 1.2
		},
		{
			"id": "UB2CwQo6",
			"type": "text",
			"x": 15.493156089475008,
			"y": -279.6896114614858,
			"width": 10.205062866210938,
			"height": 11.199987792968754,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1691098150,
			"version": 107,
			"versionNonce": 572470118,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689180,
			"link": null,
			"locked": false,
			"text": "'E'",
			"rawText": "'E'",
			"fontSize": 9.73911981997283,
			"fontFamily": 2,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 9,
			"containerId": null,
			"originalText": "'E'",
			"lineHeight": 1.15
		},
		{
			"id": "EEfSKSU7M6d3SoUagklaE",
			"type": "ellipse",
			"x": -310.61786472434255,
			"y": -214.88962366851706,
			"width": 31.199951171874986,
			"height": 39.200012207031264,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 650170810,
			"version": 95,
			"versionNonce": 2032967162,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "axyqDG4VI_SHuIwTB79S4",
					"type": "arrow"
				}
			],
			"updated": 1691799689180,
			"link": null,
			"locked": false
		},
		{
			"id": "axyqDG4VI_SHuIwTB79S4",
			"type": "arrow",
			"x": -13.356121177459016,
			"y": -277.66645108902117,
			"width": 262.0969993356896,
			"height": 66.90722777328608,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 50,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 623702566,
			"version": 407,
			"versionNonce": 1945097894,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689180,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-262.0969993356896,
					66.90722777328608
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "ggOqmX0h",
				"focus": -0.4730273142246329,
				"gap": 1
			},
			"endBinding": {
				"elementId": "EEfSKSU7M6d3SoUagklaE",
				"focus": -0.5237464660227359,
				"gap": 7.988314100472557
			},
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "n3Jonft4",
			"type": "text",
			"x": -99.56159031028005,
			"y": -292.0636925650015,
			"width": 31.669921875,
			"height": 12.974075,
			"angle": 0,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 2129063718,
			"version": 71,
			"versionNonce": 1687867066,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "1y6cA95WuBh8G1SeUa3Mf",
					"type": "arrow"
				}
			],
			"updated": 1691799689180,
			"link": null,
			"locked": false,
			"text": "cost+",
			"rawText": "cost+",
			"fontSize": 10.811729166666666,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 10,
			"containerId": null,
			"originalText": "cost+",
			"lineHeight": 1.2
		},
		{
			"id": "Hnv_H-4WaBilEZblmdOTK",
			"type": "ellipse",
			"x": -463.4178525173113,
			"y": -213.28961756500144,
			"width": 32.79998779296874,
			"height": 38.39999389648438,
			"angle": 0,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 594424506,
			"version": 87,
			"versionNonce": 1649021414,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "1y6cA95WuBh8G1SeUa3Mf",
					"type": "arrow"
				}
			],
			"updated": 1691799689180,
			"link": null,
			"locked": false
		},
		{
			"id": "1y6cA95WuBh8G1SeUa3Mf",
			"type": "arrow",
			"x": -110.82528037788953,
			"y": -277.2880817533201,
			"width": 324.3774386274638,
			"height": 60.4704873724873,
			"angle": 0,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 50,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 909486202,
			"version": 205,
			"versionNonce": 1283778426,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689182,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-324.3774386274638,
					60.4704873724873
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "n3Jonft4",
				"focus": -0.3428548868980955,
				"gap": 11.263690067609474
			},
			"endBinding": {
				"elementId": "Hnv_H-4WaBilEZblmdOTK",
				"focus": -1.0557306345084416,
				"gap": 7.082371850708498
			},
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "Hmw7m61Y",
			"type": "text",
			"x": 183.5445498264387,
			"y": -203.28967860015769,
			"width": 46.875,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1440335846,
			"version": 55,
			"versionNonce": 1480254758,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689182,
			"link": null,
			"locked": false,
			"text": "inf>4",
			"rawText": "inf>4",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "inf>4",
			"lineHeight": 1.2
		},
		{
			"id": "eDGNKUAQn8s135xQddE0k",
			"type": "freedraw",
			"x": 250.98211086159495,
			"y": -192.68964197906394,
			"width": 25.60003662109375,
			"height": 22.4000244140625,
			"angle": 0,
			"strokeColor": "#0c8599",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 895531962,
			"version": 26,
			"versionNonce": 154003514,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689182,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.60003662109375
				],
				[
					0.800048828125,
					4
				],
				[
					1.60003662109375,
					6.4000244140625
				],
				[
					2.4000244140625,
					8.800048828125
				],
				[
					4,
					10.4000244140625
				],
				[
					4,
					9.60003662109375
				],
				[
					7.20001220703125,
					4.800048828125
				],
				[
					12.800048828125,
					0.800048828125
				],
				[
					18.4000244140625,
					-4.79998779296875
				],
				[
					23.20001220703125,
					-9.5999755859375
				],
				[
					24.800048828125,
					-12
				],
				[
					25.60003662109375,
					-12
				],
				[
					25.60003662109375,
					-12
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				25.60003662109375,
				-12
			]
		},
		{
			"id": "XAU1uoQZ",
			"type": "text",
			"x": 375.91948879128245,
			"y": -241.13597531239728,
			"width": 18.509765625,
			"height": 12.646333333333333,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 596867878,
			"version": 76,
			"versionNonce": 1462718566,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689182,
			"link": null,
			"locked": false,
			"text": "'E'",
			"rawText": "'E'",
			"fontSize": 10.538611111111111,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 10,
			"containerId": null,
			"originalText": "'E'",
			"lineHeight": 1.2
		},
		{
			"id": "ilaqaDOF",
			"type": "text",
			"x": 366.29461086159495,
			"y": -202.28961756500144,
			"width": 9.375,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1492999462,
			"version": 15,
			"versionNonce": 1920520442,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689182,
			"link": null,
			"locked": false,
			"text": "4",
			"rawText": "4",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "4",
			"lineHeight": 1.2
		},
		{
			"id": "AxKlzdNm",
			"type": "text",
			"x": 524.2946466243818,
			"y": -248.08954432281394,
			"width": 18.73828125,
			"height": 12.799975585937476,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 65125542,
			"version": 50,
			"versionNonce": 720655270,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689182,
			"link": null,
			"locked": false,
			"text": "'E'",
			"rawText": "'E'",
			"fontSize": 10.666646321614564,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 10,
			"containerId": null,
			"originalText": "'E'",
			"lineHeight": 1.2
		},
		{
			"id": "A3wol8bu",
			"type": "text",
			"x": 476.71953761940745,
			"y": -205.28961756500144,
			"width": 28.125,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 2010993530,
			"version": 17,
			"versionNonce": 1810407866,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689182,
			"link": null,
			"locked": false,
			"text": "'C'",
			"rawText": "'C'",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "'C'",
			"lineHeight": 1.2
		},
		{
			"id": "SJpEwlMo",
			"type": "text",
			"x": -586.9178677761004,
			"y": 83.31048009124856,
			"width": 225,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#d0bfff",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 918891814,
			"version": 255,
			"versionNonce": 1838169018,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799994735,
			"link": null,
			"locked": false,
			"text": "Processed<-- C,B,E,G,D,H",
			"rawText": "Processed<-- C,B,E,G,D,H",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "Processed<-- C,B,E,G,D,H",
			"lineHeight": 1.2
		},
		{
			"type": "text",
			"version": 305,
			"versionNonce": 1889557114,
			"isDeleted": false,
			"id": "lpxpa6FG",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -579.8429013454363,
			"y": -173.48965418609515,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 581.25,
			"height": 19.2,
			"seed": 690060262,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1691799689182,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 3,
			"text": "B | cost['B']:2|  G['B']:{'E':1} | ['E']           | 'E'    | ",
			"rawText": "B | cost['B']:2|  G['B']:{'E':1} | ['E']           | 'E'    | ",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "B | cost['B']:2|  G['B']:{'E':1} | ['E']           | 'E'    | ",
			"lineHeight": 1.2,
			"baseline": 15
		},
		{
			"id": "V9xSkYgt",
			"type": "text",
			"x": 16.744623068626197,
			"y": -173.08954432281394,
			"width": 46.875,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 677625510,
			"version": 38,
			"versionNonce": 738468390,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689182,
			"link": null,
			"locked": false,
			"text": "2+1=3",
			"rawText": "2+1=3",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "2+1=3",
			"lineHeight": 1.2
		},
		{
			"id": "8VDmAz8X",
			"type": "text",
			"x": 192.91961086159495,
			"y": -175.08960535797019,
			"width": 28.125,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 2002897978,
			"version": 22,
			"versionNonce": 526580538,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689182,
			"link": null,
			"locked": false,
			"text": "4>3",
			"rawText": "4>3",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "4>3",
			"lineHeight": 1.2
		},
		{
			"id": "1B-c0h71MK0ba9gSniV6J",
			"type": "freedraw",
			"x": 246.1821230686262,
			"y": -167.88959315093894,
			"width": 24,
			"height": 20,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 456048250,
			"version": 22,
			"versionNonce": 952692070,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689182,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.79998779296875,
					3.20001220703125
				],
				[
					3.20001220703125,
					9.5999755859375
				],
				[
					4,
					10.39996337890625
				],
				[
					4,
					11.20001220703125
				],
				[
					7.20001220703125,
					8.79998779296875
				],
				[
					9.5999755859375,
					7.20001220703125
				],
				[
					12.79998779296875,
					2.39996337890625
				],
				[
					18.39996337890625,
					-3.20001220703125
				],
				[
					21.5999755859375,
					-7.20001220703125
				],
				[
					24,
					-8.79998779296875
				],
				[
					24,
					-8.79998779296875
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				24,
				-8.79998779296875
			]
		},
		{
			"id": "n7vNQtVN",
			"type": "text",
			"x": 367.89458644753245,
			"y": -175.88959315093894,
			"width": 9.375,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1144423654,
			"version": 33,
			"versionNonce": 1184072698,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689182,
			"link": null,
			"locked": false,
			"text": "3",
			"rawText": "3",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "3",
			"lineHeight": 1.2
		},
		{
			"id": "93npZS5I",
			"type": "text",
			"x": 476.31963527565745,
			"y": -176.08960535797019,
			"width": 28.125,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1758842362,
			"version": 44,
			"versionNonce": 1095913638,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689182,
			"link": null,
			"locked": false,
			"text": "'B'",
			"rawText": "'B'",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "'B'",
			"lineHeight": 1.2
		},
		{
			"id": "N8GZSO-aAlkhkWgv27DM6",
			"type": "freedraw",
			"x": 314.98211086159495,
			"y": -434.28961756500144,
			"width": 5.5999755859375,
			"height": 16.800018310546875,
			"angle": 0,
			"strokeColor": "#4dabf7",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 50,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1526804730,
			"version": 21,
			"versionNonce": 1882518714,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689182,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.600006103515625
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
					8.800018310546875
				],
				[
					-0.7999267578125,
					9.600006103515625
				],
				[
					-1.5999755859375,
					9.600006103515625
				],
				[
					-1.5999755859375,
					11.20001220703125
				],
				[
					-2.4000244140625,
					12.800018310546875
				],
				[
					-3.199951171875,
					12.800018310546875
				],
				[
					-3.199951171875,
					14.399993896484375
				],
				[
					-4,
					15.20001220703125
				],
				[
					-4.7999267578125,
					16
				],
				[
					-5.5999755859375,
					16.800018310546875
				],
				[
					-5.5999755859375,
					16.800018310546875
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				-5.5999755859375,
				16.800018310546875
			]
		},
		{
			"id": "TA7OL9Ef",
			"type": "text",
			"x": 338.09465968971995,
			"y": -437.4896297720327,
			"width": 9.375,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 744236986,
			"version": 45,
			"versionNonce": 290278374,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689182,
			"link": null,
			"locked": false,
			"text": "4",
			"rawText": "4",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "4",
			"lineHeight": 1.2
		},
		{
			"id": "tQRgSqZe",
			"type": "text",
			"x": 362.69463527565745,
			"y": -438.88962366851706,
			"width": 9.375,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 2010865318,
			"version": 47,
			"versionNonce": 1844071802,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689182,
			"link": null,
			"locked": false,
			"text": "3",
			"rawText": "3",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "3",
			"lineHeight": 1.2
		},
		{
			"id": "-R9p2WbGpbbX8_XNegraA",
			"type": "freedraw",
			"x": 342.98211086159495,
			"y": -439.88962366851706,
			"width": 1.5999755859375,
			"height": 26.399993896484375,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 40,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 550049126,
			"version": 93,
			"versionNonce": 1992744742,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689182,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					4.79998779296875
				],
				[
					-0.800048828125,
					6.399993896484375
				],
				[
					-0.800048828125,
					9.5999755859375
				],
				[
					-0.800048828125,
					12.79998779296875
				],
				[
					-0.800048828125,
					15.199981689453125
				],
				[
					-1.5999755859375,
					19.199981689453125
				],
				[
					-1.5999755859375,
					20
				],
				[
					-1.5999755859375,
					20.79998779296875
				],
				[
					-1.5999755859375,
					22.399993896484375
				],
				[
					-1.5999755859375,
					24.79998779296875
				],
				[
					-1.5999755859375,
					25.5999755859375
				],
				[
					-1.5999755859375,
					26.399993896484375
				],
				[
					-1.5999755859375,
					26.399993896484375
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				-1.5999755859375,
				26.399993896484375
			]
		},
		{
			"id": "KZPNB8-Nzt0u_9_-docgu",
			"type": "freedraw",
			"x": 626.1821841037824,
			"y": -439.0896053579702,
			"width": 24.800048828125,
			"height": 20,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 40,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1195115450,
			"version": 24,
			"versionNonce": 1693879866,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689182,
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
					-4,
					0.79998779296875
				],
				[
					-5.60009765625,
					1.600006103515625
				],
				[
					-11.2000732421875,
					4
				],
				[
					-12,
					4.79998779296875
				],
				[
					-13.60009765625,
					5.600006103515625
				],
				[
					-15.2000732421875,
					8
				],
				[
					-16,
					8.79998779296875
				],
				[
					-17.60009765625,
					9.600006103515625
				],
				[
					-17.60009765625,
					10.399993896484375
				],
				[
					-19.2000732421875,
					12
				],
				[
					-20.800048828125,
					12.79998779296875
				],
				[
					-21.60009765625,
					15.199981689453125
				],
				[
					-21.60009765625,
					16
				],
				[
					-23.2000732421875,
					18.399993896484375
				],
				[
					-23.2000732421875,
					19.199981689453125
				],
				[
					-24,
					20
				],
				[
					-24.800048828125,
					20
				],
				[
					-24.800048828125,
					20
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				-24.800048828125,
				20
			]
		},
		{
			"id": "YseYskhI",
			"type": "text",
			"x": 646.294610861595,
			"y": -443.88962366851706,
			"width": 9.375,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 777616570,
			"version": 58,
			"versionNonce": 1982597734,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689182,
			"link": null,
			"locked": false,
			"text": "C",
			"rawText": "C",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "C",
			"lineHeight": 1.2
		},
		{
			"id": "ysOFhobq",
			"type": "text",
			"x": 672.6943911350324,
			"y": -444.6896114614858,
			"width": 9.375,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 966334010,
			"version": 71,
			"versionNonce": 1513928442,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689182,
			"link": null,
			"locked": false,
			"text": "B",
			"rawText": "B",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "B",
			"lineHeight": 1.2
		},
		{
			"id": "JMkZOoiaPVjU2jPoroFBW",
			"type": "freedraw",
			"x": 654.1821841037824,
			"y": -443.88962366851706,
			"width": 3.2000732421875,
			"height": 21.600006103515625,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 40,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 2102041978,
			"version": 17,
			"versionNonce": 2118765990,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689182,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					3.20001220703125
				],
				[
					0,
					6.4000244140625
				],
				[
					-0.800048828125,
					8
				],
				[
					-0.800048828125,
					11.20001220703125
				],
				[
					-1.60009765625,
					12.800018310546875
				],
				[
					-1.60009765625,
					16
				],
				[
					-2.4000244140625,
					17.600006103515625
				],
				[
					-2.4000244140625,
					18.4000244140625
				],
				[
					-2.4000244140625,
					19.20001220703125
				],
				[
					-3.2000732421875,
					20
				],
				[
					-3.2000732421875,
					21.600006103515625
				],
				[
					-3.2000732421875,
					21.600006103515625
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				-3.2000732421875,
				21.600006103515625
			]
		},
		{
			"type": "text",
			"version": 472,
			"versionNonce": 1044367290,
			"isDeleted": false,
			"id": "UsDycXVO",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -581.2429410182879,
			"y": -143.88967860015765,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 534.375,
			"height": 38.4,
			"seed": 605391142,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1691799689183,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 3,
			"text": "E | cost['E']:3|  G['E']:{'G':1,'H':3} | ['G','H'] | 'G' \n                                                   | 'H'",
			"rawText": "E | cost['E']:3|  G['E']:{'G':1,'H':3} | ['G','H'] | 'G' \n                                                   | 'H'",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "E | cost['E']:3|  G['E']:{'G':1,'H':3} | ['G','H'] | 'G' \n                                                   | 'H'",
			"lineHeight": 1.2,
			"baseline": 34
		},
		{
			"id": "9dOVsYmX",
			"type": "text",
			"x": 16.344537619407447,
			"y": -145.88959315093894,
			"width": 46.875,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1131484262,
			"version": 38,
			"versionNonce": 474818790,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689183,
			"link": null,
			"locked": false,
			"text": "3+1=4",
			"rawText": "3+1=4",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "3+1=4",
			"lineHeight": 1.2
		},
		{
			"id": "NprbskNL",
			"type": "text",
			"x": 16.344537619407447,
			"y": -126.28961756500144,
			"width": 46.875,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1627414758,
			"version": 47,
			"versionNonce": 2032320634,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689183,
			"link": null,
			"locked": false,
			"text": "3+3=6",
			"rawText": "3+3=6",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "3+3=6",
			"lineHeight": 1.2
		},
		{
			"id": "VX8a2zHY",
			"type": "text",
			"x": 177.45708644753245,
			"y": -147.48969080718894,
			"width": 56.25,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 368536762,
			"version": 70,
			"versionNonce": 801315878,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689183,
			"link": null,
			"locked": false,
			"text": " inf>4",
			"rawText": " inf>4",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": " inf>4",
			"lineHeight": 1.2
		},
		{
			"id": "UeXF1SR8",
			"type": "text",
			"x": 180.5196474826887,
			"y": -253.28961756500144,
			"width": 16.119140625,
			"height": 11.008000000000001,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1353090662,
			"version": 259,
			"versionNonce": 1990762810,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689183,
			"link": null,
			"locked": false,
			"text": "'G'",
			"rawText": "'G'",
			"fontSize": 9.173333333333334,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 8,
			"containerId": null,
			"originalText": "'G'",
			"lineHeight": 1.2
		},
		{
			"type": "text",
			"version": 125,
			"versionNonce": 513320806,
			"isDeleted": false,
			"id": "EUgYkOLA",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 181.9272402561262,
			"y": -239.21279033518374,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 14.51953125,
			"height": 9.91343361119905,
			"seed": 902340538,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1691799689183,
			"link": null,
			"locked": false,
			"fontSize": 8.261194675999208,
			"fontFamily": 3,
			"text": "'E'",
			"rawText": "'E'",
			"textAlign": "center",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "'E'",
			"lineHeight": 1.2,
			"baseline": 8
		},
		{
			"id": "NiGtADlAJEfK-msy2HV7J",
			"type": "freedraw",
			"x": 251.7820986545637,
			"y": -142.28961756500144,
			"width": 22.39996337890625,
			"height": 20,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1103087718,
			"version": 19,
			"versionNonce": 842295802,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689183,
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
					1.5999755859375,
					4.79998779296875
				],
				[
					4.79998779296875,
					8.79998779296875
				],
				[
					4.79998779296875,
					9.5999755859375
				],
				[
					5.5999755859375,
					9.5999755859375
				],
				[
					8,
					7.20001220703125
				],
				[
					11.199951171875,
					3.20001220703125
				],
				[
					13.5999755859375,
					-0.79998779296875
				],
				[
					15.199951171875,
					-2.4000244140625
				],
				[
					17.5999755859375,
					-4.79998779296875
				],
				[
					19.199951171875,
					-7.20001220703125
				],
				[
					22.39996337890625,
					-10.4000244140625
				],
				[
					22.39996337890625,
					-10.4000244140625
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				22.39996337890625,
				-10.4000244140625
			]
		},
		{
			"id": "tTK41cKL",
			"type": "text",
			"x": 366.89458644753245,
			"y": -147.48962977203269,
			"width": 9.375,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 858235110,
			"version": 17,
			"versionNonce": 152750758,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689183,
			"link": null,
			"locked": false,
			"text": "4",
			"rawText": "4",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "4",
			"lineHeight": 1.2
		},
		{
			"id": "R5tNrPjZ",
			"type": "text",
			"x": 474.31963527565745,
			"y": -147.88965418609519,
			"width": 28.125,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1076830906,
			"version": 22,
			"versionNonce": 1120475834,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689183,
			"link": null,
			"locked": false,
			"text": "'E'",
			"rawText": "'E'",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "'E'",
			"lineHeight": 1.2
		},
		{
			"id": "nfMhdGYK",
			"type": "text",
			"x": 180.7195986545637,
			"y": -266.1515291860952,
			"width": 15.310546875,
			"height": 10.461874999999997,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1455537146,
			"version": 32,
			"versionNonce": 2113308134,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689183,
			"link": null,
			"locked": false,
			"text": "'H'",
			"rawText": "'H'",
			"fontSize": 8.718229166666665,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 8,
			"containerId": null,
			"originalText": "'H'",
			"lineHeight": 1.2
		},
		{
			"id": "dlxSJkfWz5Nc-6U9h1y4F",
			"type": "freedraw",
			"x": 331.78203761940745,
			"y": -404.68964197906394,
			"width": 29.5999755859375,
			"height": 1.600006103515625,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 706041274,
			"version": 17,
			"versionNonce": 1728689018,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689183,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-3.199951171875,
					0
				],
				[
					-8,
					-0.79998779296875
				],
				[
					-16,
					-0.79998779296875
				],
				[
					-22.39990234375,
					-1.600006103515625
				],
				[
					-23.199951171875,
					-1.600006103515625
				],
				[
					-24,
					-1.600006103515625
				],
				[
					-24.7999267578125,
					-1.600006103515625
				],
				[
					-26.39990234375,
					-0.79998779296875
				],
				[
					-27.199951171875,
					-0.79998779296875
				],
				[
					-28,
					-0.79998779296875
				],
				[
					-28.7999267578125,
					-0.79998779296875
				],
				[
					-29.5999755859375,
					-0.79998779296875
				],
				[
					-29.5999755859375,
					-0.79998779296875
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				-29.5999755859375,
				-0.79998779296875
			]
		},
		{
			"id": "ypnekGtH",
			"type": "text",
			"x": 338.89458644753245,
			"y": -412.28964808257956,
			"width": 9.375,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1361687782,
			"version": 13,
			"versionNonce": 775477542,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689183,
			"link": null,
			"locked": false,
			"text": "4",
			"rawText": "4",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "4",
			"lineHeight": 1.2
		},
		{
			"id": "nx1yK_mR81pE7Xt-38Ei7",
			"type": "freedraw",
			"x": 589.3821352756574,
			"y": -406.28964808257956,
			"width": 44,
			"height": 1.600006103515625,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 50,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 502094458,
			"version": 23,
			"versionNonce": 288961594,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689183,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7999267578125,
					0
				],
				[
					8,
					0
				],
				[
					11.199951171875,
					0.800018310546875
				],
				[
					12.7999267578125,
					1.600006103515625
				],
				[
					13.5999755859375,
					1.600006103515625
				],
				[
					14.39990234375,
					1.600006103515625
				],
				[
					22.39990234375,
					1.600006103515625
				],
				[
					24,
					1.600006103515625
				],
				[
					28.7999267578125,
					0.800018310546875
				],
				[
					32.7999267578125,
					0
				],
				[
					34.39990234375,
					0
				],
				[
					36.7999267578125,
					0
				],
				[
					37.5999755859375,
					0
				],
				[
					38.39990234375,
					0
				],
				[
					39.199951171875,
					0
				],
				[
					40,
					0
				],
				[
					40.7999267578125,
					0
				],
				[
					44,
					1.600006103515625
				],
				[
					44,
					1.600006103515625
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				44,
				1.600006103515625
			]
		},
		{
			"id": "0LzkYYvP",
			"type": "text",
			"x": 653.0945376194074,
			"y": -417.28964808257956,
			"width": 9.375,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 2075908390,
			"version": 34,
			"versionNonce": 558810214,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689183,
			"link": null,
			"locked": false,
			"text": "E",
			"rawText": "E",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "E",
			"lineHeight": 1.2
		},
		{
			"id": "UlymKvTe",
			"type": "text",
			"x": 187.34453761940745,
			"y": -127.88965418609519,
			"width": 46.875,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 844551910,
			"version": 28,
			"versionNonce": 1933221114,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689183,
			"link": null,
			"locked": false,
			"text": "inf>6",
			"rawText": "inf>6",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "inf>6",
			"lineHeight": 1.2
		},
		{
			"id": "UYc6_5aawxtHD5NQi1tEj",
			"type": "freedraw",
			"x": 252.58208644753245,
			"y": -123.08960535797019,
			"width": 19.20001220703125,
			"height": 19.20001220703125,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 973288698,
			"version": 16,
			"versionNonce": 1761953702,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689183,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					2.39996337890625
				],
				[
					0.79998779296875,
					5.5999755859375
				],
				[
					2.39996337890625,
					8
				],
				[
					3.20001220703125,
					9.5999755859375
				],
				[
					3.20001220703125,
					8.79998779296875
				],
				[
					4.79998779296875,
					6.39996337890625
				],
				[
					8,
					2.39996337890625
				],
				[
					12,
					-0.800048828125
				],
				[
					15.20001220703125,
					-3.20001220703125
				],
				[
					17.5999755859375,
					-6.4000244140625
				],
				[
					19.20001220703125,
					-9.60003662109375
				],
				[
					19.20001220703125,
					-9.60003662109375
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				19.20001220703125,
				-9.60003662109375
			]
		},
		{
			"id": "RgP8JEN8",
			"type": "text",
			"x": 366.89458644753245,
			"y": -129.28961756500144,
			"width": 9.375,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1433119142,
			"version": 26,
			"versionNonce": 177270202,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689183,
			"link": null,
			"locked": false,
			"text": "6",
			"rawText": "6",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "6",
			"lineHeight": 1.2
		},
		{
			"id": "KG1AHzMG",
			"type": "text",
			"x": 474.51946437721995,
			"y": -131.28961756500144,
			"width": 28.125,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 957738022,
			"version": 25,
			"versionNonce": 1435067110,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689183,
			"link": null,
			"locked": false,
			"text": "'E'",
			"rawText": "'E'",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "'E'",
			"lineHeight": 1.2
		},
		{
			"id": "eNRnuAudcEOzSP91cmp4B",
			"type": "freedraw",
			"x": 330.98211086159495,
			"y": -379.88962366851706,
			"width": 26.4000244140625,
			"height": 1.5999755859375,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 40,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 929024250,
			"version": 18,
			"versionNonce": 744433274,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689183,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-3.2000732421875,
					0
				],
				[
					-5.5999755859375,
					0
				],
				[
					-12.800048828125,
					0
				],
				[
					-13.5999755859375,
					0
				],
				[
					-16,
					0
				],
				[
					-17.5999755859375,
					0
				],
				[
					-19.2000732421875,
					0
				],
				[
					-20,
					0
				],
				[
					-21.5999755859375,
					0
				],
				[
					-22.4000244140625,
					0.79998779296875
				],
				[
					-24,
					1.5999755859375
				],
				[
					-24.800048828125,
					1.5999755859375
				],
				[
					-25.5999755859375,
					1.5999755859375
				],
				[
					-26.4000244140625,
					1.5999755859375
				],
				[
					-26.4000244140625,
					1.5999755859375
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				-26.4000244140625,
				1.5999755859375
			]
		},
		{
			"id": "mUuvQ8fJ",
			"type": "text",
			"x": 341.09465968971995,
			"y": -389.68964197906394,
			"width": 9.375,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1066971366,
			"version": 14,
			"versionNonce": 694687270,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689183,
			"link": null,
			"locked": false,
			"text": "6",
			"rawText": "6",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "6",
			"lineHeight": 1.2
		},
		{
			"id": "RvsTTnnKlNeJ_aGisCPdL",
			"type": "freedraw",
			"x": 593.3821352756574,
			"y": -384.68964197906394,
			"width": 36,
			"height": 4.79998779296875,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 40,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1636821350,
			"version": 27,
			"versionNonce": 292046650,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689183,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					4,
					-0.79998779296875
				],
				[
					8.7999267578125,
					-2.399993896484375
				],
				[
					13.5999755859375,
					-4
				],
				[
					14.39990234375,
					-4
				],
				[
					15.199951171875,
					-4.79998779296875
				],
				[
					16,
					-4.79998779296875
				],
				[
					18.39990234375,
					-4.79998779296875
				],
				[
					22.39990234375,
					-4.79998779296875
				],
				[
					23.199951171875,
					-4.79998779296875
				],
				[
					24,
					-4.79998779296875
				],
				[
					24.7999267578125,
					-4.79998779296875
				],
				[
					26.39990234375,
					-4
				],
				[
					28,
					-4
				],
				[
					28.7999267578125,
					-3.199981689453125
				],
				[
					29.5999755859375,
					-2.399993896484375
				],
				[
					30.39990234375,
					-2.399993896484375
				],
				[
					30.39990234375,
					-1.600006103515625
				],
				[
					31.199951171875,
					-1.600006103515625
				],
				[
					32,
					-1.600006103515625
				],
				[
					32.7999267578125,
					-1.600006103515625
				],
				[
					34.39990234375,
					-1.600006103515625
				],
				[
					35.199951171875,
					-0.79998779296875
				],
				[
					36,
					-0.79998779296875
				],
				[
					36,
					-0.79998779296875
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				36,
				-0.79998779296875
			]
		},
		{
			"id": "X8foqJku",
			"type": "text",
			"x": 653.294610861595,
			"y": -395.68964197906394,
			"width": 9.375,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 489119462,
			"version": 34,
			"versionNonce": 1301176678,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689183,
			"link": null,
			"locked": false,
			"text": "E",
			"rawText": "E",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "E",
			"lineHeight": 1.2
		},
		{
			"type": "text",
			"version": 443,
			"versionNonce": 1645170682,
			"isDeleted": false,
			"id": "fzPREI90",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -580.4429532253191,
			"y": -78.8897396353139,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 600,
			"height": 19.2,
			"seed": 718054330,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1691799689183,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 3,
			"text": "G | cost['G']:4|  G['G']:{'FIN':5}   | ['FIN']     | 'FIN'    | ",
			"rawText": "G | cost['G']:4|  G['G']:{'FIN':5}   | ['FIN']     | 'FIN'    | ",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "G | cost['G']:4|  G['G']:{'FIN':5}   | ['FIN']     | 'FIN'    | ",
			"lineHeight": 1.2,
			"baseline": 15
		},
		{
			"id": "dWWXK7oV",
			"type": "text",
			"x": 20.144586447532447,
			"y": -79.68964197906394,
			"width": 46.875,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1646255526,
			"version": 29,
			"versionNonce": 88687782,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689183,
			"link": null,
			"locked": false,
			"text": "4+5=9",
			"rawText": "4+5=9",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "4+5=9",
			"lineHeight": 1.2
		},
		{
			"id": "CiXMlIis",
			"type": "text",
			"x": 177.54461086159495,
			"y": -276.0896358755483,
			"width": 22.8515625,
			"height": 9.369624999999997,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 4007418,
			"version": 56,
			"versionNonce": 1113014458,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689183,
			"link": null,
			"locked": false,
			"text": "'FIN'",
			"rawText": "'FIN'",
			"fontSize": 7.808020833333332,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 7,
			"containerId": null,
			"originalText": "'FIN'",
			"lineHeight": 1.2
		},
		{
			"id": "LmSamxFe",
			"type": "text",
			"x": 186.74456203346995,
			"y": -81.48969080718894,
			"width": 46.875,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1887366842,
			"version": 22,
			"versionNonce": 574996454,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689183,
			"link": null,
			"locked": false,
			"text": "inf>9",
			"rawText": "inf>9",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "inf>9",
			"lineHeight": 1.2
		},
		{
			"id": "riTelecTirKnQt1qt6BTQ",
			"type": "freedraw",
			"x": 252.58208644753245,
			"y": -82.28961756500144,
			"width": 16,
			"height": 20,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 2029250490,
			"version": 17,
			"versionNonce": 1575164282,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689183,
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
					6.39996337890625
				],
				[
					0,
					7.20001220703125
				],
				[
					0.79998779296875,
					7.20001220703125
				],
				[
					0.79998779296875,
					8
				],
				[
					0.79998779296875,
					8.79998779296875
				],
				[
					2.39996337890625,
					7.20001220703125
				],
				[
					4.79998779296875,
					3.20001220703125
				],
				[
					6.39996337890625,
					-0.79998779296875
				],
				[
					10.39996337890625,
					-5.60003662109375
				],
				[
					12,
					-8
				],
				[
					14.39996337890625,
					-10.4000244140625
				],
				[
					16,
					-11.20001220703125
				],
				[
					16,
					-11.20001220703125
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				16,
				-11.20001220703125
			]
		},
		{
			"id": "rpRWqqr4",
			"type": "text",
			"x": 365.29448879128245,
			"y": -84.88959315093894,
			"width": 9.375,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1903117946,
			"version": 15,
			"versionNonce": 949015334,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689184,
			"link": null,
			"locked": false,
			"text": "9",
			"rawText": "9",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "9",
			"lineHeight": 1.2
		},
		{
			"id": "6QeWg2Jb",
			"type": "text",
			"x": 472.11956203346995,
			"y": -88.68964197906394,
			"width": 28.125,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1434042854,
			"version": 23,
			"versionNonce": 1945492026,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689184,
			"link": null,
			"locked": false,
			"text": "'G'",
			"rawText": "'G'",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "'G'",
			"lineHeight": 1.2
		},
		{
			"id": "gmwuX-SPsh6Aif3D0cSsh",
			"type": "freedraw",
			"x": 660.5820864475324,
			"y": -358.28964808257956,
			"width": 48,
			"height": 4.79998779296875,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 40,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1115667046,
			"version": 28,
			"versionNonce": 1385660006,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.800048828125,
					-0.79998779296875
				],
				[
					-8.800048828125,
					-0.79998779296875
				],
				[
					-11.199951171875,
					-0.79998779296875
				],
				[
					-16.800048828125,
					0
				],
				[
					-19.199951171875,
					0
				],
				[
					-27.199951171875,
					0
				],
				[
					-28.800048828125,
					0
				],
				[
					-29.5999755859375,
					0
				],
				[
					-30.4000244140625,
					0
				],
				[
					-32.800048828125,
					0
				],
				[
					-34.4000244140625,
					0
				],
				[
					-35.199951171875,
					0
				],
				[
					-36,
					0
				],
				[
					-37.5999755859375,
					0
				],
				[
					-39.199951171875,
					0
				],
				[
					-40.800048828125,
					-0.79998779296875
				],
				[
					-42.4000244140625,
					-0.79998779296875
				],
				[
					-42.4000244140625,
					-2.399993896484375
				],
				[
					-43.199951171875,
					-2.399993896484375
				],
				[
					-44.800048828125,
					-3.199981689453125
				],
				[
					-46.4000244140625,
					-4
				],
				[
					-46.4000244140625,
					-4.79998779296875
				],
				[
					-47.199951171875,
					-4.79998779296875
				],
				[
					-48,
					-4.79998779296875
				],
				[
					-48,
					-4.79998779296875
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				-48,
				-4.79998779296875
			]
		},
		{
			"id": "TrnAj99U",
			"type": "text",
			"x": 667.0945376194074,
			"y": -372.68964197906394,
			"width": 9.375,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1842768250,
			"version": 20,
			"versionNonce": 1668449018,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689184,
			"link": null,
			"locked": false,
			"text": "G",
			"rawText": "G",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "G",
			"lineHeight": 1.2
		},
		{
			"id": "XONagCu1fTGLjDqHOenB1",
			"type": "freedraw",
			"x": 321.38213527565745,
			"y": -355.0896358755483,
			"width": 24.7999267578125,
			"height": 0.79998779296875,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1428233274,
			"version": 15,
			"versionNonce": 623296934,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7999267578125,
					0
				],
				[
					1.5999755859375,
					0
				],
				[
					4.7999267578125,
					0
				],
				[
					5.5999755859375,
					0
				],
				[
					7.199951171875,
					0
				],
				[
					9.5999755859375,
					0
				],
				[
					12,
					0
				],
				[
					14.39990234375,
					0
				],
				[
					18.39990234375,
					0
				],
				[
					24,
					0
				],
				[
					24.7999267578125,
					-0.79998779296875
				],
				[
					24.7999267578125,
					-0.79998779296875
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				24.7999267578125,
				-0.79998779296875
			]
		},
		{
			"id": "8KTr1UgU",
			"type": "text",
			"x": 358.29461086159495,
			"y": -367.8896541860952,
			"width": 9.375,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1668661818,
			"version": 7,
			"versionNonce": 920392634,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689184,
			"link": null,
			"locked": false,
			"text": "9",
			"rawText": "9",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "9",
			"lineHeight": 1.2
		},
		{
			"type": "text",
			"version": 569,
			"versionNonce": 1131125990,
			"isDeleted": false,
			"id": "bjDW9YLB",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -580.4179288112566,
			"y": -40.68966639312643,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 590.625,
			"height": 19.2,
			"seed": 1095742522,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1691799689184,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 3,
			"text": "D | cost['D']:5|  G['D']:{'FIN':10} | ['FIN']     | 'FIN'    | ",
			"rawText": "D | cost['D']:5|  G['D']:{'FIN':10} | ['FIN']     | 'FIN'    | ",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "D | cost['D']:5|  G['D']:{'FIN':10} | ['FIN']     | 'FIN'    | ",
			"lineHeight": 1.2,
			"baseline": 15
		},
		{
			"id": "uKkzIGQ4",
			"type": "text",
			"x": 14.369562033469947,
			"y": -41.689641979063936,
			"width": 65.625,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1168906022,
			"version": 42,
			"versionNonce": 810912890,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689184,
			"link": null,
			"locked": false,
			"text": "5+10=15",
			"rawText": "5+10=15",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "5+10=15",
			"lineHeight": 1.2
		},
		{
			"id": "39eT9GA0",
			"type": "text",
			"x": 190.6320742405012,
			"y": -42.089605357970186,
			"width": 37.5,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1680060090,
			"version": 105,
			"versionNonce": 1391661094,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689184,
			"link": null,
			"locked": false,
			"text": "9>15",
			"rawText": "9>15",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "9>15",
			"lineHeight": 1.2
		},
		{
			"id": "_fo4QEoMzuPup7pF6ErJ7",
			"type": "freedraw",
			"x": 251.7820986545637,
			"y": -50.289617565001436,
			"width": 12,
			"height": 25.60003662109375,
			"angle": 0,
			"strokeColor": "#f02828",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 547056358,
			"version": 23,
			"versionNonce": 1436675386,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.60003662109375,
					8
				],
				[
					1.60003662109375,
					8.79998779296875
				],
				[
					8,
					19.20001220703125
				],
				[
					8.79998779296875,
					20
				],
				[
					11.20001220703125,
					25.60003662109375
				],
				[
					12,
					25.60003662109375
				],
				[
					12,
					24.79998779296875
				],
				[
					12,
					24
				],
				[
					12,
					24
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				12,
				24
			]
		},
		{
			"id": "izshtDmqcSOEK2YSnvX9T",
			"type": "freedraw",
			"x": 274.98211086159495,
			"y": -47.889654186095186,
			"width": 27.20001220703125,
			"height": 19.20001220703125,
			"angle": 0,
			"strokeColor": "#f02828",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1650283066,
			"version": 30,
			"versionNonce": 1068112742,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.60003662109375,
					0
				],
				[
					-3.20001220703125,
					0
				],
				[
					-10.4000244140625,
					3.20001220703125
				],
				[
					-12,
					4
				],
				[
					-15.20001220703125,
					7.20001220703125
				],
				[
					-16,
					8.800048828125
				],
				[
					-17.60003662109375,
					10.4000244140625
				],
				[
					-19.20001220703125,
					12
				],
				[
					-21.60003662109375,
					12.800048828125
				],
				[
					-24,
					15.20001220703125
				],
				[
					-24.800048828125,
					15.20001220703125
				],
				[
					-25.60003662109375,
					15.20001220703125
				],
				[
					-25.60003662109375,
					16
				],
				[
					-25.60003662109375,
					16.800048828125
				],
				[
					-26.4000244140625,
					16.800048828125
				],
				[
					-27.20001220703125,
					17.60003662109375
				],
				[
					-27.20001220703125,
					18.4000244140625
				],
				[
					-27.20001220703125,
					19.20001220703125
				],
				[
					-27.20001220703125,
					19.20001220703125
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				-27.20001220703125,
				19.20001220703125
			]
		},
		{
			"id": "frBDhDYHQ_WmuerK9vX_a",
			"type": "freedraw",
			"x": 371.78203761940745,
			"y": -47.089605357970186,
			"width": 12.7999267578125,
			"height": 17.5999755859375,
			"angle": 0,
			"strokeColor": "#fc0303",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1899088166,
			"version": 11,
			"versionNonce": 2082747898,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689184,
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
					-1.5999755859375,
					3.199951171875
				],
				[
					-2.39990234375,
					5.5999755859375
				],
				[
					-4.7999267578125,
					7.199951171875
				],
				[
					-11.199951171875,
					15.199951171875
				],
				[
					-12.7999267578125,
					16.79998779296875
				],
				[
					-12.7999267578125,
					17.5999755859375
				],
				[
					-12.7999267578125,
					17.5999755859375
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				-12.7999267578125,
				17.5999755859375
			]
		},
		{
			"id": "cRc7CTJ4CXUtFvYPr-Ps2",
			"type": "freedraw",
			"x": 491.78203761940745,
			"y": -51.089605357970186,
			"width": 4.7999267578125,
			"height": 24,
			"angle": 0,
			"strokeColor": "#fc0303",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1727091046,
			"version": 10,
			"versionNonce": 1876803238,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689184,
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
					-0.7999267578125,
					4
				],
				[
					-1.5999755859375,
					6.39996337890625
				],
				[
					-4,
					16.79998779296875
				],
				[
					-4,
					19.199951171875
				],
				[
					-4.7999267578125,
					24
				],
				[
					-4.7999267578125,
					24
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				-4.7999267578125,
				24
			]
		},
		{
			"type": "text",
			"version": 761,
			"versionNonce": 1423926970,
			"isDeleted": false,
			"id": "I55bZcIf",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -580.3304196559832,
			"y": -8.089629772032687,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 581.25,
			"height": 38.4,
			"seed": 361036326,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1691799689184,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 3,
			"text": "H | cost['H']:6|  G['H']:{'FIN':2,'G':1}| ['FIN','G']  | 'FIN'\n                                                          'G' ",
			"rawText": "H | cost['H']:6|  G['H']:{'FIN':2,'G':1}| ['FIN','G']  | 'FIN'\n                                                          'G' ",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "H | cost['H']:6|  G['H']:{'FIN':2,'G':1}| ['FIN','G']  | 'FIN'\n                                                          'G' ",
			"lineHeight": 1.2,
			"baseline": 34
		},
		{
			"id": "16juYYWB",
			"type": "text",
			"x": 23.744562033469947,
			"y": -10.089605357970186,
			"width": 46.875,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1234497594,
			"version": 23,
			"versionNonce": 2017130982,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689184,
			"link": null,
			"locked": false,
			"text": "6+2=8",
			"rawText": "6+2=8",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "6+2=8",
			"lineHeight": 1.2
		},
		{
			"id": "mAdh9dGY",
			"type": "text",
			"x": 24.544610861594947,
			"y": 9.110406849061064,
			"width": 46.875,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 2099593894,
			"version": 66,
			"versionNonce": 2021031802,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689184,
			"link": null,
			"locked": false,
			"text": "6+1=7",
			"rawText": "6+1=7",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "6+1=7",
			"lineHeight": 1.2
		},
		{
			"id": "aIjmgKaZ",
			"type": "text",
			"x": 195.11956203346995,
			"y": -10.689641979063936,
			"width": 28.125,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1721624378,
			"version": 10,
			"versionNonce": 1338952998,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689184,
			"link": null,
			"locked": false,
			"text": "9>8",
			"rawText": "9>8",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "9>8",
			"lineHeight": 1.2
		},
		{
			"id": "aqHAS4ib",
			"type": "text",
			"x": 194.51958644753245,
			"y": 7.710382434998564,
			"width": 28.125,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 101045754,
			"version": 33,
			"versionNonce": 67516518,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689184,
			"link": null,
			"locked": false,
			"text": "4>7",
			"rawText": "4>7",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "4>7",
			"lineHeight": 1.2
		},
		{
			"id": "v1rPOooCE-2uAUj37tUUP",
			"type": "freedraw",
			"x": 244.58208644753245,
			"y": -4.489629772032686,
			"width": 16.79998779296875,
			"height": 19.199951171875,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 674046246,
			"version": 17,
			"versionNonce": 1357146362,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.5999755859375
				],
				[
					0,
					5.5999755859375
				],
				[
					0.79998779296875,
					8
				],
				[
					1.5999755859375,
					8.79998779296875
				],
				[
					2.39996337890625,
					9.5999755859375
				],
				[
					2.39996337890625,
					8.79998779296875
				],
				[
					4,
					6.4000244140625
				],
				[
					4.79998779296875,
					3.20001220703125
				],
				[
					6.39996337890625,
					0.79998779296875
				],
				[
					8.79998779296875,
					-2.4000244140625
				],
				[
					12,
					-6.4000244140625
				],
				[
					16,
					-9.5999755859375
				],
				[
					16.79998779296875,
					-9.5999755859375
				],
				[
					16.79998779296875,
					-9.5999755859375
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				16.79998779296875,
				-9.5999755859375
			]
		},
		{
			"id": "M0uTfLYmXqngugG-gcaBp",
			"type": "freedraw",
			"x": 246.18206203346995,
			"y": 15.510370227967314,
			"width": 8,
			"height": 7.20001220703125,
			"angle": 0,
			"strokeColor": "#d51f0b",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1136466726,
			"version": 9,
			"versionNonce": 1823357862,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.60003662109375,
					1.5999755859375
				],
				[
					3.20001220703125,
					4
				],
				[
					5.60003662109375,
					5.5999755859375
				],
				[
					7.20001220703125,
					7.20001220703125
				],
				[
					8,
					7.20001220703125
				],
				[
					8,
					7.20001220703125
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				8,
				7.20001220703125
			]
		},
		{
			"id": "6FsfOu9DwlzI_l807RHOz",
			"type": "freedraw",
			"x": 255.7820986545637,
			"y": 12.310358020936064,
			"width": 8.800048828125,
			"height": 8,
			"angle": 0,
			"strokeColor": "#d51f0b",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1639667750,
			"version": 9,
			"versionNonce": 690043322,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689184,
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
					0.79998779296875
				],
				[
					-5.60003662109375,
					4.79998779296875
				],
				[
					-8,
					7.20001220703125
				],
				[
					-8.800048828125,
					8
				],
				[
					-8.800048828125,
					8
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				-8.800048828125,
				8
			]
		},
		{
			"id": "XAqoAeUtQvPy5cnVHG74v",
			"type": "freedraw",
			"x": 364.58208644753245,
			"y": 13.110345813904814,
			"width": 2.4000244140625,
			"height": 8,
			"angle": 0,
			"strokeColor": "#d51f0b",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 875762982,
			"version": 8,
			"versionNonce": 1609815782,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.60003662109375
				],
				[
					0,
					3.20001220703125
				],
				[
					-2.4000244140625,
					7.20001220703125
				],
				[
					-2.4000244140625,
					8
				],
				[
					-2.4000244140625,
					8
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				-2.4000244140625,
				8
			]
		},
		{
			"id": "SElJlsj1OZKS2en0EEApu",
			"type": "freedraw",
			"x": 485.38201320534495,
			"y": 12.310358020936064,
			"width": 0,
			"height": 9.5999755859375,
			"angle": 0,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 50,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1588931194,
			"version": 15,
			"versionNonce": 1671996198,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799759173,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					3.20001220703125
				],
				[
					0,
					7.20001220703125
				],
				[
					0,
					9.5999755859375
				],
				[
					0,
					9.5999755859375
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				0,
				9.5999755859375
			]
		},
		{
			"id": "lfboBWez",
			"type": "text",
			"x": 359.89458644753245,
			"y": -10.489629772032686,
			"width": 9.375,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 51846522,
			"version": 18,
			"versionNonce": 1717832230,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689184,
			"link": null,
			"locked": false,
			"text": "8",
			"rawText": "8",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "8",
			"lineHeight": 1.2
		},
		{
			"id": "fTWvdXoe",
			"type": "text",
			"x": 470.11956203346995,
			"y": -8.689641979063936,
			"width": 28.125,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 794803642,
			"version": 5,
			"versionNonce": 693474106,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799689184,
			"link": null,
			"locked": false,
			"text": "'H'",
			"rawText": "'H'",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "'H'",
			"lineHeight": 1.2
		},
		{
			"id": "HF9cvGxWqzNN956x6H6J5",
			"type": "freedraw",
			"x": 368.58208644753245,
			"y": -363.88962366851706,
			"width": 8.800048828125,
			"height": 9.5999755859375,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 50,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 2044081126,
			"version": 13,
			"versionNonce": 1431539558,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799695397,
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
					-2.4000244140625,
					1.5999755859375
				],
				[
					-4,
					3.199981689453125
				],
				[
					-6.4000244140625,
					5.5999755859375
				],
				[
					-6.4000244140625,
					6.399993896484375
				],
				[
					-7.199951171875,
					7.199981689453125
				],
				[
					-8,
					8
				],
				[
					-8,
					8.79998779296875
				],
				[
					-8,
					9.5999755859375
				],
				[
					-8.800048828125,
					9.5999755859375
				],
				[
					-8.800048828125,
					9.5999755859375
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				-8.800048828125,
				9.5999755859375
			]
		},
		{
			"id": "lIwBQY1tOrPvkV7f0fPnb",
			"type": "freedraw",
			"x": 680.5820864475324,
			"y": -367.0896358755483,
			"width": 11.199951171875,
			"height": 8,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 50,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 117178874,
			"version": 9,
			"versionNonce": 997602554,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799698941,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-2.4000244140625,
					0.79998779296875
				],
				[
					-3.199951171875,
					1.600006103515625
				],
				[
					-5.5999755859375,
					4
				],
				[
					-9.5999755859375,
					7.20001220703125
				],
				[
					-10.4000244140625,
					7.20001220703125
				],
				[
					-11.199951171875,
					8
				],
				[
					-11.199951171875,
					8
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				-11.199951171875,
				8
			]
		},
		{
			"id": "Lm1PNaBM",
			"type": "text",
			"x": 693.0945376194074,
			"y": -373.8896541860952,
			"width": 9.375,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 217467622,
			"version": 35,
			"versionNonce": 1777513466,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799719117,
			"link": null,
			"locked": false,
			"text": "H",
			"rawText": "H",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "H",
			"lineHeight": 1.2
		},
		{
			"id": "EJNoG1ea",
			"type": "text",
			"x": 380.69451320534495,
			"y": -368.0896358755483,
			"width": 9.375,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1019157478,
			"version": 22,
			"versionNonce": 1682054586,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691799726431,
			"link": null,
			"locked": false,
			"text": "8",
			"rawText": "8",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "8",
			"lineHeight": 1.2
		},
		{
			"type": "text",
			"version": 680,
			"versionNonce": 321158586,
			"isDeleted": false,
			"id": "LtsQQxUY",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -582.3304501735613,
			"y": 40.31033360687356,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 487.5,
			"height": 19.2,
			"seed": 59614950,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1691799981472,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 3,
			"text": "FIN | cost['FIN']:8|  G['FIN']:{} | []     |      | ",
			"rawText": "FIN | cost['FIN']:8|  G['FIN']:{} | []     |      | ",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "FIN | cost['FIN']:8|  G['FIN']:{} | []     |      | ",
			"lineHeight": 1.2,
			"baseline": 15
		},
		{
			"id": "15BIB2ZS",
			"type": "text",
			"x": -540.2941884010522,
			"y": 163.97688685950317,
			"width": 46.875,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#f08c00",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 284586854,
			"version": 108,
			"versionNonce": 664711718,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "Rmu81JVvf-B4UlF8oNkrU",
					"type": "arrow"
				}
			],
			"updated": 1691800502911,
			"link": null,
			"locked": false,
			"text": "COSTO",
			"rawText": "COSTO",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "COSTO",
			"lineHeight": 1.2
		},
		{
			"id": "rmKmbZiS",
			"type": "text",
			"x": -479.88043796653005,
			"y": 187.11037633148294,
			"width": 28.125,
			"height": 172.79999999999998,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1377709798,
			"version": 89,
			"versionNonce": 1805563706,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "Rmu81JVvf-B4UlF8oNkrU",
					"type": "arrow"
				}
			],
			"updated": 1691800505465,
			"link": null,
			"locked": false,
			"text": "A\nB\nC\nD\nE\nG\nH\nFIN\n",
			"rawText": "A\nB\nC\nD\nE\nG\nH\nFIN\n",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 169,
			"containerId": null,
			"originalText": "A\nB\nC\nD\nE\nG\nH\nFIN\n",
			"lineHeight": 1.2
		},
		{
			"id": "jV4GaRAk",
			"type": "text",
			"x": -436.4522756064562,
			"y": 185.4137275213438,
			"width": 28.125,
			"height": 153.6,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 355364006,
			"version": 78,
			"versionNonce": 1209966182,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "NAzU82GrcfZd1oYVioJs0",
					"type": "arrow"
				}
			],
			"updated": 1691800476762,
			"link": null,
			"locked": false,
			"text": "inf\n2\n1\n5\n3\n4\n6\n8",
			"rawText": "inf\n2\n1\n5\n3\n4\n6\n8",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 150,
			"containerId": null,
			"originalText": "inf\n2\n1\n5\n3\n4\n6\n8",
			"lineHeight": 1.2
		},
		{
			"id": "3dFOS9Yf",
			"type": "text",
			"x": -370.49680221550676,
			"y": 150.8980611561865,
			"width": 46.875,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#c2255c",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 410540282,
			"version": 65,
			"versionNonce": 1040080102,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "NAzU82GrcfZd1oYVioJs0",
					"type": "arrow"
				}
			],
			"updated": 1691800497664,
			"link": null,
			"locked": false,
			"text": "start",
			"rawText": "start",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "start",
			"lineHeight": 1.2
		},
		{
			"id": "YgHN5UO9",
			"type": "text",
			"x": -145.94000574220746,
			"y": 178.8609638795611,
			"width": 37.5,
			"height": 153.6,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1353926822,
			"version": 58,
			"versionNonce": 448313274,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "MilVEgXC2HCG9K3l_uYZ4",
					"type": "arrow"
				}
			],
			"updated": 1691800420082,
			"link": null,
			"locked": false,
			"text": "None\nA\nA\nA\nB\nE\nE\nH",
			"rawText": "None\nA\nA\nA\nB\nE\nE\nH",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 150,
			"containerId": null,
			"originalText": "None\nA\nA\nA\nB\nE\nE\nH",
			"lineHeight": 1.2
		},
		{
			"type": "text",
			"version": 208,
			"versionNonce": 752503610,
			"isDeleted": false,
			"id": "eOJcRUmb",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": -187.77678764484853,
			"y": 179.12059188292164,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 28.125,
			"height": 172.79999999999998,
			"seed": 927191334,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "EY32AawxGpow1z-xiQ909",
					"type": "arrow"
				}
			],
			"updated": 1691800444404,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 3,
			"text": "A\nB\nC\nD\nE\nG\nH\nFIN\n",
			"rawText": "A\nB\nC\nD\nE\nG\nH\nFIN\n",
			"textAlign": "center",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "A\nB\nC\nD\nE\nG\nH\nFIN\n",
			"lineHeight": 1.2,
			"baseline": 169
		},
		{
			"id": "Un68vqRl",
			"type": "text",
			"x": -2.6144630383874983,
			"y": 221.1388908197581,
			"width": 253.125,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#0c8599",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 727446694,
			"version": 204,
			"versionNonce": 1919299194,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691800298854,
			"link": null,
			"locked": false,
			"text": "Ruta(A,Fin):A, B, E, H, FIN",
			"rawText": "Ruta(A,Fin):A, B, E, H, FIN",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "Ruta(A,Fin):A, B, E, H, FIN",
			"lineHeight": 1.2
		},
		{
			"id": "Thf0zKyx",
			"type": "text",
			"x": -1.4558258995414235,
			"y": 280.2325043237372,
			"width": 65.625,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1435166886,
			"version": 122,
			"versionNonce": 249271994,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "r6lLIt7og8Efz_2GEFvjY",
					"type": "arrow"
				}
			],
			"updated": 1691800362289,
			"link": null,
			"locked": false,
			"text": "Costo:8",
			"rawText": "Costo:8",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "Costo:8",
			"lineHeight": 1.2
		},
		{
			"id": "7lFYZFHA",
			"type": "text",
			"x": 126.29289770580687,
			"y": 275.7180743859374,
			"width": 140.625,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#c2255c",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 693020794,
			"version": 179,
			"versionNonce": 2007857126,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "r6lLIt7og8Efz_2GEFvjY",
					"type": "arrow"
				}
			],
			"updated": 1691800363456,
			"link": null,
			"locked": false,
			"text": "ruta mas barata",
			"rawText": "ruta mas barata",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "ruta mas barata",
			"lineHeight": 1.2
		},
		{
			"id": "r6lLIt7og8Efz_2GEFvjY",
			"type": "arrow",
			"x": 73.25890323628835,
			"y": 290.17598496565523,
			"width": 42.070066236560265,
			"height": 2.6641088595674773,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 1082347962,
			"version": 403,
			"versionNonce": 2017561382,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691800363456,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					42.070066236560265,
					-2.6641088595674773
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "Thf0zKyx",
				"focus": 0.275365090050429,
				"gap": 9.08972913582977
			},
			"endBinding": {
				"elementId": "7lFYZFHA",
				"focus": 0.21014442486748972,
				"gap": 10.963928232958267
			},
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "Ep2HyNb0A95U2p-1rYCWx",
			"type": "freedraw",
			"x": 113.77080419527653,
			"y": 221.05039743011378,
			"width": 25.96915712094392,
			"height": 10.90703806563863,
			"angle": 0,
			"strokeColor": "#c2255c",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 855242342,
			"version": 65,
			"versionNonce": 2109267558,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691800314562,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.5193752172610857
				],
				[
					0,
					-1.0387504345221714
				],
				[
					0.5193752172610289,
					-2.077500869044286
				],
				[
					0.5193752172610289,
					-2.5969157120944146
				],
				[
					0.5193752172610289,
					-3.1162909293554435
				],
				[
					0.5193752172610289,
					-3.635666146616529
				],
				[
					1.0387504345221146,
					-4.155041363877615
				],
				[
					1.0387504345221146,
					-4.674416581138644
				],
				[
					1.5581256517832003,
					-5.193831424188772
				],
				[
					1.5581256517832003,
					-5.713206641449858
				],
				[
					2.077500869044229,
					-6.232581858710944
				],
				[
					2.596915712094358,
					-6.232581858710944
				],
				[
					2.596915712094358,
					-6.751957075971973
				],
				[
					2.596915712094358,
					-7.271332293233058
				],
				[
					3.1162909293554435,
					-7.790747136283187
				],
				[
					3.635666146616529,
					-7.790747136283187
				],
				[
					3.635666146616529,
					-8.310122353544273
				],
				[
					4.155041363877558,
					-8.310122353544273
				],
				[
					4.674416581138644,
					-8.829497570805302
				],
				[
					5.193831424188772,
					-8.829497570805302
				],
				[
					5.713206641449858,
					-8.829497570805302
				],
				[
					6.232581858710887,
					-9.348872788066387
				],
				[
					6.751957075971973,
					-10.387662848377602
				],
				[
					7.271332293233058,
					-10.387662848377602
				],
				[
					7.790747136283187,
					-10.387662848377602
				],
				[
					8.310122353544216,
					-10.387662848377602
				],
				[
					8.829497570805302,
					-10.90703806563863
				],
				[
					9.34887278806633,
					-10.90703806563863
				],
				[
					10.387662848377545,
					-10.90703806563863
				],
				[
					11.945788500160745,
					-10.90703806563863
				],
				[
					12.98457856047196,
					-10.90703806563863
				],
				[
					13.503953777732988,
					-10.90703806563863
				],
				[
					14.023328994994074,
					-10.90703806563863
				],
				[
					14.54270421225516,
					-10.90703806563863
				],
				[
					15.581494272566317,
					-10.90703806563863
				],
				[
					17.139619924349518,
					-10.387662848377602
				],
				[
					17.658995141610603,
					-10.387662848377602
				],
				[
					18.178409984660732,
					-10.387662848377602
				],
				[
					18.69778520192176,
					-10.387662848377602
				],
				[
					18.69778520192176,
					-9.868248005327473
				],
				[
					19.217160419182846,
					-9.348872788066387
				],
				[
					19.736535636443932,
					-9.348872788066387
				],
				[
					19.736535636443932,
					-8.829497570805302
				],
				[
					20.25591085370496,
					-8.829497570805302
				],
				[
					20.77532569675509,
					-8.829497570805302
				],
				[
					20.77532569675509,
					-8.310122353544273
				],
				[
					21.294700914016175,
					-8.310122353544273
				],
				[
					21.81407613127726,
					-8.310122353544273
				],
				[
					21.81407613127726,
					-7.271332293233058
				],
				[
					22.33345134853829,
					-6.751957075971973
				],
				[
					22.852826565799376,
					-6.232581858710944
				],
				[
					23.372241408849504,
					-5.713206641449858
				],
				[
					23.372241408849504,
					-5.193831424188772
				],
				[
					23.89161662611059,
					-5.193831424188772
				],
				[
					24.41099184337162,
					-5.193831424188772
				],
				[
					24.41099184337162,
					-4.674416581138644
				],
				[
					24.930367060632705,
					-4.674416581138644
				],
				[
					24.930367060632705,
					-4.155041363877615
				],
				[
					24.930367060632705,
					-3.635666146616529
				],
				[
					25.44974227789379,
					-3.635666146616529
				],
				[
					25.44974227789379,
					-3.1162909293554435
				],
				[
					25.96915712094392,
					-3.1162909293554435
				],
				[
					25.96915712094392,
					-3.1162909293554435
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				25.96915712094392,
				-3.1162909293554435
			]
		},
		{
			"id": "DVn56h7Ny1-V-f0F92sp1",
			"type": "freedraw",
			"x": 142.8562522455759,
			"y": 237.15130654573022,
			"width": 27.527282772727062,
			"height": 9.868248005327473,
			"angle": 0,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 2107056890,
			"version": 61,
			"versionNonce": 1289310586,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691800320468,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5193752172610289,
					0.5193752172610857
				],
				[
					0.5193752172610289,
					1.0387504345221146
				],
				[
					1.0387504345221146,
					1.0387504345221146
				],
				[
					1.5581256517832003,
					2.077500869044286
				],
				[
					1.5581256517832003,
					2.5969157120944146
				],
				[
					2.077540494833329,
					2.5969157120944146
				],
				[
					2.077540494833329,
					3.635666146616529
				],
				[
					2.596915712094358,
					3.635666146616529
				],
				[
					3.1162909293554435,
					4.155041363877615
				],
				[
					3.635666146616529,
					4.674416581138644
				],
				[
					4.155041363877558,
					4.674416581138644
				],
				[
					4.674456206927687,
					5.713206641449858
				],
				[
					5.713206641449858,
					5.713206641449858
				],
				[
					6.232581858710887,
					6.232581858710944
				],
				[
					6.751957075971973,
					6.751957075971973
				],
				[
					7.271371919022101,
					7.271332293233058
				],
				[
					7.790747136283187,
					7.271332293233058
				],
				[
					8.310122353544216,
					7.271332293233058
				],
				[
					9.34887278806633,
					7.271332293233058
				],
				[
					9.34887278806633,
					7.790747136283187
				],
				[
					10.387662848377545,
					7.790747136283187
				],
				[
					10.90703806563863,
					7.790747136283187
				],
				[
					11.42641328289966,
					8.310122353544273
				],
				[
					11.945788500160745,
					8.310122353544273
				],
				[
					12.98457856047196,
					8.310122353544273
				],
				[
					12.98457856047196,
					8.829497570805302
				],
				[
					13.503953777732988,
					8.829497570805302
				],
				[
					14.023328994994074,
					8.829497570805302
				],
				[
					15.062119055305288,
					9.348872788066387
				],
				[
					15.581494272566374,
					9.348872788066387
				],
				[
					16.100869489827346,
					9.348872788066387
				],
				[
					17.139619924349518,
					9.868248005327473
				],
				[
					17.659034767399703,
					9.868248005327473
				],
				[
					18.178409984660675,
					9.868248005327473
				],
				[
					18.69778520192176,
					9.868248005327473
				],
				[
					19.217160419182846,
					9.868248005327473
				],
				[
					19.736535636443932,
					9.868248005327473
				],
				[
					20.77532569675509,
					9.868248005327473
				],
				[
					21.81407613127726,
					9.868248005327473
				],
				[
					22.333451348538347,
					9.868248005327473
				],
				[
					23.372241408849504,
					9.868248005327473
				],
				[
					23.89161662611059,
					9.868248005327473
				],
				[
					24.410991843371676,
					9.868248005327473
				],
				[
					24.930367060632648,
					9.868248005327473
				],
				[
					25.96915712094392,
					9.348872788066387
				],
				[
					25.96915712094392,
					8.829497570805302
				],
				[
					26.488532338205005,
					8.829497570805302
				],
				[
					26.488532338205005,
					8.310122353544273
				],
				[
					27.007907555465977,
					8.310122353544273
				],
				[
					27.007907555465977,
					7.790747136283187
				],
				[
					27.007907555465977,
					7.271332293233058
				],
				[
					27.527282772727062,
					6.751957075971973
				],
				[
					27.527282772727062,
					6.232581858710944
				],
				[
					27.527282772727062,
					5.713206641449858
				],
				[
					27.527282772727062,
					5.193831424188772
				],
				[
					27.527282772727062,
					4.674416581138644
				],
				[
					27.527282772727062,
					4.155041363877615
				],
				[
					27.007907555465977,
					3.635666146616529
				],
				[
					27.007907555465977,
					3.635666146616529
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				27.007907555465977,
				3.635666146616529
			]
		},
		{
			"id": "ViVXPIjBZpwAtznw9jKCk",
			"type": "freedraw",
			"x": 170.38353501830295,
			"y": 221.5698122731639,
			"width": 27.527322398516162,
			"height": 10.387662848377545,
			"angle": 0,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 87694118,
			"version": 59,
			"versionNonce": 308646246,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691800326908,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.5193752172610289
				],
				[
					0,
					-0.5194148430501286
				],
				[
					0.5194148430501855,
					-1.0387900603112143
				],
				[
					1.0387900603112712,
					-2.077540494833329
				],
				[
					2.077540494833329,
					-2.077540494833329
				],
				[
					2.077540494833329,
					-2.5969157120944146
				],
				[
					3.1163305551446,
					-3.635705772405572
				],
				[
					3.635705772405572,
					-3.635705772405572
				],
				[
					3.635705772405572,
					-4.6744562069277436
				],
				[
					4.6744562069277436,
					-4.6744562069277436
				],
				[
					4.6744562069277436,
					-5.713246267238901
				],
				[
					5.713246267238901,
					-6.232621484499987
				],
				[
					5.713246267238901,
					-6.7519967017610725
				],
				[
					6.232621484499987,
					-7.271371919022101
				],
				[
					7.271371919022158,
					-7.790747136283187
				],
				[
					8.310161979333316,
					-8.310161979333316
				],
				[
					8.310161979333316,
					-8.829537196594401
				],
				[
					8.829537196594401,
					-8.829537196594401
				],
				[
					9.868287631116573,
					-8.829537196594401
				],
				[
					10.387662848377545,
					-9.34891241385543
				],
				[
					10.90707769142773,
					-9.34891241385543
				],
				[
					11.426452908688816,
					-9.868287631116516
				],
				[
					11.945828125949902,
					-9.868287631116516
				],
				[
					12.465203343210874,
					-9.868287631116516
				],
				[
					13.503993403522145,
					-9.868287631116516
				],
				[
					14.542743838044203,
					-9.868287631116516
				],
				[
					15.062119055305288,
					-9.868287631116516
				],
				[
					16.100909115616446,
					-9.868287631116516
				],
				[
					17.139659550138617,
					-9.34891241385543
				],
				[
					18.17840998466079,
					-9.34891241385543
				],
				[
					18.69782482771086,
					-9.34891241385543
				],
				[
					19.217200044971946,
					-9.34891241385543
				],
				[
					19.736575262233032,
					-9.34891241385543
				],
				[
					20.255950479494118,
					-9.34891241385543
				],
				[
					20.775325696755203,
					-9.34891241385543
				],
				[
					21.294740539805275,
					-9.34891241385543
				],
				[
					21.294740539805275,
					-8.829537196594401
				],
				[
					22.333490974327447,
					-8.310161979333316
				],
				[
					22.852866191588532,
					-8.310161979333316
				],
				[
					23.372241408849504,
					-7.790747136283187
				],
				[
					23.89165625189969,
					-7.790747136283187
				],
				[
					24.411031469160775,
					-7.271371919022101
				],
				[
					24.930406686421748,
					-6.7519967017610725
				],
				[
					25.449781903682833,
					-5.713246267238901
				],
				[
					25.449781903682833,
					-5.193831424188772
				],
				[
					25.96915712094392,
					-5.193831424188772
				],
				[
					26.488571963994104,
					-5.193831424188772
				],
				[
					27.007947181255076,
					-5.193831424188772
				],
				[
					27.007947181255076,
					-4.6744562069277436
				],
				[
					27.527322398516162,
					-4.6744562069277436
				],
				[
					27.527322398516162,
					-4.155080989666658
				],
				[
					27.527322398516162,
					-3.635705772405572
				],
				[
					27.527322398516162,
					-3.1163305551445433
				],
				[
					27.527322398516162,
					-2.5969157120944146
				],
				[
					27.527322398516162,
					-2.077540494833329
				],
				[
					27.527322398516162,
					-1.5581652775723
				],
				[
					27.527322398516162,
					-1.5581652775723
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				27.527322398516162,
				-1.5581652775723
			]
		},
		{
			"id": "cUD2vHW81TxaJX99fBGhB",
			"type": "freedraw",
			"x": 200.50777312891353,
			"y": 240.26759747508567,
			"width": 34.279279474488135,
			"height": 7.790747136283187,
			"angle": 0,
			"strokeColor": "#f08c00",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1568874490,
			"version": 57,
			"versionNonce": 940705018,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691800331011,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5193752172610857,
					0.5193752172610857
				],
				[
					1.0387504345221714,
					1.0387504345221714
				],
				[
					1.5581652775722432,
					1.0387504345221714
				],
				[
					2.077540494833329,
					1.5581256517832003
				],
				[
					3.1162909293555003,
					1.5581256517832003
				],
				[
					3.635666146616586,
					2.077540494833329
				],
				[
					4.6744562069277436,
					2.5969157120944146
				],
				[
					5.713206641449801,
					3.1162909293555003
				],
				[
					6.7519967017610725,
					3.635666146616529
				],
				[
					7.79074713628313,
					4.155041363877615
				],
				[
					8.829497570805302,
					4.155041363877615
				],
				[
					9.348912413855487,
					4.155041363877615
				],
				[
					10.90703806563863,
					4.155041363877615
				],
				[
					11.426413282899716,
					4.6744562069277436
				],
				[
					11.945828125949788,
					4.6744562069277436
				],
				[
					12.465203343210874,
					5.193831424188829
				],
				[
					13.503953777733045,
					5.193831424188829
				],
				[
					14.02332899499413,
					5.193831424188829
				],
				[
					14.542743838044203,
					5.713206641449858
				],
				[
					15.581494272566374,
					6.232581858710944
				],
				[
					16.10086948982746,
					6.232581858710944
				],
				[
					17.139659550138617,
					6.232581858710944
				],
				[
					18.17840998466079,
					6.7519570759720295
				],
				[
					19.217160419182846,
					7.271371919022158
				],
				[
					20.255950479494118,
					7.271371919022158
				],
				[
					20.77532569675509,
					7.271371919022158
				],
				[
					21.81407613127726,
					7.271371919022158
				],
				[
					22.333490974327447,
					7.790747136283187
				],
				[
					22.85286619158842,
					7.790747136283187
				],
				[
					23.372241408849504,
					7.790747136283187
				],
				[
					24.410991843371676,
					7.790747136283187
				],
				[
					24.930406686421748,
					7.790747136283187
				],
				[
					25.449781903682833,
					7.790747136283187
				],
				[
					25.96915712094392,
					7.790747136283187
				],
				[
					26.488532338205005,
					7.790747136283187
				],
				[
					27.527322398516162,
					7.790747136283187
				],
				[
					28.046697615777248,
					7.790747136283187
				],
				[
					28.566072833038334,
					7.790747136283187
				],
				[
					29.08544805029942,
					7.790747136283187
				],
				[
					29.60482326756039,
					7.790747136283187
				],
				[
					30.124238110610577,
					7.790747136283187
				],
				[
					30.643613327871662,
					7.271371919022158
				],
				[
					31.162988545132748,
					6.7519570759720295
				],
				[
					31.68236376239372,
					6.232581858710944
				],
				[
					32.201738979654806,
					6.232581858710944
				],
				[
					32.72115382270499,
					5.713206641449858
				],
				[
					32.72115382270499,
					5.193831424188829
				],
				[
					32.72115382270499,
					4.6744562069277436
				],
				[
					33.24052903996608,
					4.6744562069277436
				],
				[
					33.24052903996608,
					4.155041363877615
				],
				[
					33.75990425722705,
					3.1162909293555003
				],
				[
					33.75990425722705,
					2.5969157120944146
				],
				[
					34.279279474488135,
					2.5969157120944146
				],
				[
					34.279279474488135,
					2.077540494833329
				],
				[
					34.279279474488135,
					2.077540494833329
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				34.279279474488135,
				2.077540494833329
			]
		},
		{
			"id": "YndUoNW8",
			"type": "text",
			"x": 121.02909269543727,
			"y": 192.22463698844496,
			"width": 7.816874348216801,
			"height": 16.008958665148004,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 605649638,
			"version": 30,
			"versionNonce": 1116130726,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691800354942,
			"link": null,
			"locked": false,
			"text": "2",
			"rawText": "2",
			"fontSize": 13.340798887623338,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 13,
			"containerId": null,
			"originalText": "2",
			"lineHeight": 1.2
		},
		{
			"id": "RKSJzLn9",
			"type": "text",
			"x": 139.33731676507142,
			"y": 241.82568350107982,
			"width": 7.297459505166683,
			"height": 14.945197066581374,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 418937190,
			"version": 93,
			"versionNonce": 1751576742,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691800365254,
			"link": null,
			"locked": false,
			"text": "1",
			"rawText": "1",
			"fontSize": 12.454330888817804,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 11.000000000000009,
			"containerId": null,
			"originalText": "1",
			"lineHeight": 1.2
		},
		{
			"id": "3ucve8OS",
			"type": "text",
			"x": 189.198090512126,
			"y": 198.06767752776278,
			"width": 6.5853483196045595,
			"height": 13.48679335855014,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 67928442,
			"version": 72,
			"versionNonce": 1446363066,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691800371157,
			"link": null,
			"locked": false,
			"text": "3",
			"rawText": "3",
			"fontSize": 11.23899446545845,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 10,
			"containerId": null,
			"originalText": "3",
			"lineHeight": 1.2
		},
		{
			"id": "6Gr2zkQt",
			"type": "text",
			"x": 237.3709245224237,
			"y": 242.47499168068157,
			"width": 6.331747139301295,
			"height": 12.96741814128905,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1281485562,
			"version": 100,
			"versionNonce": 304647014,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691800377053,
			"link": null,
			"locked": false,
			"text": "2",
			"rawText": "2",
			"fontSize": 10.806181784407544,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 9.999999999999998,
			"containerId": null,
			"originalText": "2",
			"lineHeight": 1.2
		},
		{
			"id": "aErFZAKEuxcbhK3iYDwlq",
			"type": "ellipse",
			"x": -189.02958368524506,
			"y": 170.1508534356426,
			"width": 95.56648631733688,
			"height": 29.60484308045494,
			"angle": 0,
			"strokeColor": "#12b886",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 959313594,
			"version": 145,
			"versionNonce": 1943620794,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691800396030,
			"link": null,
			"locked": false
		},
		{
			"id": "TrbPAoHa",
			"type": "text",
			"x": -249.62908378594446,
			"y": 136.52076326338903,
			"width": 60.950563605966806,
			"height": 17.832393466431423,
			"angle": 0,
			"strokeColor": "#fd7e14",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1566893626,
			"version": 188,
			"versionNonce": 1124126310,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "EY32AawxGpow1z-xiQ909",
					"type": "arrow"
				}
			],
			"updated": 1691800448648,
			"link": null,
			"locked": false,
			"text": "Parents",
			"rawText": "Parents",
			"fontSize": 14.860327888692856,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 13.999999999999996,
			"containerId": null,
			"originalText": "Parents",
			"lineHeight": 1.2
		},
		{
			"id": "cNngK4UB",
			"type": "text",
			"x": -62.10567980529544,
			"y": 142.36386324139045,
			"width": 46.875,
			"height": 19.2,
			"angle": 0,
			"strokeColor": "#9c36b5",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 446001850,
			"version": 58,
			"versionNonce": 2031809018,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "MilVEgXC2HCG9K3l_uYZ4",
					"type": "arrow"
				}
			],
			"updated": 1691800428792,
			"link": null,
			"locked": false,
			"text": "start",
			"rawText": "start",
			"fontSize": 16,
			"fontFamily": 3,
			"textAlign": "center",
			"verticalAlign": "top",
			"baseline": 15,
			"containerId": null,
			"originalText": "start",
			"lineHeight": 1.2
		},
		{
			"id": "MilVEgXC2HCG9K3l_uYZ4",
			"type": "arrow",
			"x": -73.20714688841414,
			"y": 161.2876322210821,
			"width": 31.68236376239375,
			"height": 24.11689522025884,
			"angle": 0,
			"strokeColor": "#12b886",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 308442106,
			"version": 53,
			"versionNonce": 218567718,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691800421434,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-31.68236376239375,
					24.11689522025884
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "cNngK4UB",
				"focus": 0.6213735054558109,
				"gap": 11.101467083118706
			},
			"endBinding": {
				"elementId": "YgHN5UO9",
				"focus": -0.5850394534371696,
				"gap": 3.5504950913995685
			},
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "EY32AawxGpow1z-xiQ909",
			"type": "arrow",
			"x": -195.45758307341094,
			"y": 155.60812941049292,
			"width": 10.272878430974089,
			"height": 22.512462472428695,
			"angle": 0,
			"strokeColor": "#fd7e14",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 1367175162,
			"version": 291,
			"versionNonce": 1541804454,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691800448649,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					10.272878430974089,
					22.512462472428695
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "TrbPAoHa",
				"focus": -0.5564832910095537,
				"gap": 1.2549726806724664
			},
			"endBinding": {
				"elementId": "eOJcRUmb",
				"focus": 0.5311779155678109,
				"gap": 1
			},
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "gRO2AYc9XHtXT8ehEKnxt",
			"type": "ellipse",
			"x": -479.88416325271226,
			"y": 181.57728653143687,
			"width": 84.65944825169822,
			"height": 25.96915712094392,
			"angle": 0,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 96529638,
			"version": 71,
			"versionNonce": 629339814,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691800466600,
			"link": null,
			"locked": false
		},
		{
			"id": "NAzU82GrcfZd1oYVioJs0",
			"type": "arrow",
			"x": -367.94540844707467,
			"y": 173.26714436499805,
			"width": 33.5119082255448,
			"height": 21.16352511375169,
			"angle": 0,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 1532902438,
			"version": 89,
			"versionNonce": 1778209722,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691800493710,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-33.5119082255448,
					21.16352511375169
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "3dFOS9Yf",
				"focus": 0.025612669709580937,
				"gap": 3.1690832088115712
			},
			"endBinding": {
				"elementId": "jV4GaRAk",
				"focus": -0.636825843838396,
				"gap": 6.869958933836756
			},
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "Rmu81JVvf-B4UlF8oNkrU",
			"type": "arrow",
			"x": -490.6180582611021,
			"y": 173.26716417789254,
			"width": 18.524622331778517,
			"height": 24.93038687352731,
			"angle": 0,
			"strokeColor": "#f08c00",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 1164796666,
			"version": 166,
			"versionNonce": 200785914,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1691800505843,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					18.524622331778517,
					24.93038687352731
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "rmKmbZiS",
				"focus": -0.6348644922619435,
				"gap": 13.8432121535904
			},
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": "arrow"
		}
	],
	"appState": {
		"theme": "dark",
		"viewBackgroundColor": "#ffffff",
		"currentItemStrokeColor": "#c2255c",
		"currentItemBackgroundColor": "transparent",
		"currentItemFillStyle": "hachure",
		"currentItemStrokeWidth": 1,
		"currentItemStrokeStyle": "solid",
		"currentItemRoughness": 2,
		"currentItemOpacity": 100,
		"currentItemFontFamily": 3,
		"currentItemFontSize": 16,
		"currentItemTextAlign": "center",
		"currentItemStartArrowhead": null,
		"currentItemEndArrowhead": "arrow",
		"scrollX": 826.8463629107264,
		"scrollY": 648.8099781623254,
		"zoom": {
			"value": 0.7000000000000001
		},
		"currentItemRoundness": "round",
		"gridSize": null,
		"currentStrokeOptions": null,
		"previousGridSize": null,
		"frameRendering": {
			"enabled": true,
			"clip": true,
			"name": true,
			"outline": true
		}
	},
	"files": {}
}
```
%%