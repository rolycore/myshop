# MyShop - Documentación del Proyecto

## Descripción
MyShop es una aplicación web de comercio electrónico desarrollada con Django. Permite a los usuarios ver una lista de productos, ver detalles de productos individuales y realizar compras a través de un carrito de compras.

## Funcionalidades Principales
- Listado de productos con paginación.
- Detalles de productos con imágenes, descripción y precio.
- Agregar productos al carrito de compras.
- Administración de productos (CRUD) para administradores.
- Autenticación de usuarios.
- Carrito de compras persistente para usuarios registrados.

## Instalación y Configuración

### Requisitos Previos
- Python 3.11.x
- Django 5.0.x
- Git (opcional, para clonar el repositorio)

### Pasos de Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/rolycore/myshop.git
   cd myshop
   ```

2. **Configurar el entorno virtual:**
   ```bash
   python -m venv env
   env\Scripts\activate  # En Windows
   source env/bin/activate  # En macOS/Linux
   ```

3. **Instalar las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Aplicar las migraciones de Django:**
   ```bash
   python manage.py migrate
   ```

5. **Cargar datos de ejemplo (opcional):**
   ```bash
   python manage.py loaddata initial_data
   ```

6. **Iniciar el servidor de desarrollo:**
   ```bash
   python manage.py runserver
   ```

7. **Acceder a la aplicación:**
   Abre tu navegador y visita `http://127.0.0.1:8000/`.

## Estructura del Proyecto

- **myshop/**: Directorio principal del proyecto Django.
  - **shop/**: Aplicación principal que maneja las funcionalidades del comercio electrónico.
  - **templates/**: Directorio que contiene las plantillas HTML de la aplicación.
  - **static/**: Directorio para archivos estáticos como CSS, JavaScript e imágenes.
  - **media/**: Directorio donde se almacenarán las imágenes subidas por los usuarios.
  - **manage.py**: Script de gestión del proyecto Django.

## Uso

- **URLs importantes:**
  - `/`: Página principal con listado de productos.
  - `/product/<id>/<slug>/`: Detalles de un producto específico.
  - `/admin/`: Panel de administración de Django (requiere autenticación como superusuario).

## Contribución

Si deseas contribuir a este proyecto, sigue los pasos a continuación:

1. Fork el repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Agrega nueva funcionalidad'`).
4. Push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Crea un nuevo Pull Request.

## Créditos

Desarrollado por [Rolando Salinas](https://github.com/rolycore).

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## Contacto

Para cualquier consulta o problema, puedes contactarme a través de [shalomsolutiontech@gmail.com](mailto:shalomsolutiontech@gmail.com).
