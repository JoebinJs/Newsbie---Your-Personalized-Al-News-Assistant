from flask import Flask, request, render_template
import requests

app = Flask(__name__)

def get_latest_news(api_key, country='in', topic=None):
    if topic:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&category={topic}&apiKey={api_key}'
    else:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}'
    response = requests.get(url)
    data = response.json()
    return data['articles']

@app.route('/', methods=['GET', 'POST'])
def index():
    articles = []
    if request.method == 'POST':
        topic = request.form.get('topic')
        api_key = '21152fc2960e494ea5d7e7511cca3278'
        articles = get_latest_news(api_key, topic=topic.lower())
    return render_template('index.html', articles=articles)

if __name__ == '__main__':
    app.run(debug=True)
