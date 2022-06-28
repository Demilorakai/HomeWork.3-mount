import requests
from bs4 import BeautifulSoup



URL2 = "https://rezka.ag/series/"


HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36 OPR/87.0.4390.45 (Edition 360-1)"
}


def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req





def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all('div', class_="b-content__inline_item")
    films = []
    for item in items:
        films.append({
            "title": item.find('div', class_="b-content__inline_item-link").find('div').getText(),
            "desc": item.find('div', class_="b-content__inline_item-link").find('div').getText(),
            "link": item.find('div', class_="b-content__inline_item-link").find('a').get('href'),
            "image": item.find('div', class_="b-content__inline_item-cover").find('a').find('img').get('src'),
        })
    return films


def parser_rez():
    html = get_html(URL2)
    if html.status_code == 200:
        films = []
        for page in range(1, 2):
            print(f"{URL2}page/{page}/")
            html = get_html(f"{URL2}/page/{page}/")
            films.extend(get_data(html.text))
        return films
    else:
        raise Exception('Error in PAN!!!')

