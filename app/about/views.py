from flask import render_template

from app.about import about

@about.route('/about')
def about():
    return render_template('about.html')