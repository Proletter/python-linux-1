import xgboost as xgb
from flask import Flask
from applicationinsights.flask.ext import AppInsights
app = Flask(__name__)
app.config['APPINSIGHTS_INSTRUMENTATIONKEY'] = '413d7290-841f-4f30-96ac-9353c368cef1'
appinsights = AppInsights(app)

<<<<<<< HEAD
=======

>>>>>>> 932a223758fbb219b1da9f589a181e43ff4b919c

@app.route('/')
def hello_world():
    app.logger.info('Info log entry')
    app.logger.debug('Debug log entry')
    #app.logger.error('Error Entry')
    return 'Hello, World!'


app.run(host = "10.100.100.10", port = 8080)
    
