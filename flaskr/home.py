from flask import (
        Blueprint, flash, g, redirect,
        render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

lbp = Blueprint('home', __name__)

@lbp.route('/') 
def home():
    return render_template('landing-page/index.html') 