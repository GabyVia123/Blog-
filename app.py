from flask import Flask

app = Flask("hello")

@app.route("/")
@app.route("/hello")
def hello():
    return "Hello Word"

@app.route("/meucontato")
def meuContato():
    return render_template(index.html)