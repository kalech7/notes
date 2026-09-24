# Comandos de soporte: qué hace cada uno

Estos apuntes corresponden a equipos Linux y a un contenedor concreto. Las rutas, el ID de contenedor y el formato del log son datos del contexto original: compruébalos antes de reutilizar un comando. Los bloques siguientes son documentación; no se ejecutaron durante esta revisión.

## Reinicio inmediato mediante SysRq

```bash
echo "b" | sudo tee /proc/sysrq-trigger
```

Este comando escribe `b` en la interfaz del kernel. `echo` produce el carácter, la tubería lo entrega a `tee` y `sudo` permite escribir en la ruta protegida.

> [!warning] No es un reinicio normal
> Reinicia inmediatamente sin sincronizar ni desmontar discos; puede perder escrituras pendientes. Es una operación de emergencia, no un paso rutinario para consultar logs. No aplica a macOS.

Referencia: [documentación del kernel Linux sobre SysRq](https://docs.kernel.org/admin-guide/sysrq.html).

## Log del concentrador desde una fecha y hora

```bash
awk -v d="$(date +%F)" '$0 >= d" 16:30:00"' /srv/concentrador/log/api.log
```

`date +%F` produce la fecha del equipo en formato `AAAA-MM-DD`. `-v d=...` la pasa a awk. `$0` es la línea completa; se imprime cuando su comparación textual es mayor o igual que `fecha 16:30:00`.

Presupone que cada línea comienza con una marca de tiempo ordenable como `AAAA-MM-DD HH:MM:SS`. No exige que la fecha sea exactamente hoy: también admite fechas posteriores. Una línea sin ese formato puede compararse de forma engañosa. Este comando lee el archivo; no lo cambia.

## Log de la aplicación: QR de hoy desde las 15:40

```bash
awk -v hoy="$(date +%F)" 'substr($0,2,10)==hoy && substr($0,13,8)>="15:40:00" && tolower($0) ~ /qr/' /home/pi/config/logs/app.log
```

`substr($0,2,10)` extrae diez caracteres desde la posición 2 y exige la fecha de hoy. `substr($0,13,8)` extrae la hora y la compara con 15:40:00. Esto presupone una línea como `[2026-09-22 15:45:00] mensaje`.

`tolower($0) ~ /qr/` busca la secuencia qr sin distinguir mayúsculas. Puede coincidir dentro de una palabra; no exige una etiqueta exacta. Las tres condiciones se unen con `&&`: deben cumplirse todas. Si el log cambia de formato o zona horaria, revisa el filtro.

## Log de la aplicación: todo lo de hoy desde las 19:10

```bash
awk -v hoy="$(date +%F)" 'substr($0,2,10)==hoy && substr($0,13,8)>="19:10:00"' /home/pi/config/logs/app.log
```

Usa las mismas posiciones de fecha y hora del ejemplo anterior, pero no filtra por QR. Una línea de hoy a las 19:09:59 no pasa; una a las 19:10:00 sí pasa. Los formatos deben mantener ceros iniciales para comparar horas como texto correctamente.

## Abrir MariaDB dentro del contenedor

```bash
docker exec -it c96f7941fbdc mariadb -u root -p concentrador
```

`docker exec` ejecuta un programa en un contenedor que ya está en marcha. `-it` abre una sesión interactiva; el identificador corresponde al contenedor anotado. `mariadb` es el cliente, `-u root` selecciona el usuario, `-p` pide la contraseña y `concentrador` selecciona la base.

Abrir el cliente no modifica por sí solo la base. Las sentencias SQL que ejecutes después sí podrían hacerlo. El ID puede cambiar si se recrea el contenedor; no identifica permanentemente un ambiente.

## Texto para documentar el cierre de un ticket

La frase original es una plantilla de cierre, no evidencia de una intervención realizada hoy:

> Se reinició el dispositivo y se realizó la sincronización correctamente. Se verificó que el equipo se encuentra funcionando con normalidad, por lo que se procede con el cierre del ticket.

Para que el cierre sea comprobable, acompáñalo del equipo/ticket, fecha y hora, problema observado, acción realizada y prueba concreta de funcionamiento. Por ejemplo, indica qué sincronización finalizó y qué operación se comprobó. Usa la frase solo cuando esas verificaciones hayan ocurrido.
