from flask import Blueprint

about = Blueprint(
    'about',
    __name__,
    template_folder='templates',
    static_folder='static'
)

from app.about import views