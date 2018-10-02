from flask import render_template
from .qrcode import bp, make_qrcode_url
from app import app

app.config['SECRET_KEY'] = 'random-bytes'
app.register_blueprint(bp)

@app.route('/')
@app.route('/index')
def index():
  qrcode_url = make_qrcode_url('https://linoxide.com/linux-how-to/install-flask-python-ubuntu/')
  return render_template('index.html', title="Home", qrcode_url=qrcode_url)
