**CSS** (Cascading Style Sheets) es el lenguaje que dicta cómo deben verse los elementos [[html|HTML]] en pantalla, papel u otros medios. Permite separar la estructura del documento de su presentación visual.

## Selectores
Los selectores se utilizan para "apuntar" a los elementos HTML a los que deseas aplicar estilo.
- **Selector de etiqueta:** Apunta a todos los elementos de un tipo (ej. `p { color: red; }`).
- **Selector de clase (`.`):** Apunta a elementos que tengan un atributo class específico (ej. `.boton { padding: 10px; }`). Las clases se pueden reusar.
- **Selector de ID (`#`):** Apunta a un elemento único con un id específico (ej. `#cabecera { background: black; }`).

> [!info] Explicación
> **Especificidad y Cascada:** "Cascada" significa que el orden importa: la última regla leída sobreescribe a las anteriores. Sin embargo, la especificidad gana sobre el orden: un `#ID` es más "fuerte" que una `.clase`, y una `.clase` es más fuerte que una simple `etiqueta`.

```mermaid
flowchart LR
    subgraph Jerarquía de Especificidad (De menor a mayor)
        A[Etiqueta\nEj: p, div\nValor: 1] --> B[Clase\nEj: .boton\nValor: 10]
        B --> C[ID\nEj: #header\nValor: 100]
        C --> D[Estilo en línea\nstyle='...'\nValor: 1000]
    end
```

## El Modelo de Cajas
Consulta [[modelo de cajas]] para entender cómo CSS calcula anchos, altos, márgenes y rellenos.

## Unidades de Medida y Colores
Consulta [[Unidades de medida]] para entender píxeles, em, rem, porcentajes y códigos de color RGB/Hexadecimal.

## CSS Flexbox
El **Flexible Box Layout Module** (Flexbox) permite diseñar estructuras unidimensionales (filas o columnas) complejas fácilmente, alineando y distribuyendo el espacio de forma dinámica.

```css
.contenedor {
    display: flex;
    justify-content: center; /* Alineación horizontal */
    align-items: center;    /* Alineación vertical */
}
```

> [!info] Explicación
> Flexbox es tu mejor amigo para centrar elementos (el clásico problema del centrado vertical en CSS se soluciona en 3 líneas con Flexbox) y para barras de navegación.

## CSS Grid
**CSS Grid Layout** es un sistema de diseño bidimensional basado en cuadrículas (filas y columnas al mismo tiempo). A diferencia de Flexbox, que maneja una dimensión a la vez, Grid maneja todo el tablero.

```css
.grilla {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr; /* 3 columnas del mismo tamaño */
    gap: 20px; /* Espacio entre los elementos */
}
```

> [!info] Explicación
> Usa **Flexbox** para alinear elementos dentro de un componente (ej. ícono al lado de un texto en un botón). Usa **Grid** para definir la estructura macro de la página web (cabecera, barra lateral, contenido central, pie de página).

## Notas relacionadas
- [[Desarollo web]]
- [[html]]
