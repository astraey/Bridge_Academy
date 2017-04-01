from flask import Flask
import home, singlePrize, exercises, prizes, profile, singleExercise

app = Flask(__name__)


@app.route('/')
def hello():
    return home.homeGenerator()

if __name__ == '__main__':
    app.run()
