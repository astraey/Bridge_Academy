from flask import Flask, render_template, request, session, url_for, redirect, Markup
import json, os

app = Flask(__name__)

@app.route('/')
def homeFunction():
	if session.get('wrong_password'):
		return "wrong password"
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		return render_template('home.html')

@app.route('/profile/')
def profileFunction():
    return render_template('profile.html')

@app.route('/prizes/')
def prizesFunction():

    generatedBody = '<div class="row">'

    # A list of the prizes
    prizes = readJson("prizes.json")['prizes']




    for prize in prizes:

        generatedBody += '''





    <div class="col-sm-4 panel">

            <a href="#">
                <div class="frontpage_square thumbnail">
                  <a href="NUEVA">
                    <img src="'''+prize['img_url']+'''" style="width:50;height:50;">
                  </a>
                  <p><b>'''+prize['name']+'''</b></p>
                  <p><b>'''+prize['price']+'''</b></p>
                </div>
            </a>

    </div>

                         '''

    generatedBody += '</div>'
    generatedBody = Markup(generatedBody)


    return render_template('prizes.html', cool_body = generatedBody)

@app.route('/singlePrize/')
def singlePrizeFunction():
	return singlePrize.singlePrizeGenerator()

@app.route('/exercises/')
def exercisesFunction():
    return render_template('exercises.html')

@app.route('/singleExercise/')
def singleExerciseFunction():
	return singleExercise.singleExerciseGenerator()

@app.route('/about_us/')
def about_usFunction():
	return render_template('about_us.html')

@app.route('/test/<variable>')
def hello_name(variable):
    return render_template('test.html', message = variable)

@app.route('/login', methods=['POST'])
def login():
	users = readJson("users.json")['users']
	for user in users:
		if request.form['password'] == user['password'] and request.form['username'] ==  user['username']:
			session['logged_in'] = True
			return homeFunction()

	session['wrong_password'] = True
	return homeFunction()

@app.route('/logout')
def logout():
		session.clear()
		return redirect(url_for("homeFunction"))

def readJson(path):
	with open(path) as json_data:
		return json.load(json_data)

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=5000)
