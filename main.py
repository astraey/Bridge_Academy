from flask import Flask, render_template, request, session, url_for, redirect, Markup
import json, os, random

app = Flask(__name__)

@app.route('/')
def homeFunction():
	if session.get('wrong_password'):
		return "wrong password"
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		return redirect('/prizes/')

@app.route('/profile/')
def profileFunction():

    if not session.get('logged_in'):
        return render_template('login.html')

    else:



        index = int(session.get('id_user'))

        users = readJson("users.json")['users']


        generatedBody = '''

                        <div class="maxicenter row row2">
                            <div class="col-sm-4 panel">
                                <div class="frontpage_square thumbnail">
                                  <div class="cntr afterDiv">
                                      <p class="lessSpace"><b>'''+users[index]['name']+'''</b></p>
                                      <p class="lessSpace"><b>'''+users[index]['email']+'''</b></p>
                                      <p class="lessSpace">'''+str(users[index]['coins'])+'''<img class="coin" src="/static/media/coin.png"></p>
                                  </div>
                                </div>
                            </div>
                        </div>



                        '''

        generatedBody = Markup(generatedBody)


        return render_template('profile.html', cool_body = generatedBody)






@app.route('/prizes/')
def prizesFunction():

    generatedBody = '<div class="row row2">'

    # A list of the prizes
    prizes = readJson("prizes.json")['prizes']




    for prize in prizes:

        generatedBody += '''


    <div class="col-sm-4 panel">
            <a style="text-decoration:none" href="/prizes/'''+prize['id']+'''">
                <div class="frontpage_square thumbnail">

                  <div class="prizeimg" align="center">
                    <img src="'''+prize['img_url']+'''" class="imgSize"">
                  </div>
                  <div class="cntr afterDiv">
                  <p class="lessSpace"><b>'''+prize['name']+'''</b></p>
                  <p class="lessSpace">'''+prize['price']+'''<img class="coin" src="/static/media/coin.png"></p>
                  </div>
                </div>
            </a>

    </div>

                         '''

    generatedBody += '</div>'
    generatedBody = Markup(generatedBody)


    return render_template('prizes.html', cool_body = generatedBody)

@app.route('/prizes/<id>')
def singlePrizeFunction(id):


        prizes = readJson("prizes.json")['prizes']


        generatedBody = '''
                        <div class="maxicenter row row2">
                            <div class="col-sm-4 panel">
                                        <div class="frontpage_square thumbnail">

                                          <div class="prizeimg" align="center">
                                            <img src="'''+prizes[int(id)]['img_url']+'''" class="imgSize"">
                                          </div>
                                          <div class="cntr afterDiv">
                                              <p class="lessSpace"><b>'''+prizes[int(id)]['name']+'''</b></p>
                                              <p class="lessSpace">'''+prizes[int(id)]['price']+'''<img class="coin" src="/static/media/coin.png"></p>
                                          <div class="topDistance">
                                                <a href="/prizes/redeem/'''+id+'''">
                                                    <input type="submit" class="btn btn-primary" value="Redeem" />
                                                </a>

                                          </div>
                                         </div>
                                         </div>

                                </div>
                            </div>


                     '''


        generatedBody = Markup(generatedBody)


        return render_template('prizes.html', cool_body = generatedBody)




