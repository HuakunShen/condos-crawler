# condos-crawler

Web Crawler Scrapying Condos Data for data analysis

## Instructions

1. `cd CondosCrawler`
2. `scrapy crawl region_all -O toronto.json`

Results will be saved to `toronto.json`. The json saved is an array of pages.

The main logic is in [region_all.py](./CondosCrawler/CondosCrawler/spiders/region_all.py).

The page number can be specified payload. I wrote a method to update page number.

The city I am querying didn't appear in the request parameters. If you wanna use another location. Go to https://condos.ca/{city_name}, use Chrome > network to find the query and copy its url and payload.

Each object in it is a single page. Each page should contain 1000 **hits**, except for the last page.

Suppose a page is loaded as a python dictionary, here is the sample content (key `hits` not included)

- nbHits: 2511
- page: 2
- nbPages: 3
- hitsPerPage: 1000
- exhaustiveNbHits: True
- exhaustiveTypo: True
- query:
- params: query=&filters=(offer%3A%22Sale%22)%20AND%20(status%3A%22Active%22)%20AND%20- (locality_id%3D1)&page=2&hitsPerPage=2500
- renderingContent: {}
- processingTimeMS: 13

The key `hits` corresponds to an array of homes.

See [`condos.ipynb`](./condos.ipynb) for more details.
