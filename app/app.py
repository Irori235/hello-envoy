from flask import Flask

app = Flask(__name__)


@app.route('/')  # type: ignore
def hello_world() -> str:
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
