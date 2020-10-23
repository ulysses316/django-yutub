# Taller de Django

## Tutoriales guiados con la documentación oficial.
Estos son los enlaces principales para crear una aplicacion de django paso a paso, pero pueden encontrar mas enlaces de interes en la [Documentacion](https://docs.djangoproject.com/en/3.1/) esta la podras encontrar tanto en ingles como en español.
- [Requests and responses](https://docs.djangoproject.com/en/3.1/intro/tutorial01/)
- [Models and the admin site ](https://docs.djangoproject.com/en/3.1/intro/tutorial02/)
- [Views and templates ](https://docs.djangoproject.com/en/3.1/intro/tutorial03/)
- [Forms and generic views](https://docs.djangoproject.com/en/3.1/intro/tutorial04/)
- [Testing](https://docs.djangoproject.com/en/3.1/intro/tutorial05/)
- [Static files](https://docs.djangoproject.com/en/3.1/intro/tutorial06/)
- [Customizing the admin site](https://docs.djangoproject.com/en/3.1/intro/tutorial07/)

## Instalacion.

1. Clonar el repositorio de github.

`git clone https://github.com/ulysses316/django-yutub.git`

2. Crear un virtual environment (opcional, pero recomendable)

`python3 -m venv venv`

`source venv/bin/activate` # Linux

`./venv/bin/activate` # Windows

Si no podemos crear el ambiente virtual habra que instalarlo.

3. Instalar dependencias.

`pip install -r requirements.txt`

4. Hacer migraciones y correr el servidor

`python manage.py migrate`
`python manage.py runserver`

5. Para salir del entorno virtual

`deactivate`