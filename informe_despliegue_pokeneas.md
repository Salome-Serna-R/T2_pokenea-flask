# Informe de Entrega – Despliegue de POKENEAS en AWS con Docker Swarm

---

## **Autoras**

- **Salomé Serna**  
- **María Clara**

**Usuario Docker Hub:** `saloserna`

---

## **Descripción general**

Se desplegó la aplicación **Pokeneas (Flask)** en un entorno de **AWS EC2**, utilizando **Docker Swarm** para el manejo de réplicas y el balanceo de carga.  

La aplicación consume imágenes almacenadas en un bucket **Amazon S3** denominado `t2-pokeneas`, y muestra información detallada de cada personaje (“pokenea”) a partir de un archivo local **`data.py`**, el cual contiene atributos como nombre, altura, habilidad, frase e imagen asociada.  

El proyecto utiliza contenedores Docker distribuidos mediante Swarm y se encuentra disponible de manera pública en **Docker Hub**.

---

## **Pasos realizados**

### **1. Creación de la instancia EC2**
- Sistema operativo: **Ubuntu Server 22.04 LTS**  
- Tipo de instancia: **t3.micro (free tier)**  
- Se configuró un grupo de seguridad con los puertos **22 (SSH)** y **80 (HTTP)** abiertos.  
- Se generó y descargó la clave **`.pem`** para la conexión segura.

---

### **2. Instalación de Docker y configuración del Swarm**
```bash
sudo apt update && sudo apt install docker.io -y
sudo systemctl enable docker
sudo docker swarm init


Imagen disponible públicamente en:
https://hub.docker.com/r/saloserna/pokeneas