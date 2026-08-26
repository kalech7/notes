---
tags:
  - algebra-lineal
  - svd
  - repaso
related: "[[00 Índice - Espectro, SVD y rango bajo]]"
---

# Resumen y preguntas de repaso

Anterior: [[05 Espacio latente, PCA e interpretación]] · Volver al [[00 Índice - Espectro, SVD y rango bajo|índice]]

Formulario completo: [[00 Formulario razonado - fundamentos, espectro y SVD|todas las fórmulas explicadas paso a paso]].

## Tabla esencial

| Concepto | Qué responde | Fórmula central |
| --- | --- | --- |
| Autovector | ¿Qué dirección conserva una matriz cuadrada? | $Av=\lambda v$, $v\neq0$ |
| Espectro | ¿Cuáles son sus escalas propias? | conjunto de $\lambda_i$ |
| SVD | ¿Qué ejes ortogonales y escalas describen $A$? | $A=U\Sigma V^T$ |
| Puente espectral | ¿De dónde salen los valores singulares? | $\sigma_i^2=\lambda_i(A^TA)$ |
| Rango | ¿Cuántas direcciones activas hay? | cantidad de $\sigma_i>0$ |
| Rango bajo | ¿Cómo comprimir con $k$ direcciones? | $A_k=U_k\Sigma_kV_k^T$ |
| Error espectral | ¿Cuál es la peor dirección omitida? | $\lVert A-A_k\rVert_2=\sigma_{k+1}$ |
| Error Frobenius | ¿Cuál es la pérdida total? | $\sqrt{\sum_{i>k}\sigma_i^2}$ |
| PCA | ¿Qué direcciones explican variación centrada? | SVD de $X_c$ |

## Errores que debes detectar

- Aplicar el lenguaje $Av=\lambda v$ a una matriz rectangular.
- Confundir autovalores con valores singulares.
- Creer que toda matriz real tiene autovectores ortogonales.
- Confundir SVD reducida con SVD compacta.
- Truncar columnas originales en vez de componentes singulares.
- Elegir $k$ sin declarar norma, umbral u objetivo.
- Llamar «varianza explicada» a $\sigma_i^2$ sin centrar los datos.
- Interpretar una dirección latente como concepto semántico demostrado.
- Ignorar ambigüedad de signo y tolerancia numérica.
- Usar el cálculo como sustituto del argumento matemático.

## Preguntas para recordar activamente

1. Define autovector y explica el requisito no nulo.
2. ¿Qué ventajas aporta una matriz simétrica?
3. ¿Por qué $X^TX$ y $XX^T$ son semidefinidas positivas?
4. Explica $V^T\rightarrow\Sigma\rightarrow U$ con palabras.
5. Da las dimensiones de la SVD completa, reducida y compacta.
6. Deriva $A^TAv_i=\sigma_i^2v_i$.
7. ¿Por qué los valores singulares son no negativos?
8. Explica la ambigüedad de signo.
9. Enuncia operacionalmente Eckart-Young-Mirsky.
10. ¿Qué diferencia hay entre error espectral y Frobenius?
11. Defiende $k=2$ para el caso del módulo y limita la afirmación.
12. ¿Qué es rango efectivo?
13. ¿Qué representa $U_k\Sigma_k$?
14. ¿Por qué PCA exige centrado?
15. ¿Qué validación falta antes de dar significado a una dirección latente?

## Mini examen con respuestas plegadas

> [!question]- Una matriz $5\times4$, ¿tiene autovalores?
> No en el sentido $Xv=\lambda v$, porque transforma $\mathbb{R}^4$ en $\mathbb{R}^5$. Sí podemos estudiar los autovalores de $X^TX$ y $XX^T$.

> [!question]- Si $\sigma=(10,3,0.1)$ y eliges $k=2$, ¿cuál es el error espectral óptimo?
> $\sigma_3=0.1$.

> [!question]- ¿Puede una matriz tener autovalores cero y un valor singular positivo?
> Sí. $B=\begin{bmatrix}0&1\\0&0\end{bmatrix}$ tiene autovalores $(0,0)$ y valores singulares $(1,0)$.

> [!question]- ¿Qué convierte la SVD de una matriz de datos en PCA?
> Centrar las columnas primero y adoptar la interpretación estadística de la covarianza.

## Lista final

- [ ] Distingo espectro y SVD.
- [ ] Puedo auditar dimensiones.
- [ ] Explico cada factor de la SVD.
- [ ] Calculo e interpreto dos tipos de error.
- [ ] Defiendo $k$ con un criterio explícito.
- [ ] Distingo rango algebraico y numérico.
- [ ] No atribuyo semántica sin validación.
- [ ] Sé cuándo SVD corresponde a PCA.
- [ ] Puedo seguir la explicación de Python en [[python/00 Índice - Demo computacional M05]].
