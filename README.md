# flask-app-template
template flask app for getting started quickly

## Blueprints
Contains 2 blueprint patterns to choose from. Both are registered at app/__init__.py, delete as appropriate.
* funtional pattern: home 
  * files are separated by type
  * view file is in app/views 
  * templates in app/templates/home
* divisional pattern: about
  * files are separated out into their functions
  * view file and templates all contained in app/about directory

## Getting Started
To install the requirements:
```
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
```
to run the app
```
flask run
```