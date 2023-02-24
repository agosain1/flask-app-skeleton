# A skeleton  Flask app for creating production ready apps

## Structure:
- `appServer` dir - Contains the flask initialization and API server code.
- `tests` dir - Unit tests 

## Build
- make-image.sh

Builds the docker image. 

## Makefile
- build: Builds the docker image.
- run: Runs the docker image.
- kill: Cleans up the docker container and image.

## Gunicorn
- Gunicorn is the python based WSGI HTTP Server to allow concurrency and load management in Production systems.
- gunicorn appServer:"create_app()" -w 2 --threads 2 -b 0.0.0.0:8001

## Third-Party Libs
Name     | Version
---------|------------
Flask    | latest
Gunicorn | latest

## The Blueprint class takes three basic arguments:
api = Blueprint('api', 'api', url_prefix='/api')
The first argument is the blueprints name

The second argument is very important it’s the import_name. This name has to be set to the name of our package (which is also api) as Flask uses the import_name for some internal operations such as locating the template folder of the blueprint and locating various files and objects of the main application from the blueprint. (This ensures that methods like render_template and send_static_files work properly and give us the actual files that we want)

The third argument is the url prefix of the blueprint. With this we were able to remove the redundancy of prefixing all our api urls with /api.

## Put the config settings in instance/app_settings.py and make sure .gitignore has instance/ Also names must be UPPERCASE

## Ubuntu: sudo apt-get install psycopg2 libpq-dev python-dev
