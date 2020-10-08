# pt-twitoff
DSPT7 Unit3 Sprint3 Webapp

This webapp is a functioning Natural Language Processing (NLP) model that uses Logistic Regression to determine
the likelihood of a tweet being written between two selected users using Twitter's API functionality. 

The application is dynamic and customizable, allowing users to add their own favorite twitter users to use for comparison, as well as writing their own sample text to run through the machine.

**Usage:**
    Starting on the middle section, twitter users can be added to the database by typing in their twitter handle (minus the @) and hitting the
    "Add User" button underneath. This will either add the user (if input correctly) or kick back an error (username was incorrect or doesnt exist).
    If trying to add a user already in the database, a message will appear that this user is already in the database.

    When adding, a successful addition will also display the tweets that were captured (only original tweets, not @replies or retweets)
    and added to the database.

    Currently added users are listed above the input field, and clicking on their names furnishes their tweets stored in the database.

    Next, on the left side of the page, one can compare two twitter users from a drop down menu, and input their own text field to run through the predictor. 

**History:**
    Since our api calls are limited to 200 tweets, and out of those last 200 tweets, we filter out retweets and replies, sometimes there is not much history of tweets to use for the model to be trained on. 
    This is remedied by adding user history, up to the max allotment of 3200 tweets. This allows for sufficient history on a user that the model can use to train and improve accuracy.

    On the right side of the page, current twitter users are available in a drop down menu to individually add their entire history to further expand the model's training data.

**Backend**
    This webapp uses SpaCy embeddings to vectorize each word in a tweet, stored in a database along side the tweet. These embeddings are important because when a user-supplied phrase is passed into the predictor, they are used to train the logistic regression model and test and predict using the user-supplied vectors -- thus: a twitter user is predicted based on the analysis of their own history of words and phrases.
