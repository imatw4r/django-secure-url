python secure_urls/manage.py migrate
python secure_urls/manage.py collectstatic --no-input
gunicorn --chdir secure_urls secure_urls.wsgi --bind :8000 --log-file -
