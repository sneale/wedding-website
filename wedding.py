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

@app.route('/rsvp', methods=['GET', 'POST'])
def rsvp():
	from models import Guest
	error = ''
	if request.method == "POST":
		if 'name' in request.form:
			if request.form.get('name') == '':
				error = 'Name field cannot be blank'
				return render_template('rsvp.html', error=error)
			elif not request.form.get('attending') and not request.form.get('notAttending'):
				error = 'Must RSVP with a resonse'
				return render_template('rsvp.html', error=error)
			else:
				attending = True if request.form.get('attending') else False
				guest = Guest(request.form.get('name'), attending=attending)
				db.session.add(guest)
				db.session.commit()
	return render_template('rsvp.html')

@app.route('/guestlist')
def guetslist():
	from models import Guest
	guests = Guest.query.all()
	return render_template('guestlist.html', guests=guests)

if __name__ == '__main__':
    app.run()