---
title: "Jerarquía de Memoria y Memoria Caché"
date_created: 2026-09-28
date_modified: 2026-09-28
tags:
  - arquitectura-de-computadores
  - jerarquia-de-memoria
  - memoria-cache
  - amat
  - mapeo-de-cache
  - sistemas-digitales
aliases:
  - Jerarquía de Memoria
  - Memoria Caché
  - Cache Mapping
  - AMAT
---

# Jerarquía de Memoria y Memoria Caché

Como se introdujo fundamentalmente en [[Funcionamiento del Sistema de Memoria]] y se exploró conceptualmente en [[Principios de funcionamiento]], el diseño de la memoria de un computador se enfrenta a una limitación física y económica ineludible: **las tecnologías de memoria más veloces son prohibitivamente caras y de baja densidad por unidad de área, mientras que las de mayor capacidad son exponencialmente más lentas**.

Para resolver esta disparidad (la llamada *Memory Wall* o brecha de velocidad procesador-memoria), los sistemas modernos implementan una **jerarquía piramidal de memoria**, orquestada por hardware y respaldada por el principio físico rector de la **localidad de referencia**.

---

## 1. Principio Físico Rector: Localidad de Referencia

La efectividad de cualquier jerarquía de memoria depende de que los programas no acceden a su espacio de direcciones de forma uniforme o puramente aleatoria, sino con una fuerte tendencia predecible.

```mermaid
flowchart TD
    subgraph PrincipioLocalidad [Principio de Localidad de Referencia]
        LT["<b>Localidad Temporal</b><br>Si un dato se referencia en t₀,<br>tenderá a referenciarse de nuevo en t₀ + Δt"]
        LE["<b>Localidad Espacial</b><br>Si una dirección de memoria X se referencia,<br>las direcciones contiguas X + 1, X + 2 tenderán a referenciarse pronto"]
    end
    LT --> Cache["Memoria Caché:<br>Almacena datos recientes y bloques adyacentes"]
    LE --> Cache
```

### 1.1 Localidad Temporal
- **Fundamento:** Un elemento de memoria que ha sido accedido recientemente tiene una altísima probabilidad de ser consultado nuevamente en el futuro inmediato.
- **Ejemplos de software:** Variables contadoras de bucles (`i++`), punteros a pilas de ejecución (*stack frame*), variables acumuladoras locales.
- **Mecanismo hardware:** Mantener los datos recientemente accedidos en los niveles más cercanos a la CPU (L1/L2).

