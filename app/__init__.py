from flask import Flask

from app import models
#functional
from app.views import home
# divisional
from app.about import about

app = Flask(__name__)

app.register_blueprint(about)
app.register_blueprint(home.home)