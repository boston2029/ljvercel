import json
import os

from flask import Flask, render_template, request
from flask_mail import Mail

jobs = {}
with open('jobs.json') as file:
    content = file.read()
    jobs = json.loads(content)

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.zoho.com'
app.config['MAIL_USERNAME'] = os.environ['MAIL_USERNAME']
app.config['MAIL_PASSWORD'] = os.environ['MAIL_PASSWORD']
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEFAULT_SENDER'] = ('Jobs At Libit', os.environ['MAIL_USERNAME'])

mail = Mail(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/job/<slug>')
def job(slug):
    return render_template('job.html', slug=slug, job=jobs[slug])


@app.route('/apply')
def apply():
    mail.send_message(
        subject='Libit Application Recieved',
        recipients=[request.args.get('to')],
        bcc=['jobs@mail.libit.xyz'],
        html=render_template('emails/apply.html', job=request.args.get('job'))
    )
    return 'Email sent'


@app.context_processor
def context_processor() -> dict:
    return {'jobs': jobs}
