from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
        return "This is a basic server"

if __name__ == "__main__":
    app.run(debug = True)