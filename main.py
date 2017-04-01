from flask import Flask, render_template
import home, singlePrize, exercises, prizes, profile, singleExercise

app = Flask(__name__)


@app.route('/')
def hello():
	return app.send_static_file('index.html')

#@app.route('/hello/<user>')
#def hello_name(user):
#   return render_template('hello.html', name = user)

if __name__ == '__main__':
    app.run()
