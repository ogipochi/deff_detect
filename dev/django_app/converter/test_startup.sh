sleep 10
python manage.py makemigrations
python manage.py migrate
python manage.py shell < test_initial.py
python manage.py runserver
