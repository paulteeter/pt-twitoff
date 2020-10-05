from flask import Flask, render_template, request
from .db_model import DB, User, Tweet
from .twitter import add_user_tweepy



def create_app():
    '''Create and configure an instance of our flask application'''
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///twitoff.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(app)

    @app.route('/')
    def root():
        return render_template('base.html', title='Home',
            users=User.query.all())

    @app.route('/user', methods=['POST'])
    @app.route('/user/<name>', methods=['GET'])
    def add_or_update_user(name=None, message=''):
        name = name or request.values['user_name']
        
        try:
            if request.method == 'POST':
                add_user_tweepy(name)
                message = 'User {} successfully added to DB'.format(name)
            tweets = User.query.filter(User.username == name).one().tweet
        except Exception as e:
            print('Error adding {}: {}'.format(name, e))
            raise e
            tweets =  []

        return render_template('user.html', title=name, message=message, tweets=tweets)
    
    @app.route('/tweets/<user>/<tweet>')
    def add_tweet(user, tweet):
        tweet = Tweet(user=user, tweet=tweet)
        DB.session.add(tweet)
        DB.session.commit()

        return f'The tweet has been added to the tweet table!'

    return app

    # if __name__ == "__main__":
    #     app.run()