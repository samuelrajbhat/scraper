from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse


from main import templates, root_router

from heatware_scraper import heatware_scraper


scraper = heatware_scraper()

@root_router.get("/heatware", response_class= HTMLResponse)
async def read_heatware_item(request:Request):
    display_data = scraper.heatware_scraper()
    return templates.TemplateResponse(request=request, name= 'webscraper.html', context={"id":display_data})
