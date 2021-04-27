# Ziwa Blog App
## Description
This web application allows a user to:
* Register.
* Login
* Author and post a blog
* Edit own blog posts
* Comment on blog posts when logged in.
* For forgetten passwords, initiate password reset via an email notification prompt.
* Change password

## Demo
The live site is accesible from https://ziwa.herokuapp.com/

## Installation
### Requirements
* The project is developed and tested using Python - 3.8.5 on ubuntu 20 OS but should work on other environments too.

### Virtual environment
mkdir <project_directory>
cd <project_directory>
pip install virtualenv
virtualenv env venv
source venv/bin/activate

### Cloning the repository
* git clone https://github.com/kennedynjoroge/ziwa.git

### Cloning the repository
pip3 install -r requirements

The following libraries are required
asgiref==3.3.4
crispy-bootstrap5==0.3.1
dj-database-url==0.5.0
Django==3.2
django-crispy-forms==1.11.2
django-heroku==0.3.1
gunicorn==20.1.0
psycopg2==2.8.6
python-decouple==3.4
python-dotenv==0.17.0
pytz==2021.1
sqlparse==0.4.1
whitenoise==5.2.0

### Running Tests
python3.6 manage.py test

## Known Bugs
* The comment functionality is currently working from /admin site only. 
* The whole post is being displayed on main page. Should display only a small snippet and provide read more link.

## Technologies Used
* Source code editor - pycharm
* Git and Github - source code version contrl
* Django framework
* Heroku for production deployment
* Bootstrap - for UI.

## License
MIT License