@app.route('/prizes/redeem/<id>')
def redeemFunction(id):

    if not session.get('logged_in'):
        return render_template('login.html')
    else:

        index = int(session.get('id_user'))

        users = readJson("users.json")

        prizes = readJson("prizes.json")['prizes']

        capital = users['users'][int(index)]['coins']

        if capital < int(prizes[int(id)]['price']):
            generatedBody = '''
                            <div class="maxicenter row row2">
                                <div class="col-sm-4 panel">
                                            <div class="frontpage_square thumbnail">

                                              <div class="prizeimg" align="center">
                                                <img src="'''+prizes[int(id)]['img_url']+'''" class="imgSize"">
                                              </div>
                                              <div class="cntr afterDiv">
                                                  <p class="lessSpace"><b>'''+prizes[int(id)]['name']+'''</b></p>
                                                  <p class="lessSpace">'''+prizes[int(id)]['price']+'''<img class="coin" src="/static/media/coin.png"></p>
                                                  <p style="color:red">You don't have enough coins</p>
                                              <div class="topDistance">
                                                    <a href="/prizes/redeem/'''+id+'''">
                                                        <input type="submit" class="btn btn-primary" value="Redeem" />
                                                    </a>

                                              </div>
                                             </div>
                                             </div>

                                    </div>
                                </div>


                         '''
        else:

                    users['users'][int(index)]['coins'] = int(users['users'][int(index)]['coins']) - int(prizes[int(id)]['price'])

                    with open('users.json', 'w') as f:
                        json.dump(users, f)



                    generatedBody = '''
                                    <div class="maxicenter row row2">
                                        <div class="col-sm-4 panel">
                                                    <div class="frontpage_square thumbnail">

                                                      <div class="prizeimg" align="center">
                                                        <img src="'''+prizes[int(id)]['img_url']+'''" class="imgSize"">
                                                      </div>
                                                      <div class="cntr afterDiv">
                                                          <p class="lessSpace"><b>'''+prizes[int(id)]['name']+'''</b></p>
                                                          <p class="lessSpace">'''+prizes[int(id)]['price']+'''<img class="coin" src="/static/media/coin.png"></p>
                                                          <p style="color:green">The item has been succesfully redeemed</p>
                                                      <div class="topDistance">
                                                            <a href="/prizes/redeem/'''+id+'''">
                                                                <input type="submit" class="btn btn-primary" value="Redeem" />
                                                            </a>

                                                      </div>
                                                     </div>
                                                     </div>

                                            </div>
                                        </div>


                                 '''

        generatedBody = Markup(generatedBody)


        return render_template('prizes.html', cool_body = generatedBody)



@app.route('/exercises/')
def exercisesFunction():

    generatedBody = '<div class="row row2">'

    # A list of the prizes
    categories = readJson("questions.json")
    for category in categories:
        generatedBody += '''

    <div class="col-sm-4 panel">
                <a style="text-decoration:none" href="/exercises/'''+str(categories[category]["id"])+'''">
                <div class="frontpage_square thumbnail">
                  <div class="prizeimg" align="center">
                    <img src="/static/media/'''+str(category).lower()+'''.jpg" class="imgSize"">
                    <p class="space"><b>'''+str(category)+'''</b></p>
                  </div>
                </div>
                </a>
            </a>

    </div>

                         '''

    generatedBody += '</div>'
    generatedBody = Markup(generatedBody)


    return render_template('exercises.html', cool_body = generatedBody)




@app.route('/exercises/<id>')
def singleExercisesFunction(id):


    generatedBody = '''
	<div class="row row3"><div class="exercices"><div class="prizeimg question frontpage_square thumbnail"><div class="space cntr afterDiv"><p class="cntr lessSpace"><b></b></p><form action="/answered/" method="post">
    <label for="labelSpace exampleSelect1">How much is 4*5 - 17</label>
    <select class="formControl form-control" id="exampleSelect1">
      <option>1</option>
      <option>2</option>
      <option>3</option>
      <option>4</option>
      <option>5</option>
    </select>
	</div></div></div></div>


	<div class="row row3"><div class="exercices"><div class="prizeimg question frontpage_square thumbnail"><div class="space cntr afterDiv"><p class="cntr lessSpace"><b></b></p><form action="/answered/" method="post">
    <label for="labelSpace exampleSelect2">What is heavier, a kilogram of metal or a kilogram of grass</label>
    <select class="formControl form-control" id="exampleSelect1">
      <option>A kilogram of metal</option>
      <option>A kilogram of grass</option>
      <option>They wheight the same amout</option>
    </select>
	</div></div></div></div>


	<div class="row row3"><div class="exercices"><div class="prizeimg question frontpage_square thumbnail"><div class="space cntr afterDiv"><p class="cntr lessSpace"><b></b></p><form action="/answered/" method="post">
    <label for="labelSpace exampleSelect2">Name one of Albert Einstein's Work</label>
    <select class="formControl form-control" id="exampleSelect1">
      <option>Pythagorean theorem</option>
      <option>General Theory of Relativity</option>
      <option>Fundamental Theorem of Algebra</option>
	  <option>The Four Color Problem</option>
    </select>
	</div></div></div></div>


	<div class="row row3"><div class="exercices"><div class="prizeimg question frontpage_square thumbnail"><div class="space cntr afterDiv"><p class="cntr lessSpace"><b></b></p><form action="/answered/" method="post">
    <label for="labelSpace exampleSelect2">If y – 9 = 25, what is the value for y?</label>
    <select class="formControl form-control" id="exampleSelect1">
      <option>35</option>
      <option>36</option>
      <option>34</option>
    </select>
	</div></div></div></div>

	<a href="/profile/" class="buttonCenter">
		<button type="button" class="btn cntr btn-primary">Answer</button>
	</a>



    '''

    generatedBody = Markup(generatedBody)


    return render_template('exercises.html', cool_body = generatedBody)



