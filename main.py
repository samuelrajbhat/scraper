from fastapi import FastAPI, APIRouter, Request
from scraper import Scraper
from pathlib import Path
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Form

BASE_DIR = Path(__file__).resolve().parent
print("hello:", BASE_DIR)
templates = Jinja2Templates(directory = str(Path(BASE_DIR, 'app/templates')))


root_router = APIRouter()
web_router = APIRouter()
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name= "static")

quotes = Scraper()
display_data = []

from heatware_scraper import heatware_scraper


scraper = heatware_scraper()

@root_router.get("/")
async def root(request: Request):
    
    return templates.TemplateResponse("index.html",{"request": request})




@root_router.get("/webscraper", response_class= HTMLResponse)
async def read_heatware_item(request:Request):
    display_data = scraper.heatware_scraper()
    return templates.TemplateResponse(request=request, name= 'webscraper.html', context={"id":display_data})



@root_router.get("/items/{id}", response_class= HTMLResponse)
async def render_html(request: Request, id):
    display_data = quotes.scrapedata(id)

    return templates.TemplateResponse(request=request, name= 'scrape_quotes.html', context={"id":display_data})


app.include_router(root_router)
app.include_router(web_router, prefix='/temp', tags= ["temp"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")




