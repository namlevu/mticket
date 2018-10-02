from flask import render_template, request
from .qrcode import bp, make_qrcode_url
import base64

from app import app

app.config['SECRET_KEY'] = 'abc'
app.register_blueprint(bp)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    base_url = "http://www.namvl.com/"
    email = request.form['email']
    tel = request.form['tel']
    ticket_quanlity = request.form['quanlity']
    bought_at = '2018/10/10'
    amount = request.form['amount']
    key = email + '&' + tel + '&' + ticket_quanlity + '&' + bought_at + '&' + amount
    url = base_url + key
    qrcode_url = make_qrcode_url(url)
    return render_template('index.html', title="Home", qrcode_url=qrcode_url)

  if request.method == 'GET':
    #qrcode_url = make_qrcode_url('/key=?')
    return render_template('index.html', title="Home")

@app.route('/checkin')
def checkin():
  return ""