@app.route('/exercises2/<id>')
def singleExercisesFunction2(id):


    generatedBody = '<div class="row row2">'

    categories = readJson("questions.json")
    for category in categories:
        if str(categories[category]["id"]) == str(id):
            numQ = str(len(categories[category]["questions"]))
            #return str(categories[category]["questions"][str(random.randint(1,int(numQ)))])
            randomNum = random.randint(1,int(numQ))
            tempVar = categories[category]["questions"][str(randomNum)]


#########################################################################################

            generatedBody += '''<div class="exercices"><div class="prizeimg question frontpage_square thumbnail"><div class="cntr afterDiv">'''

            generatedBody += '''<p class="cntr lessSpace"><b>'''+tempVar["text"]+'''</b></p><form action="/answered/" method="post">'''




            resp = []

            for i in range(0, len(tempVar['respuestas'])):
                resp.append(tempVar['respuestas'][i])

                generatedBody += '''
                <div class="checkbox">
                <input type="radio" name="check[] value="'''+str(i)+'''"">'''+str(tempVar['respuestas'][i])+'''</input>
                </div>
                '''

            selected = request.form.getlist('check[]')

            generatedBody += '''<a href="/exercises/'''+str(id)+'''/'''+str(randomNum)+'''/'''+str(selected)+'''" class="btn btn-info" role="button">Submit</a></form></div></div></div></div>'''
            generatedBody = Markup(generatedBody)


    return render_template('exercises.html', cool_body = generatedBody)


@app.route('/exercises/<id>/<q>/<r>')
def validateExercisesFunction(id, q, r):


    generatedBody = '<div class="row row2">'

    categories = readJson("questions.json")
    # for category in categories:
        #if str(categories[category]["id"]) == str(id):
            #for question in categories[category]["questions"]:
                #if categories[category][question]['id'] == str(q):
                    #correct = categories[category][question]['correct']
                    #correctIndex = categories[category][question].index(correct)
                    #if correctIndex == r:
                        #sum2points(int(session.get('id_user')))
    return "no correct answer"


#########################################################################################

    generatedBody += '''<div class"exercices"><div class="prizeimg question frontpage_square thumbnail"><div class="cntr afterDiv">'''

    generatedBody += '''<p class="cntr lessSpace"><b>'''+tempVar["text"]+'''</b></p><form>'''

    for answer in tempVar['respuestas']:


        generatedBody += '''

        <div class="checkbox">
            <input type="radio" name="hola">'''+answer+'''</input>
        </div>

        '''




    generatedBody += '</form></div></div></div></div>'
    generatedBody = Markup(generatedBody)


    return render_template('exercises.html', cool_body = generatedBody)


@app.route('/answered/', methods=['POST'])
def answeredFunction():
	name=request.form['yourname']
	email=request.form['youremail']
	return render_template('about_us.html')


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
            session['id_user'] = user['id']
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

def sum2points(userid):
    users = readJson("users.json")
    users['users'][int(index)]['coins'] += 2



if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=5000)
