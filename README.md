# django-app-management
Django App made for internal management in a small office. It supports adding, modifying, vewing, deleting and exporting information through the Django admin panel 
and connected to a Postgresql DB, using Django Jazzmin as interface.
To test it:
- clone repository.
- install requirements.
- create Postgresql DB.
- Use your DB information in the DATABASES section of the settings.py file inside the proyecto1 folder.
- create superuser with the terminal.
- make migrations and migrate.
- run server locally with python manage.py runserver
- go to localhost:8000/admin and login with the superuser 

It may have a lot of bugs since it is only a prototype. I'm working on an english version (this version is currently in spanish only) with a more in detail explanation
of the models and features.
