from flask import Flask

app = Flask("__main__")

@app.route('/')
def home():
    return '<h1> Hello World!!!</h1>'

@app.route('/secondpage')
def page2():
    return '<h1> Dami is here!!!</h1>'