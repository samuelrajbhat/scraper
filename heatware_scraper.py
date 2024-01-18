from requests_html import HTMLSession


class heatware_scraper():
    def heatware_scraper(self):
        url = f'https://www.heatware.net/postgresql/postgresql-show-tables-psql-examples/#:~:text=PostgreSQL%20Command%20to%20Show%20All%20Tables%20in%20Current%20Schema&text=Open%20a%20Terminal%20or%20Command,%2DU%20username%20%2Dd%20databasename%20.'
        session = HTMLSession()
        result = session.get(url)
        print(result.status_code)

        scrape_element = []

        if result.status_code == 200:
            scrape_text = result.html.find('div.dynamic-entry-content')
            # scrape_heading = result.html.find('p')
            # print(scrape_text)
           
            
            
            # for q , r  in zip(scrape_text,scrape_heading) :
            for q   in scrape_text :
                # if q is not None or r is not None:
                    dict_item = {
                        'text': q.find('p', first = True).text.strip(),
                        # 'Headig' : r.find('h2', first = True) if r is not None else ''.text.strip(),
                        
                    }
                    scrape_element.append(dict_item)
            return scrape_element

heatware = heatware_scraper()
heatware.heatware_scraper()
