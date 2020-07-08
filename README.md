# alpha
run:
pip install pip env
pipenv shell
pip install requirements.txt

Create a postrgresql database
set the database credentials in settings.py
run:

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

cd into alpha_db and run:
npm install
npm run serve
