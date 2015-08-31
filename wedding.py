from flask import Flask, render_template, request
from flask.ext.assets import Environment, Bundle
app = Flask(__name__)

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
	error = ''
	if request.method == "POST":
		if 'name' in request.form:
			if request.form.get('name') == '':
				error = 'Name field cannot be blank'
				return render_template('rsvp.html', error=error)
	return render_template('rsvp.html')

if __name__ == '__main__':
    app.run()