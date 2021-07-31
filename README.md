# Profiles REST API Code

Source Code for Profiles REST API

## To add the python virtual environment run the below commands
pip install virtualenv
virtualenv myenv
## Or we can run the below command to create a new python virtual environment
python -m venv myenv
### To activate the virtual environemnt
myenv/Scripts/activate
### To deactivate the virtual environment
deactivate

## To install the required packages in the virtual environment
### Activate the virtual environment and run the below command
pip install -r requirement.txt

## To create a Django project
### Activate the virtual environment and run the below command
django-admin.py startproject profiles_project .

## To create a new Django app within the same root folder
### Activate the virtual environment and run the below command
python manage.py startapp profiles_api

## To run the Django server from the virtual environment
### Make sure to activate the virtual environment and run the below command
python manage.py runserver
### With this you can access it on browser using "localhost:8000/"

##