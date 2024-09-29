# Task Manager en Python con MySQL

Este proyecto es una aplicación de gestión de tareas desarrollada en Python, utilizando MySQL como base de datos para almacenar las tareas. Permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) en una lista de tareas.

## Características

- Añadir nuevas tareas.
- Listar todas las tareas.
- Actualizar el estado de una tarea (pendiente o completada).
- Eliminar tareas.

## Requisitos

Antes de comenzar, asegúrate de tener lo siguiente instalado en tu sistema:

- **Python 3.x**
- **MySQL Server** (y MySQL Workbench para gestionar gráficamente la base de datos)
- **Paquetes de Python** necesarios (ver más abajo).

## Instalación

### 1. Clonar el repositorio

Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/tuusuario/nombre-del-repositorio.git
   ```

cd nombre-del-repositorio


### 2. Crear un entorno virtual (opcional pero recomendado)
Para aislar las dependencias, crea un entorno virtual:
```sh
 python -m venv venv
   ```
 ```sh
    venv\Scripts\activate
    ```

### 3. Instalar dependencias
Instala los paquetes necesarios ejecutando:
 ```sh
   pip install -r requirements.txt
    ```

### 4. Configurar la base de datos MySQL
Abre MySQL Workbench o cualquier otro cliente de MySQL.
Crea la base de datos y las tablas necesarias ejecutando el siguiente script:
sql
Copiar código
CREATE DATABASE task_manager;

USE task_manager;

CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    status ENUM('pending', 'completed') DEFAULT 'pending'
);
5. Configurar el archivo de conexión a la base de datos
Crea un archivo config.py en el directorio raíz del proyecto con la siguiente configuración para conectarse a la base de datos:

python

db_config = {
    'host': 'localhost',
    'user': 'root',  # Cambia 'root' por tu usuario de MySQL
    'password': 'tu_contraseña',  # Cambia 'tu_contraseña' por tu contraseña de MySQL
    'database': 'task_manager'
}
Uso
Ejecutar el programa
Para iniciar la aplicación de gestión de tareas, ejecuta el siguiente comando:


python main.py
## Funcionalidades
### El programa ofrece las siguientes opciones a través de un menú interactivo:

- Añadir una nueva tarea.
- Ver todas las tareas.
- Actualizar el estado de una tarea.
- Eliminar una tarea.
- Salir del programa.
