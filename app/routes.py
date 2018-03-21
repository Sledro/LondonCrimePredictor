from flask import render_template
from app import app
<<<<<<< HEAD
from flask import request
import pandas as pd
import numpy as np
#Define our x and y and reshape if needed
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
import datetime
import calendar
# Import smtplib for the actual sending function
import smtplib
# Import the email modules we'll need
from email.mime.text import MIMEText

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    #print(fire())
    return render_template('index.html', title='Home')

##After prediction button on index page is clicked, values passed here.
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        month = request.form['month']
        monthString = calendar.month_name[int(month)]
        year = request.form['year']
        crimeType, crimeCount = loadDataset(month,year)
        return render_template('predict.html', title='Data Analysis App', month=monthString, year=year, crimeType=crimeType, crimeCount=crimeCount)

def loadDataset(month,year):
    #Read data from csv and hold it in our data frame
    df = pd.read_csv('./Dataset/Cleaned.csv', parse_dates=['Month'])
    #Group our data by the number of each type of crimes commit each month
    groupedCrimes= df.set_index('Month', drop=False).groupby(pd.Grouper(level='Month', freq='M'))['Crime type'].value_counts().unstack()
    #I change the dates to be integers, I am not sure this is the best way    
    groupedCrimes.index = pd.to_datetime(groupedCrimes.index)  
    groupedCrimes.index = (groupedCrimes.index - pd.to_datetime('1970-01-01')).days
    y = np.asarray(groupedCrimes)
    X = np.asarray(groupedCrimes.index).reshape(-1, 1)
    #Setup our training data
    X_train, X_test, y_train, y_test = train_test_split(X,y,train_size=.9,random_state=42)
    model = LinearRegression() #create linear regression object
    model.fit(X_train.reshape(-1,1), y_train) #train model on train data
    model.score(X_train, y_train) #check score
    today = datetime.datetime(int(year),int(month),int(31))
    predictMonthEnding = (today - pd.to_datetime('1970-01-01')).days
    ans = model.predict(predictMonthEnding) #Date to predict - converting datetime's to # of days since 1970-01-01
    pt=pd.to_datetime(predictMonthEnding, unit='D') #Convert to human date to display on table
    df = pd.DataFrame(ans[:,:], index=ans[:,0], columns=['Bicycle theft','Burglary', 'Criminal damage and arson','Drugs','Other crime', 'Other theft'
    ,'Possession of weapons','Public order', 'Robbery','Shoplifting','Theft from the person', 'Vehicle crime','Violence and sexual offences'])
    df.insert(0, "Predicted Date", pt) #Add new index 
    df = df.set_index('Predicted Date') 
    series=df.idxmax(axis=1)
    crimeType = series[0]
    series=df.max(axis=1)
    crimeCount = format(series[0], '.0f')
    return crimeType, crimeCount

@app.route('/about')
def about():
    #print(fire())
    return render_template('about.html', title='About us')

@app.route('/contact')
def contact():
    if request.method == 'POST':
        month = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        reply = sendMail(month, email, subject, message)
    return render_template('contact.html', title='Contact us')
    
def sendMail(month, email,subject, message):
    # Open a plain text file for reading.  For this example, assume that
    # the text file contains only ASCII characters.
    fp = open(textfile, 'rb')
    # Create a text/plain message
    msg = MIMEText(fp.read())
    fp.close()

    # me == the sender's email address
    # you == the recipient's email address
    msg['Subject'] = subject
    msg['From'] = email
    msg['To'] = "dan@sledro.com"

    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    s = smtplib.SMTP('localhost')
    s.sendmail(me, [dan@sledro.com], message.as_string())
    s.quit()
    return 0

if __name__ == '__main__':
    app.run(debug=True)
=======
from app.fireTest import fire

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    print(fire())
    return render_template('index.html', title='Home', user=user, posts=posts, fire=fire())

>>>>>>> bf2e4662fbba3b816a800986b701e34632953e98
