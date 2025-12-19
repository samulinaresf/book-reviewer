# Book Summary Web

Este es un proyecto web desarrollado con Django para la gestión y visualización de resúmenes de libros.

## Requisitos

- Python 3.x
- Django 5.1
- MySQL
- Git

## Instalación

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/samulinaresf/book-summary-web.git
   cd book-summary-web

2. **Crea y activa un entorno virtual:**
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

3.- **Instala las dependencias:**
pip install -r requirements.txt
Configura el archivo .env:

4.- **En la raíz del proyecto, encontrarás un archivo llamado .env.example. Copia este archivo y renómbralo a .env:**
cp .env.example .env

5.- **Abre el archivo .env y completa las variables necesarias:**
SECRET_KEY='tu_clave_secreta_aquí'
DEBUG=True
DB_NAME='nombre_de_tu_base_de_datos'
DB_USER='tu_usuario_de_base_de_datos'
DB_PASSWORD='tu_contraseña_de_base_de_datos'
Nota: La clave secreta (SECRET_KEY), la información de la base de datos (DB_NAME, DB_USER, DB_PASSWORD) deben ser personalizadas según tu entorno de desarrollo.

6.- **Aplica las migraciones para configurar la base de datos:**
python manage.py migrate

7.- **Crea un superusuario para acceder al panel de administración de Django:**
python manage.py createsuperuser

8.- **Inicia el servidor local:**
python manage.py runserver
Luego, puedes acceder al sitio en http://localhost:8000.

Uso
Visita la página principal en http://localhost:8000 para ver los resúmenes de libros.
Accede al panel de administración de Django en http://localhost:8000/admin utilizando el superusuario creado previamente.
Contribución
Si deseas contribuir a este proyecto, realiza un fork del repositorio y envía tus cambios a través de un pull request.

Licencia
Este proyecto se distribuye bajo la licencia MIT. ¡Siéntete libre de utilizarlo y modificarlo!

Esto es solo una estructura básica que incluye información sobre cómo instalar y configurar el proyecto, cómo iniciar el servidor y una breve explicación sobre la creación del archivo `.env`. Puedes agregar más detalles o ajustar este texto según las necesidades de tu proyecto.
