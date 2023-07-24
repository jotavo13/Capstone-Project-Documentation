pip3 install -r deps.txt

python manage.py collectstatic --no-input

python manage.py migrate
