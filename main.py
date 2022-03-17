import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
}


def get_data(url):
    r = requests.get(url=url, headers=headers)

    with open("index.html", "w", encoding="utf-8") as file:
        file.write(r.text)


def get_mail():
    with open(file='index.html') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    mail = soup.find_all("div", class_='col6-10')
    data = []
    for dbm in mail:
        if dbm.find('a'):
            area_data = dbm.find('a').get('href')
            if "mailto:" in area_data:
                data.append(area_data[7:])

    all_mails = set(data)
    with open("res.txt", "w", encoding="utf-8") as file:
        file.write(str(all_mails))


def main():
    store = 'ikea'
    get_data(url=f'https://www.zlatestranky.sk/hladanie/{store}/')
    get_mail()


if __name__ == '__main__':
    main()


