---
title: "Capítulo 5 · Identificar y priorizar características · Preguntas y ejercicio resuelto"
created: 2026-09-25
tags:
  - lecturas/software-architecture
capitulo: 5
orden: 9
---

# Preguntas y ejercicio resuelto

[Inicio del libro](../00%20Empieza%20aqu%C3%AD.md) → [Capítulo 5 · Identificar y priorizar características](00%20%C3%8Dndice.md) → Nota 9 de 9

**Objetivo:** Revisar prioridades cuando una promoción cambia la demanda.

> [!info] Contexto del capítulo
> Segunda edición. PedidoClaro y sus cifras son ejemplos didácticos propios; Silicon Sandwiches es la kata del libro. El [índice del capítulo](00%20%C3%8Dndice.md) conserva el alcance y las referencias generales.

## 9. Preguntas de comprobación

### 1. Negocio pide «máxima satisfacción». ¿Qué preguntas harías primero?

> [!success]- Solución razonada
> Pediría un problema observable, cuándo ocurre y qué resultado espera el cliente. Si abandona por tiempos de carga, relacionaría rendimiento con carga real; si recibe pedidos equivocados, investigaría integridad y proceso. No seleccionaría todas las características de la tabla automáticamente.

### 2. ¿Qué oculta dividir 1.000 matrículas entre diez horas?

> [!success]- Solución razonada
> Oculta la distribución temporal. Concentrarlas en diez minutos multiplica por sesenta la tasa media de llegadas. Después faltan solicitudes por matrícula, duración de sesión y sincronización de acciones para dimensionar.

### 3. El lote de fondos es rápido, pero falla al 85 %. ¿Qué falta verificar?

> [!success]- Solución razonada
> Recuperabilidad y consistencia de resultados parciales: dónde retoma, cuánto tarda y cómo evita omitir o duplicar trabajo. También fiabilidad, crecimiento del volumen y evidencia de corrección. Medir únicamente duración de ejecuciones exitosas es insuficiente.

### 4. ¿Cómo decidirías si mapas debe bloquear los pedidos?

> [!success]- Solución razonada
> Preguntaría qué pierde el usuario sin tráfico y si puede continuar con direcciones básicas. Probaría ese fallo y acordaría una degradación aceptable. Una integración auxiliar no debería convertirse accidentalmente en condición para todo el negocio.

### 5. ¿Qué evidencia justificaría microkernel frente a Template Method?

> [!success]- Solución razonada
> Variaciones ejecutables que requieran contratos y evolución independientes, junto con beneficios que compensen su coste. Para pocas variaciones internas, diseño o configuración pueden bastar. Compararía acoplamiento, pruebas, despliegue, rendimiento y mantenimiento con el equipo.

### 6. ¿Qué harías si seguridad no está entre las tres principales?

> [!success]- Solución razonada
> Documentaría sus mínimos y los comprobaría igualmente. Si los riesgos requieren aislamiento u otra decisión estructural crítica, reconsideraría la lista. Delegar pagos no garantiza autorización correcta ni protección de los datos propios.

### 7. Aparece una octava candidata. ¿Debe rechazarse?

> [!success]- Solución razonada
> No por su número. Examinaría su necesidad y qué desplaza, conservaría alternativas en «Otras consideradas» y negociaría el conjunto principal. Siete limita la conversación; no sustituye el juicio ni obliga a un ranking total.

## 10. Ejercicio aplicado: una promoción cambia la demanda

**Supuesto nuevo:** PedidoClaro anuncia una promoción y prevé 6.000 sesiones en dos minutos. El presupuesto operativo no crece y los locales tienen capacidad limitada.

Entrega una hoja revisada: tres preguntas para negocio; demanda digital frente a capacidad de cocina; dos alternativas y sus costes; tres conductoras; una candidata desplazada; y una prueba con criterio de aceptación. Explica la admisión de pedidos y la comunicación de esperas.

> [!success]- Orientación para resolverlo
> Pregunta cuántos pedidos puede preparar cada local, si se permiten franjas futuras y qué espera quien ve la promoción. Compara preparar capacidad informática y escalonar admisiones con un ajuste dinámico de recursos; ambos necesitan limitar compromisos según cocina. Un control de admisión puede proteger continuidad, pero añade espera y exige informar con claridad. Conserva o cambia el top 3 justificando el objetivo comercial. Prueba el pico y una cocina saturada: no basta una web rápida si confirma pedidos imposibles. Todo umbral adicional debe etiquetarse como supuesto pendiente de validación.

---

**Anterior:** [Hoja de trabajo PedidoClaro](08%20Hoja%20de%20trabajo%20PedidoClaro.md) · **Índice:** [Volver al capítulo](00%20%C3%8Dndice.md) · **Siguiente:** [Laboratorio integrador](../06%20Apoyo%20y%20repaso/02%20Laboratorio%20integrador.md)
