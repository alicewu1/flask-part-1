from flask import Flask

app = Flask(__name__)

@app.route('/') ## .route creates landing page for app
def hello_world():
    return 'Hello world!'

@app.route('/career')
def career():
    return 'This is our career page...'

@app.route('/dashboards')
def dashboards():
    return 'This is our list of dashboards!'

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=80) ## .run actually runs the app