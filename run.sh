#!/bin/bash
cd network_inventory
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata inventory
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'password')"
python manage.py runserver 0.0.0.0:8000