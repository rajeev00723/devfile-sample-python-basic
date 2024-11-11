from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():
    name = request.json.get("name", "Rajeev")
    message = f"Hello, {name}! Welcome to the interactive Flask app!"
    return jsonify(message=message)

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)
    app.run(port=port, host='0.0.0.0')
