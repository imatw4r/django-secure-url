python secure_urls/manage.py migrate
python secure_urls/manage.py collectstatic
gunicorn --chdir secure_urls secure_urls.wsgi --log-syslog --bind :8000 
