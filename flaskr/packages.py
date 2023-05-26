from flask import (
        Blueprint, flash, g, redirect,
        render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

pbp = Blueprint('packages', __name__)

@pbp.route('/packages') 
def packages():
    packages = [
        {
            'category': 'learn',
            'price': '$49.00',
            'image': 'static/home/assets/images/meeting-01.jpg',
            'date': 'Nov 12',
            'title': 'Get NCLEX Exam Materials',
            'description': 'Morbi in libero blandit lectus cursus ullamcorper.',
            'alt': 'NCLEX Prep'
        },

        {
            'category': 'book',
            'price': '$50.00',
            'image': 'static/home/assets/images/meeting-01.jpg',
            'date': 'Nov 12',
            'title': 'Best and Cheap AirBnB',
            'description': 'Morbi in libero blandit lectus cursus ullamcorper.',
            'alt': 'Book Airbnb'
        },
        
        {
            'category': 'travel',
            'price': '$114.00',
            'image': 'static/home/assets/images/meeting-01.jpg',
            'date': 'Nov 12',
            'title': 'New Lecturers Meeting',
            'description': 'Morbi in libero blandit lectus cursus ullamcorper.',
            'alt': 'NCLEX Prep'
        },
        
        {
            'category': 'book',
            'price': '$50.00',
            'image': 'static/home/assets/images/meeting-01.jpg',
            'date': 'Nov 12',
            'title': 'New Lecturers Meeting',
            'description': 'Morbi in libero blandit lectus cursus ullamcorper.',
            'alt': 'NCLEX Prep'
        },
        
        {
            'category': 'travel',
            'price': '$14.00',
            'image': 'static/home/assets/images/meeting-01.jpg',
            'date': 'Nov 12',
            'title': 'New Lecturers Meeting',
            'description': 'Morbi in libero blandit lectus cursus ullamcorper.',
            'alt': 'NCLEX Prep'
        },

        {
            'category': 'learn',
            'price': '$14.00',
            'image': 'static/home/assets/images/meeting-01.jpg',
            'date': 'Nov 12',
            'title': 'New Lecturers Meeting',
            'description': 'Morbi in libero blandit lectus cursus ullamcorper.',
            'alt': 'NCLEX Prep'
        },
    ]

    return render_template('packages/packages.html', packages=packages ) 

# @pbp.route('/packages/packages-details') 
# def details():
#     return render_template('packages/packages-details.html')

@pbp.route('/packages/details')
def details():
    return render_template('packages/package-details.html')