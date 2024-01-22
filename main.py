from fastapi import FastAPI, APIRouter, Request
from scraper import Scraper
from heatware_scraper import heatware_scraper
from pathlib import Path
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

BASE_DIR = Path(__file__).resolve().parent
print("hello:", BASE_DIR)
templates = Jinja2Templates(directory = str(Path(BASE_DIR, 'app/templates')))


root_router = APIRouter()
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name= "static")

quotes = Scraper()
heatware = heatware_scraper()
display_data = []


@root_router.get("/items/{id}", response_class= HTMLResponse)
async def render_html(request: Request, id):
    display_data = quotes.scrapedata(id)

    return templates.TemplateResponse(request=request, name= 'index.html', context={"id":display_data})

    print(display_data)

# @root_router.get("/get/{cat}")
# async def read_scraper_item(cat:str):
#     return quotes.scrapedata(cat)


# @root_router.get("/heatware")
# async def read_heatware_item():
#     return heatware.heatware_scraper()

app.include_router(root_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")




