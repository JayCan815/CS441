
from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def index():
        return 'Web App with Python Flask!'
@app.route('/bye')
def indexx():
        return 'Bye!'

app.run(host='0.0.0.0', port=80)