### 1.2 Localidad Espacial
- **Fundamento:** Si una dirección de memoria es accedida en un instante dado, es extremadamente probable que las direcciones físicamente contiguas sean referenciadas en el corto plazo.
- **Ejemplos de software:** Recorrido secuencial de vectores y matrices en memoria (`for (int i=0; i<N; i++) array[i]`), ejecución secuencial de código de instrucciones de máquina ($PC \leftarrow PC + 4$).
- **Mecanismo hardware:** Cuando ocurre un fallo de caché, **no se transfiere únicamente la palabra solicitada**, sino un **bloque continuo completo** ($K$ palabras o 64 bytes) desde la DRAM hacia la caché (como se detalló en [[Principios de funcionamiento#Memoria principal]]).

---

## 2. La Pirámide de la Jerarquía de Memoria

Expandiendo el modelo preliminar de [[Funcionamiento del Sistema de Memoria#Jerarquía de Memoria]], la jerarquía moderna se estructura en los siguientes niveles tecnológicos:

```mermaid
graph TD
    Reg["<b>Registros del CPU</b><br>&lt; 1 ciclo | ~0.5 ns | ~1 - 2 KB | Flip-Flops"]
    L1["<b>Caché L1 (I-Cache y D-Cache separadas)</b><br>~1 - 2 ns (3-4 ciclos) | 32 - 64 KB | SRAM en núcleo"]
    L2["<b>Caché L2 (Unificada por núcleo)</b><br>~3 - 5 ns (10-14 ciclos) | 256 KB - 1 MB | SRAM rápida"]
    L3["<b>Caché L3 (Compartida multi-core)</b><br>~10 - 20 ns (40-60 ciclos) | 8 - 64 MB | SRAM de alta densidad"]
    RAM["<b>Memoria Principal (DRAM)</b><br>~50 - 100 ns (150-200 ciclos) | 16 - 128 GB | DDR4/DDR5 (Capacitores)"]
    SSD["<b>Almacenamiento Secundario (NVMe / SSD)</b><br>~10 - 50 µs | 512 GB - 8 TB | Flash NAND"]
    HDD["<b>Almacenamiento Masivo / Terciario (HDD / Red)</b><br>~5 - 15 ms | 10+ TB | Magnético / Cloud"]

    Reg --> L1 --> L2 --> L3 --> RAM --> SSD --> HDD
```

### Tabla Comparativa de Tecnologías Físicas

| Nivel | Tecnología Dominante | Tiempo de Acceso Típico | Capacidad Típica | Administrado por |
| :--- | :--- | :--- | :--- | :--- |
| **Registros** | CMOS Multiplexores / Flip-Flops | $< 0.5\text{ ns}$ | $64 - 128 \times 64\text{ bits}$ | Compilador ([[Fases del Compilador y Analisis Lexico]]) |
| **Caché L1** | SRAM (6T celdas de transistores) | $\sim 1\text{ ns}$ | $32 - 64\text{ KB}$ | Hardware de caché dedicado |
| **Caché L2** | SRAM (6T celdas) | $\sim 3 - 4\text{ ns}$ | $512\text{ KB} - 2\text{ MB}$ | Hardware de caché |
| **Caché L3** | SRAM de celda densa o eDRAM | $\sim 15 - 20\text{ ns}$ | $16 - 64\text{ MB}$ | Hardware de caché |
| **Memoria RAM** | DRAM (1 Transistor + 1 Capacitor) | $\sim 60 - 80\text{ ns}$ | $16 - 64\text{ GB}$ | Sistema Operativo + MMU |
| **SSD NVMe** | Flash NAND 3D TLC/QLC | $\sim 20 - 50\ \mu\text{s}$ | $1 - 4\text{ TB}$ | SO (Sistema de archivos) |

> [!info] ¿Por qué L1 se divide en I-Cache y D-Cache?
> La caché L1 se descompone físicamente en una **I-Cache** (Instruction Cache) y una **D-Cache** (Data Cache) para implementar una arquitectura **Harvard a nivel L1**. Como se verá en [[Pipeline de Instrucciones y Riesgos (Hazards)]], esto previene **riesgos estructurales**, permitiendo que la etapa de búsqueda de instrucción (*IF*) y la de acceso a datos (*MEM*) accedan a la caché en el mismo ciclo de reloj sin colisión de buses.

---

## 3. Mapeo de Memoria Caché y Descomposición de Direcciones

Como se explicó en [[Principios de funcionamiento#Función de correspondencia]], la caché contiene muchísimas menos líneas ($C$) que bloques la memoria principal ($M$). 

Una dirección física generada por la CPU de $A$ bits se descompone unívocamente en tres campos: **Etiqueta (Tag)**, **Índice (Index)** y **Desplazamiento (Offset)**.

```
+---------------------------+------------------------+-------------------------+
|        Tag (t bits)       |     Index (s bits)     |     Offset (b bits)     |
+---------------------------+------------------------+-------------------------+
|<------------------------------ Ancho de Dirección (A bits) ------------------>|
```

### Fórmulas Matemáticas Exactas de Dimensionamiento
Sea:
- $A$: Número total de bits del bus de direcciones (típicamente 32 o 64 bits).
- $B$: Tamaño del bloque o línea de caché en bytes (típicamente $B = 64\text{ bytes}$).
- $C$: Capacidad total de datos de la caché en bytes.
- $N$: Número de vías (*ways*) por conjunto (en mapeo directo $N=1$; en asociativa por conjuntos $N \in \{2, 4, 8, 16\}$).

1. **Bits de Desplazamiento de Bloque ($b$ - Offset):**
   Determina qué byte específico dentro de la línea de caché se está direccionando:
   $$b = \log_2(B)$$
2. **Número Total de Líneas de la Caché ($L$):**
   $$L = \frac{C}{B}$$
3. **Número de Conjuntos de la Caché ($S$):**
   $$S = \frac{L}{N} = \frac{C}{N \cdot B}$$
4. **Bits de Índice ($s$ - Index):**
   Identifica cuál de los $S$ conjuntos debe consultarse:
   $$s = \log_2(S)$$
5. **Bits de Etiqueta ($t$ - Tag):**
   Identificador único para confirmar que el bloque presente en la línea corresponde exactamente al bloque solicitado de la DRAM:
   $$t = A - (s + b)$$

---

### 3.1 Mapeo Directo (*Direct Mapped Cache*)
- **Estructura:** Cada bloque de la memoria principal se asigna a **exactamente una línea de caché**. Corresponde a $N=1$ vía ($S = L$).
- **Función de Mapeo:**
  $$\text{Línea de Caché} = (\text{Número de Bloque}) \pmod{L}$$

```mermaid
flowchart LR
    subgraph Direccion [Dirección de 32 bits]
        Tag["Tag (18 bits)"]
        Index["Index (8 bits)"]
        Offset["Offset (6 bits)"]
    end

    subgraph CacheMem [Caché Mapeo Directo (256 Líneas)]
        Line0["Línea 0: [V | Tag | 64B Datos]"]
        LineK["Línea K: [V | Tag | 64B Datos]"]
        Line255["Línea 255: [V | Tag | 64B Datos]"]
    end

    Index -->|Decodificador 1 a 256| LineK
    LineK -->|Compara Tag| Comp{Tag == Tag?}
    Comp -- Sí y V=1 --> Hit[Cache Hit!]
    Comp -- No o V=0 --> Miss[Cache Miss!]
```

- **Ventajas:** Hardware extremadamente simple; tiempo de acierto (*Hit Time*) mínimo ya que no requiere conmutación asociativa ni multiplexores de selección múltiple.
- **Desventaja Crítica:** Vulnerable a **fallos por conflicto** y **vapuleo (*thrashing*)** (descrito en [[Principios de funcionamiento#Función de Correspondencia Directa]]), donde dos bloques compiten continuamente por la misma línea.

---

### 3.2 Caché Completamente Asociativa (*Fully Associative Cache*)
- **Estructura:** Cualquier bloque de memoria puede almacenarse en **cualquier línea disponible de la caché**. Solo existe un único conjunto ($S = 1$).
- **Bits de Índice:** $s = \log_2(1) = 0$ bits. No existe campo de índice; la dirección se divide únicamente en:
  $$\text{Tag} = A - b \quad \text{y} \quad \text{Offset} = b$$
- **Mecanismo:** La dirección de la etiqueta debe compararse **en paralelo simultáneo** contra todas las etiquetas de todas las líneas mediante $L$ comparadores físicos de hardware.
- **Ventajas:** Cero fallos de conflicto.
- **Desventajas:** Consumo eléctrico y complejidad circuital desmesurados. Solo se implementa en estructuras reducidas como el **TLB** (*Translation Lookaside Buffer* de la memoria virtual).

---

### 3.3 Asociativa por Conjuntos de $N$ Vías (*N-Way Set Associative Cache*)
Es el compromiso óptimo estándar de la industria (utilizado en procesadores Intel, AMD, ARM y RISC-V).

- La caché se divide en $S$ conjuntos, y cada conjunto contiene exactamente $N$ líneas (vías).
- Un bloque se mapea a un conjunto específico según su índice:
  $$\text{Conjunto} = (\text{Número de Bloque}) \pmod S$$
  pero dentro de ese conjunto, el bloque puede colocarse en **cualquiera de las $N$ vías**.

```mermaid
flowchart TD
    subgraph DireccionFisica [Dirección Física]
        T[Tag]
        I[Index]
        O[Offset]
    end

    subgraph SetK [Conjunto K (4 Vías)]
        Way0["Vía 0: [Tag₀ | Datos₀]"]
        Way1["Vía 1: [Tag₁ | Datos₁]"]
        Way2["Vía 2: [Tag₂ | Datos₂]"]
        Way3["Vía 3: [Tag₃ | Datos₃]"]
    end

    I -->|Selecciona Conjunto| SetK
    T --> Comp0["Comp 0"]
    T --> Comp1["Comp 1"]
    T --> Comp2["Comp 2"]
    T --> Comp3["Comp 3"]

    Way0 --> Comp0
    Way1 --> Comp1
    Way2 --> Comp2
    Way3 --> Comp3

    Comp0 --> Mux["Lógica de Acierto / MUX"]
    Comp1 --> Mux
    Comp2 --> Mux
    Comp3 --> Mux
    Mux --> Out[Dato al CPU]
```

---

## 4. Políticas de Reemplazo y Políticas de Escritura

Cuando ocurre un fallo y el conjunto de destino está lleno, el hardware debe decidir qué línea expulsar para alojar el nuevo bloque.

### 4.1 Políticas de Reemplazo
1. **LRU (*Least Recently Used*):** Expulsa la línea que no ha sido accedida por más tiempo. Requiere bits de estado para mantener el orden temporal. Excelente tasa de aciertos gracias a la localidad temporal.
2. **Pseudo-LRU (Tree-PLRU):** Aproximación de bajo costo en silicio de LRU basada en un árbol binario de bits de decisión (utilizada en cachés modernas de 8 y 16 vías para evitar la sobrecarga de LRU puro).
3. **FIFO (*First-In, First-Out*):** Expulsa la línea que lleva más tiempo dentro de la caché, sin importar qué tan frecuentemente fue usada recientemente.
4. **Random (Aleatoria):** Selecciona una víctima al azar. Implementación casi nula en silicio; rendimiento sorprendentemente cercano a LRU en cargas de trabajo de alta dispersión.

---

### 4.2 Políticas de Escritura

Las operaciones de lectura (*loads*) traen datos a la caché sin alterarlos; sin embargo, las operaciones de escritura (*stores*) modifican el valor del bloque, creando inconsistencias entre la copia en caché y la copia en DRAM.

```mermaid
flowchart TD
    subgraph PoliticasEscritura [Políticas de Escritura]
        WT["<b>Write-Through</b><br>Escribe en Caché y DRAM simultáneamente.<br>Simple pero satura el bus de memoria."]
        WB["<b>Write-Back</b><br>Escribe solo en Caché y activa el Dirty Bit.<br>Escribe en DRAM solo al desalojar el bloque.<br>Óptimo rendimiento de ancho de banda."]
    end
```

#### Write-Through vs. Write-Back
- **Write-Through (Escritura Directa):** Cada escritura de la CPU actualiza tanto la línea de caché como el bloque en la memoria principal DRAM simultáneamente.
  - *Ventaja:* Coherencia absoluta e inmediata; no requiere desalojos complejos.
  - *Desventaja:* El CPU se frena ante la latencia lenta de la DRAM (mitigado parcialmente con un *Write Buffer*).
- **Write-Back (Post-Escritura con *Dirty Bit*):** La CPU modifica únicamente la línea en la caché. Dicha línea se marca con un bit de estado denominado **Dirty Bit** (o bit de modificación $D=1$).
  - *Ventaja:* Las escrituras sucesivas a la misma variable ocurren a la velocidad ultra-rápida de la SRAM ($\sim 1\text{ ns}$) sin tráfico hacia el bus del sistema.
  - *Costo:* Al desalojar una línea víctima por reemplazo, si $D=1$, el bloque debe escribirse forzosamente en DRAM antes de cargar el nuevo dato.

#### Acierto y Fallo de Escritura: Write-Allocate vs. No-Write-Allocate
- **Write-Allocate (Fallo con Ubicación):** Si ocurre un fallo al escribir, se carga el bloque desde la DRAM hacia la caché y luego se ejecuta la escritura. (Usado típicamente en conjunto con *Write-Back*).
- **No-Write-Allocate (Fallo sin Ubicación):** Si ocurre un fallo al escribir, se modifica el dato directamente en la DRAM sin cargar el bloque en la caché. (Usado con *Write-Through*).

---

## 5. Métrica de Rendimiento: AMAT (*Average Memory Access Time*)

El rendimiento de un sistema de memoria no se mide por su capacidad, sino por el **Tiempo Medio de Acceso a Memoria (AMAT)**:

$$\text{AMAT} = \text{Hit Time} + (\text{Miss Rate} \times \text{Miss Penalty})$$

Donde:
- $\text{Hit Time}$: Tiempo que toma determinar si el dato está en la caché y entregarlo a la CPU.
- $\text{Miss Rate}$: Fracción de accesos a memoria que resultan en fallos ($1 - \text{Hit Rate}$).
- $\text{Miss Penalty}$: Tiempo adicional necesario para transferir el bloque desde el nivel inferior de la jerarquía.

### 5.1 Extensión de AMAT para Jerarquías Multinivel (L1, L2, L3, DRAM)

En sistemas contemporáneos con tres niveles de caché:

$$\text{AMAT} = T_{h, L1} + M_{L1} \cdot \Big[ T_{h, L2} + M_{L2} \cdot \big( T_{h, L3} + M_{L3} \cdot T_{\text{DRAM}} \big) \Big]$$

Donde:
- $M_{L1}, M_{L2}, M_{L3}$ son las **tasas de fallo locales** (*Local Miss Rates*) de cada nivel:
  $$M_{\text{local}} = \frac{\text{Fallos en este nivel}}{\text{Accesos que llegaron a este nivel}}$$
- Las **tasas de fallo globales** (*Global Miss Rates*) se calculan respecto a todos los accesos originales de la CPU:
  $$M_{\text{global, L2}} = M_{L1} \times M_{L2}$$
  $$M_{\text{global, L3}} = M_{L1} \times M_{L2} \times M_{L3}$$

---

## 6. Ejercicio Analítico Resuelto de Ingeniería

### Enunciado:
Un procesador de $32\text{ bits}$ de direcciones posee una memoria caché de datos L1 de $64\text{ KB}$, asociativa por conjuntos de $4\text{ vías}$ ($N=4$), con bloques de $64\text{ bytes}$.
- $T_{h, L1} = 1\text{ ns}$, Tasa de fallos $M_{L1} = 5\%$.
- Caché L2 unificada de $1\text{ MB}$, asociativa de $8\text{ vías}$, con $T_{h, L2} = 4\text{ ns}$ y tasa de fallos local $M_{L2} = 10\%$.
- Penalización de acceso a DRAM: $T_{\text{DRAM}} = 70\text{ ns}$.

### Paso 1: Descomposición de la Dirección Física en L1
1. **Bits de Offset ($b$):**
   $$b = \log_2(64) = 6\text{ bits}$$
2. **Número de Bloques (Líneas Totales $L$):**
   $$L = \frac{64\text{ KB}}{64\text{ Bytes}} = \frac{65536}{64} = 1024\text{ líneas}$$
3. **Número de Conjuntos ($S$):**
   $$S = \frac{L}{N} = \frac{1024}{4} = 256\text{ conjuntos}$$
4. **Bits de Índice ($s$):**
   $$s = \log_2(256) = 8\text{ bits}$$
5. **Bits de Etiqueta ($t$):**
   $$t = 32 - (s + b) = 32 - (8 + 6) = 32 - 14 = 18\text{ bits}$$

*Estructura de la dirección:* `[Tag: 18 bits] | [Index: 8 bits] | [Offset: 6 bits]`.

### Paso 2: Cálculo del AMAT del Sistema
Aplicando la fórmula multinivel (L1 + L2 + DRAM):
$$\text{Penalización de Fallo L1} = T_{h, L2} + (M_{L2} \times T_{\text{DRAM}}) = 4\text{ ns} + (0.10 \times 70\text{ ns}) = 4\text{ ns} + 7\text{ ns} = 11\text{ ns}$$

$$\text{AMAT} = T_{h, L1} + (M_{L1} \times \text{Penalización L1}) = 1\text{ ns} + (0.05 \times 11\text{ ns}) = 1\text{ ns} + 0.55\text{ ns} = 1.55\text{ ns}$$

> [!note] Conclusión del Ejercicio
> A pesar de que la memoria DRAM tarda $70\text{ ns}$ por acceso, la presencia de la jerarquía L1/L2 bien dimensionada reduce el tiempo medio de acceso efectivo percibido por el núcleo a apenas **$1.55\text{ ns}$**, un factor de aceleración de más de $45\times$.

---

## Notas Relacionadas y Enlaces de Vault
- [[Funcionamiento del Sistema de Memoria]] — Conceptos fundamentales de organización y tecnologías de memoria interna y externa.
- [[Principios de funcionamiento]] — Elementos de diseño de caché, mapeo directo y asociativo preliminar.
- [[Pipeline de Instrucciones y Riesgos (Hazards)]] — Impacto de las latencias de memoria y cachés Harvard en el pipeline de la CPU.
- [[Fases del Compilador y Analisis Lexico]] — Gestión eficiente de buffers de lectura en memoria para scanners de alto rendimiento.
