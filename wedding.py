from flask import Flask, render_template, request
from flask.ext.assets import Environment, Bundle

from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/wedding.db'
db = SQLAlchemy(app)

assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle('css/app.scss', filters='pyscss', output='all.css')
assets.register('scss_all', scss)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/info')
def info():
	return render_template('info.html')

@app.route('/details')
def details():
	return render_template('details.html')

@app.route('/bridal')
def bridal():
	return render_template('bridal.html')

@app.route('/accomodations')
def accomodations():
	return render_template('accomodations.html')

@app.route('/rsvp', methods=['GET', 'POST'])
def rsvp():
	# from models import Guest
	# error = ''
	# if request.method == "POST":
	# 	if request.form.get('name') == '':
	# 		error = 'Name field cannot be blank'
	# 		return render_template('rsvp.html', error=error)
	# 	elif request.form.get('email') == '':
	# 		error = "Please enter an email address"
	# 		return render_template('rsvp.html', error=error)
	# 	if 'name' in request.form:
	# 		if not request.form.get('attending') and not request.form.get('notAttending'):
	# 			error = 'Must RSVP with a resonse'
	# 			return render_template('rsvp.html', error=error)
	# 		else:
	# 			attending = "Yes" if request.form.get('attending') else "No"
	# 			email = request.form.get('email')
	# 			plus_one = request.form.get('plus_one')
	# 			comments = request.form.get('comments')
	# 			guest = Guest(request.form.get('name'), attending=attending, email=email, comments=comments, plus_one=plus_one)
	# 			db.session.add(guest)
	# 			db.session.commit()
	return render_template('rsvp.html')

@app.route('/guestlist')
def guetslist():
	from models import Guest
	guests = Guest.query.all()
	return render_template('guestlist.html', guests=guests)

if __name__ == '__main__':
    app.run()