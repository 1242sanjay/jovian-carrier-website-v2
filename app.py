from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "Hello world"

@app.route("/hello")
def hello():
  return "<h2>Hello jovian</h2>"
  


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)