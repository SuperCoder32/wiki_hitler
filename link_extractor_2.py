import requests

DOMAIN = 'https://en.wikipedia.org/w/api.php'
HEADERS = {'User-Agent': 'wiki_hitler_BOT/0.0 (https://github.com/SuperCoder32/wiki_hitler; pietarcho@gmail.com)'}

def query(req):
    req['action'] = 'query'
    req['format'] = 'json'
    req['prop'] = 'linkshere'
    req['lhprop'] = 'title'
    req['lhnamespace'] = '0'
    req['lhshow'] = '!redirect'
    req['lhlimit'] = 'max'

    return requests.get(DOMAIN, params=req).json()

def parse_res(res):
    res = res['query']['pages']
    pageid = next(iter(res))
    res = res[pageid]['linkshere']
    res = [obj['title'] for obj in res]

def main(title):
    res = parse_res(query({'titles': title}))

    print(res)

if __name__ == '__main__':
    import sys
    main(*sys.argv[1:])
