from flask import Flask, render_template
from flask.ext.assets import Environment, Bundle
app = Flask(__name__)

assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle('css/app.scss', filters='pyscss', output='all.css')
assets.register('scss_all', scss)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()