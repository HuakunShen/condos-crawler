import json
import scrapy
from pprint import pprint


class RegionAllSpider(scrapy.Spider):
    name = 'region_all'
    allowed_domains = ['condos.ca', "1tvig461ec-dsn.algolia.net"]
    url = "https://1tvig461ec-dsn.algolia.net/1/indexes/condos_search_listings_entry_date_unix_desc/query?x-algolia-agent=Algolia%20for%20JavaScript%20(3.35.1)%3B%20Browser&x-algolia-application-id=1TVIG461EC&x-algolia-api-key=ef5048180c7c3423dd61e2f8a3481969"
    payload = {
        "params": "query=&filters=(offer%3A%22Sale%22)%20AND%20(status%3A%22Active%22)%20AND%20(locality_id%3D1)&hitsPerPage=2500"
    }
    headers = {
        'accept': 'application/json',
        'accept-language': 'en-CA,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'content-type': 'application/x-www-form-urlencoded',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'Referer': 'https://condos.ca/',
        'Referrer-Policy': 'strict-origin-when-cross-origin'
    }

    def get_payload(self, page: int):
        cpy = self.payload.copy()
        cpy['params'] += f"&page={page}"
        return cpy

    def start_requests(self):
        yield scrapy.Request(method='POST', url=self.url,
                             headers=self.headers,
                             body=json.dumps(self.get_payload(0)),
                             callback=self.parse)

    def parse(self, response):
        res = response.json()
        if res['page'] < res['nbPages']:
            yield scrapy.Request(method='POST',
                                 url=self.url,
                                 headers=self.headers,
                                 body=json.dumps(
                                     self.get_payload(res['page'] + 1)),
                                 callback=self.parse)
        yield res
