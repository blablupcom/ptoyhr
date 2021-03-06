import requests
from bs4 import BeautifulSoup as bs
import scraperwiki
from datetime import datetime
from multiprocessing.dummy import Pool
from multiprocessing import cpu_count
import grequests
from concurrent.futures import ThreadPoolExecutor


start_urls = ['http://www.amazon.com/Best-Sellers-Appliances/zgbs/appliances/ref=zg_bs_nav_0',
'http://www.amazon.com/Best-Sellers-Appstore-Android/zgbs/mobile-apps/ref=zg_bs_nav_0',
'http://www.amazon.com/Best-Sellers-Arts-Crafts-Sewing/zgbs/arts-crafts/ref=zg_bs_nav_0',
'http://www.amazon.com/Best-Sellers-Automotive/zgbs/automotive/ref=zg_bs_nav_0',
'http://www.amazon.com/Best-Sellers-Baby/zgbs/baby-products/ref=zg_bs_nav_0',
'http://www.amazon.com/Best-Sellers-Beauty/zgbs/beauty/ref=zg_bs_nav_0',
'http://www.amazon.com/best-sellers-books-Amazon/zgbs/books/ref=zg_bs_nav_0',
'http://www.amazon.com/best-sellers-camera-photo/zgbs/photo/ref=zg_bs_nav_0',
'http://www.amazon.com/Best-Sellers-Cell-Phones-Accessories/zgbs/wireless/ref=zg_bs_nav_0',
'http://www.amazon.com/Best-Sellers-Clothing/zgbs/apparel/ref=zg_bs_nav_0',
'http://www.amazon.com/Best-Sellers-Collectible-Coins/zgbs/coins/ref=zg_bs_nav_0',
'http://www.amazon.com/Best-Sellers-Computers-Accessories/zgbs/pc/ref=zg_bs_nav_0',
'http://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/ref=zg_bs_nav_0',
'http://www.amazon.com/Best-Sellers-Entertainment-Collectibles/zgbs/entertainment-collectibles/ref=zg_bs_nav_0',
'http://www.amazon.com/Best-Sellers-Gift-Cards/zgbs/gift-cards/ref=zg_bs_nav_0',
'http://www.amazon.com/Best-Sellers-Grocery-Gourmet-Food/zgbs/grocery/ref=zg_bs_nav_0',
'http://www.amazon.com/Best-Sellers-Health-Personal-Care/zgbs/hpc/ref=zg_bs_nav_0',
'http://www.amazon.com/Best-Sellers-Home-Kitchen/zgbs/home-garden/ref=zg_bs_nav_0',
'http://www.amazon.com/Best-Sellers-Home-Improvement/zgbs/hi/ref=zg_bs_nav_0',
'http://www.amazon.com/Best-Sellers-Industrial-Scientific/zgbs/industrial/ref=zg_bs_nav_0',
'http://www.amazon.com/Best-Sellers-Jewelry/zgbs/jewelry/ref=zg_bs_nav_0',
'http://www.amazon.com/Best-Sellers-Kindle-Store/zgbs/digital-text/ref=zg_bs_nav_0',
'http://www.amazon.com/Best-Sellers-Kitchen-Dining/zgbs/kitchen/ref=zg_bs_nav_0',
'http://www.amazon.com/Best-Sellers-MP3-Downloads/zgbs/dmusic/ref=zg_bs_nav_0',
'http://www.amazon.com/Best-Sellers-Magazines/zgbs/magazines/ref=zg_bs_nav_0',
'http://www.amazon.com/best-sellers-movies-TV-DVD-Blu-ray/zgbs/movies-tv/ref=zg_bs_nav_0',
'http://www.amazon.com/best-sellers-music-albums/zgbs/music/ref=zg_bs_nav_0',
'http://www.amazon.com/Best-Sellers-Musical-Instruments/zgbs/musical-instruments/ref=zg_bs_nav_0',
'http://www.amazon.com/Best-Sellers-Office-Products/zgbs/office-products/ref=zg_bs_nav_0',
'http://www.amazon.com/Best-Sellers-Patio-Lawn-Garden/zgbs/lawn-garden/ref=zg_bs_nav_0',
'http://www.amazon.com/Best-Sellers-Pet-Supplies/zgbs/pet-supplies/ref=zg_bs_nav_0',
'http://www.amazon.com/Best-Sellers-Prime-Pantry/zgbs/pantry/ref=zg_bs_nav_0',
'http://www.amazon.com/best-sellers-shoes/zgbs/shoes/ref=zg_bs_nav_0',
'http://www.amazon.com/best-sellers-software/zgbs/software/ref=zg_bs_nav_0',
'http://www.amazon.com/Best-Sellers-Sports-Outdoors/zgbs/sporting-goods/ref=zg_bs_nav_0',
'http://www.amazon.com/Best-Sellers-Sports-Collectibles/zgbs/sports-collectibles/ref=zg_bs_nav_0',
'http://www.amazon.com/Best-Sellers-Toys-Games/zgbs/toys-and-games/ref=zg_bs_nav_0',
'http://www.amazon.com/best-sellers-video-games/zgbs/videogames/ref=zg_bs_nav_0',
'http://www.amazon.com/Best-Sellers-Watches/zgbs/watches/ref=zg_bs_nav_0']
pool = Pool(cpu_count() * 20)

