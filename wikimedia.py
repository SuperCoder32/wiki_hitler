import requests

DOMAIN = 'https://en.wikipedia.org/w/api.php'
HEADERS = {'User-Agent': 'wiki_hitler_BOT/0.0 (https://github.com/SuperCoder32/wiki_hitler; pietarcho@gmail.com)'}

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
    req['format'] = 'json'
    
    res = requests.post(DOMAIN, params=req, data=data, headers=HEADERS).json()
    token = res['query']['tokens']['logintoken']

    data['lgtoken'] = token
    return requests.post(DOMAIN, params=req, data=data, headers=HEADERS).json()


if __name__ == '__main__':
    print(login())
