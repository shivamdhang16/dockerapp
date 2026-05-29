from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
<<<<<<< HEAD
    return "Jay hind from india main 5  branch !"
=======
    return "Jay hind from india dev 3 branch !"
>>>>>>> dev

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

