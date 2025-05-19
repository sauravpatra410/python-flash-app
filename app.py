from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Flask on port 5000!'

if __name__ == '__main__':
    app.run(port=5000)
