from bottle import request, response, post, get, abort
import json
_tweets = []

def authorize():
    ip = request['REMOTE_ADDR']
    if ip != '127.0.0.1':
        abort(401, 'You are not authorized to access this endpoint')

@post('/tweets')
def creation_handler():
    authorize()
    data = request.json
    _tweets.append(data)
    pass

@get('/tweets')
def listing_handler():
    authorize()
    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
    return json.dumps(_tweets)