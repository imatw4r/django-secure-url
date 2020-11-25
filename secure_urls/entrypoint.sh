python manage.py migrate
python manage.py collectstatic --no-input
gunicorn secure_urls.wsgi --bind :8000 --access-logformat  "{'remote_ip':'%(h)s','request_id':'%({X-Request-Id}i)s','response_code':'%(s)s','request_method':'%(m)s','request_path':'%(U)s','request_querystring':'%(q)s','request_timetaken':'%(D)s','response_length':'%(B)s'}" --access-logfile -
