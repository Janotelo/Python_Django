# Python_Django

### Description
This is my personal version control and backup of files as I learn "Python Django - The Practical Guide" that I got in Udemy. This is the second time I learn this course and got the chance to use github.   
  
Learn how to build web applications and websites with Python and the Django framework by purchasing Python Django - The Practical Guide in Udemy. [Click here to view the course in Udemy.](https://www.udemy.com/course/python-django-the-practical-guide/){:target="_blank"}  

### Note:
1. My final project for this course is not commited in this repository, instead it is private. You can visit my website by clicking [here](http://django-blog3-env.eba-kjabuy9t.ap-southeast-2.elasticbeanstalk.com/){:target="_blank"}  
- The web app is deployed using AWS Elastic Beanstlak.
- The static and uploaded files are serve using AWS S3.
- The database is served using AWS RDS through PostgreSQL.
2. I initialized a Python Virtual Environment for deploying the django server.  
- `python -m venv {name}` - *Command to create Virtual Environment*  
- `{name}\Scripts\activate.bat` - *Command to run Virtual Environment*  
- `python -m pip freeze > requirements.txt` - *Records the environments currect package list into requirements.txt. For deployment*

### Dependencies
Here are the following dependencies installed needed for all projects in this repository:
1. django
2. Pillow

### Useful Commands for Django Framework
1. `python manage.py runserver` - *To deploy the development server locally.*
2. `python manage.py startapp {app_name}` - *To add an app/module inside the project.*
3. `python manage.py makemigrations` - *To initialize the models added in the app or project.*
4. `python manage.py migrate` - *To do migrations.*
5. `python manage.py createsuperuser` - *To create a super user for admin page.*
6. `python manage.py collectstatic` - *To collect all static files from the whole project directory to a single directory. Getting ready for deployment*

### See Documentations for Reference
1. [Django Documentation](https://docs.djangoproject.com/en)
2. [PEP 8 - Style Guide for Python Code](https://peps.python.org/pep-0008/)