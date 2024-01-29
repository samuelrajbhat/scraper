from requests_html import HTMLSession


class heatware_scraper():
    def heatware_scraper(self):
        url = f'https://webscraper.io/test-sites'
        session = HTMLSession()
        result = session.get(url)
        print(result.status_code)

        dict_item = []
       
        if result.status_code == 200:
            scrape_text = result.html.find ('div.row.test-site')
            # scrape_heading = result.html.find('p')
            # print(scrape_text)
           
            # print("print", scrape_text)
            
            # for q , r  in zip(scrape_text,scrape_heading) :
            for q   in scrape_text :
                if (q.find('p')):
                    dict_item.append(q.find('p', first = True).text.strip())
                dict_item.append(q.find('div.col-lg-7.order-lg-2', first = True).text.strip())
                if (q.find('hr.test-site-divider')):
                    continue
                    # 'Headig' : r.find('h2', first = True) if r is not None else ''.text.strip(),
           
        return dict_item    
heatware = heatware_scraper()
heatware.heatware_scraper()
