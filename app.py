from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

messages = []


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/messages', methods=['GET', 'POST'])
def handle_messages():
    if request.method == 'POST':
        message = request.json.get('message')
        if message:
            messages.append(message)
            return jsonify({'status': 'Message received'}), 201
        return jsonify({'status': 'No message received'}), 400
    elif request.method == 'GET':
        return jsonify({'messages': messages}), 200


if __name__ == '__main__':
    app.run(debug=True, port=6600)
