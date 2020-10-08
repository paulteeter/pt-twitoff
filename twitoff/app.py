from os import getenv
from flask import Flask, render_template, request
from .db_model import DB, User, Tweet
from .twitter import add_user_tweepy, update_all_users
from .predict import predict_user




def create_app():
    '''Create and configure an instance of our flask application'''
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URL')
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

    @app.route('/compare', methods=['POST'])
    def compare(message=''):
        user1 = request.values['user1']
        user2 = request.values['user2']
        tweet_text = request.values['tweet_text']

        if user1 == user2:
            message = 'Cannot compare a user to themselves!'
        else:
            prediction = predict_user(user1, user2, tweet_text)

            message = f'''{tweet_text} is more likely to be said by {user1 if prediction else user2} 
                          than {user2 if prediction else user1}'''

        return render_template('predict.html', title='Prediction', message=message)


    @app.route('/update', methods = ['GET'])
    def update():
        update_all_users()
        return render_template('base.html', title="All Tweets updated!",
                        users=User.query.all())

    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template('base.html', title='Reset!')
        
    return app