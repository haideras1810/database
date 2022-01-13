# alpha

## Installation

```bash
pip install pip env
pipenv shell
pip install requirements.txt
```

### Set up Database

Create a postrgresql database
set the database credentials in settings.py
run:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### Set up Front-ends

cd into alpha_db and run:

```bash
npm install
npm run serve
```
