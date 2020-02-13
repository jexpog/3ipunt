# 3ipunt

## Backup

En los ficheros de backupdb y backupweb son los script de python3 para ejecutar backups.

Hay con crontab que ejecuta esto todos los días y cuando tiene mas de 15 días los elimina.


## EndPoints


Moodle esta instalado en la url:

https://moodle.startpime.com/

Grafana con la monitorización del servidor

https://grafana.startpime.com

Vereis que hay mas virtualhost en concreto prometheus.
Con prometheus sacamos las métricas luego las mostramos en grafana. 

Prometheus lo podemos configurar para las métricas obtener lo que deseamos.

## Instalacion de moodle

- Ultima version estable

- php 72

- MariaDB 10.1.44

## Ansible

He creado un role de ansible para la instalación inicial mariadb + php + apache.

descarga el cms y lo descomprime en la ruta indicada.










