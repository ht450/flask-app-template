# flask-app-template
<<<<<<< HEAD
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
=======
My template flask app for quickly getting started with flask.

Run the setup script (windows) to set up the virtual environment and install the necessary modules, then you can delete it. 
(for mac and linux, replace `venv\Scripts\activate` with `venv\bin\activate`)

This app is set up using flask blueprints.
It has both a functional (home) and divisional (about) blueprint as examples. 
Delete whichever type you don't need.
See http://exploreflask.com/en/latest/blueprints.html for differences between them.
>>>>>>> ccb671fc4eba1096c6f50e677e0b80504294d90a
