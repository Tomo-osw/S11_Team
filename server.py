import os, flask
PORT = int(os.environ['PORT'])
app = flask.Flask('app server')

@app.route("/")
def index():
  return 'Hello, DockerFile'

app.run(debug=True, host='0.0.0.0', port=80)