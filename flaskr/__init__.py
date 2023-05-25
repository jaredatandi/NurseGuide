import os
from flask import Flask, render_template
from flask_fontawesome import FontAwesome

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    fontawesome = FontAwesome(app)
    app.config.from_mapping(
            SECRET_KEY = 'dev',
            DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
            )
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    @app.route('/hello')
    def hello():
        return 'Hello there' 

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import home
    app.register_blueprint(home.lbp)

    return app