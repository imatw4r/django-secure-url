# Functionalities:

- [x] A form that adds links or files for protection
- [x] Generating links protected with a password
- [x] Expiry of links after a specified time
- [x] A form that allows you to go to a secured link or download a protected file
- [x] Counting correct redirects
- [x] User Agent saving
- [x] REST API
- [x] The secured endpoint for adding elements
- [x] The secured endpoint for downloading statistics
- [x] An open endpoint to access secure items (if the password was correct)
- [x] Admin panel

# Requirements

- python3.8
- pipenv
- docker
- docker-compose

# Running application

0. Run `cp env_example .env`
1. Execute command `docker-comopse up --build`
2. Nginx server application on `localhost:8000`
3. Gunicorn server application on `localhost`

> Warning
>
> > Serving files with Gunicorn works only in DEBUG=True mode.

# Endpoints

1. `login` - login
2. `logout` - logout
3. `api/url` - Secure URL API
4. `api/file` - Secure File API
5. `api/url/redirect/<pk>` - Url Redirect Retrieve API
6. `api/file/redirect/<pk>` - File Redirect Retrieve API
7. `api/stats/overall` - File/Url count endpoint APi
