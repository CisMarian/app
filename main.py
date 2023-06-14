from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    data = {
        "status": "ok",
        "data": "jakies dane"
    }
    return jsonify(data)


if __name__ == "__main__":
    app.run()
