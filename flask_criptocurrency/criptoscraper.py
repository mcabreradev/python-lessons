from flask import Flask, json
from crawler import Crawler
app = Flask(__name__)
data = Crawler()


@app.route('/')
def hello_world():
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run(debug=True)
