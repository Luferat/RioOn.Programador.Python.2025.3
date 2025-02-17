from flask import Flask, request, render_template_string

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello Word!'


if __name__ == '__main__':
    app.run(debug=True)
