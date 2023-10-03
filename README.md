
## 1. Install Virtual Environment in Python
For installing virtual environment in python use the following command:


Windows-
bash
pip install virtualenv

Linux-
bash
sudo apt install python3-venv

## 2. Create Virtual Environment for Python:-
For creating virtual environment in Python use the following command:

Windows-
bash
python -m venv virtual_environment_name

Linux-
bash
virtualenv my_project

## 3. Activate the Virtual Environment:-

To activate the virtual environment in Python use the following command:

Windows-
bash
virtual_environment_name\Scripts\activate

Linux-
bash
source .venv/bin/activate

## 4. Install Dependencies:-
For Installing dependencies of the project install the requirements.txt file by using the following command:
bash
pip install -r requirements.txt


## 5. Add PostgreSQL credentials for database connectivity:-
For Adding the credentials for database connectivity make some required changes in the .env file.

## 6. Make Migrations:-
Create Migrations for packaging up your model changes into individual migration files and Migrate is responsible for applying those to your database.

The command for making migrations:
bash
python manage.py makemigrations
python manage.py migrate

For Adding the migrations of a particular modal use the following command:
bash
python manage.py makemigrations modal_name

## 7. Run Project:-
To Run the Project use the following command:
bash
python manage.py runserver

