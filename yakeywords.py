# -*- codding: utf-8 -*-
import os

from fake_useragent import UserAgent
import lxml.html
import requests

from settings import *



class Snoop(object):
    def __init__(self, start, pages, keywords):
        self.keywords = list(map(str.lower, keywords))
        self.pages = [50 * (start + i - 1) for i in range(pages)]

        self.session = requests.Session()

        headers = {'User-Agent': UserAgent().chrome}
        self.session.headers.update(headers)


    def find(self):
        for page in self.pages:
            url = f'http://www.yaplakal.com/st/{page}'
            print(url)

            response = self.session.get(url)
            if response.status_code == 200:
                html = lxml.html.fromstring(response.content)
                titles = html.xpath(f'.//a[@class="subtitle"]/text()')[:50]
                urls = html.xpath(f'.//a[@class="subtitle"]/@href')[:50]

                for i in range(50):
                    for word in self.keywords:
                        if titles[i].find(word) >= 0:
                            print(f'\t{titles[i]}')
                            print(f'\t{urls[i]}', end='\n\n')
                            break


if __name__ == '__main__':
    snoop = Snoop(start, pages, keywords)
    snoop.find()

    input('Для завершения нажмите "Enter"')
