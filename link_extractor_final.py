import requests

DOMAIN = 'https://en.wikipedia.org/w/api.php'
HEADERS = {'User-Agent': 'wiki-degrees-BOT/0.0 (https://github.com/SuperCoder32/wiki_hitler; pietarcho@gmail.com)'}


def query(req):
    req['action'] = 'query'
    req['format'] = 'json'
    req['generator'] = 'linkshere'
    req['glhprop'] = 'title'
    req['glhnamespace'] = '0'
    req['glhshow'] = '!redirect'
    req['glhlimit'] = 'max'

    return requests.get(DOMAIN, params=req).json()


def parse_response(res):
    try:
        cont = res['continue']
    except KeyError:
        cont = None

    try:
        res = res['query']['pages']
    except KeyError:
        res = set()
    else:
        res = set(item['title'] for item in res.values())

    return cont, res


def get_all_articles(title):
    title = title.replace(' ', '+')
    request = dict()

    request['titles'] = title

    response = query(request)
    cont, articles = parse_response(response)

    while cont is not None:
        request.update(cont)

        response = query(request)
        cont, new_articles = parse_response(response)

        articles.update(new_articles)

    return articles
