**Ubicación**
* Interna.- relacionada principalmente con la memoria principal, luego la
cache y los registros.
* Externa.- relacionada con dispositivos periféricos (discos, cintas)
**Capacidad**
* Se expresa normalmente en términos de bytes (8 bits) de palabras.
Longitudes comunes son de 8, 16 y 32 bits. Se considera el tamaño de la
palabra y el número de palabras
Unidad de Transferencia
* En memorias internas es igual al número de líneas de entrada/salida de
datos del módulo de memoria. A menudo es igual a la longitud de palabra.

---

* ***Palabra.-** es la unidad «natural» de organización de la memoria
* **Unidades direccionables:** Por defecto la unidad direccionable es la palabra. En algunos casos se direcciona a nivel de byte. La relación entre la longitud A de una dirección y el número N de unidades direccionables, es 2<sup>A</sup> = 𝑁.
* **Unidad de transferencia.-** es el número de bits que se leen o escriben en memoria a la vez.
	*Palabra (cache y procesador)*
	*Bloques (memoria interna y cache)*
## Método de acceso
* **Secuencial.-** la memoria se organiza en unidades de datos llamadas registros. El acceso se realiza con una secuencia lineal específica. Se utiliza un mecanismo de lectura/escritura compartida que se traslada desde su posición actual a la deseada. Ejemplo: Unidad de cinta

* **Directo.-** tiene asociado un mecanismo de lectura/escritura. Los bloques individuales o registros tienen una dirección única basada en su dirección física. Ejemplo: unidad de disco

*  **Aleatorio.-** cada posición tiene un único mecanismo de acceso. La posición puede seleccionarse aleatoriamente y ser accedida directamente. Ejemplo: la memoria principal y algunos sistemas de caché son de acceso aleatorio.

* **Asociativa.-** permite hacer una comparación de ciertas posiciones de bits dentro de una palabra buscando que coincidan con unos valores dados. Ejemplo: Las memorias caché pueden emplear acceso asociativo.
## Tipos de memoria:
* **Memoria dinámica (DRAM):** compuesta de celdas que almacenan los datos como carga de capacitores, los cuales tienen la tendencia a descargarse, por lo que requieren periodos de refrescamiento de la carga. Es esencialmente un dispositivo analógico. Las memorias DRAM se utilizan en la memoria principal.
*  **Memoria estática (SRAM):** es un dispositivo digital que utiliza los mismos elementos lógicos usados en el procesador. las memorias SRAM se usan en la caché
* **Memorias ROM (Read Only Memory):** Son memorias de solo lectura. Originalmente se grababan durante el proceso de fabricación con determinados programas específicos. Ejemplos: microprogramas, BIOS, programas del sistema, etc.
* **PROM (Programable Read Only Memory)**: Pueden ser grabadas por el usuario con ayuda de un dispositivo especial, aunque una sola vez.
* **EPROM (Erase Programable Read Only Memory):** Pueden ser grabadas o borradas por el usuario con ayuda de un dispositivo especial que emplea una luz ultravioleta. Es posible reprogramarlas varias veces.
* EEPROM (Electrical Erase Programable Read Only Memory): Pueden ser grabadas o borradas por el usuario. Es posible situarlas online en algunos sistemas computacionales (BIOS actuales).
* Flash memory: Su nombre se debe a que pueden ser borradas en bloques a alta velocidad.
![[Pasted image 20230730184430.png]]
