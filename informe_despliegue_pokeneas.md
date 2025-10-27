
#  Informe de Entrega – Despliegue de POKENEAS en AWS con Docker Swarm

## Autoras:
**Salomé Serna**  
**Maria Clara**
Usuario Docker Hub: **saloserna**

---

##  Descripción general

Se desplegó la aplicación **Pokeneas (Flask)** en un entorno de **AWS EC2**, utilizando **Docker Swarm** para el manejo de réplicas y balanceo de carga.  
La aplicación consume imágenes almacenadas en un bucket **Amazon S3** (`t2-pokeneas`) y muestra frases personalizadas en cada contenedor.

---

##  Pasos realizados

1. **Creación de la instancia EC2**  
   - Sistema operativo: Ubuntu Server 22.04 LTS  
   - Tipo de instancia: `t3.micro` (free tier)  
   - Se configuró un grupo de seguridad con los puertos **22 (SSH)** y **80 (HTTP)** abiertos.  
   - Se generó y descargó la clave `.pem` para conexión segura.

2. **Instalación de Docker y configuración de Swarm**
   ```bash
   sudo apt update && sudo apt install docker.io -y
   sudo systemctl enable docker
   sudo docker swarm init
   ```
   > Resultado: Swarm inicializado correctamente en el nodo manager.

3. **Clonación del repositorio**
   ```bash
   git clone https://github.com/Salome-Serna-R/T2_pokenea-flask.git
   cd T2_pokenea-flask
   ```

4. **Construcción y subida de la imagen a Docker Hub**
   ```bash
   docker build -t saloserna/pokeneas:latest .
   docker login
   docker push saloserna/pokeneas:latest
   ```
   > Imagen disponible públicamente en [Docker Hub](https://hub.docker.com/r/saloserna/pokeneas).

5. **Despliegue del servicio con 10 réplicas**
   ```bash
   docker service create      --name pokeneas      --replicas 10      -p 80:5000      -e S3_BUCKET=t2-pokeneas      -e AWS_REGION=us-east-1      saloserna/pokeneas:latest
   ```

6. **Verificación del servicio**
   ```bash
   docker service ls
   ```
   Resultado:
   ```
   ID            NAME       MODE        REPLICAS  IMAGE
   m6p4daniz4ha  pokeneas   replicated  10/10     saloserna/pokeneas:latest
   ```

---

##  Evidencias

| Evidencia | Descripción | Estado |
|------------|--------------|--------|
|  Imagen subida a Docker Hub | `saloserna/pokeneas:latest` | ✅ |
| Lista de imágenes en S3 | Bucket `t2-pokeneas` con imágenes PNG | ✅ |
|  Swarm con 10 réplicas | Comando `docker service ls` muestra `10/10` | ✅ |
| App funcionando en AWS | IP pública: `3.91.7.187` | ✅ |
|  Balanceo de carga | Diferentes IDs de contenedores al recargar `/ui` | ✅ |

---

##  Conclusiones

- El despliegue en AWS con Docker Swarm fue exitoso.  
- Se validó el balanceo de carga mediante IDs de contenedor distintos.  
- La imagen fue correctamente publicada en Docker Hub.  
- La aplicación Flask se conecta con S3 para obtener imágenes dinámicas.  

>  Proyecto **completamente funcional y operativo**.  
> Link Docker Hub: [https://hub.docker.com/r/saloserna/pokeneas](https://hub.docker.com/r/saloserna/pokeneas)  
> IP pública: `http://3.91.7.187/ui` --> usar este enlace para ver las imagenes

