#-*- coding: utf-8 -*-

from flask import Flask, request
import json

app = Flask('slackbot')
SLACK_TOKEN = YOUR_SLACK_TOKEN

@app.route('/', methods=['POST'])
def hello_world():
    token = request.form['token']
    if token != SLACK_TOKEN:
        result = {'text': 'wrong request!'}
	return json.dumps(result)

    trigger_word = request.form['trigger_word']
    text = request.form['text']

    if 'soju' in text:
        result = {'text': 'samgyeopsal'}
    elif 'ricewine' in text:
        result = {'text': 'kimchi buchimgae'}
    else:
        result = {'text': 'chicken'} 
    return json.dumps(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=YOUR_PORT_NUM)

