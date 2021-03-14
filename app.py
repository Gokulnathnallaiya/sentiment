
from flask import request, jsonify, Flask
import flask

from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer



app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return  "hello world"

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    text = request.form.get('text')
    
    blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())
    if(blob.sentiment[1]>blob.sentiment[2]):
        return "positive"
    elif (blob.sentiment[1]<blob.sentiment[2]):
        return "negative"
    else:
        return "neutral"

    


# # A route to return all of the available entries in our catalog.
# @app.route('/api/v1/resources/books/all', methods=['GET'])
# def api_all():
#     return jsonify(books)

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)