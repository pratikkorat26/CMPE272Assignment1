from flask import Flask

app = Flask(__name__)

@app.route('/world')
def hello():
    return "World"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6001, debug = True)
