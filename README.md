W celu uruchomienia aplikacji należy wpisać komendy:

pip install -r requirements.txt
python manage.py makemigrations accounts
pyton manage.py makemigrations proj
python manage.py migrate
python manage.py runserver

Na począku należy zarejestrować administratora. W tym celu należy wpisać:

python manage.py createsuperuser
