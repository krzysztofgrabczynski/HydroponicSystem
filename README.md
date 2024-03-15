# <p align=center> <a name="top">HydroponicSystem</a></p>  

Project implemented as part of a recruitment task.

## Description

Application for managing hydroponic systems. Provides CRUD operations for hydroponic systems, performs measurmenets for specific system, displays a list of systems the user owns, and retrieves system information with recent saved measurements. Application has user management: authorization and authentication (token authentication).

The project uses Docker, PostgreSQL database, linters such as Flake8 and Black formatting. The application has also been tested by unit tests (using pytest) and by using Postman.

If you want to check out my other projects [click here.](https://github.com/krzysztofgrabczynski)

## Tools used in project

<p align=center><a href="https://www.python.org"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="60" height="60"/></a> 
<a href="https://www.djangoproject.com/"> <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="60" height="60"/> </a>
<a href="https://git-scm.com/"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/git/git-original.svg" alt="git" width="60" height="60"/> </a> 
<a href="https://www.postgresql.org.pl/"> <img src="https://raw.githubusercontent.com/devicons/devicon/55609aa5bd817ff167afce0d965585c92040787a/icons/postgresql/postgresql-original-wordmark.svg" alt="psql" width="60" height="60"/> </a>
<a href="https://www.docker.com/"> <img src="https://raw.githubusercontent.com/devicons/devicon/55609aa5bd817ff167afce0d965585c92040787a/icons/docker/docker-original-wordmark.svg" alt="docker" width="60" height="60"/> </a></p>


## Directory tree

```
├───core                              # Main direcory of the project with files such as 'settings.py', etc.
└───src                               # Directory with apps
    ├───hydroponic_system             # Directory with hydroponic system management
    └───user                          # Directory with user management (authorization and authentication)
├───tests                             # Directory with unit tests
|
│   .gitignore
│   Dockerfile
│   README.md
│   docker-compose.yml
│   docker-entrypoint.sh              # Entrypoint file with actions such as migrations, unittesting, etc.
│   manage.py
│   requirements.txt                  # txt file with dependencies
```

## Install for local use (using Docker)
- Clone the repository
- Create .env file and add requirement variables such as 'SECRET_KEY' or database parameters
- Build the Docker image using ``` docker-compose build ```
- Run containers using ``` docker-compose up ```
- Everything done! 

## Install for local use (using local virtual environment and bash)
- Clone the repository
- Create virtual environment using ``` python -m venv venv ``` in project directory
- Use ``` . venv/Scripts/activate ``` to activate the virtual environment
- Install required packages by ``` pip install -r requirements.txt ```
- Create .env file and add requirement variables such as 'SECRET_KEY' or database parameters
- Enter the ``` python manage.py migrate --run-syncdb ``` to update migrations
- Now, you can run the application with this: ``` python manage.py runserver ```
- Everything done! You can open Instagram app in your browser by ctrl + left click on http link in your console

 ## How to use that app after installing
-
-
-

[Go to top](#top) 
