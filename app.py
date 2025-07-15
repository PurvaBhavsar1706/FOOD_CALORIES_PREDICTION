# Flask main application file
from flask import Flask, render_template, redirect, url_for
from auth import auth as auth_blueprint
from predict import predict as predict_blueprint

app = Flask(__name__)
app.secret_key = 'your_secret_key'

app.register_blueprint(auth_blueprint)
app.register_blueprint(predict_blueprint)

@app.route('/')
def index():
    return redirect(url_for('auth.login'))

if __name__ == '__main__':
    app.run(debug=True)
