import requests
from lxml import html

site_url = 'https://eresearch.fidelity.com/eresearch/gotoBL/fidelityTopOrders.jhtml'
base_url = 'https://eresearch.fidelity.com'

def start_scraping():
    # NOTE: Load the web page
    print('feching the page...')
    response = requests.get(site_url)
    page = html.fromstring(response.text)

    # NOTE: Extract data from fetched page
    rowsData = page.xpath('//table[@id="topOrdersTable"]/tbody//tr')

    scraped_data = []
    for row in rowsData:
        rank = row.xpath('.//td[@class="first"]/text()')[0]
        symbol =  row.xpath('.//td[@class="second"]/span/@fmr-param-symbol')[0]
        company = row.xpath('.//td[@class="third"]/text()')[0]
        priceChange = row.xpath('.//td[contains(@class, "fourth")]/text()')[0]
        buyOrder = row.xpath('.//td[@class="fifth"]/text()')[0]
        sellOrder = row.xpath('.//td[@class="seventh"]/text()')[0]
        news = row.xpath('.//td[contains(@class, "eight")]/span/a/@href')[0]

        scraped_data.append((
            rank, symbol, company, priceChange, buyOrder, sellOrder, base_url+news
        ))

    for row in scraped_data:
       rank, symbol, company, priceChange, buyOrder, sellOrder, news = row
       print(rank, symbol, company, priceChange, buyOrder, sellOrder, news)

if (__name__ == '__main__'):
    start_scraping()