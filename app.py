from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Jay hind from india dev 2 branch !"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

