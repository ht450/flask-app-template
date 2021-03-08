from flask import render_template

from app.about import bp

@bp.route('/about')
def about():
    return render_template('about.html')