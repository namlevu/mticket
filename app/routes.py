from flask import render_template, request
from .qrcode import bp, make_qrcode_url
from app import app

app.config['SECRET_KEY'] = 'abc'
app.register_blueprint(bp)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
  qrcode_url = make_qrcode_url('http://www.namvl.com')
  if request.method == 'POST':
    qrcode_url = make_qrcode_url('http://www.msn.com')
  if request.method == 'GET':
    qrcode_url = make_qrcode_url('http://www.google.com')
  return render_template('index.html', title="Home", qrcode_url=qrcode_url)

@app.route('/checkin')
def checkin():
  return ""
