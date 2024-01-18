from requests_html import HTMLSession


class Scraper():
    def scrapedata(self, tag):
        url = f'https://quotes.toscrape.com/tag/{tag}'
        session = HTMLSession()
        result = session.get(url)
        print(result.status_code) 

        qlist = []

        quotes  = result.html.find('div.quote')

        for q in quotes:
            item = {
                'Text': q.find('span.text', first = True).text.strip(),
                'Author': q.find('small.author', first = True).text.strip(),
                }
            qlist.append(item)
        
        return qlist
    
quotes = Scraper()
quotes.scrapedata('life')


         