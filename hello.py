from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('login.htm')


@app.route('/hello/<name>')
def hello_name():
	return'Hello {0}!'.format(name)

@app.route('/blog/<int:postID>')
def show_post(postID):
	return 'Post Number {0}'.format(postID)

@app.route('/login', methods=['POST', 'GET'])
def login():
	if request.method == 'POST':
		user = request.form['um']
		pswd = request.form['pw']
		if user == 'admin' and pswd == 'Panther$':
			#return redirect(url_for('welcome'), user)
			return render_template('welcome.htm', name=user)
		else:
			#return redirect(url_for('rejection'), user)
			return render_template('rejection.htm', name=user)
	return 'login'

# @app.route('/welcome/<name>')
# def welcome(name):
# 	#return'Welcome {0}!'.format(name)
# 	return render_template('welcome.htm', name)

# @app.route('/rejection/<name>')
# def rejection(name):
# 	return '{0} is not a valid user'.format(name)

if __name__ == "__main__":
	app.run()
