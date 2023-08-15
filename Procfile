web: python3 -m venv myvenv
web: source myvenv/bin/activate
web: python3 -m pip install --upgrade pip
web: pip install -r requirements.txt
web: python manage.py makemigrations
web: python manage.py migrate
web: python manage.py updatedict
web: python manage.py runserver 0.0.0.0:51000
