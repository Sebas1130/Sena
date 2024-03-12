# django-CRUD
Una aplicación sencilla construida con Django

### Setup
Actualizar el sistema
```bash
sudo apt-get update
```
Para obtener este repositorio, ejecute el siguiente comando dentro de su terminal habilitada para git
```bash
git clone  https://github.com/Sebas1130/Sena.git
```

Antes de correr la aplicacion tienes que tener instalado docker si no lo tienes instalado puedes seguir estas instruciones

```bash

https://docs.docker.com/engine/install/

```

Una vez instalado docker puede seguir con estos comandos Para correr la aplicacion y levantar los contenedores

Primero construye la imagen 
```bash
export COMPOSE_FILE=local.yml; docker-compose build
```

Despues levantamos los contendores
```bash
export COMPOSE_FILE=local.yml; docker-compose up
```

Una vez que el servidor esté hosted dirígete a http://0.0.0.0:8000/api/empleados/ o http://0.0.0.0:8000/api/calcularPuntaje/

Saludos y feliz codificación :)
