from flask import Flask
from .db_model import DB, User, Tweet



def create_app():
    '''Create and configure an instance of our flask application'''
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///twitoff.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(app)

    @app.route('/')
    def root():
        return 'Welcome to TwitOFF!'

    @app.route('/<username>/<followers>')
    def add_user(username, followers):
        user = User(username=username, followers=followers)
        DB.session.add(user)
        DB.session.commit()

        return f'{username} has been added to the DB!'
    
    @app.route('/tweets/<user_id>/<tweet>')
    def add_tweet(user_id, tweet):
        tweet = Tweet(user_id=user_id, tweet=tweet)
        DB.session.add(tweet)
        DB.session.commit()

        return f'The tweet has been added to the tweet table!'

    return app

    # if __name__ == "__main__":
    #     app.run()