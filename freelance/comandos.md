echo "b" | sudo tee /proc/sysrq-trigger

awk -v d="$(date +%F)" '$0 >= d" 16:30:00"' /srv/concentrador/log/api.log




awk -v hoy="$(date +%F)" 'substr($0,2,10)==hoy && substr($0,13,8)>="15:40:00" && tolower($0) ~ /qr/' /home/pi/config/logs/app.log

awk -v hoy="$(date +%F)" 'substr($0,2,10)==hoy && substr($0,13,8)>="19:10:00"' /home/pi/config/logs/app.log

docker exec -it c96f7941fbdc mariadb -u root -p concentrador



Se reinició el dispositivo y se realizó la sincronización correctamente. Se verificó que el equipo se encuentra funcionando con normalidad, por lo que se procede con el cierre del ticket.