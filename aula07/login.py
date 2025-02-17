from flask import Flask, request, render_template_string

app = Flask(__name__)

usuarios = [
    {'login': 'joca', 'senha': '123'},
    {'login': 'maria', 'senha': '456'},
    {'login': 'joao', 'senha': '789'}
]


@app.route('/')
def index():
    return 'Hello Word!'


if __name__ == '__main__':
    app.run(debug=True)
