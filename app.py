from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello ArgoCD AutoSync enabled v4 </h1>'
