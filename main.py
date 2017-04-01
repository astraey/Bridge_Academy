from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def homeFunction():
    return render_template('home.html')

@app.route('/profile/')
def profileFunction():
    return render_template('profile.html')

@app.route('/prizes/')
def prizesFunction():
    return render_template('prizes.html')

@app.route('/singlePrize/')
def singlePrizeFunction():
	return singlePrize.singlePrizeGenerator()

@app.route('/exercises/')
def exercisesFunction():
    return render_template('exercises.html')

@app.route('/singleExercise/')
def singleExerciseFunction():
	return singleExercise.singleExerciseGenerator()

@app.route('/test/<variable>')
def hello_name(variable):
    return render_template('test.html', message = variable)



if __name__ == '__main__':
    app.run()
