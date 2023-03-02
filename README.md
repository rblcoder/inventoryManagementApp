# inventoryManagementApp
An inventory management system

Create a virtual environment
```shell
python -m venv venv
```
Activate the virtual environment using
```shell
source venv/bin/activate
```
Upgrade pip
```shell
pip install --upgrade pip
```
Run migration
```shell
python manage.py migrate
```
Create a superuser
```shell
python manage.py createsuperuser
```
To run the application:
```shell
python manage.py runserver
```

To deploy this to Elastic Beanstalk by uploading a zip file containing the code:
To zip the files for uploading to Elastic Beanstalk
```shell
git archive -v -o myapp.zip --format=zip HEAD
```
After uploading the zip file from Elastic Beanstalk console, edit enviroment variables in Elastic Beanstalk console under environment -> Configuration -> Software -> Environment Properties 

set APP_HOST to the url of the Elastic Beanstalk application

set SECRET_KEY 
To generate a secret key refer to https://www.educative.io/answers/how-to-generate-a-django-secretkey

set IS_DEVELOPMENT to False

Used the bootstrap theme
https://startbootstrap.com/previews/sb-admin
