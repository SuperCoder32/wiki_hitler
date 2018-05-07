import requests

FORMAT = 'json'
DOMAIN = 'https://en.wikipedia.org/w/api.php'
HEADERS = {'User-Agent': 'FindHitlerBot/0.0 (pietarcho@gmail.com)'}

def query(req):
    req['action'] = 'query'
    req['format'] = 'json'
    req['list'] = 'embeddedin'
    req['eilimit'] = '5000'

    return requests.get(DOMAIN, params=req, headers=HEADERS).json()


USERNAME = 'FindHitlerBot'
PASSWORD = 'SuccerY!'

def login():
    """action=query&meta=tokens&type=login"""

    data = dict()
    data['lgname'] = USERNAME
    data['lgpassword'] = PASSWORD

    req = dict()
    req['action'] = 'query'
    req['meta'] = 'tokens'
    req['type'] = 'login'
    req['format'] = FORMAT
    
    res = requests.post(DOMAIN, params=req, data=data, headers=HEADERS).json()
    token = res['query']['tokens']['logintoken']

    data['lgtoken'] = token
    return requests.post(DOMAIN, params=req, data=data, headers=HEADERS).json()


if __name__ == '__main__':
    print(login())
