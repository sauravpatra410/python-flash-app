from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Flask deployed using app service in azure"

if __name__ == "__main__":
    # Bind to 0.0.0.0 so it's accessible outside the container
    app.run(host='0.0.0.0', port=5000)
