from flask import Flask, render_template
from flask_socketio import SocketIO, send


app = Flask(__name__)
app.config['SECRET_KEY'] = 'very_secret_string'

socketio = SocketIO(app, cors_allowed_origins='*')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@socketio.on('message')
def handle_message(data):
    send(data, broadcast=True)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    socketio.run(app)