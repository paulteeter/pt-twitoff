from flask import Flask


def create_app():
    '''Create and configure an instance of our flask application'''
    app = Flask(__name__)
    # app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///twitoff.db'
    # DB.init_app(app)

    @app.route('/')
    def root():
        return 'Welcome to TwitOFF!'
    
    return app