import pyrebase
import os

def fire():
    config = {
        "apiKey": "AIzaSyBTOy5F3Gl0t0P4_7DYUYUCm6JYwjUZnVU",
        "authDomain": "londoncrimepredictor.firebaseapp.com",
        "databaseURL": "https://londoncrimepredictor.firebaseio.com",
        "storageBucket": "londoncrimepredictor.appspot.com",
        "serviceAccount": "/Users/sledro/Documents/firebaseServiceAccountKey.json"
    }

    passw = os.environ['YOUR_ENV_VARIABLE']
    firebase = pyrebase.initialize_app(config)

    # Get a reference to the auth service
    auth = firebase.auth()

    # Log the user in YOUR_ENV_VARIABLE is a local mac veriable set via bash $ export YOUR_ENV_VARIABLE=your_password
    # By using this I can keep my password off github
    user = auth.sign_in_with_email_and_password("admin@sledro.com", os.environ['YOUR_ENV_VARIABLE'])

    # before the 1 hour expiry:
    user = auth.refresh(user['refreshToken'])
    # now we have a fresh token
    user['idToken']

    # Get a reference to the database service
    db = firebase.database()
    fires = db.child("items").child("item").child("0").child("batters").get(user['idToken']).val()
    return(fires)
  
