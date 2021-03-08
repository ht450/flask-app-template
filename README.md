# flask-app-template
My template Flask App for quickly getting started with Flask.

## Blueprints
This app is set up using Flask Blueprints and has both functional (home) and divisional (about) blueprint examples. 
Both are registered at `app/__init__.py`. 

Delete whichever type you don't need.

See http://exploreflask.com/en/latest/blueprints.html for differences between them.
* funtional pattern: home 
  * files are separated by type
  * view file is in `app/views` 
  * templates in `app/templates/home`
* divisional pattern: about
  * files are separated out into their functions
  * view file and templates all contained in `app/about` directory

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
