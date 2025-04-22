from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "DevOps external today ok."

@app.route('/kalyan')
def kal():
    return "kalyan"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)