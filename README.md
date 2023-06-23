# Preparación de archivos, carpetas, Git y entorno virtual para el proyecto Django

Para ver este archivo con mayor legibilidad, presionar `control + shift + v`

- Extensiones sugeridas para Visual Studio Code y Python

    1. Python (necesario para cualquier proyecto Python)
    2. Pylance (necesario para cualquier proyecto Python)

## Creación de la estructura del proyecto

- Crear la carpeta `Proyecto`
- Abrir VSCode en esa carpeta

## Crear el entorno virtual

```
python -m venv .venv
```

- Activar el entorno desde VSCode como se indica en las diapositivas.

## Crear la estructura del proyecto

- Crear la carpeta `project`
- Crear el archivo `.gitignore`
- Crear el archivo `README.md`

## Instalación de Django

```
pip install django
```

## Preparar Git

- Agregar en `.gitignore` las siguientes líneas:

```
.venv
!**/migrations/__init__.py
**/migrations/*.py
__pycache__/
```

## Inicialización de Git

- Realizar el primer commit, sin el cual no se puede crear otra rama

```
git init
```

Nota: Git puede pedirte tu configuración (nombre y email) si aún no lo has hecho. Ver clase 16

## Crear el proyecto Django y ejecutar el servidor Django

```
cd project
django-admin startproject config .
python manage.py runserver
```

- Abrir el navegador y ejecutar el servidor Django en la dirección `127.0.0.1:8000`

## Cambiar el idioma de Django a español y probar

- Abrir `project/config/settings.py`
- Buscar la variable constante llamada `LANGUAGE_CODE` que es una cadena. Cambiar `'en-us'` por `'es'`

```
python manage.py runserver
```

- Abrir el navegador y ejecutar el servidor Django en la dirección `127.0.0.1:8000`

## Primer commit y nueva rama de desarrollo

```
git add .
git commit -m "Primer commit"
```

Nota: Visual Studio Code puede pedir tus credenciales cuando haces tu primer commit

- Crear rama para el desarrollo llamada "prueba" y cambiarse a ella

```
git branch prueba
git checkout prueba
```

##  ✏️ Agregar el código hecho en clase y que parte está en las diapositivas

## Fusionar cambios en la rama principal y luego volver a la de desarrollo o prueba

```
cd ..
cd ..
git add .
git commit -m "Creación de la estructura del proyecto"
git checkout master
git merge prueba
git checkout prueba
```

## Publicar el repositorio en GitHub

- Presionar `control + shift + p`
- Escribir: "git publicar rama"
- Elegir publicar público
- Visita tu sitio GitHub y corrobora que estén tu repositorio publicado
