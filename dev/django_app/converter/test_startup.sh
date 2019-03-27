sleep 10
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
python manage.py shell < test_initial.py
python manage.py runserver
gunicorn -b 0.0.0.0:8000 converter.wsgi
