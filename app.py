from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Welcome'

@app.route('/v1/inspiration-score')
def api_articles():
    return 'Searched'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5001)
