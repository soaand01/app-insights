from flask import Flask
from opencensus.ext.azure.trace_exporter import AzureExporter
from opencensus.ext.flask.flask_middleware import FlaskMiddleware
from opencensus.trace.samplers import ProbabilitySampler

app = Flask(__name__)
middleware = FlaskMiddleware(
    app,
    exporter=AzureExporter(connection_string='InstrumentationKey=1a5086d1-3527-4464-b409-5514da0f7b6a;IngestionEndpoint=https://westeurope-5.in.applicationinsights.azure.com/'),
    sampler=ProbabilitySampler(rate=1.0)
)

@app.route('/')
def hello():
    app.logger.debug('This is a debug log message.')
    app.logger.info('This is an information log message.')
    app.logger.warning('This is a warning log message.')
    app.logger.error('This is an error message.')
    app.logger.critical('This is a critical message.')
    return 'Hello World!'

@app.route('/error')
def error():
    a = 42
    b = 0
    c =a/b
    return "a / b = {c}".format(c=c)

if __name__ == '__main__':
    app.run(host='localhost', port=8080, threaded=True)
