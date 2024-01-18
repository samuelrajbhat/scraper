from fastapi import FastAPI
from scraper import Scraper
from heatware_scraper import heatware_scraper

app = FastAPI()
quotes = Scraper()

heatware = heatware_scraper()


@app.get("/get/{cat}")
async def read_scraper_item(cat):
    return quotes.scrapedata(cat)

@app.get("/heatware")
async def read_heatware_item():
    return heatware.heatware_scraper()