# def scrape(response, **kwargs):
#         listing_soup = bs(response.text, 'lxml')
#         asin_nums = listing_soup.find_all('div', 'zg_itemImmersion')
#         for asin_num in asin_nums:
#             asin = ''
#             try:
#                 asin = asin_num.find('a')['href'].split('dp/')[-1].strip()
#             except:
#                 pass
#             amazon_price = ''
#             try:
#                 amazon_price = asin_num.find('strong', 'price').text.strip()
#             except:
#                 pass
#             total_offer_count = ''
#             try:
#                 total_offer_count = asin_num.find('div', 'zg_usedPrice').find('a').text.strip().split(u'\xa0')[0].replace('used & new', '')
#             except:
#                 pass
#             lowest_price = ''
#             try:
#                 lowest_price = asin_num.find('div', 'zg_usedPrice').find('span', 'price').text.strip()
#             except:
#                 pass
#             today_date = str(datetime.now())
#             return asin, today_date, amazon_price, total_offer_count, lowest_price
        #     scraperwiki.sqlite.save(unique_keys=['Date'], data={'ASIN': asin, 'Date': today_date, 'Amazon Price': amazon_price, 'Total Offer Count': total_offer_count, 'Lowest Price': lowest_price})


def multiparse(links):
         l = links.find('a')['href'].encode('utf-8')
         if l:
             return l

asis = []
def parse(url):

    page = requests.get(url)
    soup = bs(page.text, 'lxml')
    links_lists = []
    try:
        active_sel = soup.find('span', 'zg_selected').find_next()
        if active_sel.name == 'ul':
            links_lists= active_sel.find_all('li')
            asins = pool.map(multiparse, links_lists)
            for asin in asins:
                async_list = []
                for i in xrange(1, 6):
                        print (asin+'?&pg={}'.format(i))
                        rs = requests.get(asin+'?&pg={}'.format(i))
                        listing_soup = bs(rs.text, 'lxml')
                        asin_nums = listing_soup.find_all('div', 'zg_itemImmersion')
                        for asin_num in asin_nums:
                            asin = ''
                            try:
                                asin = asin_num.find('a')['href'].split('dp/')[-1].strip()
                            except:
                                pass
                            amazon_price = ''
                            try:
                                amazon_price = asin_num.find('strong', 'price').text.strip()
                            except:
                                pass
                            total_offer_count = ''
                            try:
                                total_offer_count = asin_num.find('div', 'zg_usedPrice').find('a').text.strip().split(u'\xa0')[0].replace('used & new', '')
                            except:
                                pass
                            lowest_price = ''
                            try:
                                lowest_price = asin_num.find('div', 'zg_usedPrice').find('span', 'price').text.strip()
                            except:
                                pass
                            today_date = str(datetime.now())
                            return asin, today_date, amazon_price, total_offer_count, lowest_price
                    
                #     rs = (grequests.get(asin+'?&pg={}'.format(i), hooks = {'response' : scrape}))
                #     async_list.append(rs)
                # parse(asin)
                # grequests.map(async_list)


    except:
        parse(url)


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=39) as executor:
            for start_url in start_urls:
                result = executor.submit(parse, start_url)
                print result
                
#      for start_url in start_urls:
#          parse(start_url)
