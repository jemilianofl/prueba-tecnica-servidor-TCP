# **Cliente y Servidor TCP en Python**

**Este proyecto implementa un servidor TCP y un cliente TCP en Python para la comunicación en la misma máquina (localhost) utilizando el puerto 5000. El objetivo principal es demostrar el manejo de conexiones TCP y la interacción básica entre cliente y servidor.**

## **Descripción**

### **Servidor TCP**

El servidor se encarga de:

- Escuchar conexiones entrantes en `localhost:5000`.
- Recibir mensajes de los clientes y responder con el mismo mensaje en mayúsculas.
- Gestionar comandos especiales:
  - `APAGAR`: Cierra la conexión con el cliente.
  - `DESCONEXION`: Apaga el servidor de manera remota.
  - `LISTAR`: Envía una lista de los clientes conectados (dirección IP y puerto).

### **Cliente TCP**

El cliente se encarga de:

- Conectarse al servidor en `localhost:5000`.
- Permitir al usuario ingresar mensajes para enviar al servidor.
- Mostrar en consola la respuesta recibida del servidor.
- Cerrar la conexión cuando se envía el comando `APAGAR` o `DESCONEXION`.

## **Requisitos**

- Python 3.x
- No se requiere ninguna librería externa adicional (usa la librería estándar de Python)

## **Instrucciones de Ejecución**

### **1. Clonar el repositorio**

Si aún no lo has hecho, clona el repositorio:

```bash
git clone https://github.com/jemilianofl/prueba-tecnica-servidor-TCP.git
cd prueba-tecnica-servidor-TCP
```

### **2. Ejecutar el Servidor**

Para iniciar el servidor, ejecuta el siguiente comando:

```bash
python servidor.py
```

El servidor se ejecutará en `localhost:5000` y esperará conexiones de clientes.

### **3. Ejecutar el Cliente**

Para iniciar un cliente, ejecuta el siguiente comando en otra terminal:

```bash
python cliente.py
```

El cliente se conectará al servidor y permitirá enviar mensajes. Puedes escribir comandos como:

- `LISTAR` para ver los clientes conectados.
- `APAGAR` para cerrar la conexión del cliente.
- `DESCONEXION` para apagar el servidor.
- `HOLA CLIENTE`: Saludo al cliente.

## **Autor**

Desarrollado por José Emiliano Flores Pérez