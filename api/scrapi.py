from bottle import request, response, post, get, abort
import json
_tweets = []

@post('/tweets')
def creation_handler():
    data = request.json
    _tweets.append(data)
    pass

@get('/tweets')
def listing_handler():
    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
    return json.dumps(_tweets)