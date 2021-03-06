from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/ShoeHappy')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()
shoes = db.shoes


db = client.get_default_database()
shoes = db.shoes
comments = db.comments

client = MongoClient()
db = client.Playlister
shoes = db.shoes


app = Flask(__name__)


@app.route('/')
def home():
    """
    Takes the user to the home/main page of the website
    """

    return render_template('main.html')

@app.route('/questions', methods=['GET', 'POST'])
def index():
    """

    """
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('question_category.html')


@app.route('/question_category')
def question_category():
    """
    This takes the user to the question category page
    """
    return render_template('question_category.html')

@app.route('/comfort')
def questions_for_comfort():
    """
    This takes the user to the questions about comfort
    """
    return render_template('comfort.html')

@app.route('/style')
def questions_for_style():
    """
    This takes the user to the questions about style
    """
    return render_template('style.html')

@app.route('/needs')
def questions_for_needs():
    """
    This takes the user to the questions about needs
    """
    return render_template('needs.html')

@app.route('/results/')
def results():
    """
    This takes the user to the results page
    """
    return render_template('results.html')

@app.route('/real_results')
def real_results():
    """
    takes the user to a different results page
    """
    return render_template('real_results.html')

@app.route('/more_results/')
def more_results():
    """
    Takes the user to a different results page
    """
    return render_template('more_results.html')

@app.route('/fun')
def fun():
    return render_template('fun.html')
    

if __name__ == '__main__':
    app.run(debug=True)